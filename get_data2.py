import csv
import pandas
		
#colnames = ['This study']
data = pandas.read_csv('Wellmer_LFY_ChIP_Seq_microarray_overlap_without_spacing.csv',sep='\t')

ID = []
for i in range(len(data)):
	ID.append(data["Locus"][i])
print("ID : ",ID)
	
	
data2 = pandas.read_csv('../big_files/GSE96806/tab_sep_ChIP_Seq_GSE96806.csv',sep='\t')

data3 = data2[data2['Nearest_PromoterID'].isin(ID)]
print("data3 : ",data3)

data3.to_csv(r'Wellmer_LFY_ChIP_Seq_microarray_overlap_V2.csv', index=None, sep='\t', header =True)
