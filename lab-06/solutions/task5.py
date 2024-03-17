import numpy as np

stops = set(2**i for i in range(1, 30))

s = 0
for i in range(2 ** 20 + 1):
    x = np.random.default_rng().normal(1000, 10)
    s += x
    if i in stops:
        print("%7d %.6f" % (i, s / i))