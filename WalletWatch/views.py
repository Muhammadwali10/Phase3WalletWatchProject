import click
from controllers import add_transaction, get_transactions, edit_transaction, delete_transaction, get_summary


@click.group()
def cli():
    pass


def main_menu():
    while True:
        click.echo("\nWalletWatch - Main Menu")
        click.echo("1. Add Transaction")
        click.echo("2. List Transactions")
        click.echo("3. Edit Transaction")
        click.echo("4. Delete Transaction")
        click.echo("5. Generate Summary")
        click.echo("6. Exit")

        choice = click.prompt("Please select an option", type=int)

        if choice == 1:
            add()
        elif choice == 2:
            list()
        elif choice == 3:
            edit()
        elif choice == 4:
            delete()
        elif choice == 5:
            summary()
        elif choice == 6:
            click.echo("Exiting WalletWatch. Goodbye!")
            break
        else:
            click.echo("Invalid option. Please try again.")


@cli.command()
@click.option('--type', prompt='Transaction type (income/expense)', help='Type of transaction')
@click.option('--amount', prompt='Amount', type=float, help='Amount of transaction')
@click.option('--description', prompt='Description', help='Description of transaction')
def add(type, amount, description):
    add_transaction(type, amount, description)
    click.echo('Transaction added successfully.')


@cli.command()
def list():
    transactions = get_transactions()
    for t in transactions:
        click.echo(
            f'{t.id}: {t.type} - {t.amount} - {t.description} - {t.date}')


@cli.command()
@click.option('--id', prompt='Transaction ID', type=int, help='ID of the transaction to edit')
@click.option('--type', prompt='New transaction type (income/expense)', help='New type of transaction')
@click.option('--amount', prompt='New amount', type=float, help='New amount of transaction')
@click.option('--description', prompt='New description', help='New description of transaction')
def edit(id, type, amount, description):
    edit_transaction(id, type, amount, description)
    click.echo('Transaction updated successfully.')


@cli.command()
@click.option('--id', prompt='Transaction ID', type=int, help='ID of the transaction to delete')
def delete(id):
    delete_transaction(id)
    click.echo('Transaction deleted successfully.')


@cli.command()
def summary():
    total_income, total_expenses, balance = get_summary()
    click.echo(f'Total Income: {total_income}')
    click.echo(f'Total Expenses: {total_expenses}')
    click.echo(f'Balance: {balance}')


if __name__ == '__main__':
    cli()
