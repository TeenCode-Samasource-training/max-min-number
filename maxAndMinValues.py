def findMaxMin(n):
	try:
		list=[]
		if type(n).__name__!='list':
			raise TypeError
		elif min(n)==max(n):
			list.append(min(n))
		else:
			list.append(min(n))
			list.append(max(n))
		return list
	except TypeError:
		print ("Rats!, i only accept a list parammeter")
