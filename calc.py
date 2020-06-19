'''
@Author: your name
@Date: 2020-06-19 20:54:14
@LastEditTime: 2020-06-19 20:55:11
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \demo_calc\calc.py
'''
def neuron(x, w, b):
    y = x * w + b
    y = max(0, y)
    return y

if __name__ == "__main__":
    print(f"neuron(4, 1, 3):{neuron(4, 1, 3)}")