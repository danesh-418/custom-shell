# custom-shell

A python library that allows you to make shells.

## Installation

```shell
uv pip install git+https://github.com/danesh-418/custom-shell
```

## Usage

See [the example](examples/ex1).

### Walkthrough

First, create a `Shell` object (with an optional prompt and intro text):
```python
from custom_shell import Shell

shell = Shell(prompt="> ", intro="Welcome to the shell!")
```
Next, create apps using [`click`](https://click.palletsprojects.com/en/stable/):
```python
import click

@click.command()
def hello_world():
    click.echo("Hello World!")
```
Then assign the commands to names:
```python
shell["hello"] = hello_world
```
Finally, run the shell:
```python
shell.run()
```
