import click

from api import create_app

application = create_app(None)


@click.command('hi')
def hi():
    print('hi')


application.cli.add_command(hi, 'hi')
