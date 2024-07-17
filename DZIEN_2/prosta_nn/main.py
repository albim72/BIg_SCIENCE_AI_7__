import numpy as np
from simplenn import SimpleNeuralNetwork

network = SimpleNeuralNetwork()
print(network)
# print(network.weights)

train_inputs = np.array([[1,1,0],[1,1,1],[1,1,0],[1,0,0],[0,1,1],[0,1,0],])
train_output = np.array([[0,1,0,0,1,0]]).T
train_iterators = 50_000


network.train(train_inputs,train_output,train_iterators)
print(network.weights)

print("ocena modelu")
testdata = np.array([[1,1,1],[1,0,0],[0,1,1],[0,1,0],[0,0,1],[0,0,0],])

for data in testdata:
    print(f"wynik dla {data} wynosi: {network.propagation(data)}")
