from matplotlib import pyplot as plt

yvalues, xvalues = [],[]
for i in range(-100, 100):
    xvalue = i
    yvalue = i ** 2
    yvalues.append(yvalue)
    xvalues.append(xvalue)

fig, ax = plt.subplots()
ax.plot(xvalues, yvalues)

plt.show()
