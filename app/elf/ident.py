#!/usr/bin/python

import struct
import binascii

class ELFIdentException(Exception):
    pass


class ELFIdentClass(object):

    ELFCLASSNONE = 0
    ELFCLASS32 = 1
    ELFCLASS64 = 2

    to_string = {
        ELFCLASSNONE: "ELFNONE",
        ELFCLASS32: "ELF32",
        ELFCLASS64: "ELF64"
    }


class ELFIdentData(object):

    ELFDATANONE = 0
    ELFDATA2LSB = 1
    ELFDATA2MSB = 2

    to_string = {
        ELFDATANONE: "ELFDATANONE",
        ELFDATA2LSB: "2's complement, little endian",
        ELFDATA2MSB: "2's complement, big endian"
    }


class ELFIdent(object):
    """
    ELF identification class.
    """

    ident_format = "<1s1s1s1s1s1s1s1s1s7s"

    # e_ident
    EI_MAG0         = 0     # File identification
    EI_MAG1         = 1     # File identification
    EI_MAG2         = 2     # File identification
    EI_MAG3         = 3     # File identification
    EI_CLASS        = 4     # File class
    EI_DATA         = 5     # Data encoding
    EI_VERSION      = 6     # File version
    EI_OSABI        = 7     # Operating System/ABI spec
    EI_OSABIVERSION = 8     # ABI Version
    EI_PAD          = 9     # Start of padding bytes
    EI_NIDENT       = 16    # Size of ident

    def __init__(self, e_ident):
        (self.ei_mag0,
         self.ei_mag1,
         self.ei_mag2,
         self.ei_mag3,
         self.ei_class,
         self.ei_data,
         self.ei_version,
         self.ei_osabi,
         self.ei_osabiversion,
         self.ei_pad) = struct.unpack(
             self.ident_format, e_ident[0:struct.calcsize(self.ident_format)])

    def MAG0(cls):
        return binascii.hexlify(cls.ei_mag0)

    def MAG1(cls):
        return binascii.hexlify(cls.ei_mag1)

    def MAG2(cls):
        return binascii.hexlify(cls.ei_mag2)

    def MAG3(cls):
        return binascii.hexlify(cls.ei_mag3)

    def CLASS(cls):
        return binascii.hexlify(cls.ei_class)

    def DATA(cls):
        return binascii.hexlify(cls.ei_data)

    def VERSION(cls):
        return binascii.hexlify(cls.ei_version)

    def OSABI(cls):
        return binascii.hexlify(cls.ei_osabi)

    def OSABIVERSION(cls):
        return binascii.hexlify(cls.ei_osabiversion)

    def PAD(cls):
        return binascii.hexlify(cls.ei_pad)

    def is_elf(cls):
        return ((cls.MAG0() == "7f") and
                (cls.MAG1() == "45") and
                (cls.MAG2() == "4c") and
                (cls.MAG3() == "46"))

    def get_arch(cls):
        return cls.CLASS()

    def debug(cls):
        print("  Magic: %s %s %s %s" % (cls.MAG0(),
                                        cls.MAG1(),
                                        cls.MAG2(),
                                        cls.MAG3()))
        print("  Class: %s" % ELFIdentClass.to_string[int(cls.CLASS())])
        print("  Data: %s" % ELFIdentData.to_string[int(cls.DATA())])
        print("  Version: %s" % cls.VERSION())
        print("  OSABI: %s" % cls.OSABI())
        print("  OSABIVERSION: %s" % cls.OSABI())
        # print "  EI_PAD     = %s" % cls.EI_PAD(data)
