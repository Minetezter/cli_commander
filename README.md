# cli-commander

CLI commander is an easy-to-use python library for running CLI commands.
All commands are supported on Linux Mint 21, and some commands are supported on other
systems too.

**Very good packge! You can actually get the output of commands,
assign command output to variables,
print command output, and more!**

# Pip installation:
**Run this in your command prompt/shell:**

```
pip install cli_commander
```

# Importing cli-commander

How to import cli-commander with no issues:

```python
import cli_commander.commands
```

# cli-commander venv

Create a new virtual environment like this:

```python
import cli_commander.commands as cli

cli.venv("MyExampleVenv").new()
```

Get into an existing virtual environment like this:

```python
import cli_commander.commands as cli

cli.venv("MyExampleVenv").new()
```

You can leave a virtual environment using the venv.leave() function.
Example:

```python
import cli_commander.commands as cli

myVenv = cli.venv("MyExampleVenv").enter()
myVenv.leave()
```

# Need help with the 98 more functions?

**Run this:**

```python
import cli_commander.commands as cli
help(cli)
```

# Thank you
