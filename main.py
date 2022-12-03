import pandas as pd
import numpy as np
import timeit


train_csv_path = "train.csv"
samles_csv = "sample_submission.csv"


train_df = pd.read_csv(train_csv_path)
samples_df = pd.read_csv(samles_csv)

train_prices = train_df['SalePrice'].to_list()
samples_prices = samples_df['SalePrice'].to_list()



max_train = np.max(train_prices)
max_samples = np.max(samples_prices)


start_filter = timeit.default_timer()
lambda_filtered_samples = filter(lambda x: x < max_samples/2, train_prices)
print(f'filter using lambda filter  took {timeit.default_timer() - start_filter}')


start_filter = timeit.default_timer()
filtered_samples_using_forloop =[]
for x in train_prices:
    if x < max_samples/2:
        filtered_samples_using_forloop.append(x)
print(f'filter using for loop took {timeit.default_timer() - start_filter}')
        
        
start_filter = timeit.default_timer()
comprehension_filter = [x for x in train_prices if x < max_samples/2]
print(f'filter using  comprehension list {timeit.default_timer() - start_filter} ')