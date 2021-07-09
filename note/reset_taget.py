import numpy as np
import pandas
import pandas as pd

SEED = 1000
path = '../input/enhance-data/'
enhance_data = pd.read_csv(path + "Google_backtrans.csv")
np.random.seed(SEED)
frac = 1 # frac越小，则新的target的值越接近原来的值
for _index in enhance_data.index.values:
    enhance_data.loc[_index,'target'] = np.random.normal(enhance_data.loc[_index,'target'],frac*enhance_data.loc[_index,'standard_error'])
enhance_data.to_csv(path + "fix_target_backtrans.csv")

print()