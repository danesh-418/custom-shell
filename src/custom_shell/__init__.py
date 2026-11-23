import cmd
import shlex
from functools import wraps

import click


class Shell(cmd.Cmd):
    def __init__(self, prompt=None, intro=""):
        super().__init__()
        self.prompt = prompt if not prompt is None else f"({__name__}) "
        self.intro = intro
    def run(self):
        self.cmdloop()
    def __setitem__(self, cmd_name: str, func: click.Command | click.Group):
        @wraps(func.callback)  # pyright: ignore[reportArgumentType]
        def wrapper(arg):
            try:
                func(shlex.split(arg), standalone_mode=False)
            except Exception as exc:
                if exc == KeyboardInterrupt:
                    raise

        setattr(self, f"do_{cmd_name}", wrapper)


if __name__ == "__main__":
    Shell().cmdloop()
