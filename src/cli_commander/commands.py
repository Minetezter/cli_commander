from os import system
from sys import exit as ex

def curl(url):
    '''Runs C URL/curl Linux command. Basically for making HTTP/1.1 requests, but uses Linux commands.
    Automatically sends a GET request, but that can be changed with the curlCom() function.'''
    system(f"curl {url}")


def curlCom(command):
    '''Same as the curl() function, but if you want to change the method from GET, you can use this.'''
    system(f"curl {command}")


def alias(command=""):
    '''You can run the Linux alias command. 
    You can also input specific alias commands and add arguments.'''
    system(f"alias {command}")


def alias_p(command=""):
    '''Same as the alias command, but automatically adds the argument "-p".'''
    system(f"alias -p {command}")


def write(username, tty):
    '''runs the Linux write command, and automatically adds the arguments ("username" and "TTY").
    Used for chatting with users. Very simple and easy to use. Does not allow the "options" argument.'''
    command = "write " + username + " " + tty
    system(command)


def exit():
    '''Runs the python 3 Linux exit() command.
    Because using os.system() for running the "exit()" command does not work well,
    this actually uses the sys module.'''
    ex()


def ip_addr():
    '''Runs the Linux "ip addr" command.
    Returns the host's IP address, along with a liitle more data.
    Very simple function.'''
    system("ip addr")


def man(item):
    '''Runs the Linux "man" command, which returns the description of the given command.'''
    system("man " + item)


def venv(venvname):
    '''Creates a Linux virtual environment.
    You can use the command "cli_commander.venv(<venv name>).new()", to create a new virtual environment.
    You can use the command "cli_commander.venv(<venv name>).enter()", to enter an existing virtual environment.'''
    class opt:
        def new():
            '''Create a new virtual environment.'''
            system(f"python3 -m venv {venvname}")
            system(f"cd {venvname}")
            system("source bin/activate")
            
            class venvoptions:
                def leave():
                    system("deactivate")
            
            return venvoptions
        
        def enter():
            '''Enter an existing virtual environment.'''
            system(f"cd ./{venvname}")
            system("source bin/activate")
            
            class venvoptions:
                def leave():
                    system("deactivate")
            
            return venvoptions
    
    return opt


def w(user=""):
    '''Runs the Linux "w" command with the "user" argument set to the given user.
    You do not have to enter a value for the "user" argument, because it automatically gets set to null.'''
    system(f'w {user}')


def pip_install(library):
    '''Tries to run Linux "pip install" command on the given library.
    Should work, if the conditions are right.'''
    system(f"pip install {library}")


def pip_search(library):
    '''Tries to run the Linux "pip search" command, although it may be down forever.'''
    system(f"pip search {library}")


def pip_help(library):
    '''Runs the Linux "pip help" command, on the given library.'''
    system(f"pip help {library}")


def PIP(mode, library):
    '''Runs the given "pip" command, on the given library.'''
    system(f"pip {mode} {library}")


def get_help(obj):
    '''Normally works. Will only not work if the given command does not have the property "--help".'''
    system(f"{obj} --help")


def vim(vimname):
    '''Creates a vim file of the given name. for example, you can run vim("main.py").
    This creates the local file "main.py". Run man("vim") for more info.'''
    system(f"vim {vimname}")


def vi(viname):
    '''Runs the Linux "v" command.
    Basically an old-fashioned vim. I would recommend vim.'''
    system(f"vi {vimname}")


def wall():
    '''Runs the "wall" command.
    Similar to the "write" command, but your message gets sent to everyone.'''
    system("wall")


def which(item):
    '''Runs the "which" command.
    Shows the file path to a command.'''
    system(f"which {item}")


def enterPathOf(*path):
    '''Opens a file path.'''
    endPath = path[0]
    
    if len(path) > 1:
      endPath = ""
      for i in path:
          endPath += f"/{i}"
    
    system(endPath)


def wCom(command):
    '''Runs the given properties of the "w" command'''
    system(f"w -{command}")


def ipCom(command):
    '''Runs the given properties of the "ip" command
    In my opinion, a very useful funcion/command.'''
    system(f"ip {command}")


def ip_address():
    '''Runs the Linux "ip address" command.
    An attribute of the "ip" command. Does the same as the "ip addr" command.'''
    system("ip address")


def ip_addrlabel():
    '''Runs the Linux "ip addrlabel" command.
    An attribute of the "ip" command.'''
    system("ip addrlabel")


def ip_fou():
    '''Runs the Linux "ip fou" command.
    An attribute of the "ip" command.'''
    system("ip fou")


def ip_help():
    '''Runs the Linux "ip help" command.
    An attribute of the "ip" command.'''
    system("ip help")


def ip_ila():
    '''Runs the Linux "ip ila" command.
    An attribute of the "ip" command.'''
    system("ip ila")


