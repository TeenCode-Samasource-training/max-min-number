def findMaxMin(numbers):
	minimum = min(numbers)
	maximum = max(numbers)
	if minimum == maximum:
		return [maximum]

	return [minimum, maximum]