# Author: magneticchen
# note:
# For normal variable use lower case
# For matrix variable use all upper case
# The meaning of "error" is equivalent to "cost"
import numpy as np
# Matrix
import NN_function as f
# Activation function etc.
# Import some essential module and function

class NeuralNetwork(object):
    def __init__(self, LayersCount = 1, LayerNeuronsCount = [1], Name = "Unamed_Neural_Network"):
        self.LayersCount = LayersCount
        self.LayerNeuronsCount = LayerNeuronsCount
        self.Weight = []
        self.Bias = []
        self.Name = Name
        # Initialize some general variable for NN
        for x in range(0, self.LayersCount-1):
            self.Weight.append(np.random.randn(self.LayerNeuronsCount[x], self.LayerNeuronsCount[x+1]))
            self.Bias.append(np.random.randn(1, self.LayerNeuronsCount[x+1]))
    # Initlalize NN structure

    def __str__(self):
        s = "An "+self.Name+"@NeuralNetwork object\nDetail:\n\n"
        for layer in range(0, self.LayersCount-1):
            s = s+"*** layer"+str(layer)+" ("+str(self.LayerNeuronsCount[layer])+" Neurons) ***\n"
            s = s+">>>layer"+str(layer)+" to layer"+str(layer+1)+" Weight\n"
            s = s+str(self.Weight[layer])+"\n"
            s = s+">>>layer"+str(layer)+" to layer"+str(layer+1)+" Bias\n"
            s = s+str(self.Bias[layer])+"\n\n"
        # Print its layer by layer one by one
        s = s+"*** layer"+str(self.LayersCount)+" ("+str(self.LayerNeuronsCount[self.LayersCount-1])+" Neurons) ***\n"
        # Last layer
        return s
    # Print detail info for Neural Network

    def feed(self, InputData):
        A = f.sigmoid(InputData)
        for layer in range(0, self.LayersCount-1):
            W = np.dot(A, self.Weight[layer])
            B = np.dot(np.ones((InputData.shape[0],1)), self.Bias[layer])
            A = f.sigmoid(W+B)
        return f.logit(A)
        # Variable explianation
        # A = ActivationFunction(BacksideSum)
        # W = A*Weight
        # B = Ones(InputDataAmount, 1)*Bias
        # BacksideSum = W+B or InputData
    # Feed data forward

    def savetoFile(self, FileName):
        print()
    # Save Neural Network to .node File

class train(object):
    def BackPropagation(MyNeuralNetwork, InputData, OutputData, speed = 0.1):
        # "speed" is the training speed, which "weight adjustment" = speed * djdw
        DJDW = []
        DELTA = []
        A = []
        Z = []
        # djdw = tangen of weight relative to cost(error), actually "dj/dw"
        # delta = FrontsideError*DerivativeofActivationFunction(BacksideSum)
        # a = ActivationFunction(BacksideSum)
        # Z = BacksideSum
        Z.append(InputData)
        A.append(f.sigmoid(Z[-1]))
        for layer in range(0, MyNeuralNetwork.LayersCount-1):
            W = np.dot(A[-1], MyNeuralNetwork.Weight[layer])
            B = np.dot(np.ones((InputData.shape[0],1)), MyNeuralNetwork.Bias[layer])
            Z.append(W+B)
            A.append(f.sigmoid(Z[-1]))
            # For variable explianation go NeuralNetwork.feed()
        # Push data forward and collect all Z and A
        DELTA.insert(0, -np.dot((f.sigmoid(OutputData)-A[MyNeuralNetwork.LayersCount-1]), f.Derivativeofsigmoid(Z[MyNeuralNetwork.LayersCount-1])))
        for layer in range(MyNeuralNetwork.LayersCount-2, -1, -1):
            DJDW.insert(0, np.dot(np.transpose(A[layer]), DELTA[0]))
            # remark that DELTA[0] is always the latest one
            DELTA.insert(0, np.dot(DELTA[0], np.transpose(MyNeuralNetwork.Weight[layer]))*f.Derivativeofsigmoid(Z[layer]))
            # Delta = Deltafront*transpose(ThisLayerWeight)*DerivativeofActivationFunction(ThisLayerBacksideSum)
            # For variable explianation go NeuralNetwork.feed()
        # Get all tangen of weight relative to cost(error)
        for layer in range(0, MyNeuralNetwork.LayersCount-1):
            MyNeuralNetwork.Weight[layer] = MyNeuralNetwork.Weight[layer]-speed*DJDW[layer]
            MyNeuralNetwork.Bias[layer] = MyNeuralNetwork.Bias[layer]-speed*np.dot(np.ones((1, InputData.shape[0])), DELTA[layer+1])
        # Add adjustment to each weight

def mixNeuralNetwork(NN1, NN2):
    print()