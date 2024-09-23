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

## Set Up a Virtual Environment (optional but recommended):

python3 -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`

## Install Dependencies:

pip install -r requirements.txt

## Usage

To run the WalletWatch application, use the following command:

## python main.py

Available Commands

## Add a Transaction:

## python main.py add

Follow the prompts to enter the transaction type, amount, and description.

## List Transactions:

## python main.py list

Displays all transactions stored in the database.

## Edit a Transaction:

## python main.py edit

Follow the prompts to enter the transaction ID and new details.

## Delete a Transaction:

## python main.py delete

Follow the prompt to enter the transaction ID to delete.

## Generate Summary:

## python main.py summary

Displays the total income, total expenses, and balance.

# Author

Mohamed Mowlid Ibrahim
