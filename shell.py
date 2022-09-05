import cmd
# from cmd import Cmd


class Shell(cmd.Cmd):
    prompt = "(hbnb) "
    pass

if __name__ == "__main__":
    shell = Shell()
    shell.cmdloop()