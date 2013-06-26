#!/usr/bin/env python

import subprocess
import re


def main():
    """ Kill the python server """
    try:
        pid = subprocess.check_output("lsof -i :12345 -F".split(" "))
    except subprocess.CalledProcessError:
        print "Server already stopped."
    else:
        pid = re.findall('p[0-9]*', pid)[0][1:]
        print "Stopping server %s" % pid
        kill = "kill -9 " + pid
        subprocess.call(kill.split(" "))

if __name__ == '__main__':
    main()
