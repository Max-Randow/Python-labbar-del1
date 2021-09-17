def choose(n,k):
	if k == n:
		return 1
	if k == 0:
		return n
	# N = 1000 , K = 900 -> 1000 -900 < 1000

	if k < (n-k):
		k = n-k 
		print(f"k changed to: {k}")
	#1000!/(800!(200!) <=> (a -> b)!/(a-b)!
	
	return mult_between(n,k+1)//mult_between(n-k,1)

def mult_between(n,k):
	if n == k:
		return n
	else:
		
		return mult_between(n-1,k) * n
