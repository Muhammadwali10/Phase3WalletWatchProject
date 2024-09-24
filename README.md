# WalletWatch - Personal Finance Management Tool

## Overview

WalletWatch is a command-line interface (CLI) application designed to help users manage their personal finances efficiently. It allows users to track their income and expenses, view transaction history, edit or delete transactions, and generate financial summaries. The application uses SQLAlchemy for database interaction and SQLite for data storage.

## Features

- **Add Income/Expense**: Users can record new transactions, specifying the type, amount, and description.
- **Display Transactions**: Users can view a list of all transactions stored in the database.
- **Edit/Delete Transactions**: Users can update or remove existing transactions as needed.
- **Generate Summaries**: Users can obtain summaries of their total income, expenses, and overall balance.
- **Persistent Data Storage**: The database ensures data persistence and integrity across sessions.

## Installation

1. **Clone the Repository**:

   git clone https://github.com/yourusername/WalletWatch.git
   cd WalletWatch

## Set Up a Virtual Environment :

python3 -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`

## Install Dependencies:

pip install -r requirements.txt

## Usage

To run the WalletWatch application, use the following command:

## cd WalletWatch

Available Commands

## python main.py

When you run the application, you will be presented with the main menu where you can select various options:

WalletWatch - Main Menu

1. Add Transaction
2. List Transactions
3. Edit Transaction
4. Delete Transaction
5. Generate Summary
6. Exit
   Please select an option [1-6]: //you will get to choose from this 6 options

# Author

Mohamed Mowlid Ibrahim
