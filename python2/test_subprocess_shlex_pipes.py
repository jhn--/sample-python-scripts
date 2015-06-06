import subprocess, shlex
#from subprocess import Popen, PIPE

p1 = subprocess.Popen(['echo', 'atrail', 'brief', '0', '9999'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['wc'], stdin=p1.stdout, stdout=subprocess.PIPE)
p3 = subprocess.Popen(['grep', '1'], stdin=p2.stdout)

p1.stdout.close()
p2.stdout.close()

output = p3.communicate()[0]