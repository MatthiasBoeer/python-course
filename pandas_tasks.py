import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def swap(dataframe, column1, column2):
    cols = list(dataframe.columns)
    c1 = cols.index(column1)
    c2 = cols.index(column2)

    cols[c1], cols[c2] = cols[c2], cols[c1]
    return dataframe[cols]

def trim(dataframe, column):
    lower = dataframe[column].quantile(0.05)
    upper = dataframe[column].quantile(0.95)

    return dataframe[dataframe[column].between(lower, upper)]

def fill_na(dataframe):
    numeric_columns = dataframe.select_dtypes(include=np.number).columns
    dataframe[numeric_columns] = dataframe[numeric_columns].fillna(dataframe[numeric_columns].mean())

def merge_dataframes():
    dict1 = {
        "ID" : [1,2,3],
        "Name" : ["Matthias", "Inga", "Laurine"],
        "Age" : ["99", "24", "24"]
    }
    print(dict1)

    dict2 = {
        "ID" : [1,2,3],
        "Status" : ["Unc", "Baby", "Newborn"],
        "IQ" : ["0", "100", "200"]
    }
    # print(dict2)

    df1 = pd.DataFrame(dict1)
    df2 = pd.DataFrame(dict2)

    merged = pd.merge(df1, df2, on="ID")
    # print(merged)

    appended = pd.concat([df1, df2], axis=1)
    # print(appended)
    return merged, appended

def histogram(dataframe, column):
    dataframe[column].hist(bins=20, edgecolor="blue")
    plt.title("Histogram of {}".format(column))
    plt.xlabel(column)
    plt.ylabel("Frequency")

    plt.show()

def correlation(dataframe):
    correlation_matrix = dataframe.corr(numeric_only=True)
    print(correlation_matrix)

def main():
    # task 1
    dataframe = pd.read_csv("resources/dataTitanic.csv")

    # task 2
    dataframe = dataframe.set_index("PassengerId")

    # task 3
    dataframe["Worth Saving?"] = np.where(dataframe["Pclass"] == 1, "Yes, right this way", "Hell No, peasant.")

    # task 4
    columns = dataframe.columns
    missing_values = dataframe.isna().sum()

    # task5
    dataframe = dataframe.sort_index(axis=1)
    dataframe = swap(dataframe, "Age", "Worth Saving?")

    # task 6
    dataframe = trim(dataframe, "Age")

    # task 7
    fill_na(dataframe)

    # print(dataframe.head())

    # task 8
    merge_dataframes()

    # task 9
    # histogram(dataframe, "Age")

    # task 10
    correlation(dataframe)


if __name__ == "__main__":
    main()