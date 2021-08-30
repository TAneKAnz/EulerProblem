# find all primes below 1,000,000
mask = [False for x in range(1000001)]
primes = []
for x in range(2,1000001):
  if not mask[x]:
    primes.append(x)
    for i in range(x+x,1000001,x):
      mask[i] = True
#brute-force
result = 0
for x in primes:
  for n in range(1,x*2):
    print(x)
    if (abs((n**3+n**2*x)**(1/3) - round((n**3+n**2*x)**(1/3))))<0.000000001:
      result +=1
      print(result,x,n,sep=' ')
print(result)