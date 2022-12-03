## This is an experimental feature for testing the speed of filter lambda versus for loop filter

![image-results](/results.png)

The main purpose of this repository is to test the speed factor of using lambda filter or normal for loop

At first, I downloaded the dataset from [kaggle](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data). The main reason I used this data is that I wanted a quick dataset just to test a specific feature.

Next:
1. Install pandas and numpy libraries
2. Load the train.csv and sample_submissions.csv using pandas. The main reason that I loaded only train and sample_submissions is that I need a huge range of nunbers to filter out from.
3. run the following command 
    `
    python3 main.py
    `

This is the expected output
`
filter using lambda filter  took 1.5939585864543915e-06

filter using for loop took 0.000283005996607244

filter using  comprehension list 0.00021229800768196583 
`
