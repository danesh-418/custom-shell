import apps.os_utils

from custom_shell import Shell

shell = Shell()

shell["exit"] = apps.os_utils.exit
shell["ls"] = apps.os_utils.ls
shell["echo"] = apps.os_utils.echo

shell.run()
