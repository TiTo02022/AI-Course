import pandas as pd
chipo=pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv',sep='\t')
#print(chipo.head(10))
#x=chipo.shape[0]
#print(x)
#print(len(chipo.columns))
#print(list(chipo.columns))
#indx=chipo.index
#print(indx)

print(chipo.item_price.dtype)