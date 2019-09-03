

def readInt(file, size):
    return int.from_bytes(file.read(size), byteorder='little')

def readColorTable(file, colorTableSize):
    print("colorTableSize: " + str(colorTableSize))
    size = 1 << (colorTableSize + 1)
    colorTable = []

    for i in range(size):
        color = readInt(file, 3)
        # print(str(i) + ": " + str(color))
        print(str(i) + ": " + hex(color))
        colorTable.append(color)

    print("colorTable: " + str(size) + " -> " + str(len(colorTable)))

    return colorTable