def ip_ioam():
    '''Runs the Linux "ip ioam" command.
    An attribute of the "ip" command.'''
    system("ip ioam")


def ip_l2tp():
    '''Runs the Linux "ip 12tp" command.
    An attribute of the "ip" command.'''
    system("ip l2tp")


def ip_macsec():
    '''Runs the Linux "ip macsec" command.
    An attribute of the "ip" command.'''
    system("ip macsec")


def ip_maddress():
    '''Runs the Linux "ip maddress" command.
    An attribute of the "ip" command.'''
    system("ip maddress")


def ip_monitor():
    '''Runs the Linux "ip monitor" command.
    An attribute of the "ip" command.'''
    system("ip monitor")


def ip_ntable():
    '''Runs the Linux "ip ntable" command.
    An attribute of the "ip" command.'''
    system("ip ntable")


def python3():
    '''Runs the Linux "python3" command.
    Allows you to run python commands inside python. Runs the version the system is running'''
    system("python3")


def python_file(file):
    '''Runs a python file.
    Runs the file of the single argument "file". Vim files are normally callable using this command.'''
    system(f"python {file}")


def cpp():
    '''Runs the Linux "cpp" command.
    Basically allows you to run C++ in python.'''
    system("cpp")


def dirs():
    '''Runs the Linux "dirs" command.
    Displays the file path you are in.'''
    system("dirs")


def dir():
    '''Runs the Linux dir command.
    I would use the ls command instead. These two commands are very similar.'''
    system("dir")


def printf(arg):
    '''This function runs the Linux BASH "printf <arguments>" command.
    Prints the value of the single argument "arg".'''
    system(f"printf '{arg}'")


def echo(arg):
    '''Runs the Linux BASH "echo()" command.
    Very similar to the "printf" BASH function/command.'''
    system(f'echo "{arg}"')


def times():
    '''Runs the Linux "times" command.
    Very easy to use, with no arguments.'''
    system("times")


def pwd():
    '''Runs the "pwd" Linux command.
    Displays the file/directory you are in.'''
    system("pwd")


def type(command):
    '''Runs the Linux "Type" command.
    Shows the FULL path to the given command.'''
    system(f"type {command}")


def jobs(obj):
    '''Runs the Linux "jobs" command on the given object.'''
    system(f"jobs {obj}")


def ulimit(case=""):
    '''Runs the Linux ulimit command.
    Has one optional argument ("case"). If it works, it should display "Unlimited" on the screen.'''
    system(f"ulimit {case}")


def TRUE():
    '''Executes true. Normally useless.'''
    system("true")


def FALSE():
    '''Executes false. Normally useless.'''
    system("false")


def call_if(args):
    '''Calls the Linux BASH "if" command.
    Because I do not include a lot of BASH functions, This is normally not usable.'''
    system(f"if {args} then")


def w_h():
    '''Runs the Linux "w -h" command.
    An attribute of the "w" command.'''
    system("w -h")


def w_u():
    '''Runs the Linux "w -u" command.
    An attribute of the "w" command.'''
    system("w -u")


def w_s():
    '''Runs the Linux "w -s" command.
    An attribute of the "w" command.'''
    system("w -s")


def w_f():
    '''Runs the Linux "w -f" command.
    An attribute of the "w" command.'''
    system("w -f")


def w_o():
    '''Runs the Linux "w -o" command.
    An attribute of the "w" command.'''
    system("w -o")


def w_i():
    '''Runs the Linux "w -i" command.
    An attribute of the "w" command.'''
    system("w -i")


def version(obj):
    '''Tries to get the version of an command/object.
    Normally fails.'''
    system(f"{obj} -V")


def source(file):
    '''Runs the Linux "source" command.
    Can never read binary files. Very useful command.'''
    system(f"source {file}")


def alt(command):
    '''Runs commands that are not as separate functions.'''
    system(command)


def uname():
    '''Runs the Linux "uname" command.
    Returns the platform your on. Use the "uname_a()" function to get your full username, platform, version, and more!'''
    system("uname")


def uname_a():
    '''Runs the Linux "uname -a" command.
    An attribute of the "uname" command. Very recommended!'''
    system("uname -a")


def uname_s():
    '''Runs the Linux "uname -s" command.
    An attribute of the "uname" command.'''
    system("uname -s")


def uname_n():
    '''Runs the Linux "uname -n" command.
    An attribute of the "uname" command.'''
    system("uname -n")


def uname_r():
    '''Runs the Linux "uname -r" command.
    An attribute of the "uname" command.'''
    system("uname -r")


def uname_v():
    '''Runs the Linux "uname -v" command.
    An attribute of the "uname" command.'''
    system("uname -v")


def uname_m():
    '''Runs the Linux "uname -m" command.
    An attribute of the "uname" command.'''
    system("uname -m")


