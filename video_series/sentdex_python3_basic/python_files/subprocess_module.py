#! python3

import subprocess

output = subprocess.check_output('ls', shell=True)
print(output)
