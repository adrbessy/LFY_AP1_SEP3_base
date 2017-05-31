import csv
import pandas
import numpy as np
		
data1 = pandas.read_csv('../big_files/GSE576/GSE576_treated/tab_sep_LFY_regulated_genes_with_GSE96799.csv',sep='\t')
data2 = pandas.read_csv('intersect_microarray576_CHIP28063_down_up_ID.txt',sep='\t')
#df = pandas.DataFrame({'Col1': ['Bob', 'Joe', 'Bill', 'Mary', 'Joe'],
                   #'Col2': ['Joe', 'Steve', 'Bob', 'Bob', 'Steve'],
                   #'Col3': np.random.random(5)})
df1 = data1[['ID','Annotation']]
df2 = data2[['ID']]
#print(type(data2))
#df2 = unique(data2[['ID']])
print(df2)
#print("df1 : ",df1)
#result = pd.merge(left, right, how='right', on=['key1', 'key2'])
result = pandas.merge(df2, df1, how='outer', on=['ID'])
result = result[:371]
#print("result : ",result)	



#ID = []
#for i in range(len(data)):
	#ID.append(data["Locus"][i])
#print("ID : ",ID)
	
	
#data2 = pandas.read_csv('../big_files/GSE96806/tab_sep_ChIP_Seq_GSE96806.csv',sep='\t')

#data3 = data2[data2['Nearest_PromoterID'].isin(ID)]
#print("data3 : ",data3)

result.to_csv(r'merge_Schmid_Winter.csv', index=None, sep='\t', header =True)