def uname_p():
    '''Runs the Linux "uname -p" command.
    An attribute of the "uname" command.'''
    system("uname -p")


def uname_i():
    '''Runs the Linux "uname -i" command.
    An attribute of the "uname" command.'''
    system("uname -i")


def uname_o():
    '''Runs the Linux "uname -o" command.
    An attribute of the "uname" command.'''
    system("uname -o")


def unameCom(command):
    '''Runs the given property of the "uname" command.'''
    system(f"uname {command}")


def ls():
    '''Runs the Linux "ls" command.
    Very similar to the "dir" command, but I recommend using this instead.'''
    system("ls")


def lsCom(command):
    '''Runs the given property of the "ls" command.'''
    system(f"ls {command}")


def bash():
    '''Runs the Linux "bash" command.'''
    system("bash")


def sh():
    '''Runs the Linux "sh" command.
    One of my favorites from cli_commander. I really recommend it!'''
    system("sh")


def env():
    '''Displays data about your environment.
    Very useful and easy to use!'''
    system("env")


def edit():
    '''Runs the Linux "edit" command.'''
    system("edit")


def edit_action(file):
    '''Runs the Linux "edit action" command.
    An attribute of the "edit" command. Has one argument, "file".'''
    system(f"edit {file}")


def editCom(command):
    '''Runs the given property of the "edit" command.'''
    system(f"edit {command}")


def install_d(directory):
    '''Runs the Linux "install -d" command.
    An attribute of the "install" command. One argument "directory". Works the same as the Linux command.'''
    system(f"install -d {directory}")


def install_D():
    '''Runs the Linux "install -D" command.
    An attribute of the "install" command.'''
    system(f"install -D")


def install_g(group):
    '''Runs the Linux "install -g" command.
    An attribute of the "install" command. One argument "group". Works the same as the Linux command.'''
    system(f"install -g group={group}")


def install_m(mode):
    '''Runs the Linux "install -m" command.
    An attribute of the "install" command. One argument "mode". Works the same as the Linux command.'''
    system(f"install -m mode={mode}")


def install_o(owner):
    '''Runs the Linux "install -o" command.
    An attribute of the "install" command. One argument "owner". Works the same as the Linux command.'''
    system(f"install -g owner={owner}")


def install_p(preserve_timestamps):
    '''Runs the Linux "install -p" command.
    An attribute of the "install" command. One argument "preserve_timestamps". Works the same as the Linux command.'''
    system(f"install -p {preserve_timestamps}")


def install_s(strip):
    '''Runs the Linux "install -s" command.
    An attribute of the "install" command. One argument "strip". Works the same as the Linux command.'''
    system(f"install -s {strip}")


def install_S(suffix):
    '''Runs the Linux "install -S" command.
    An attribute of the "install" command. One argument "suffix". Works the same as the Linux command.'''
    system(f"install -p suffix={suffix}")


def install_t(target_directory):
    '''Runs the Linux "install -t" command.
    An attribute of the "install" command. One argument "target_directory". Works the same as the Linux command.'''
    system(f"install -t target_directory={target_directory}")


def install_T(no_target_directory):
    '''Runs the Linux "install -T" command.
    An attribute of the "install" command. One argument "no_target_directory". Works the same as the Linux command.'''
    system(f"install -T {no_target_directory}")


def install_Z():
    '''Runs the Linux "install -Z" command.
    An attribute of the "install" command.'''
    system(f"install -Z")


def installCom(command):
    '''Runs the given property of the "install" command.'''
    system(f"install {command}")


def ssh():
    '''Runs the ssh command'''
    system("ssh")


def sshCom(command):
    '''Runs the given ssh property.'''
    system(f"ssh {command}")


def zipCom(command):
    '''Runs the given zip property'''
    system(f"zip {command}")


def commandCom(command):
    '''Runs the given command property'''
    system(f"command {command}")


def command_v(arg):
    '''Runs the Linux "command -v" command.
    An attribute of the "command" command. One argument "arg". Works the same as the Linux "command" command.'''
    system(f"command -v {arg}")


def command_V(arg):
    '''Runs the Linux "command -V" command.
    An attribute of the "command" command. One argument "arg". Works the same as the Linux "command" command.'''
    system(f"command -V {arg}")


def command_p(arg):
    '''Runs the Linux "command -p" command.
    An attribute of the "command" command. One argument "arg". Works the same as the Linux "command" command.'''
    system(f"command -p {arg}")


def unminimize():
    '''Runs the "unminimize" command.'''
    system("unminimize")


def ls_all():
    '''Runs the Linux "ls -all" command.
    Very useful.'''
    system("ls -all")


def mtr(ip, mode=""):
    '''Runs the Linux "mtr" command!
    Very recommended! Very useful! Track IP addresses, and more!'''
    system(f"mtr {mode} {ip}")


def logname():
    '''Gets your username.'''
    system("logname")

