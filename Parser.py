print("& - and");
print("| - or");
print("! - not");
print("( - begin clause");
print(") - end clause\n");

fileName = "expressions.txt";
inFile = open(fileName, 'r').read().splitlines();
for line in inFile:
	literals = [];
	numOfLiterals = 0;
	numOfClauses = 0;
	openClause = 0;
		
	for char in line:
		if char == '(':
			openClause = 1;
			
		elif char == ')' and openClause == 1:
			numOfClauses += 1;
			openClause = 0;
				
		elif char == '&':
			continue;
			
		elif char == '!':
			continue;
			
		elif char == '|':
			continue;
			
		elif char == '\n':
			continue;
				
		else: 
			if char in literals:
				continue;
			literals.append(char);
	
	print line;
	print "Literals: ", literals;
	print "Number of literals: ", len(literals);
	print "Number of clauses: ", numOfClauses;
	print "";