import csv, sqlite3

con = sqlite3.connect("LFY_base.db")
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
###########################
#cur.execute("""
#SELECT Locus_Identifier 
#FROM microarrays_GSE911
#WHERE Pvalue_35sLFY_LER_up < '0.05'
#AND Pvalue_Dex_mock_up < '0.05'
#AND Pvalue_DexCyclo_cyclo_up < '0.05'

#INTERSECT

#SELECT Locus_Identifier 
#FROM microarrays_GSE28062 
#WHERE Pvalue_LFYGR_WT_up < '0.05' 

#""")
#col_name_list = [tuple[0] for tuple in cur.fetchall()]
#print(str(col_name_list).replace('u',''))
###############################
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

## CREATE a table
#cur.execute("""CREATE TABLE ChIP_Seq_GSE20176 (
#Nhits_GSM506208_090323,
#lengthRead_GSM506208_090323, 
#strand_GSM506208_090323, 
#chr_GSM506208_090323, 
#pos_GSM506208_090323,
#Nhits_GSM506209_090305,
#lengthRead_GSM506209_090305, 
#strand_GSM506209_090305, 
#chr_GSM506209_090305, 
#pos_GSM506209_090305,
#Nhits_GSM506209_090313,
#lengthRead_GSM506209_090313, 
#strand_GSM506209_090313, 
#chr_GSM506209_090313, 
#pos_GSM506209_090313,
#Nhits_GSM506210_090323,
#lengthRead_GSM506210_090323, 
#strand_GSM506210_090323, 
#chr_GSM506210_090323, 
#pos_GSM506210_090323,
#Nhits_GSM506210_090408,
#lengthRead_GSM506210_090408, 
#strand_GSM506210_090408, 
#chr_GSM506210_090408, 
#pos_GSM506210_090408,
#Nhits_GSM506211_090305,
#lengthRead_GSM506211_090305, 
#strand_GSM506211_090305, 
#chr_GSM506211_090305, 
#pos_GSM506211_090305,
#Nhits_GSM506211_090313,
#lengthRead_GSM506211_090313, 
#strand_GSM506211_090313, 
#chr_GSM506211_090313, 
#pos_GSM506211_090313
#);""")

### INSERT data from a file
#with open('GSE20176_RAW/GSM506211_090313.soa','rb') as fin: # `with` statement available in 2.5+
	## csv.DictReader uses first line in file for column headings by default
	#dr = csv.DictReader(fin, delimiter='\t') # comma is default delimiter
	#to_chip_db = [(i['Nhits'], i['lengthRead'], i['strand'], i['chr'], i['pos'] ) for i in dr]
#cur.executemany("INSERT INTO ChIP_Seq_GSE20176 (Nhits_GSM506211_090313, lengthRead_GSM506211_090313, strand_GSM506211_090313, chr_GSM506211_090313, pos_GSM506211_090313) VALUES (?, ?, ?, ?, ?);", to_chip_db)
#con.commit()

### DROP a table
#cur.execute('drop table if exists ChIP_Seq_GSE20176;')
#con.commit()

######### Display the names of the tables ############   
#res = con.execute("SELECT name FROM sqlite_master WHERE type='table';")
#for name in res:
	#print name[0]

######### Display the names of the columns from a table ############   
cur.execute("SELECT * FROM ChIP_Seq_GSE46986")
col_name_list = [tuple[0] for tuple in cur.description]
print(col_name_list)

##### Display the first column content
#cur.execute("""SELECT Nhits_GSM506209_090305 age FROM ChIP_Seq_GSE20176""")
#for row in cur:
    #print('{0} '.format(row[0]))

con.close()