from subprocess import PIPE, Popen


def main():
    import os
    p = Popen('/usr/bin/bash', shell=True, bufsize=0, stdin=PIPE, stdout=PIPE, stderr=PIPE, close_fds=True)
    (child_stdin, child_stdout, child_stderr) = (p.stdin, p.stdout, p.stderr)
    child_stdin.write(b"ls -l\n")
    print(child_stdout.read())
    child_stdin.write(b"exit\n")


if __name__ == '__main__':
    main()