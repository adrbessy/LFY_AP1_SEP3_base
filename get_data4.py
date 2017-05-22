import csv
import pandas
		
data = pandas.read_csv('merge2.csv',sep='\t')
#print(data[['log2_Fold_Change_4h']])
#data[['log2_Fold_Change_4h']] = data[['log2_Fold_Change_4h']].apply(pd.to_numeric)

data2 = []

#for i in range(len(data)	):
	#if data['log2_Fold_Change_4h'][i] < 0 :
		#print("yes !")
		#data2.append(data.iloc[i])
#print("data2 : ",data2)

#up-regulated = data[[data.log2_Fold_Change_4h] > 0]
#down-regulated = data[data.log2_Fold_Change_4h < 0]
#up-regulated = data.loc[(data["log2_Fold_Change_4h"] > 0) ]

#up-regulated.to_csv(r'up-regulated_genes.csv', index=None, sep='\t', header =True)
#down-regulated.to_csv(r'down-regulated_genes.csv', index=None, sep='\t', header =True)
