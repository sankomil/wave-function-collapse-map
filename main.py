from classes.grid import Grid


if __name__ == '__main__':
    test = Grid()
    test.wfc()
    for x in range(test.width):
        print("")
        for y in range(test.height):
            print(test.grid[x][y].entropy, end=" ")
    
    test.wfc()

    print("\n")
    for x in range(test.width):
        print("")
        for y in range(test.height):
            print(test.grid[x][y].entropy, end=" ")

    test.wfc()

    print("\n")
    for x in range(test.width):
        print("")
        for y in range(test.height):
            print(test.grid[x][y].entropy, end=" ")

    
    test.wfc()

    print("\n")
    for x in range(test.width):
        print("")
        for y in range(test.height):
            print(test.grid[x][y].entropy, end=" ")
    
    print("\n")