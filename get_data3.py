import csv
import pandas
		
data1 = pandas.read_csv('../papers/Goslin_Wellmer_2017/PP2017-00098R1_Supplemental_Dataset_3.csv',sep='\t')
data2 = pandas.read_csv('Wellmer_LFY_ChIP_Seq_microarray_overlap_V2.csv',sep='\t')

df1 = data1[['Locus','log2_Fold_Change_4h', 'P-value_4h','adjusted_P-value_4h']]

#print("df1 : ",df1)
#result = pd.merge(left, right, how='right', on=['key1', 'key2'])
result = pandas.merge(data2, df1, how='outer', on=['Locus'])
print("result : ",result)	



#ID = []
#for i in range(len(data)):
	#ID.append(data["Locus"][i])
#print("ID : ",ID)
	
	
#data2 = pandas.read_csv('../big_files/GSE96806/tab_sep_ChIP_Seq_GSE96806.csv',sep='\t')

#data3 = data2[data2['Nearest_PromoterID'].isin(ID)]
#print("data3 : ",data3)

result.to_csv(r'merge.csv', index=None, sep='\t', header =True)
