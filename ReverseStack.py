def reverseStack(inputStack, extraStack) :
	if len(inputStack)<=1:
		return 
	while len(inputStack)!=1:
		ele = inputStack.pop()
		extraStack.append(ele)
	lastElement = inputStack.pop()	

	while len(extraStack)!=0:

		ele = extraStack.pop()
		inputStack.append(ele)
	reverseStack(inputStack,extraStack)	
	inputStack.append(lastElement)	

