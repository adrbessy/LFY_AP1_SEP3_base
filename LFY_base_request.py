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
cur.execute("""
SELECT COUNT(Locus_Identifier) 
FROM microarrays_GSE96799
WHERE FC_2_4h > '0.05'
AND PValue_2_4h < '0.01' 
""")
result = cur.fetchone()
print(result)
############################### gives 476 DEGs

########################### I want the LFY DEGs number with the third replicate
cur.execute("""
SELECT COUNT(Locus_Identifier) 
FROM microarrays_GSE96799
WHERE FC_4_4h > '0.05'
AND PValue_4_4h < '0.01' 
""")
result = cur.fetchone()
print(result)
############################### gives 516 DEGs

########################### I want the LFY DEGs number with the fourth replicate
cur.execute("""
SELECT COUNT(Locus_Identifier) 
FROM microarrays_GSE96799
WHERE FC_5_4h > '0.05'
AND PValue_5_4h < '0.01' 
""")
result = cur.fetchone()
print(result)
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

####### combination UNION and INTERSECT
#(select * 
#from t1
#union
#select * 
#from t2)
#intersect
#(select * 
#from t3)



### DROP a table
#cur.execute('drop table if exists ChIP_Seq_GSE20176;')
#con.commit()

######### Display the names of the tables ############   
#res = con.execute("SELECT name FROM sqlite_master WHERE type='table';")
#for name in res:
	#print name[0]

######### Display the names of the columns from a table ############   
#cur.execute("SELECT * FROM ChIP_Seq_GSE46986")
#col_name_list = [tuple[0] for tuple in cur.description]
#print(col_name_list)

##### Display the first column content
#cur.execute("""SELECT Nhits_GSM506209_090305 age FROM ChIP_Seq_GSE20176""")
#for row in cur:
    #print('{0} '.format(row[0]))

con.close()