def checkRedundantBrackets(expression) :
	stack = []
	n = len(expression)
	for i in range(n):
		if expression[i] == '(' or expression[i] == '+' or expression[i] == '-' or expression[i] == '*' or expression[i] == '/':
			stack.append(expression[i])
		elif expression[i]==')':
			if stack[-1]=='(':
				return True
			else:
				while stack[-1] != '(':
					stack.pop()	
				
				stack.pop()
							
				
	return False	