#!/usr/bin/python


class ELFIdentException(Exception):
    pass


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
            return data[field]
        else:
            raise ELFIdentException("Invalid binary data")

    @classmethod
    def EI_MAG0(cls, data):
        return format(data[cls.MAG0], '02x')

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
        print cls.EI_MAG0(data)
        print cls.EI_MAG1(data)
        print cls.EI_MAG2(data)
        print cls.EI_MAG3(data)
        return ((cls.EI_MAG0(data) == "7f") and
                (cls.EI_MAG1(data) == 69) and
                (cls.EI_MAG2(data) == 76) and
                (cls.EI_MAG3(data) == 70))

    @classmethod
    def get_arch(cls, data):
        return cls.EI_CLASS(data)

    @classmethod
    def debug(cls, data):
        print "ELF Identification:"
        print "  EI_MAG0    = %s" % cls.EI_MAG0(data)
        print "  EI_MAG1    = %c" % cls.EI_MAG1(data)
        print "  EI_MAG2    = %c" % cls.EI_MAG2(data)
        print "  EI_MAG3    = %c" % cls.EI_MAG3(data)
        print "  EI_CLASS   = %s" % cls.EI_CLASS(data)
        print "  EI_DATA    = %s" % cls.EI_DATA(data)
        print "  EI_VERSION = %s" % cls.EI_VERSION(data)
        print "  EI_PAD     = %s" % cls.EI_PAD(data)
