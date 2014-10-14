#!/usr/bin/python

from .utils import Singleton
import os
import mmap
from .elf import ELFIdent


class BinaryDataException(Exception):
    pass


class BinaryArch(object):
    """
    This class stores information about binary format.
    """

    UNKNOWN = 0
    ELFCLASS32 = 1
    ELFCLASS64 = 2
    PE32 = 3
    PE64 = 4

    arch = {
        UNKNOWN: 'Unknown',
        ELFCLASS32: 'ELF 32 bits',
        ELFCLASS64: 'ELF 64 bits',
        PE32: 'PE 32 bits',
        PE64: 'PE 64 bits'
    }


@Singleton
class BinaryData(object):
    """
    BinaryData is a singleton class responsible to load the binary.
    """

    def __init__(self, filename):
        self.filename = filename
        if os.path.isfile(self.filename):
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
            raise BinaryDataException("No binary memory found.")

    def is_elf(self):
        """
        Verify the binary format, ELF or PE.

        Returns:
          True if successful, False otherwise.
        """

        return ELFIdent(self.data).is_elf()

    def is_pe(self):
        pass

    def get_arch(self):
        """
        Returns:
          The binary class defined on BinaryArch class.
        """
        ident = ELFIdent(self.data)
        if ident.is_elf():
            return int(ident.get_arch())

        if self.is_pe():
            print("Get PECLASS")

        return BinaryArch.UNKNOWN

    def debug(self):
        """
        Binary information
        """

        print("File format: %s" % BinaryArch.arch[self.arch])
