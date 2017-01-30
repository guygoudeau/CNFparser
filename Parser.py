print("\n& - and")
print("| - or")
print("! - not")
print("( - begin clause")
print(") - end clause\n")
print("abcdef = 101010\n")

a = 1
b = 0
c = 1
d = 0
e = 1
f = 0

fileName = "expressions.txt"
inFile = open(fileName, 'r').read().splitlines()

for line in inFile:

	literals = []
	currentClause = []
	evaledClause = []
	numOfLiterals = 0
	numOfClauses = 0

	for char in range(0, len(line)):
		if line[char] == "(":
			numOfClauses += 1
			currentClause = []
			evaledClause = []
			
		if line[char] != ")":
			currentClause.append(line[char])
			if line[char - 1] == "!":
				if eval(line[char]) == 1:
					evaledClause.append(0)
				else:
					evaledClause.append(1)

		if line[char].isalpha():
			evaledClause.append(line[char])
			if line[char] not in literals:
				literals.append(line[char])

		else:
			currentClause.append(line[char])
		
	print line
	print "Literals: ", literals
	print "Number of literals: ", len(literals)
	print "Number of clauses: ", numOfClauses
	print ""