#!/usr/bin/python

from utils import Singleton
import os
import mmap
from elf import ELFIdent


class BinaryDataException(Exception):
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


@Singleton
class BinaryData(object):
    """
    BinaryData is a singleton class responsible to load the binary.
    """

    def __init__(self, filename):
        if os.path.isfile(filename) is True:
            self.filename = filename
            f = open(self.filename, "rb")
            self.mem = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            self.data = bytearray(self.mem)
            self.arch = self.get_arch()
        else:
            raise BinaryDataException("Invalid filename.")

    def get_filename(self):
        """
        Returns:
          Return the filename.
        """

        return self.filename

    def get_data(self):
        """
        Returns:
          Return the bytearray data.
        """

        return self.data

    def get_mem(self):
        """
        Returns:
          Return the mmap loaded binary.
        """

        return self.mem

    def __del__(self):
        """
        Closes the mmap.
        """

        try:
            self.mem.close()
        except:
            raise BinaryDataException("No binary memmory found.")

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

