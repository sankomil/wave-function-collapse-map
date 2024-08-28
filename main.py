from classes.grid import Grid


if __name__ == '__main__':
    test = Grid()
    result = test.wfc()

    while result != 0:

        for x in range(test.width):
            print("")
            for y in range(test.height):
                print(test.grid[x][y].entropy, "|", end=" ")
        print("\n")
        
        result = test.wfc()

