import numpy as np
import matplotlib.pyplot as plt

for i in range(1,4):
	nrm=np.random.normal(0.0,1.0,1000)
	np.savetxt("data/normal_datapoints"+str(i)+".csv",nrm,delimiter=",")
	plt.hist(nrm)
	plt.title('Normal Distribution')
	plt.savefig('plots/normal_plot'+str(i)+'.png')
	plt.show()

