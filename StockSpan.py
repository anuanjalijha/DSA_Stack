def stockSpan(price, n) :
	monotonicStack = []

    # Declare an ans list and initialize it with -1. It will store
    # the stock span for each day.
	ans = [-1] * n

    # Iterate over the 'prices' list in reverse.
	for i in range(n - 1, -1, -1):
        
        # Repeat while monotonic stack is not empty and price of the 'ith'
        # day is greater or equal to the price of the day that is at the
        # top of the stack.
		while monotonicStack and price[i] >= price[monotonicStack[-1]]:
            # Stock Span for the day at the top of stack is given by: 
            # index of the day at the top - current index.
			span = monotonicStack[-1] - i

            # Assign the span value of the day at the top of the stack
            # to the 'ans' list.
			ans[monotonicStack[-1]] = span

            # Pop out the top element.
			monotonicStack.pop()

        # Push 'i' into the stack.
		monotonicStack.append(i)

    # Iterate over the 'prices' list.
	for i in range(n):
        # If the span of 'ith' day is -1 then assign 'i' + 1 to it.
		if ans[i] == -1:
			ans[i] = i + 1

    # Return the 'ans' list.
	return ans