SIZEOFTHECHESSBOARD = 8
stateOfPosition = []

def checkPositionOfTheQueen(firstQueen, secondQueen):
	diff = (abs(firstQueen[0] - secondQueen[0]), abs(firstQueen[1] - secondQueen[1]))
	if diff[0] == diff[1] or diff[0] == 0 or diff[1] == 0:
		return False
	return True

def cover(rowIndex):
	if rowIndex == SIZEOFTHECHESSBOARD:
		global numberOfTrueChessboards
		numberOfTrueChessboards = numberOfTrueChessboards + 1
		return 1

	#global numberOfSteps
	#numberOfSteps = numberOfSteps + 1
	localNumberOfChessboards = 0

	for columnIndex in range(0, SIZEOFTHECHESSBOARD):
		firstQueen = (rowIndex, columnIndex)
		checkPosition = True
		for secondQueen in stateOfPosition:
			if not checkPositionOfTheQueen(firstQueen, secondQueen):
				checkPosition = False
				break

		if checkPosition == True:
			stateOfPosition.append(firstQueen)
			localNumberOfChessboards = localNumberOfChessboards + cover(rowIndex + 1)
			stateOfPosition.pop()

	if localNumberOfChessboards == 0:
		localNumberOfChessboards = 1
	return localNumberOfChessboards
#------------------------------------------

SIZEOFTHECHESSBOARD = int(input())

#numberOfSteps = 0
numberOfTrueChessboards = 0
numberOfChessboards = cover(0)

print(numberOfTrueChessboards)
#print("numberOfTrueChessboards: ", numberOfTrueChessboards)
#print("numberOfChessboards: ", numberOfChessboards)
#print("expect: ", numberOfChessboards / numberOfTrueChessboards)