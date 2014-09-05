from app import Binary, BinaryException


if __name__ ==  '__main__':
    try:
        b = Binary("/bin/bash")
    except BinaryException as e:
        print e

