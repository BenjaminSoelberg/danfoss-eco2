from ghidra.program.model.symbol import SourceType
l = currentProgram.getListing()
for line in file("mappings.txt"):
    pieces = line.split(",")
    address = toAddr(long(pieces[1], 16))
    symbolName = pieces[0]
    comment = pieces[2]
    print("creating symbol %s at address %s" % (symbolName, address))
    d = l.getDataAt(address)
    if d is not None:
        s = d.getPrimarySymbol()
        if s is not None:
            s.setName(symbolName, SourceType.USER_DEFINED)
        else:
            createSymbol(address, symbolName, False)
    else:
        createSymbol(address, symbolName, False)


# Copy cdata
 setBytes(toAddr(0x200024b8), getBytes(toAddr(0x0003d338), 0x580))