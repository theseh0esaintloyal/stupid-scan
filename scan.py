from __future__ import print_function
import subprocess
from sys import argv


class bcolors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def is_host_up(output):
    """The worst output parsing in the world"""
    output = str(output[0])
    return '0% packet loss' in output and '100% packet loss' not in output


command_template = 'ping {ip} -c 1'

shit = '.'.join(argv[1].split('.')[:-1])
ips = ['{}.{}'.format(shit, fuck) for fuck in range(0, 255)]

# Iterate through all the possible IPs in the network
for ip in ips:
    # Construct the ping command
    command = command_template.format(ip=ip)

    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

    # Run the command and capture its output
    output = process.communicate()

    print(ip, end=' ')
    if is_host_up(output):
        print(bcolors.OKGREEN + 'is up' + bcolors.ENDC)
    else:
        print(bcolors.FAIL + 'is down' + bcolors.ENDC)
