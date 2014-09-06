#!/usr/bin/python

from ..binary_data import BinaryData, BinaryArch

#import binascii

class EhdrFields(object):
    pass

class EhdrException(Exception):
    pass

class Ehdr64(object):
    pass

class Ehdr32(object):
    pass

class Ehdr(object):
    """
    ELF Header.
    """

    def __init__(self):
        try:
            self.binary = BinaryData(None)
            if self.binary.arch == BinaryArch.ELFCLASS32:
                self.ehdr = Ehdr32()
            elif self.binary.arch == BinaryArch.ELFCLASS64:
                self.ehdr = Ehdr64()
            else:
                raise EhdrException("[BINARY_DATA] Binary not recognized.")
        except:
            raise EhdrException("[BINARY_DATA] Error getting BinaryData.")
