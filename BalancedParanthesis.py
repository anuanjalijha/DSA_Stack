def isBalanced(expression) :
	s = []
	for char in expression:
		if char in '({[':
			s.append(char)
		elif char is ')':
			if (not s or s[-1]!='('):
				return False
			s.pop()
		elif char is '}':
			if (not s or s[-1]!='{'):
				return False
			s.pop()
		elif char is ']':
			if (not s or s[-1]!='['):
				return False
			s.pop()	
	if (not s):
		return True	
	return False			
