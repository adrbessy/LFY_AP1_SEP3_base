import csv, sqlite3

con = sqlite3.connect("../big_files/LFY_base.db")
cur = con.cursor()

###########REQUEST###############""



##### We want ALL locus identifier from microarrays_GSE28062 and microarrays_GSE911 
##### where Pvalue of down regulated  genes FC are < 0.05 for the condition 35S::LFY Ler vs WT Ler
##### AND where annotation contains "DNA binding"
##### AND where Pvalue of down regulated  genes FC are < 0.05 for the condition for the condition 35S::LFY-GR Ler Dexa vs WT Ler Dexa

#cur.execute("""
#SELECT Locus_Identifier 
#FROM microarrays_GSE911
#WHERE Pvalue_35sLFY_LER_down < '0.05' 
#AND Annotation LIKE '%DNA binding%'

#INTERSECT

#SELECT Locus_Identifier 
#FROM microarrays_GSE28062 
#WHERE Pvalue_LFYGR_WT_down < '0.05' 
#""")
#col_name_list = [tuple[0] for tuple in cur.fetchall()]
#print(str(col_name_list).replace('u',''))

########################### I want the LFY DEGs number with the first replicate
#cur.execute("""
#SELECT COUNT(Locus_Identifier) 
#FROM microarrays_GSE96799
#WHERE FC_1_4h > '0.05'
#AND PValue_1_4h < '0.01' 
#""")
#result = cur.fetchone()
#print(result)
############################### gives 876 DEGs

########################### I want the LFY DEGs number with the second replicate
#cur.execute("""
#SELECT COUNT(Locus_Identifier) 
#FROM microarrays_GSE96799
#WHERE FC_2_4h > '0.05'
#AND PValue_2_4h < '0.01' 
#""")
#result = cur.fetchone()
#print(result)
############################### gives 476 DEGs

########################### I want the LFY DEGs number with the third replicate
#cur.execute("""
#SELECT COUNT(Locus_Identifier) 
#FROM microarrays_GSE96799
#WHERE FC_4_4h > '0.05'
#AND PValue_4_4h < '0.01' 
#""")
#result = cur.fetchone()
#print(result)
############################### gives 516 DEGs

########################### I want the LFY DEGs number with the fourth replicate
#cur.execute("""
#SELECT COUNT(Locus_Identifier) 
#FROM microarrays_GSE96799
#WHERE FC_5_4h > '0.05'
#AND PValue_5_4h < '0.01' 
#""")
#result = cur.fetchone()
#print(result)
############################### gives 680 DEGs

#cur.execute("""
#SELECT Locus_Identifier 
#FROM microarrays_GSE96799
#WHERE PValue_1_2h < '0.05'
#AND PValue_1_4h < '0.05'
#AND PValue_1_8h < '0.05'
#AND PValue_1_12h < '0.05'
#AND PValue_4_2h < '0.05'

#INTERSECT

#SELECT Nearest_PromoterID 
#FROM ChIP_Seq_GSE96806 
#WHERE Peak_Score > '200' 

#""")
#col_name_list = [tuple[0] for tuple in cur.fetchall()]
#print(str(col_name_list).replace('u',''))

######################## Want intersect ID from ChIP_Seq_GSE28063 with Locus_Identifier from microarrays_GSE576

#cur.execute("""
#SELECT Locus_Identifier
#FROM microarrays_GSE576
#WHERE FC_31_32_39_40_GSE576 < '-0.5' 
#AND Pvalue_31_32_39_40_down < '0.01'

#INTERSECT

#SELECT ID 
#FROM ChIP_Seq_GSE28063  

#""")
#col_name_list = [tuple[0] for tuple in cur.fetchall()]
#print(str(col_name_list).replace('u',''))

######################## Want the same but with more input
#cur.execute("""
#SELECT microarrays_GSE576.Locus_Identifier, microarrays_GSE576.Annotation
#FROM microarrays_GSE576
#INNER JOIN ChIP_Seq_GSE28063 ON microarrays_GSE576.Locus_Identifier=ChIP_Seq_GSE28063.ID
#WHERE FC_31_32_39_40_GSE576 < '-0.5' 
#AND Pvalue_31_32_39_40_down < '0.01' 

#""")
#print(cur.fetchall())
#col_name_list = [tuple[0] for tuple in cur.fetchall()]
#print(str(col_name_list).replace('u',''))
#print([d[0] for d in cur.description])
#for row in cur:
    #print('{0} '.format(row[1]))
#SELECT my_table_1.stock, my_table_2.price, recommendation, volume
    #FROM my_table_1
    #INNER JOIN my_table_2 ON  my_table_1.stock=my_table_2.stock
    #WHERE stock=?
#########################
####### combination UNION and INTERSECT
#(select * 
#from t1
#union
#select * 
#from t2)
#intersect
#(select * 
#from t3)

#cur.execute("""CREATE TABLE IF NOT EXISTS ChIP_Seq_GSE28063 (
#PEAK_chr, 
#PEAK_start, 
#PEAK_end, 
#GENE_chr,
#GENE_start,
#GENE_end,
#ID
#);""")

### INSERT data from a file
#with open('../big_files/nearest_genes.txt','rb') as fin: # `with` statement available in 2.5+
	## csv.DictReader uses first line in file for column headings by default
	#dr = csv.DictReader(fin, delimiter='\t') # comma is default delimiter
	#to_chip_db = [(i['PEAK_chr'], i['PEAK_start'], i['PEAK_end'], i['GENE_chr'], i['GENE_start'], i['GENE_end'], i['ID'] ) for i in dr]
#cur.executemany("INSERT INTO ChIP_Seq_GSE28063 (PEAK_chr, PEAK_start, PEAK_end, GENE_chr,GENE_start,GENE_end,ID) VALUES (?, ?, ?, ?, ?, ?, ?);", to_chip_db)
#con.commit()

### DROP a table
#cur.execute('drop table if exists microarrays_GSE576;')
#con.commit()

######### Display the names of the tables ############   
res = con.execute("SELECT name FROM sqlite_master WHERE type='table';")
for name in res:
	print name[0]

######### Display the names of the columns from a table ############   
#cur.execute("SELECT * FROM microarrays_GSE576")
#col_name_list = [tuple[0] for tuple in cur.description]
#print(col_name_list)

##### Display the first column content
#cur.execute("""SELECT Nhits_GSM506209_090305 age FROM ChIP_Seq_GSE20176""")
#for row in cur:
    #print('{0} '.format(row[0]))

con.close()