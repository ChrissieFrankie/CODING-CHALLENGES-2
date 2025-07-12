from pandas import read_csv # the csvs contain the data you need to use

test_csv = read_csv("titanic/test.csv") # read the test.csv file
train_csv = read_csv("titanic/train.csv") # read the train.csv file

print(test_csv.head()) # read the first 5 rows of the test_csv
print(train_csv.head()) # read the first 5 rows of the train_csv


