#!/usr/bin/python

from ..binary_data import BinaryData, BinaryArch

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
            if self.binary.arch == BinaryArch.ELF32:
                self.ehdr = Ehdr32()
            elif self.binary.arch == BinaryArch.ELF64:
                self.ehdr = Ehdr64()
            else:
                raise EhdrException("Binary not recognized.")
        except:
            raise EhdrException("Error getting BinaryData.")
