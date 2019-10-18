def createCounter():
	global l
	l = 0
	def counter():
		global l
		l += 1
		return l
	return counter
	
x = createCounter()
print(x(),x(),x())
