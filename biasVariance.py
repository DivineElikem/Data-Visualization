import matplotlib.pyplot as plt

variance = [1,2,4,8,16,32,64,128,256]
bias_squared = [256,128,64,32,16,8,4,2,1]
total_error = [x+y for x,y in zip(variance,bias_squared)]

xs = [x for x,_ in enumerate(variance)]

plt.plot(xs,variance, 'b-', label='variance')
plt.plot(xs,bias_squared, 'g-.', label='bias squared')
plt.plot(xs,total_error, 'r:', label='total error')

plt.legend(loc=9)
plt.xlabel('Model Complexity')
plt.title('Bias-Variance Trade off')
plt.show()


