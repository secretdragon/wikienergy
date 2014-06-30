import sys
sys.path.append('../')
#print sys.path
import numpy as np

import numpy as np
from disaggregator import evaluation_metrics as evm

def unit_rss(t,p):
    residuals = np.array([x-y for (x,y) in zip(t,p)])
    squares = np.array([x**2 for x in residuals])
    return squares.sum()

if __name__=='__main__':
    truth = np.ones(7)
    prediction = np.zeros(7)
    print evm.sum_error(truth,prediction)
    print 'The sum of the squared residuals(evm) is {} '.format(evm.rss(truth,prediction))
    print 'The sum of the squared residuals(unit) is {}'.format(unit_rss(truth,prediction))
