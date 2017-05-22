import csv
import pandas
#with open('../papers/Goslin_Wellmer_2017/PP2017-00098R1_Supplemental_Dataset_3.csv', 'rb') as csvfile:
	#spamreader = csv.reader(csvfile, delimiter='\t')
	#for row in spamreader:
		#content = list(row[i] for i in [22])
		#print content	
		
#colnames = ['This study']
data = pandas.read_csv('../papers/Goslin_Wellmer_2017/PP2017-00098R1_Supplemental_Dataset_3.csv',sep='\t')
#This_study = data["This_study"]

#print(data["Locus"][1])

genes=[]
for i in range(len(data)):
	if data["This_study"][i] == "Yes" :
		print(data["Locus"][i],"!", data["Description"][i],"!",data["Time-point:"][i])
		#genes.append([data["Locus"][i], data["Description"][i]])
		
#genes.to_csv(r'../papers/Goslin_Wellmer_2017/LFY_chip-seq_microarray_overlap_Locus_Description.txt', header=None, index=None, sep='\t', mode='a')

















#c_maxes = df.groupby(['Locus.identifier']).PValueLogRatio_Rep_1_2h.transform(max)
#df = df[df.PValueLogRatio_Rep_1_2h == c_maxes]