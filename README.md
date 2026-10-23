**About Project**

This project presents a secure academic certificate verification framework that 
combines Federated Learning, Blockchain Technology, Remote Attestation to ensure 
privacy-preserving and tamper-resistant certificate verification.

The framework uses the OULAD (Open University Learning Analytics Dataset) for 
federated learning-based eligibility prediction and secures academic records 
through blockchain storage, attestation tokens, and cryptographic verification.


**Objectives**
Preserve student data privacy using Federated Learning.
Predict certificate eligibility from academic records.
Secure academic verification records using SHA-256 hashes.
Generate attestation tokens for integrity verification.
Implement digital signatures for authentication.
Store verification records on Ethereum Blockchain.
Perform Remote Attestation.
Verify academic certificates through a web dashboard.



**Federated Learning Module**
Framework - Flower Framework
            PyTorch
Aggregation Algorithm - FedAvg(Federated Averaging)


**Blockchain Module**
Technologies - Ethereum
               Ganache
               Truffle
              Solidity
              Web3.py
Smart Contracts
Blockchain Storage


**Security Layer**
SHA-256 Verification Hash : Used to generate a unique fingerprint for each academic record.
Attestation Token : Generated from academic verification records for remote attestation.


**Remote Attestation Module**
Remote Attestation verifies that academic records stored on blockchain have not been modified.

**Project Structure**

OULAD Dataset
        ↓
Federated Learning
(Flower + FedAvg)
        ↓
Eligibility Prediction
        ↓
SHA-256 Verification Hash
        ↓
Attestation Token
        ↓
Digital Signature
        ↓
Ethereum Blockchain
        ↓
Remote Attestation
        ↓
Certificate Verification
        ↓
React Dashboard
