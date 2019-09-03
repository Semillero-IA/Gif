#!/usr/bin/python3

import os
import sys
from Gif.GifReader import GifReader

if __name__ == "__main__":

    print(sys.byteorder)    # 'little' o 'big'

    if len(sys.argv) > 1:
        gifObj = GifReader(sys.argv[1])
    else:
        print("No se ha especificado la ruta del archivo \"gif\"")
