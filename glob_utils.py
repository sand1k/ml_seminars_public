import numpy as np
import os

def preview_data(data):
    # print out some data points
    num_rows, num_cols = data.shape
    for j in range(num_cols - 1):
        print('{:>8s}'.format('X[:,{}]'.format(j)),end='')
    print('{:>10s}'.format('y'))
    print('-'*26)
    for i in range(10):
        for j in range(num_cols - 1):
            print('{:8.2f}'.format(data[i, j]), end='')
        print('{:10.2f}'.format(data[i, num_cols - 1]))
    print('...')