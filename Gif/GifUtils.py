
import random

def readInt(file, size):
    return int.from_bytes(file.read(size), byteorder='little')

def saveNewGif(file, colorTable, initPosition, finalPosition):
    outfile = open("test.gif", "wb")
    file.seek(0)

    outfile.write(file.read(initPosition))

    colorTable.sort()
    for color in colorTable:
        mutate = (random.randint(0, 0xff) << 0xf) | (random.randint(0, 0xff) << 7) | random.randint(0, 0xff)
        print('mutate: ' + hex(mutate))
        print('old: ' + hex(color))
        newcolor = color & mutate
        print('new: ' + hex(newcolor))
        outfile.write(newcolor.to_bytes(3, byteorder='little'))

    print('=== posiciones ===')
    print(finalPosition)
    print(outfile.tell())
    file.seek(finalPosition)
    outfile.write(file.read())
    file.seek(finalPosition)

def readColorTable(file, colorTableSize):
    size = 1 << (colorTableSize + 1)
    colorTable = []

    for i in range(size):
        color = readInt(file, 3)
        # print(str(i) + ": " + str(color))
        # print(str(i) + ": " + hex(color))
        colorTable.append(color)

    print("colorTable: " + str(size) + " -> " + str(len(colorTable)))
    return colorTable

def mutateColorTable(file, colorTableSize):
    size = 1 << (colorTableSize + 1)
    outfile = open("test.gif", "wb")
    tableInitPosition = file.tell()
    tableFinalPosition = -1
    colorTable = []

    for i in range(size):
        color = readInt(file, 3)
        colorTable.append(color)

    tableFinalPosition = file.tell()

    file.seek(0)
    outfile.write(file.read(tableInitPosition))
    colorTable.sort()

    for color in colorTable:
        mutate = (random.randint(0, 0xff) << 0xf) | (random.randint(0, 0xff) << 7) | random.randint(0, 0xff)
        newcolor = color & mutate
        outfile.write(newcolor.to_bytes(3, byteorder='little'))

    file.seek(tableFinalPosition)
    outfile.write(file.read())
    outfile.close()
    file.seek(tableFinalPosition)

    return colorTable