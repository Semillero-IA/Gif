

from .GifUtils import *

class GifHeader:

    class Options:
        def __init__(self):
            self.useGlobalColorTable = False
            self.colorResolution = 0
            self.colorTableSorted = False
            self.globalColorTableSize = 0

        def read(self, flags):
            self.globalColorTableSize = (flags & 7)
            self.colorTableSorted = ((flags >> 3) & 1) == 1
            self.colorResolution = (flags >> 4) & 7
            self.useGlobalColorTable = ((flags >> 7) & 1) == 1

            print(self.useGlobalColorTable)
            print(self.colorResolution)
            print(self.colorTableSorted)
            print(self.globalColorTableSize)

    def __init__(self):
        self.version = ""
        self.width = 0
        self.height = 0

        self.options = GifHeader.Options()

        self.bgColor = 0
        self.aspectRatio = 0
        self.colorTable = []

    def read(self, file):
        version = file.read(6)
        version = version.decode("utf-8")

        if version.lower() == "gif89a" or version.lower() == "gif87a":
            self.width = readInt(file, 2)
            self.height = readInt(file, 2)
            flags = readInt(file, 1)
            self.bgColor = readInt(file, 1)
            self.aspectRatio = (readInt(file, 1) + 15) / 64

            print("Versión: " + version)
            print("flags: " + str(bin(flags)))
            print("dimensiones: " + str(self.width) + "x" + str(self.height))

            self.version = version
            self.options.read(flags)

            if (self.options.useGlobalColorTable):
                self.colorTable = readColorTable(file, self.options.globalColorTableSize)
            else:
                print("La imagen no tiene tabla de colores global")

            return True
        else:
            print("la cabecera no coincide con el formato GIF")
            return False