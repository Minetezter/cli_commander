import os
import random

def GET_CLI_OUTPUT(command):
    rand = hex(random.randint(100001, 999998))

    os.system(f"{command} > {rand}.txt")

    fs = open(f"{rand}.txt", 'rb')
    out = fs.read()
    fs.close()

    os.remove(f"{rand}.txt")

    return out


def curl(url):
    '''Runs C URL/curl Linux command. Basically for making HTTP/1.1 requests, but uses Linux commands.
    Automatically sends a GET request, but that can be changed with the curlCom() function.'''
    return GET_CLI_OUTPUT(f"curl {url}")


def curlCom(command):
    '''Same as the curl() function, but if you want to change the method from GET, you can use this.'''
    return GET_CLI_OUTPUT(f"curl {command}")


def alias(command=""):
    '''You can run the Linux alias command. 
    You can also input specific alias commands and add arguments.'''
    return GET_CLI_OUTPUT(f"alias {command}")


def alias_p(command=""):
    '''Same as the alias command, but automatically adds the argument "-p".'''
    return GET_CLI_OUTPUT(f"alias -p {command}")


def write(username, tty):
    '''runs the Linux write command, and automatically adds the arguments ("username" and "TTY").
    Used for chatting with users. Very simple and easy to use. Does not allow the "options" argument.'''
    command = "write " + username + " " + tty
    os.system(command)


def exit():
    '''Runs the python 3 Linux exit() command.
    Because using os.system() for running the "exit()" command does not work well,
    so this just exits.'''
    exit()


def ip_addr():
    '''Runs the Linux "ip addr" command.
    Returns the host's IP address, along with a liitle more data.
    Very simple function.'''
    return GET_CLI_OUTPUT("ip addr")


def man(item):
    '''Runs the Linux "man" command, which returns the description of the given command.'''
    os.system("man " + item)


def venv(venvname):
    '''Creates a Linux virtual environment.
    You can use the command "cli_commander.venv(<venv name>).new()", to create a new virtual environment.
    You can use the command "cli_commander.venv(<venv name>).enter()", to enter an existing virtual environment.'''
    class opt:
        def new():
            '''Create a new virtual environment.'''
            os.system(f"python3 -m venv {venvname}")
            os.system(f"cd {venvname}")
            os.system("source bin/activate")
            
            class venvoptions:
                def leave():
                    os.system("deactivate")
            
            return venvoptions
        
        def enter():
            '''Enter an existing virtual environment.'''
            os.system(f"cd ./{venvname}")
            os.system("source bin/activate")
            
            class venvoptions:
                def leave():
                    return os.system("deactivate")
            
            return venvoptions
    
    return opt


def w(user=""):
    '''Runs the Linux "w" command with the "user" argument set to the given user.
    You do not have to enter a value for the "user" argument, because it automatically gets set to null.'''
    return GET_CLI_OUTPUT(f'w {user}')


def pip_install(library):
    '''Tries to run Linux "pip install" command on the given library.
    Should work, if the conditions are right.'''
    os.system(f"pip install {library}")


def pip_search(library):
    '''Tries to run the Linux "pip search" command, although it may be down forever.'''
    os.system(f"pip search {library}")


def pip_help(library):
    '''Runs the Linux "pip help" command, on the given library.'''
    os.system(f"pip help {library}")


def PIP(mode, library):
    '''Runs the given "pip" command, on the given library.'''
    os.system(f"pip {mode} {library}")


def get_help(obj):
    '''Normally works. Will only not work if the given command does not have the property "--help".'''
    return GET_CLI_OUTPUT(f"{obj} --help")


def vim(vimname):
    '''Creates a vim file of the given name. for example, you can run vim("main.py").
    This creates the local file "main.py". Run man("vim") for more info.'''
    os.system(f"vim {vimname}")


def vi(viname):
    '''Runs the Linux "v" command.
    Basically an old-fashioned vim. I would recommend vim.'''
    os.system(f"vi {vimname}")


def wall():
    '''Runs the "wall" command.
    Similar to the "write" command, but your message gets sent to everyone.'''
    os.system("wall")


def which(item):
    '''Runs the "which" command.
    Shows the file path to a command.'''
    return GET_CLI_OUTPUT(f"which {item}")


def enterPathOf(*path):
    '''Opens a file path.'''
    endPath = path[0]
    
    if len(path) > 1:
      endPath = ""
      for i in path:
          endPath += f"/{i}"
    
    os.system(endPath)


def wCom(command):
    '''Runs the given properties of the "w" command'''
    return GET_CLI_OUTPUT(f"w -{command}")


def ipCom(command):
    '''Runs the given properties of the "ip" command
    In my opinion, a very useful funcion/command.'''
    return GET_CLI_OUTPUT(f"ip {command}")


