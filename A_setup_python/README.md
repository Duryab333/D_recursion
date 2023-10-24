# Assignment A: Setup Python &nbsp; (10 Pts)

This assignment will setup your base Python enviroment. If you already have it, simply run challenges and answer questions (if any). If you cannot run challenges, set up the needed software.


### Challenges
- [Challenge 1:](#1-challenge-terminal) Terminal
- [Challenge 2:](#2-challenge-python3) Python3
- [Challenge 3:](#3-challenge-pip) pip
- [Challenge 4:](#4-challenge-test-python) Test Python

Points: [4, 2, 2, 2]


&nbsp;
### 1.) Challenge: Terminal

If you are using *MacOS* or *Linux*, skip steps for *Windows*.

For *Windows*:

- Use a Unix emulator such as
[cygwin](https://www.cygwin.com),
the built-in Windows Subsystem for Linux
[WSL](https://learn.microsoft.com/en-us/windows/wsl/install)
or a
[Linux VM](https://ubuntu.com/tutorials/how-to-run-ubuntu-desktop-on-a-virtual-machine-using-virtualbox).

    - Windows *CMD.EXE* is no option and *Powershell* is not recommended since it is not compatible with Unix standards.

- Follow instructions for
[setting up *cygwin*](../Cygwin_setup.md),
in particular for:
  - switching from `/cygdrive/c` to `/c`
  - selecting your `HOME`-directory
  - configuring `.bashrc` in your `HOME`-directory and
  - defining `PATH` in `.bashrc`.

Open a terminal and type commands:
```sh
> cd                    # change to HOME-directory
> pwd                   # print path to working directory
> ls -la                # show content of HOME-directory
> whoami                # show user identity
> cat .profile              # file may not exist
> cat .bashrc               # for Mac, use .zshrc
> echo $PATH            # show PATH variable
```
Explain commands. If you are not familiar, find out about these basic Unix shell (bash, zsh, ...) commands (e.g. from [introduction](https://cs.lmu.edu/~ray/notes/bash) or 
[tutorial](https://linuxconfig.org/bash-scripting-tutorial-for-beginners)).

On *Mac*, use file *.zshrc* instead of *.bashrc*. If file does not exist
in the `HOME`-directory, it can be created as a text file using an editor.

Find out about
[ differences between](https://www.baeldung.com/linux/bashrc-vs-bash-profile-vs-profile)
`.profile` and `.bashrc` (Mac: `.zshrc`):
  - When is `.profile` executed?
  - When is `.bashrc` (Mac: `.zshrc`) executed?

(4 Pts)


&nbsp;
### 2.) Challenge: Python3
Check if you have Python 3 installed on your system. Name three differences between [Python 2 and 3](https://www.guru99.com/python-2-vs-python-3.html#7). 

Run commands in terminal (version 3.x.y may vary):
```sh
> python --version
Python 3.12.0
```

If you see error *command not found*, add path to Python installation to
PATH variable in `.bashrc` (Mac: `.zshrc`).

(2 Pts)


&nbsp;
### 3.) Challenge: pip
Check if you have a Python package manager installed (pip, conda, ... ). [`pip`](https://pip.pypa.io) is Python's default package manager to install additional Python packages and libraries.

Follow [instructions](https://pip.pypa.io/en/stable/installing) for installation:
- [download](https://bootstrap.pypa.io/get-pip.py) the `get-pip.py` file.
- run `python get-pip.py`
- or update pip to latest version: `python -m pip install --upgrade pip`

Run commands in terminal:
```
> pip --version
pip 23.2.1 from C:\Users\svgr2\AppData\Local\Programs\Python\Python312\Lib\site-
packages\pip (python 3.12)
```
(2 Pts)


&nbsp;
### 4.) Challenge: Test Python
Start Python in the terminal and execute commands:
```py
> python
Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.

>>> print('Hello World')
Hello World

>>> help('modules')
...lists installed python packages

>>> 2+3*4
14

>>> x = 2+3*4
>>> x
14
```

Create a file *print_sys.py* with following content.
```py
import platform

impl = platform.python_implementation()
ver = platform.version()
mach = platform.machine()
sys = platform.system()

print('Python impl:    ' + impl)
print('Python version: ' + ver)
print('Python machine: ' + mach)
print('Python system:  ' + sys)
print('Python version: ' + platform.python_version())
```

Run file *print_sys.py*. Output varies depending on your system.
```
> python print_sys.py
Python impl:    CPython
Python version: 10.0.19045
Python machine: AMD64
Python system:  Windows
Python version: 3.12.0
```
(2 Pts)
