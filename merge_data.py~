import csv
import pandas
		
data1 = pandas.read_csv('../big_files/GSE576/GSE576_treated/all.csv',sep='\t')
data2 = pandas.read_csv('../big_files/GSE576/GSE576_treated/tab_sep_LFY_regulated_genes_with_GSE96799.csv',sep='\t')

df1 = data1[['ath1_probe', 'FC_27_28_35_36_GSE576','P.value_GSE576_27_28_35_36_down','P.value_27_28_35_36_up','FC_29_30_37_38_GSE576','P.value_GSE576_29_30_37_38_down','P.value_29_30_37_38_up','FC_31_32_39_40_GSE576','P.value_GSE576_31_32_39_40_down','P.value_31_32_39_40_up','FC_33_34_41_42_GSE576','P.value_GSE576_33_34_41_42_down','P.value_33_34_41_42_up']]
df2 = data2[['Locus.Identifier','ath1_probe', 'Annotation']]

#print("df1 : ",df1)
#result = pd.merge(left, right, how='right', on=['key1', 'key2'])
result = pandas.merge(df1, df2, how='outer', on=['ath1_probe'])
#print("result : ",result)	



#ID = []
#for i in range(len(data)):
	#ID.append(data["Locus"][i])
#print("ID : ",ID)
	
	
#data2 = pandas.read_csv('../big_files/GSE96806/tab_sep_ChIP_Seq_GSE96806.csv',sep='\t')

#data3 = data2[data2['Nearest_PromoterID'].isin(ID)]
#print("data3 : ",data3)

result.to_csv(r'merge_.csv', index=None, sep='\t', header =True)
