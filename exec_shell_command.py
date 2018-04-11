# execute a basic shell command and get stdout and stderr
# unix systems only.
from subprocess import Popen, PIPE
args = ['time', 'echo', 'hello python']
ret = Popen(args, stdout=PIPE, stderr=PIPE)
out, err = ret.communicate()
print('out is: %s' % out)
print('err is: %s' % err)