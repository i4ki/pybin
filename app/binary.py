#!/usr/bin/python

from .elf import Ehdr
from .binary_data import BinaryData


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
        self.binary = BinaryData(filename)
        self.data = self.binary.get_data()
        self.arch = self.binary.get_arch()
        self.binary.debug()
        self.ehdr = Ehdr()
