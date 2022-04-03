import numpy as np

class ProcessData:

    def __init__(self):
        pass


    def get_prices_step(self, prices_array):
        steps = np.array(0)

        sliced_prices = prices_array[1:]

        for i in range(sliced_prices.shape[0]):
            step = sliced_prices[i] - prices_array[i]

            steps = np.append(steps, step)
        
        return steps