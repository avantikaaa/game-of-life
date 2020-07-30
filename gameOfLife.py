from sys import argv
from grid import *
from random import randint

def generateIndex(n):
	return randint(3, n-3)

def addShape(grid, gridShape):
	return {"tub": tub, "square": square, "ship": ship, "barge": barge, "boat": boat, "longboat": longBoat, "snake": snake, "beehive": beeHive, "glider": glider}[gridShape](grid, generateIndex(SIZE), generateIndex(SIZE))

'''
def printGrid(grid):
	for i in grid:
		for j in i:
			print (j, end = " ")
		print()
	print()
'''

def alive(n, value):
	if value == 1:
		return n == 2 or n == 3
	return n == 3

def neighbours(grid, i, j):
	count = 0
	for m in range (i-1, i+2):
		for n in range (j-1, j+2):
			if m < SIZE and m >= 0 and n < SIZE and n >= 0:
				count += grid[m][n]
	count -= grid[i][j]
	return count

def printNeighbours(grid):
	for i in range (0, SIZE):
		for j in range (0, SIZE):
			print(int(alive(neighbours(grid, i, j))), end = " ")
		print()

def nextPattern(grid):
	new = EmptyGrid(SIZE)
	
	for i in range (SIZE):
		for j in range (SIZE):
			new[i][j] = int(alive(neighbours(grid, i, j), grid[i][j]))
	return new

def main():
    print("Legend:-\n\t0: Quit\n\t1: Continue\n\t2: Append Shape\n")
    gridShape = argv[1]
    grid = EmptyGrid(SIZE)
    grid = addShape(grid, gridShape)
    appendShape = 1
    
#	printGrid(grid)

    while appendShape != 0:
    	if appendShape == 2:
    		shape = input("Enter Shape: ")
    		grid = addShape(grid, shape)
    	if grid == EmptyGrid(SIZE):
    		break
    	
#		printNeighbours(grid)
    	printGrid(grid)
    	
    	new = nextPattern(grid)
    	
    	if grid == new:
    		print("This is a static pattern".center(2*SIZE + 3, "-"))
    		break
    	grid = new[:]
    	
    	appendShape = int(input("Do you wish to continue(0, 1, 2): "))
	
    print("Thank You".center(2*SIZE + 3, "-"))

main()
