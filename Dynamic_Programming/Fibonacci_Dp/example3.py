

cache = {}
def fibonnaci(n):
	global cache
	if n in cache.keys():
		return cache[n]
	
	if n < 2 :
		return n

	cache[n] = fibonnaci(n-1) + fibonnaci(n-2)

	return cache[n]

print(fibonnaci(100))