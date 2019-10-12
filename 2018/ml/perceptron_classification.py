import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

from perceptron import Perceptron

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# preparing data
df = pd.read_csv(url, header=None)

y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)

X = df.iloc[0:100, [0,2]].values

plt.scatter(X[:50,0], X[:50,1], color='red', marker='o', label='щетинистый')
plt.scatter(X[50:100,0], X[50:100,1], color='blue', marker='x', label='разноцветный')

plt.xlabel('длина чашелистика')
plt.ylabel('длина лепестка')

plt.legend(loc='upper left')
plt.show()

# training model
neuron = Perceptron(eta=0.1, n_iter=10)
neuron.fit(X, y)

plt.plot(range(1, len(neuron.errors_)+1), neuron.errors_, marker='o')
plt.xlabel('Эпохи')
plt.ylabel('Число случаев ошибочной классификации')

plt.show()
