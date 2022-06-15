def memoizeFibonacci(n):

	cache = {}

	def fibonnaci(n):

		if n in cache.keys() :
			return cache[n]

		if n < 2 :
			return n 

		cache[n] =  fibonnaci(n-1) + fibonnaci(n-2) 

		return cache[n]

	return fibonnaci(n)


func = memoizeFibonacci

print(func(500))