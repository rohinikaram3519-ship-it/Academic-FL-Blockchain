"""pytorchexample: A Flower / PyTorch app."""

import torch
import torch.nn as nn
import torch.nn.functional as F
from flwr_datasets import FederatedDataset
from flwr_datasets.partitioner import IidPartitioner
from torch.utils.data import DataLoader ,random_split
from torchvision.transforms import Compose, Normalize, ToTensor
from medmnist import PathMNIST

class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()

        self.conv1 = nn.Conv2d(1, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)

        self.fc1 = nn.Linear(16 * 4 * 4, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):

        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))

        x = x.view(-1, 16 * 4 * 4)

        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))

        return self.fc3(x)


fds = None  # Cache FederatedDataset

pytorch_transforms = Compose([ToTensor(), Normalize((0.5,), (0.5, ))])


def apply_transforms(batch):
    """Apply transforms to the partition from FederatedDataset."""
    batch["img"] = [pytorch_transforms(img) for img in batch["img"]]
    return batch


def load_data(partition_id, num_partitions, batch_size):

    dataset = PathMNIST(
        root="./data",
        train=True,
        download=True,
        transform=pytorch_transforms,
    )

    partition_size = len(dataset) // num_partitions

    lengths = [partition_size] * num_partitions

    lengths[-1] += len(dataset) - sum(lengths)

    datasets = random_split(
        dataset,
        lengths,
        generator=torch.Generator().manual_seed(42),
    )

    partition = datasets[partition_id]

    train_size = int(0.8 * len(partition))
    val_size = len(partition) - train_size

    train_dataset, test_dataset = random_split(
        partition,
        [train_size, val_size],
    )

    trainloader = DataLoader(
        train_dataset,
        batch_size=batch_size,
        shuffle=True,
    )

    testloader = DataLoader(
        test_dataset,
        batch_size=batch_size,
    )

    return trainloader, testloader


def load_centralized_dataset():
    test_dataset = PathMNIST(
    root="./data",
    train=False,
    download=True,
    transform=pytorch_transforms,
   )
    dataset = test_dataset.with_format("torch").with_transform(apply_transforms)
    return DataLoader(dataset, batch_size=128)


def train(net, trainloader, epochs, lr, device):
    """Train the model on the training set."""
    net.to(device)  # move model to GPU if available
    criterion = torch.nn.CrossEntropyLoss().to(device)
    optimizer = torch.optim.SGD(net.parameters(), lr=lr, momentum=0.9)
    net.train()
    running_loss = 0.0
    for _ in range(epochs):
        for images, labels in trainloader:

            images = images.to(device)

            labels = labels.squeeze().long().to(device)
            optimizer.zero_grad()
            loss = criterion(net(images), labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
    avg_trainloss = running_loss / (epochs * len(trainloader))
    return avg_trainloss


def test(net, testloader, device):
    """Validate the model on the test set."""
    net.to(device)
    criterion = torch.nn.CrossEntropyLoss()
    correct, loss = 0, 0.0
    with torch.no_grad():
        for images, labels in testloader:
            images = images.to(device)
            labels = labels.squeeze().long().to(device)
            outputs = net(images)
            loss += criterion(outputs, labels).item()
            correct += (torch.max(outputs.data, 1)[1] == labels).sum().item()
    accuracy = correct / len(testloader.dataset)
    loss = loss / len(testloader)
    return loss, accuracy
