#!/usr/bin/python

from elf import ELFIdent, Ehdr
from pe import PEIdent
from binary_data import BinaryData


class BinaryException(Exception):
    pass


class Binary(object):
    """
    Binary class is responsible to identify the binary.
    """

    def __init__(self, filename):
        """
        Args:
          filename (str): binary file name. Ex.: /bin/bash
        """
        try:
            self.binary = BinaryData(filename)
            self.data = self.binary.get_data()
            self.arch = self.binary.get_arch()
            self.binary.debug()
            ELFIdent.debug(self.data)
            self.ehdr = Ehdr()
        except:
            raise BinaryException("[BINARY] Error creating BinaryData.")
