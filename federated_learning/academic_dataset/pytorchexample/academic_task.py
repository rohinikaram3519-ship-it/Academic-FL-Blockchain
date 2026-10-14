import pandas as pd
import torch
import torch.nn as nn

from torch.utils.data import (
    Dataset,
    DataLoader,
    random_split
)

# -----------------------
# Neural Network
# -----------------------

class Net(nn.Module):

    def __init__(self):

        super().__init__()

        self.fc1 = nn.Linear(5, 32)
        self.fc2 = nn.Linear(32, 16)
        self.fc3 = nn.Linear(16, 2)

    def forward(self, x):

        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)

        return x


# -----------------------
# Dataset
# -----------------------

class OULADDataset(Dataset):

    def __init__(self, csv_file):

        df = pd.read_csv(csv_file)

        self.X = df[
            [
                "highest_education",
                "age_band",
                "num_of_prev_attempts",
                "studied_credits",
                "disability",
            ]
        ].values

        self.y = df[
            "certificate_eligible"
        ].values

    def __len__(self):

        return len(self.X)

    def __getitem__(self, idx):

        return (
            torch.tensor(
                self.X[idx],
                dtype=torch.float32
            ),
            torch.tensor(
                self.y[idx],
                dtype=torch.long
            )
        )


# -----------------------
# Data Loader
# -----------------------

def load_data(
    partition_id,
    num_partitions,
    batch_size
):

    modules = [
        "AAA",
        "BBB",
        "CCC",
        "DDD",
        "EEE",
        "FFF",
        "GGG",
    ]

    module = modules[partition_id]

    dataset = OULADDataset(
        f"data/client_{module}.csv"
    )

    train_size = int(
        0.8 * len(dataset)
    )

    test_size = len(dataset) - train_size

    train_dataset, test_dataset = random_split(
        dataset,
        [train_size, test_size]
    )

    trainloader = DataLoader(
        train_dataset,
        batch_size=batch_size,
        shuffle=True
    )

    testloader = DataLoader(
        test_dataset,
        batch_size=batch_size
    )

    return trainloader, testloader

def train(net, trainloader, epochs, lr, device):

    net.to(device)

    criterion = nn.CrossEntropyLoss()

    optimizer = torch.optim.Adam(
        net.parameters(),
        lr=lr
    )

    net.train()

    running_loss = 0.0

    for _ in range(epochs):

        for features, labels in trainloader:

            features = features.to(device)

            labels = labels.to(device)

            optimizer.zero_grad()

            outputs = net(features)

            loss = criterion(
                outputs,
                labels
            )

            loss.backward()

            optimizer.step()

            running_loss += loss.item()

    avg_loss = running_loss / (
        epochs * len(trainloader)
    )

    return avg_loss

def test(net, testloader, device):

    net.to(device)

    criterion = nn.CrossEntropyLoss()

    correct = 0

    loss = 0.0

    net.eval()

    with torch.no_grad():

        for features, labels in testloader:

            features = features.to(device)

            labels = labels.to(device)

            outputs = net(features)

            loss += criterion(
                outputs,
                labels
            ).item()

            predictions = outputs.argmax(
                dim=1
            )

            correct += (
                predictions == labels
            ).sum().item()

    accuracy = (
        correct / len(testloader.dataset)
    )

    loss = (
        loss / len(testloader)
    )

    return loss, accuracy

def load_centralized_dataset():

    dataset = OULADDataset(
        "data/oulad_processed.csv"
    )

    return DataLoader(
        dataset,
        batch_size=128
    )