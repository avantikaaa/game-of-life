#Assumption: size is never lesser than 10
SIZE = 25
#INDEX = 4		#randomly chosen
X = 1
EMPTY = 0
def EmptyGrid(n):
	l = [EMPTY]*n
	out = []
	for i in range (n):
		out.append(l[:])
	return out

def tub(grid, i, j):
	grid[i][j+1] = X
	grid[i][j-1] = X
	grid[i-1][j] = X
	grid[i+1][j] = X
	return grid

def barge(grid, i, j):
	grid = tub(grid, i, j)
	return tub(grid, i+1, j+1)

def square(grid, i, j):
	grid[i][j] = X
	grid[i+1][j] = X
	grid[i][j+1] = X
	grid[i+1][j+1] = X
	return grid

def boat(grid, i, j):
	grid[i+1][j+1] = 1
	return tub(grid, i, j)

def longBoat(grid, i, j):
	grid[i+2][j+2] = 1
	return barge(grid, i, j)
	
def ship(grid, i, j):
	grid = tub(grid, i, j)
	grid[i-1][j-1] = X
	grid[i+1][j+1] = X
	return grid

def snake(grid, i, j):
	grid = square(grid, i, j)
	grid = square(grid, i, j+2)
	grid[i][j+1] = 0
	grid[i+1][j+2] = 0
	return grid

def beeHive(grid, i, j):
	grid = tub(grid, i, j)
	grid = tub(grid, i, j+1)
	grid[i][j] = 0
	grid[i][j+1] = 0
	return grid

def glider(grid, i, j):
	grid = boat(grid, i, j)
	grid[i][j-1] = 0
	grid[i+1][j-1] = 1
	return grid

def printGrid(grid):
	l = [" ", "O"]
	print("_" * (2 * SIZE + 3))
	for i in grid:
		print("|", end = " ")
		for j in i:
			print (l[j], end = " ")
		print("|")
	print("|" + "_" * (2 * SIZE + 1) + "|")
	print()

if __name__ == "__main__":
	grid = EmptyGrid(SIZE)
	printGrid(ship(grid, 2, 2))
