import subprocess

subprocess.run("ifconfig",shell=False)
subprocess.run("sudo ifconfig eno1 down",shell=True)
subprocess.run("sudo ifconfig eno1 hw ether 00:11:22:33:44:55",shell=True)
subprocess.run("sudo ifconfig eno1 up",shell=True)
subprocess.run("ifconfig",shell=True)
