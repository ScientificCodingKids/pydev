import datetime as dt

tic = dt.datetime.now()

sum = 0
for i in range(1, 1000000):
    sum = sum + i
toc = dt.datetime.now()

print('sum is %f' % sum)
print('it takes %f secs' % (toc-tic).total_seconds())

# Gauss' trick
tic = dt.datetime.now()
n = 1000000
sum2 = n * (n+1)/2
toc = dt.datetime.now()
print('sum is %.9f' % sum)
print('it takes %f secs using Gaussian method' % (toc-tic).total_seconds())

