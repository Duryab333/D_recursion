# Cygwin setup on *Windows*

[Cygwin](https://www.cygwin.com) is a Unix-Emulator that provides
a terminal in which Unix commands can be executed on Windows 
using
[bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell))
(*Bourne Again Shell*) as command-line interpreter -
*bash* was developed in 1989 as a successor to the
*Bourne Shell:*
*[sh](https://en.wikipedia.org/wiki/Bourne_shell)*.


[<bash terminal>](https://cdn.ttgtmedia.com/rms/onlineimages/REF_bash_command_line_3.jpg)


*Cygwin* is <span style="text-decoration:underline">not</span>
a Unix container or virtual machine system (unlike
[WSL](https://learn.microsoft.com/en-us/windows/wsl/about)).
*Cygwin* emulates most (not all) Unix system calls such that
most Unix commands can execute on Windows.

Alternatives to *Cygwin* such as
[GitBash]()
can be used, but have some flaws and drawbacks on Windows
(*GitBash*, for example, performs strange path conversions, see
[link](https://stackoverflow.com/questions/54258996/git-bash-string-parameter-with-at-start-is-being-expanded-to-a-file-path)).

Good introductions to *bash* are:

- [https://cs.lmu.edu/~ray/notes/bash](https://cs.lmu.edu/~ray/notes/bash).

- Also recommended is the 
[Tutorial for Beginners](https://linuxconfig.org/bash-scripting-tutorial-for-beginners).


&nbsp;
## Steps
1. [Installation](#1-installation)
2. [Configure paths in .bashrc](#2-configure-paths-in-bashrc)


&nbsp;
## 1. Installation

1. Download the installer `setup-x86_64.exe` from
[https://www.cygwin.com/install.html](https://www.cygwin.com/install.html).


1. Run the installer `setup-x86_64.exe`.

    - select useful Unix commands during installation:
        - Editors/`vim` - visual editor,
        - Web/`wget` - web downloader,
        - Net/`curl` - web downloader.


1. Change *cygwin* default path `/cygdrive/c` to: `/c`:

    - navigate to the *cygwin* installation directory.

    - inside, edit `/etc/fstab` and replace line
        ```
        none /cygdrive cygdrive binary,posix=0,user 0 0
        with:
        none / cygdrive binary,posix=0,user 0 0
        ```


1. Add bash-user that works with Windows and create
   *bash* HOME directory.

    - Find out your Windows user name: <user_name>

    - Create or select a directory that you want to use as
      HOME-directory for *bash*, e.g. your Windows
      HOME-directory `C:\Users\<user_name>`.

    - Edit file `/etc/nsswitch.conf`:
        - to use the Windows HOME-directory, comment line
            ```
            #db_home:
            ```
        - for using a different directory as HOME-directory, enter
            ```sh
            db_home: /c/<path>      # e.g. db_home: /c/users/svgr
            ```


1. Open a new *bash* terminal and test changes:

    ```sh
    $ whoami
    <user_name>         # your user name appears

    $ echo $HOME        # print path to HOME-directory
    <home_directory>    # output, e.g. /c/Users/svgr

    $ cd $HOME          # change into HOME-directory
    $ ls -la            # show content
    total 203
    drwxr-xr-x+ 1 svgr2 Kein      0 Oct  4 22:20 .
    drwxrwx---+ 1 svgr2 Kein      0 Jan  1  2022 ..
    -rw-------  1 svgr2 Kein  14476 Oct  4 22:20 .bash_history
    -rwxr-xr-x+ 1 svgr2 Kein   2717 Oct  4 20:28 .bashrc
    ...

    $ echo Hello >hello.txt     # create file hello.txt with content Hello
    $ ls -la                    # show new file exists in $HOME
    total 203
    -rw-r--r--  1 svgr2 Kein      6 Oct  7 23:38 hello.txt
    ...

    $ cat hello.txt             # output content of file
    Hello
    ```


1. Open Windows file explorer (
    [ ? ](https://geekflare.com/wp-content/uploads/2021/06/14-alternative-file-managers-to-replace-windows-10-file-explorer.jpg)
    ) and navigate to file `hello.txt`.
    Open the file by clicking (ending `.txt` should open the
    file with *notepad*).


1. Return to *bash* terminal:
    - change to HOME-directory and
    - open file `.bashrc`
        ```sh
        $ cd            # change to bash HOME-directory
        $ ls -la        # find file .bashrc
        total 203
        -rwxr-xr-x+ 1 svgr2 Kein   2717 Oct  4 20:28 .bashrc

        $ cat .bashrc   # output file .bashrc
        ...
        ```


&nbsp;
## 2. Configure paths in `.bashrc`

[PATH](https://en.wikipedia.org/wiki/PATH_(variable)) is an
environment variable on Unix-like operating systems that
specifys a set of directories where executable programs are
located. A *"command not found"* error occurs when PATH is
not properly configured.

1. Open `.bashrc` using an editor such as
    *[sublime](https://www.sublimetext.com)* or
    *[vim](https://www.vim.org)* (select in *cygwin* setup)
    and append lines for PATH configurations.
    ```sh
    $ vim .bashrc       # open file .bashrc in vim editor
    ```

1. Append PATH configurations at the end of the file - only
    those relevant on your system - and djust paths for your
    system:

    ```sh
    # add Windows system paths
    export PATH=".:/usr/bin:/usr/local/bin"
    export PATH="${PATH}:$(cygpath ${SYSTEMROOT}):$(cygpath ${SYSTEMROOT})/system32"

    # if Java, add Java path
    export JAVA_HOME="/c/Program Files/Java/jdk-21"
    export PATH="${PATH}:${JAVA_HOME}/bin"

    # if Python, add Python path
    export PYTHON_HOME="/c/Users/svgr2/AppData/Local/Programs/Python/Python312"
    export PATH="${PATH}:${PYTHON_HOME}"
    export PATH="${PATH}:${PYTHON_HOME}/Scripts"

    # if Docker, add Docker path
    export DOCKER_HOME="/c/Program Files/Docker/Docker"
    export PATH="${PATH}:${DOCKER_HOME}/resources/bin"
    ...
    ```

1. Verify paths have been added to *PATH* variable:
    ```sh
    $ source .bashrc    # reload .bashrc to activate PATH definitions
    $ echo ${PATH}                      # show PATH
    .:/usr/bin:/usr/local/bin:/c/WINDOWS:/c/WINDOWS/system32:/c/Program ...

    $ echo ${$PATH} | tr ':' '\n'       # pretty print PATH
    .
    /usr/bin
    /usr/local/bin
    /c/WINDOWS
    /c/WINDOWS/system32
    /c/Program Files/Java/jdk-21/bin
    /c/opt/maven/bin
    /c/Users/svgr2/AppData/Local/Programs/Python/Python312
    /c/Users/svgr2/AppData/Local/Programs/Python/Python312/Scripts
    /c/Program Files/Docker/Docker/resources/bin
    /c/Program Files/MySQL/MySQL Workbench 8.0 CE
    /c/Program Files (x86)/Git/bin
    /c/Program Files/Oracle/VirtualBox
    /c/opt/Qt6/Tools/mingw1120_64/bin
    /c/opt/Qt6/6.2.4/mingw_64/bin
    ```
    Paths may vary based on your system.


1. Start programs to verify paths have properly been set.

    ```sh
    $ java --version
    java 21 2023-09-19 LTS
    Java(TM) SE Runtime Environment (build 21+35-LTS-2513)
    Java HotSpot(TM) 64-Bit Server VM (build 21+35-LTS-2513, mixed mode, sharing)

    $ python --version
    Python 3.12.0

    $ docker --version
    Docker version 24.0.6, build ed223bc
    ```
