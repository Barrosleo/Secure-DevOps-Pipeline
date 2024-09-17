# Secure DevOps Pipeline User Guide

## Introduction
This guide provides instructions on how to set up and use the Secure DevOps Pipeline to ensure automated security testing and compliance checks.

## Prerequisites
- Python 3.x
- Required Python libraries: pytest, bandit, safety, flake8, license-checker

## Installation
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Barrosleo/Secure-DevOps-Pipeline.git
    ```

2. **Navigate to the Project Directory**:
    ```bash
    cd Secure-DevOps-Pipeline
    ```

3. **Install Required Libraries**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the CI/CD Pipeline
- Push code to the `main` branch or create a pull request to trigger the CI/CD pipeline.
- The pipeline will run automated security tests and compliance checks.

### Running Tests Locally
- To run the security tests locally:
    ```bash
    pytest tests/test_security.py
    ```
- To run the compliance checks locally:
    ```bash
    pytest tests/test_compliance.py
    ```

## Troubleshooting
- Ensure all required libraries are installed.
- Verify the paths to your source code and test files are correct.
