import csv
import pandas
		
data = pandas.read_csv('down-regulated_genes.csv',sep='\t')

data = data[['Chr','Start','End']]
print(data)
data.to_csv(r'down-regulated_genes.narrowPeak', index=None, sep='\t', header =True)


