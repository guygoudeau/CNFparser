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
		
	for char in line:
		if char == '(':
			numOfClauses += 1
			currentClause = []
			evaledClause = []
			
		elif char != ')':
			currentClause.append(char)
			if line[char - 1] == "!":
				if eval(char) == 1:
					evaledClause.append(0)
				else:
					evaledClause.append(1)
			else:
				if char.isalpha():
					evaledClause.append(char)
					
		else:
			currentClause.append(char)
					 
		if char in literals:
			continue
		literals.append(char)
	
	print line
	print "Literals: ", literals
	print "Number of literals: ", len(literals)
	print "Number of clauses: ", numOfClauses
	print ""