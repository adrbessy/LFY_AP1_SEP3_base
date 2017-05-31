import csv
import pandas
		
data1 = pandas.read_csv('intersect_chip_microarray_Wellmer_down_up-regulated_genes.csv',sep='\t')
data2 = pandas.read_csv('intersect_microarray576_CHIP28063_down_up_ID.txt',sep='\t')
data1 = data1[['ID']]
data2 = data2[['ID']]
print(data1.merge(data2))


#data = data[['Chr','Start','End']]
#print(data)
#data.to_csv(r'down-regulated_genes.narrowPeak', index=None, sep='\t', header =True)