def ip_address():
    '''Runs the Linux "ip address" command.
    An attribute of the "ip" command. Does the same as the "ip addr" command.'''
    return GET_CLI_OUTPUT("ip address")


def ip_addrlabel():
    '''Runs the Linux "ip addrlabel" command.
    An attribute of the "ip" command.'''
    return GET_CLI_OUTPUT("ip addrlabel")


def ip_fou():
    '''Runs the Linux "ip fou" command.
    An attribute of the "ip" command.'''
    return GET_CLI_OUTPUT("ip fou")


def ip_help():
    '''Runs the Linux "ip help" command.
    An attribute of the "ip" command.'''
    return GET_CLI_OUTPUT("ip help")


def ip_ila():
    '''Runs the Linux "ip ila" command.
    An attribute of the "ip" command.'''
    return GET_CLI_OUTPUT("ip ila")


def ip_ioam():
    '''Runs the Linux "ip ioam" command.
    An attribute of the "ip" command.'''
    return GET_CLI_OUTPUT("ip ioam")


def ip_l2tp():
    '''Runs the Linux "ip 12tp" command.
    An attribute of the "ip" command.'''
    return GET_CLI_OUTPUT("ip l2tp")


def ip_macsec():
    '''Runs the Linux "ip macsec" command.
    An attribute of the "ip" command.'''
    return GET_CLI_OUTPUT("ip macsec")


def ip_maddress():
    '''Runs the Linux "ip maddress" command.
    An attribute of the "ip" command.'''
    return GET_CLI_OUTPUT("ip maddress")


def ip_monitor():
    '''Runs the Linux "ip monitor" command.
    An attribute of the "ip" command.'''
    return GET_CLI_OUTPUT("ip monitor")


def ip_ntable():
    '''Runs the Linux "ip ntable" command.
    An attribute of the "ip" command.'''
    return GET_CLI_OUTPUT("ip ntable")


def python3():
    '''Runs the Linux "python3" command.
    Allows you to run python commands inside python. Runs the version the system is running'''
    os.system("python3")


def python_file(file):
    '''Runs a python file.
    Runs the file of the single argument "file". Vim files are normally callable using this command.'''
    os.system(f"python {file}")


def cpp():
    '''Runs the Linux "cpp" command.
    Basically allows you to run C++ in python.'''
    os.system("cpp")


def dirs():
    '''Runs the Linux "dirs" command.
    Displays the file path you are in.'''
    return GET_CLI_OUTPUT("dirs")


def dir():
    '''Runs the Linux dir command.
    I would use the ls command instead. These two commands are very similar.'''
    return GET_CLI_OUTPUT("dir")


def printf(arg):
    '''This function runs the Linux BASH "printf <arguments>" command.
    Prints the value of the single argument "arg".'''
    return GET_CLI_OUTPUT(f"printf '{arg}'")


def echo(arg):
    '''Runs the Linux BASH "echo()" command.
    Very similar to the "printf" BASH function/command.'''
    return GET_CLI_OUTPUT(f'echo "{arg}"')


def times():
    '''Runs the Linux "times" command.
    Very easy to use, with no arguments.'''
    return GET_CLI_OUTPUT("times")


def pwd():
    '''Runs the "pwd" Linux command.
    Displays the file/directory you are in.'''
    return GET_CLI_OUTPUT("pwd")


def type(command):
    '''Runs the Linux "Type" command.
    Shows the FULL path to the given command.'''
    return GET_CLI_OUTPUT(f"type {command}")


def jobs(obj):
    '''Runs the Linux "jobs" command on the given object.'''
    return GET_CLI_OUTPUT(f"jobs {obj}")


def ulimit(case=""):
    '''Runs the Linux ulimit command.
    Has one optional argument ("case"). If it works, it should display "Unlimited" on the screen.'''
    return GET_CLI_OUTPUT(f"ulimit {case}")


def TRUE():
    '''Executes true. Normally useless.'''
    return GET_CLI_OUTPUT("true")


def FALSE():
    '''Executes false. Normally useless.'''
    return GET_CLI_OUTPUT("false")


def call_if(args):
    '''Calls the Linux BASH "if" command.
    Because I do not include a lot of BASH functions, This is normally not usable.'''
    return GET_CLI_OUTPUT(f"if {args} then")


def w_h():
    '''Runs the Linux "w -h" command.
    An attribute of the "w" command.'''
    return GET_CLI_OUTPUT("w -h")


def w_u():
    '''Runs the Linux "w -u" command.
    An attribute of the "w" command.'''
    return GET_CLI_OUTPUT("w -u")


def w_s():
    '''Runs the Linux "w -s" command.
    An attribute of the "w" command.'''
    return GET_CLI_OUTPUT("w -s")


