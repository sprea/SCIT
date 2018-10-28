import numpy as np
import matplotlib.pyplot as plt

for i in range(1,4):
	poi=np.random.poisson(100,1000)
	np.savetxt("data/poisson_datapoints"+str(i)+".csv",poi,delimiter=",")
	plt.hist(poi)
	plt.title('Poisson Distribution')
	plt.savefig('plots/poisson_plot'+str(i)+'.png')
	plt.show()

