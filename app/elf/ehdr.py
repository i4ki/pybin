#!/usr/bin/python

from ..binary_data import BinaryData, BinaryArch

from ident import ELFIdent, ELFIdentClass

import binascii

class EhdrFields64(object):
    pass

class EhdrFields32(object):

    TYPE = 15
    TYPE_SIZE = 17

    MACHINE = 17
    MACHINE_SIZE = 19

    VERSION = 19
    VERSION_SIZE = 21

    ENTRY = 23
    ENTRY_SIZE = 27


class Ehdr64(object):
    pass

class Ehdr32(object):
    """
    ELF header.
    """

    def __init__(self, binary):
        self.binary = binary

    def get_field(self, start, end, direction=None):
        if direction != None:
            return binascii.hexlify(str(self.binary[start:end:direction]))
        else:
            return binascii.hexlify(str(self.binary[start:end]))

    def e_type(self):
        return self.get_field(EhdrFields32.TYPE, EhdrFields32.TYPE_SIZE)

    def e_machine(self):
        return self.get_field(EhdrFields32.MACHINE, EhdrFields32.MACHINE_SIZE)

    def e_version(self):
        return self.get_field(EhdrFields32.VERSION, EhdrFields32.VERSION_SIZE)

    def e_entry(self):
        return self.get_field(EhdrFields32.ENTRY_SIZE, EhdrFields32.ENTRY, -1)

    """
    def e_phoff(self):
        return binascii.hexlify(str(self.__elf.binary[31:27:-1]))

    def e_shoff(self):
        return binascii.hexlify(str(self.__elf.binary[35:31:-1]))

    def e_ehsize(self):
        return binascii.hexlify(str(self.__elf.binary[41:39:-1]))

    def e_phentsize(self):
        return binascii.hexlify(str(self.__elf.binary[43:41:-1]))
    
    def e_phnum(self):
        return binascii.hexlify(str(self.__elf.binary[45:43:-1]))

    def e_shentsize(self):
        return binascii.hexlify(str(self.__elf.binary[47:45:-1]))

    def e_shnum(self):
        return binascii.hexlify(str(self.__elf.binary[49:47:-1]))

    def e_shstrndx(self):
        return binascii.hexlify(str(self.__elf.binary[51:49:-1]))
    """

class Ehdr(object):
    """
    ELF Header.
    """

    def __init__(self):

        self.binary = BinaryData(None)
        self.data = self.binary.get_data()

        if self.binary.arch == BinaryArch.ELFCLASS32:
		    self.ehdr = Ehdr32(self.binary.get_data())
        elif self.binary.arch == BinaryArch.ELFCLASS64:
		    self.ehdr = Ehdr64()
        else:
		    print "[BINARY_DATA] Binary not recognized."
        self.debug()


    def save_fields(self):
        self.e_type = self.ehdr.e_type()
        self.e_machine = self.ehdr.e_machine()
        self.e_version = self.ehdr.e_version()
        self.e_entry = self.ehdr.e_entry()

    def debug(self):

        print "ELF Header:"
        ELFIdent.debug(self.data) 

