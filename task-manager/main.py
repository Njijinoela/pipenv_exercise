import click
from db import init_db
from task import add_task, view_tasks

# Initialize the database when the app starts
init_db()

@click.group()
def cli():
    """Task Manager CLI."""
    pass

@click.command()
@click.argument('description')
@click.option('--status', default='Pending', help='The status of the task (default: Pending)')
def add(description, status):
    """Add a new task."""
    add_task(description, status)
    click.echo(f"Task added: {description} - {status}")

@click.command()
def show():
    """Show all tasks."""
    tasks = view_tasks()
    if tasks:
        for task in tasks:
            click.echo(f"ID: {task[0]}, Description: {task[1]}, Status: {task[2]}")
    else:
        click.echo("No tasks found.")

# Add the commands to the CLI
cli.add_command(add)
cli.add_command(show)

if __name__ == "__main__":
    cli()
