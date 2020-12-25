import re
from prediction_data import dataset,feature_set,no_of_items

def calc_prob(word,category):
    if word not in feature_set or word not in dataset[category]:
        return 0
    return float(dataset[category][word])/no_of_items[category]
def weighted_prob(word,category):
    basic_prob=calc_prob(word,category)
    if word in feature_set:
        tot=sum(feature_set[word].values())
    else:
        tot=0
    weight_prob=1
    return weight_prob

def test_prob(test,category):
    split_data=re.split('[^a-zA-Z0-9\']',test)
    data=[]
    #print("split data is",split_data)
    for i in split_data:
        if ' ' in i:
            i=i.split(' ')
            for j in i:
                if j not in data:
                    data.append(j.lower())
        elif len(i)>2 and i not in data:
            data.append(i.lower())
    p=1
    for i in data:
        p*=calc_prob(i,category)
    return p
def naive_bayes(test):
    results={}
    for i in dataset.keys():
        cat_prob=float(no_of_items[i])/sum(no_of_items.values())
        #print("class probability of",i,"is",cat_prob)
        test_prob1=test_prob(test,i)
        results[i]=test_prob1*cat_prob
    return results
print("Enter the tuple")
text=input()
result=naive_bayes(text)
if result['easy'] > result['tough'] and result['easy']>result['medium']:
    print("Easy")
    '''print(result['easy'])
    print(result['tough'])'''
elif result['medium'] > result['tough'] and result['medium']>result['easy']:
        print("Medium")
else:
    print("Tough")
'''    print(result['easy'])
    print(result['tough'])'''
