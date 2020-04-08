#!/usr/bin/python
import subprocess
import sys


class launcher:
    image = "empty"
    command = "ls"

    def __init__(self, _image, _command):
        self.image = _image
        self.command = _command

    def run(self):
        docker_run = "docker run --name build " + self.image + " /bin/bash -c \"" + self.command + "\""
        docker_rm = "docker rm build"
        subprocess.call(docker_run, shell=True)
        subprocess.call(docker_rm, shell=True)


if __name__ == '__main__':
    program = launcher(sys.argv[1], sys.argv[2])
    program.run()
