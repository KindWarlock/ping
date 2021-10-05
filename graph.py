import matplotlib.pyplot as plt

data = []

with open('ping-filtered.txt', 'r') as file:
    data = list(map(float,file.read().splitlines()))

plt.hist(data, bins=1000)
plt.xlim(72, 80)    # дальше идут совсем редкие значения
plt.ylabel("Частота")
plt.xlabel("Время")

plt.show()
plt.savefig('ping-hist.png')
