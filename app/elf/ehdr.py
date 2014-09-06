#!/usr/bin/python

from ..binary_data import BinaryData, BinaryArch

import binascii

class EhdrFields(object):

    TYPE = 15
    TYPE_END = 17

    MACHINE = 17
    MACHINE_END = 19


class EhdrException(Exception):
    pass

class Ehdr64(object):
    pass

class Ehdr32(object):
    """
    ELF header.
    """

    def __init__(self, binary):
        self.binary = binary

    def get_field(self, start, end):
        return binascii.hexlify(str(self.binary[start:end]))

    def e_type(self):
        return self.get_field(EhdrFields.TYPE, EhdrFields.TYPE_END)

    def e_machine(self):
        return self.get_field(EhdrFields.MACHINE, EhdrFields.MACHINE_END)

class Ehdr(object):
    """
    ELF Header.
    """

    def __init__(self):
        try:
            self.binary = BinaryData(None)
            if self.binary.arch == BinaryArch.ELFCLASS32:
                self.ehdr = Ehdr32(self.binary.get_data())
                print self.ehdr.e_type()
                print self.ehdr.e_machine()
            elif self.binary.arch == BinaryArch.ELFCLASS64:
                self.ehdr = Ehdr64()
            else:
                raise EhdrException("[BINARY_DATA] Binary not recognized.")
        except:
            raise EhdrException("[BINARY_DATA] Error getting BinaryData.")
