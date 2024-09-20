from models import Transaction
from database import session


def add_transaction(type, amount, description):
    transaction = Transaction(
        type=type, amount=amount, description=description)
    session.add(transaction)
    session.commit()


def get_transactions():
    return session.query(Transaction).all()


def edit_transaction(transaction_id, type=None, amount=None, description=None):
    transaction = session.query(Transaction).filter_by(
        id=transaction_id).first()
    if transaction:
        if type:
            transaction.type = type
        if amount:
            transaction.amount = amount
        if description:
            transaction.description = description
        session.commit()


def delete_transaction(transaction_id):
    transaction = session.query(Transaction).filter_by(
        id=transaction_id).first()
    if transaction:
        session.delete(transaction)
        session.commit()


def get_summary():
    transactions = get_transactions()
    total_income = sum(t.amount for t in transactions if t.type == 'income')
    total_expenses = sum(t.amount for t in transactions if t.type == 'expense')
    balance = total_income - total_expenses
    return total_income, total_expenses, balance
