

import os
from .GifHeader import GifHeader
from .GifImagePart import GifImagePart

class GifReader:
    _file = None

    def __init__(self, filePath):
        self.filePath = filePath
        self.header = GifHeader()
        self.imagePart = GifImagePart()

        if os.path.isfile(filePath):
            try:
                self._file = open(filePath, "rb")
                self.header.read(self._file)
                self.imagePart.read(self._file)

                self._file.close()
            except IOError as ex:
                print("Ha ocurrido un error abriendo el archivo: \"" + filePath + "\": " + ex.errno)
        else:
            print("El archivo \"" + filePath + "\" no existe")
