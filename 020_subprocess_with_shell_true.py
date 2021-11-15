import subprocess
# don't use "shell=True", it can be cause security problems
subprocess.run("ls -l", capture_output=True, shell=True)
# put arguments in a list
subprocess.run(["ls","-l"], capture_output=True)