import os
import sys

import click


@click.command()
@click.argument("exit_code", help="The exit code to exit with", default=0)
def exit(exit_code):
    """Exits"""
    sys.exit(exit_code)

@click.command()
@click.argument("text", help="The text to echo", default="")
def echo(text):
    """Echoes the specified text"""
    click.echo(text)

@click.command()
@click.argument("directory", help="The directory to list", default=".", type=click.Path(file_okay=False, dir_okay=True, exists=True))
def ls(directory):
    """Lists the contents of a directory"""
    click.echo("\n".join(os.listdir(directory)))
