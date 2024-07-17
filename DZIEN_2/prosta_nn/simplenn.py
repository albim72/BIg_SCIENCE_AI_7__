import numpy as np

class SimpleNeuralNetwork:
    def __init__(self):
        np.random.seed(1)
        self.weights = 2*np.random.random((3,1))-1

    def __repr__(self):
        return (f"Nowa siec neuronowa oparta na klasie: {self.__class__.__name__}\n"
                f"Wylosowano wagi z ziarnem = 1:\n{self.weights}")

    # def __new__(cls, *args, **kwargs):
    #     return object.__new__(SimpleNeuralNetwork)
