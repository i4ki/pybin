import sys
sys.path.append('app/')

from app.binary import Binary, BinaryException

if __name__ ==  '__main__':
    b = Binary("/bin/bash")

