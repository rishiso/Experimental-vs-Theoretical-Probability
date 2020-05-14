from random import randint
from matplotlib import pyplot as plt

def flip(n):
    heads = 0
    for i in range(n):
        if randint(0, 1) == 0:
            heads += 1
    return heads / n


max_flips = 100000

x = list(range(100, max_flips, max_flips // 250))
y = list(map(flip, x))

plt.plot(x, y, label="Experimental")
plt.xlabel("Number of Coin Flips")
plt.ylabel("Probability of Heads")
plt.title("Experimental vs Theoretical Probability")
plt.hlines(.50, 0, max_flips, color="r", label="Theoretical")
plt.legend()
plt.show()