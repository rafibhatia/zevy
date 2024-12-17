import random, time, copy

WIDTH = 60
HEIGHT = 20

# Create the grid
nextCells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#')  # Live cell
        else:
            column.append(' ')  # Dead cell
    nextCells.append(column)

while True:
    print('\n\n\n\n\n')  # Clear the screen
    currentCells = copy.deepcopy(nextCells)

    # Print the current grid
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')
        print()  # Newline after each row

    # Calculate the next grid
    for x in range(WIDTH):
        for y in range(HEIGHT):
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Count the number of living neighbors
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1

            # Apply Conway's Game of Life rules
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                # Stay alive
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # Become alive
                nextCells[x][y] = '#'
            else:
                # Die or stay dead
                nextCells[x][y] = ' '

    time.sleep(1)  # Pause to make the grid easier to see
