#!/usr/bin/python

import mmap
import os.path

from elf import ELFIdent
from pe import PEIdent


class BinaryException(Exception):
    pass


class BinaryArch(object):
    """
    This class stores information about binary format.
    """

    ELF32 = 0
    ELF64 = 1
    PE32 = 2
    PE64 = 3
    UNKNOWN = 4

    arch = {
        ELF32: 'ELF 32 bits',
        ELF64: 'ELF 64 bits',
        PE32: 'PE 32 bits',
        PE64: 'PE 64 bits',
        UNKNOWN: 'Unknown'
    }


class Binary(object):
    """
    Binary class is responsible to load binary file using
    mmap.
    """

    def __init__(self, filename):
        """
        Args:
          filename (str): binary file name. Ex.: /bin/bash
        """

        if os.path.isfile(filename) is True:
            self.filename = filename
            self.__load__()
        else:
            raise BinaryException("Invalid filename.")

    def __load__(self):
        """
        Load binary to the memory, using mmap.
        """
        if self.filename:
            f = open(self.filename, "rb")
            self.mem = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            self.data = bytearray(self.mem)
            self.arch = self.get_arch()
            self.debug()
        else:
            raise BinaryException("Invalid filename.")

    def get_filename(self):
        """
        Returns:
          filename value.
        """

        return self.filename

    def is_elf(self):
        """
        Verify the binary format, ELF or PE.

        Returns:
          True if successful, False otherwise.
        """

        try:
            return ELFIdent.is_elf(self.data)
        except:
            raise BinaryException("Invalid byte array.")

    def is_pe(self):
        pass

    def get_arch(self):
        """
        Returns:
          The binary class defined on BinaryArch class.
        """

        if ELFIdent.is_elf(self.data):
            klass = ELFIdent.get_arch(self.data)
            if klass == 1:
                return BinaryArch.ELF32
            elif klass == 2:
                return BinaryArch.ELF64
            else:
                return BinaryArch.UNKNOWN

        if self.is_pe():
            print "Get PECLASS"

        return BinaryArch.UNKNOWN

    def debug(self):
        """
        Binary information
        """

        print "File format: %s" % BinaryArch.arch[self.arch]

    def __del__(self):
        """
        Closes the mmap.
        """

        try:
            self.mem.close()
        except:
            raise BinaryException("No binary memmory found.")
