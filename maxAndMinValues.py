def findMaxMin(numbers):
	if max(numbers) == min(numbers):
		return [max(numbers)]
	return [min(numbers),max(numbers)]