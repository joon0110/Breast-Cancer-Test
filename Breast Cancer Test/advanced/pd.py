import pandas as pd

def advancedStats(data, labels):
    '''Advanced stats should leverage pandas to calculate
    some relevant statistics on the data.

    data: numpy array of data
    labels: numpy array of labels
    '''
    # convert to dataframe
    df = pd.DataFrame(data)

    # print skew and kurtosis for every column
    # TODO
    for col in  df.columns:
        print("Column {} statistics:".format(col))
        print("\tSkewness: "+str(df[col].skew())+"\tKurtosis: "+str(df[col].kurtosis()))
        print("\n")
        
    # assign in labels
    df["labels"] = labels

    print("\n\nDataframe statistics")

    # groupby labels into "benign" and "malignant"
    # TODO
    gp = df.groupby("labels")

    # collect means and standard deviations for columns,
    # grouped by label

    # Print mean and stddev for Benign
    print("Benign Stats:")
    # TODO
    print("Mean:")
    print(gp.mean().loc["B"])
    print("Std:")
    print(gp.std().loc["B"])  
    print("\n")

    # Print mean and stddev for Malignant
    print("Malignant Stats:")
    # TODO
    print("Mean:")
    print(gp.mean().loc["M"])
    print("Std:")
    print(gp.std().loc["M"])
    