def w_f():
    '''Runs the Linux "w -f" command.
    An attribute of the "w" command.'''
    return GET_CLI_OUTPUT("w -f")


def w_o():
    '''Runs the Linux "w -o" command.
    An attribute of the "w" command.'''
    return GET_CLI_OUTPUT("w -o")


def w_i():
    '''Runs the Linux "w -i" command.
    An attribute of the "w" command.'''
    return GET_CLI_OUTPUT("w -i")


def version(obj):
    '''Tries to get the version of an command/object.
    Normally fails.'''
    return GET_CLI_OUTPUT(f"{obj} -V")


def source(file):
    '''Runs the Linux "source" command.
    Can never read binary files. Very useful command.'''
    os.system(f"source {file}")


def alt(command):
    '''Runs commands that are not as separate functions.'''
    os.system(command)


def uname():
    '''Runs the Linux "uname" command.
    Returns the platform your on. Use the "uname_a()" function to get your full username, platform, version, and more!'''
    return GET_CLI_OUTPUT("uname")


def uname_a():
    '''Runs the Linux "uname -a" command.
    An attribute of the "uname" command. Very recommended!'''
    return GET_CLI_OUTPUT("uname -a")


def uname_s():
    '''Runs the Linux "uname -s" command.
    An attribute of the "uname" command.'''
    return GET_CLI_OUTPUT("uname -s")


def uname_n():
    '''Runs the Linux "uname -n" command.
    An attribute of the "uname" command.'''
    return GET_CLI_OUTPUT("uname -n")


def uname_r():
    '''Runs the Linux "uname -r" command.
    An attribute of the "uname" command.'''
    return GET_CLI_OUTPUT("uname -r")


def uname_v():
    '''Runs the Linux "uname -v" command.
    An attribute of the "uname" command.'''
    return GET_CLI_OUTPUT("uname -v")


def uname_m():
    '''Runs the Linux "uname -m" command.
    An attribute of the "uname" command.'''
    return GET_CLI_OUTPUT("uname -m")


def uname_p():
    '''Runs the Linux "uname -p" command.
    An attribute of the "uname" command.'''
    return GET_CLI_OUTPUT("uname -p")


def uname_i():
    '''Runs the Linux "uname -i" command.
    An attribute of the "uname" command.'''
    return GET_CLI_OUTPUT("uname -i")


def uname_o():
    '''Runs the Linux "uname -o" command.
    An attribute of the "uname" command.'''
    return GET_CLI_OUTPUT("uname -o")


def unameCom(command):
    '''Runs the given property of the "uname" command.'''
    return GET_CLI_OUTPUT(f"uname {command}")


def ls():
    '''Runs the Linux "ls" command.
    Very similar to the "dir" command, but I recommend using this instead.'''
    return GET_CLI_OUTPUT("ls")


def lsCom(command):
    '''Runs the given property of the "ls" command.'''
    return GET_CLI_OUTPUT(f"ls {command}")


def bash():
    '''Runs the Linux "bash" command.'''
    os.system("bash")


def sh():
    '''Runs the Linux "sh" command.
    One of my favorites from cli_commander. I really recommend it!'''
    os.system("sh")


def env():
    '''Displays data about your environment.
    Very useful and easy to use!'''
    return GET_CLI_OUTPUT("env")


def edit():
    '''Runs the Linux "edit" command.'''
    os.system("edit")


def edit_action(file):
    '''Runs the Linux "edit action" command.
    An attribute of the "edit" command. Has one argument, "file".'''
    os.system(f"edit {file}")


def editCom(command):
    '''Runs the given property of the "edit" command.'''
    os.system(f"edit {command}")


def install_d(directory):
    '''Runs the Linux "install -d" command.
    An attribute of the "install" command. One argument "directory". Works the same as the Linux command.'''
    os.system(f"install -d {directory}")


def install_D():
    '''Runs the Linux "install -D" command.
    An attribute of the "install" command.'''
    os.system(f"install -D")


def install_g(group):
    '''Runs the Linux "install -g" command.
    An attribute of the "install" command. One argument "group". Works the same as the Linux command.'''
    os.system(f"install -g group={group}")


def install_m(mode):
    '''Runs the Linux "install -m" command.
    An attribute of the "install" command. One argument "mode". Works the same as the Linux command.'''
    os.system(f"install -m mode={mode}")


def install_o(owner):
    '''Runs the Linux "install -o" command.
    An attribute of the "install" command. One argument "owner". Works the same as the Linux command.'''
    os.system(f"install -g owner={owner}")


def install_p(preserve_timestamps):
    '''Runs the Linux "install -p" command.
    An attribute of the "install" command. One argument "preserve_timestamps". Works the same as the Linux command.'''
    os.system(f"install -p {preserve_timestamps}")


