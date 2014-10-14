#!/usr/bin/python

from ..binary_data import BinaryData, BinaryArch

from .ident import ELFIdent

import struct
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

    PHOFF = 27
    PHOFF_SIZE = 31


class Ehdr64(object):
    pass


class Ehdr32(object):
    """
    ELF header.
    """

    Elf32_Ehdr = "<16sHHIIIIIHHHHHH"

    def __init__(self, binary):
        self.binary = binary

        (self.e_ident,
         self.e_type,
         self.e_machine,
         self.e_version,
         self.e_entry,
         self.e_phoff,
         self.e_shoff,
         self.e_flags,
         self.e_ehsize,
         self.e_phentsize,
         self.e_phnum,
         self.e_shentsize,
         self.e_shnum,
         self.e_shstrndx) = [0] * 14

    def load(self):
        (self.e_ident,
         self.e_type,
         self.e_machine,
         self.e_version,
         self.e_entry,
         self.e_phoff,
         self.e_shoff,
         self.e_flags,
         self.e_ehsize,
         self.e_phentsize,
         self.e_phnum,
         self.e_shentsize,
         self.e_shnum,
         self.e_shstrndx) = struct.unpack(
             self.Elf32_Ehdr, self.binary[0:struct.calcsize(self.Elf32_Ehdr)])

        if (self.e_ident[0:4] == '\x7fELF'):
            self.ident = ELFIdent(self.e_ident)

        return self.ident.is_elf()

    def type(self):
        return self.e_type

    def machine(self):
        return self.e_machine

    def version(self):
        return self.e_version

    def entry(self):
        return self.e_entry

    def e_phoff(self):
        return self.e_phoff


class Ehdr(object):
    """
    ELF Header.
    """

    def __init__(self):

        self.binary = BinaryData(None)
        self.data = self.binary.get_data()

        if self.binary.arch == BinaryArch.ELFCLASS32:
            self.ehdr = Ehdr32(self.binary.get_data())
            if not self.ehdr.load():
                print("[BINARY_DATA] Not ELF")
        elif self.binary.arch == BinaryArch.ELFCLASS64:
            self.ehdr = Ehdr64()
        else:
            print("[BINARY_DATA] Binary not recognized.")
        self.debug()

    def save_fields(self):
        self.e_type = self.ehdr.type()
        self.e_machine = self.ehdr.machine()
        self.e_version = self.ehdr.version()
        self.e_entry = self.ehdr.entry()
        self.e_phoff = self.ehdr.phoff()

    def debug(self):

        print("ELF Header:")
        ident = ELFIdent(self.data)
        ident.debug()
