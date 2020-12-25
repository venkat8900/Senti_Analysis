import re
import csv
from stopwords import stopwords

fh=open("training.csv","r")

# The delimiter in the csv file is '+' instead of comma. This was done to compromise with the commas in the sentence in the sentence of the dataset used.
reader = csv.reader(fh, delimiter='+')

# It is the dictionary that has the data : { label(positive/negative) : { word : count of number of occurences of the word } }
dataset={}

# It is the dictionary that keeps the count of records that are labeled a label l for each label l
# That is, { label l : No. of records that are labeled l }
no_of_items={}

# This is the dictionary that contains the count of the occurences of word under each label
# That is, { word : { label l : count of the occurence of word with label l } }
feature_set={}
word_count={}
stopword_count={}
# For each sentence in dataset
for row in reader:
    # Initialize the label in the dictionary if not present already
    no_of_items.setdefault(row[1],0)
    word_count.setdefault(row[1],0)
    stopword_count.setdefault(row[1],0)
    # Increase the count of occurence of label by 1 for every occurence
    no_of_items[row[1]]+=1
    # Initialize the dictionary for a label if not present
    dataset.setdefault(row[1],{})
    #print("dataset is",dataset)
    # Split the sentence with respect to non-characters, and donot split if apostophe is present
    split_data=re.split('[^a-zA-Z\']',row[0])
    # For every word in split data
    #print("split data is",split_data)
    for i in split_data:
        # Removing stop words to a small extent by ignoring words with length less than 3
        if len(i) > 2:
            # Initialize the word count in dataset
            dataset[row[1]].setdefault(i.lower(),0)
            #print("dataset is",dataset)
            # Increase the word count on its occurence with label row[1]
            dataset[row[1]][i.lower()]+=1
            word_count[row[1]]+=1
            # Initialze a dictionary for a newly found word in feature set
            feature_set.setdefault(i.lower(),{})
            # If the label was found for the word, for the first time, initialize corresponding count value for word as key
            feature_set[i.lower()].setdefault(row[1],0)
            # Increment the count for the word in that label 
            feature_set[i.lower()][row[1]]+=1
        if i in stopwords:
                        stopword_count[row[1]]+=1
print (feature_set)
print("no of items\n")
print (no_of_items)
print("dataset")
print(dataset)
print(word_count)
print(stopword_count)
