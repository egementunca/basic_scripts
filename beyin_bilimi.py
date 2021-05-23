import matplotlib.pyplot as plt
import scipy.optimize
import numpy as np
import matplotlib.markers as mmark

def parabola(x,a):
    return a*(x**2)

def line(x,a,b):
    return a*x+b



labels = []
#labels.append('radius = 3, 4')

dataset = [[158,58,'M'],[158,59,'M'],[158,63,'M'],[160,64,'L'],[163,64,'L'],[165,61,'L'],[163,60,'M'],[163,61,'M'],[168,66,'L'],[170,63,'L']]
x1m = []
x2m = []
x1l = []
x2l = []
for i in range(len(dataset)):
	if dataset[i][2] == 'M':
		x1m.append(dataset[i][0])
		x2m.append(dataset[i][1])
	elif dataset[i][2] == 'L':
		x1l.append(dataset[i][0])
		x2l.append(dataset[i][1])

plt.scatter(x1m,x2m,marker="*",color="r",zorder=1)
plt.scatter(x1l,x2l,marker="*",color="b")

plt.scatter([161],[61],marker="x",color="g")
circle1 = plt.Circle((161,61),3,fill=False)
circle2 = plt.Circle((161,61),4,fill=False)

fig = plt.gcf()
fig.gca().add_artist(circle1)
fig.gca().add_artist(circle2)
#fit_params , pcov = scipy.optimize.curve_fit(line,x,y)
#x= np.linspace(0.1,.3)
#print(fit_params)
#y_fit = line(x,*fit_params)
#plt.plot(x,y_fit,zorder=0)
#plt.legend(labels,loc=2)
plt.ylabel("Kilo")
plt.xlabel("Boy")
#plt.figtext(0.14,0.75,"k: {}".format(*fit_params))
plt.show()
