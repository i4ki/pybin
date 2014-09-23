#!/usr/bin/python


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

    MAG0 = 0
    MAG1 = 1
    MAG2 = 2
    MAG3 = 3
    CLASS = 4
    DATA = 5
    VERSION = 6
    PAD = 7

    @classmethod
    def get_field(cls, data, field):
        if data:
            return format(data[field], '02x')
        else:
            raise ELFIdentException("[ERROR] ELFIdent data invalid.")

    @classmethod
    def EI_MAG0(cls, data):
        return cls.get_field(data, cls.MAG0)

    @classmethod
    def EI_MAG1(cls, data):
        return cls.get_field(data, cls.MAG1)

    @classmethod
    def EI_MAG2(cls, data):
        return cls.get_field(data, cls.MAG2)

    @classmethod
    def EI_MAG3(cls, data):
        return cls.get_field(data, cls.MAG3)

    @classmethod
    def EI_CLASS(cls, data):
        return cls.get_field(data, cls.CLASS)

    @classmethod
    def EI_DATA(cls, data):
        return cls.get_field(data, cls.DATA)

    @classmethod
    def EI_VERSION(cls, data):
        return cls.get_field(data, cls.VERSION)

    @classmethod
    def EI_PAD(cls, data):
        return cls.get_field(data, cls.PAD)

    @classmethod
    def is_elf(cls, data):
        return ((cls.EI_MAG0(data) == "7f") and
                (cls.EI_MAG1(data) == "45") and
                (cls.EI_MAG2(data) == "4c") and
                (cls.EI_MAG3(data) == "46"))

    @classmethod
    def get_arch(cls, data):
        return cls.EI_CLASS(data)

    @classmethod
    def debug(cls, data):
        print("  Magic: %s %s %s %s" % (cls.EI_MAG0(data),
                                        cls.EI_MAG1(data),
                                        cls.EI_MAG2(data),
                                        cls.EI_MAG3(data)))
        print("  Class: %s" % ELFIdentClass.to_string[int(cls.EI_CLASS(data))])
        print("  Data: %s" % ELFIdentData.to_string[int(cls.EI_DATA(data))])
        print("  Version: %s" % cls.EI_VERSION(data))
        # print "  EI_PAD     = %s" % cls.EI_PAD(data)
