import msvcrt
import sys

while(True):
    if msvcrt.kbhit():
        sys.stdout.write('y')
        break
    else:
        sys.stdout.write('n')