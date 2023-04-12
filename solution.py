import scipy.stats as stats
import pandas as pd
import numpy as np

chat_id = 704471350

def solution(x: np.array) -> bool:
    Ttest = stats.ttest_1samp(a=x, popmean=500)
    alpha = 0.02
    if alpha < Ttest.pvalue:
      res = False
    else:
      res = True

    return res
