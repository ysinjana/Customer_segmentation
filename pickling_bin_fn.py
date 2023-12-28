import pickle
from bins_fn import bins

with open('bins_function.pkl', 'wb') as file:
    pickle.dump(bins, file)