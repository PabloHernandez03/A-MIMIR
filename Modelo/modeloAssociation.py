import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import association_rules

dataFrame = pd.read_csv('./DatasetAssociation.csv')
frequent_itemsets = apriori(dataFrame, min_support=0.5, use_colnames=True)
rules = association_rules(frequent_itemsets, metric='lift', min_threshold=0.8,num_itemsets=1)

print(frequent_itemsets)
print("-"*20)
print(rules)