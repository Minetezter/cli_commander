# cli-commander

CLI commander is an easy-to-use python library for running CLI commands.
All commands are supported on Linux Mint 21, and some commands are supported on other
systems too.

# Pip installation:
**Run this in your command prompt/shell:**

```
pip install cli_commander
```

# Importing cli-commander

How to import cli-commander with no issues:

```python
from cli_commander import commands
```

# cli-commander venv

Create a new virtual environment like this:

```python
from cli_commander import commands as cli

cli.venv("MyExampleVenv").new()
```

Get into an existing virtual environment like this:

```python
from cli_commander import commands as cli

cli.venv("MyExampleVenv").new()
```

You can leave a virtual environment using the venv.leave() function.
Example:

```python
from cli_commander import commands as cli

myVenv = cli.venv("MyExampleVenv").enter()
myVenv.leave()
```

# Need help with the 98 more functions?

**Run this:**

```python
from cli_commander import commands as cli
help(cli)
```

# Thank you