def install_s(strip):
    '''Runs the Linux "install -s" command.
    An attribute of the "install" command. One argument "strip". Works the same as the Linux command.'''
    os.system(f"install -s {strip}")


def install_S(suffix):
    '''Runs the Linux "install -S" command.
    An attribute of the "install" command. One argument "suffix". Works the same as the Linux command.'''
    os.system(f"install -p suffix={suffix}")


def install_t(target_directory):
    '''Runs the Linux "install -t" command.
    An attribute of the "install" command. One argument "target_directory". Works the same as the Linux command.'''
    os.system(f"install -t target_directory={target_directory}")


def install_T(no_target_directory):
    '''Runs the Linux "install -T" command.
    An attribute of the "install" command. One argument "no_target_directory". Works the same as the Linux command.'''
    os.system(f"install -T {no_target_directory}")


def install_Z():
    '''Runs the Linux "install -Z" command.
    An attribute of the "install" command.'''
    os.system(f"install -Z")


def installCom(command):
    '''Runs the given property of the "install" command.'''
    os.system(f"install {command}")


def ssh():
    '''Runs the ssh command'''
    return GET_CLI_OUTPUT("ssh")


def sshCom(command):
    '''Runs the given ssh property.'''
    os.system(f"ssh {command}")


def zipCom(command):
    '''Runs the given zip property'''
    return GET_CLI_OUTPUT(f"zip {command}")


def commandCom(command):
    '''Runs the given command property'''
    return GET_CLI_OUTPUT(f"command {command}")


def command_v(arg):
    '''Runs the Linux "command -v" command.
    An attribute of the "command" command. One argument "arg". Works the same as the Linux "command" command.'''
    return GET_CLI_OUTPUT(f"command -v {arg}")


def command_V(arg):
    '''Runs the Linux "command -V" command.
    An attribute of the "command" command. One argument "arg". Works the same as the Linux "command" command.'''
    return GET_CLI_OUTPUT(f"command -V {arg}")


def command_p(arg):
    '''Runs the Linux "command -p" command.
    An attribute of the "command" command. One argument "arg". Works the same as the Linux "command" command.'''
    return GET_CLI_OUTPUT(f"command -p {arg}")


def unminimize():
    '''Runs the "unminimize" command.'''
    os.system("unminimize")


def ls_all():
    '''Runs the Linux "ls -all" command.
    Very useful.'''
    return GET_CLI_OUTPUT("ls -all")


def mtr(ip, mode=""):
    '''Runs the Linux "mtr" command!
    Very recommended! Very useful! Track IP addresses, and more!'''
    return GET_CLI_OUTPUT(f"mtr {mode} {ip}")


def logname():
    '''Gets your username.'''
    return GET_CLI_OUTPUT("logname")

def mkdir(dirname):
    '''Runs the linux 'mkdir' command.
    Creates a new directory of the given name.'''
    os.system(f"mkdir {dirname}")

def history():
    '''Runs the history command. Allows you to view a long history of commands you've run.'''
    return GET_CLI_OUTPUT("history")

def mv(start, dest):
    '''Runs the Linux mv [filename] [filename] command.
    Lets you move files.'''
    os.system(f"mv {start} {dest}")

def rm(file):
    '''Removes the given file.'''
    os.system(f"rm {file}")

def sudo(args):
    '''Runs the Linux "sudo [command]" command.
    Pretty useful.'''
    return GET_CLI_OUTPUT(f"sudo {args}")

def ping(address):
    '''Runs the linux ping command.
    Very useful.'''
    return GET_CLI_OUTPUT(f"ping {address}")

def sudo_apt_install(arg):
    '''Installs software.'''
    os.system(f"sudo apt install {arg}")

def sudo_aptget_install(arg):
    '''Also installs software. mostly for systems other than Linux'''
    os.system(f"sudo apt-get install {arg}")

def tcpdump(address):
    '''Runs the tcpdump command! Very useful and highly recommanded!'''
    os.system(f"sudo tcpdump {address}")

def tcpdump_w(address, file):
    '''Runs the tcpdump command! Very useful and highly recommanded!'''
    os.system(f"sudo tcpdump {address} -w {file}")

def tcpdump_r(address, file):
    '''Runs the tcpdump command! Very useful and highly recommanded!'''
    os.system(f"sudo tcpdump {address} -r {file}")

def sudo_reboot():
    '''Runs the sudo reboot Linux command.'''
    os.system("sudo reboot")

def ifconfig(name):
    """Runs the Linux ifconfig command.
    Gets addresses. Really good!"""
    return GET_CLI_OUTPUT(f"ifconfig {name}")

def date(args=""):
    """Gets the current date."""
    return GET_CLI_OUTPUT(f"date {args}")
