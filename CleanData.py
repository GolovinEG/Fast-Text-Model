import pandas as pd

def remove_dates(text: str):
    months = ("january", "february", "march", "april", "may", "june",
              "july", "august", "september", "october", "november", "december")
    for month in months:
        text = text.replace(month, "")
    start = 0
    year_starts = ("19", "20") #Assumes an year starting with 19 or 20
    for year_start in year_starts:
        index = text.find(year_start, start) #Records the index of the first year in text
        while index != -1 and index + 4 < len(text): #As lond as the text has years
            #If the following two charcters after the year_start are numbers - found an year, remove it from the text
            if text[index:index + 4].isnumeric() and not text[index + 4].isnumeric(): text = text.replace(text[index:index + 4], "", 1)
            else: start = index + 1 #Not an year - skip this number
            index = text.find(year_start, start) #Records the index of the next year in text
    return text

def clean_data(csv_path: str, label_culumn: str, full_data: list | str):
    '''Cleans the data by removing date related text
    Parameter
    ---------
    cas_path - the file path to the dataset csv

    label_column - the label of the column containing dateset's target
    
    full_data - the label (or list of labels) of the dataframe that will be used as the input'''
    df = pd.read_csv(csv_path)
    full_exists = False
    if type(full_data == type(list())):
        for item in full_data: #Combines multiple values into a single input
            if full_exists: df["full"] = df["full"] + " " + df[item] #Additional
            else: #Initial
                df["full"] = df[item]
                full_exists = True
    else: df["full"] = df[full_data]
    df["full"] = df["full"].apply(remove_dates)
    df[["full", label_culumn]].to_csv(csv_path[:-4] + "_clean.csv") #Makes a cleaned copy of the data 
    return

clean_data("fake_news.csv", "label", ["title", "text"]) #Removes date related text