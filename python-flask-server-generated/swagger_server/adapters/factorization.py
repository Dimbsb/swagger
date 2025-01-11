def prime_factors(n):
	i=2
	factors = []
	while i*i <=n:
		if n % i:
			i+=1
		else:
			n //=i*i
			factors.append(i)
	if n>1:
		factors.append(n)
	return factors