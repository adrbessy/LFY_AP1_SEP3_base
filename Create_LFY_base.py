import csv, sqlite3

con = sqlite3.connect("LFY_base.db")
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS microarrays_GSE911 (
Locus_Identifier, 
ath1_probe, 
Annotation, 
FC_35sLFY_LER REAL, 
Pvalue_35sLFY_LER_down REAL, 
Pvalue_35sLFY_LER_up REAL, 
FC_Dex_mock REAL, 
Pvalue_Dex_mock_down REAL, 
Pvalue_Dex_mock_up REAL, 
FC_DexCyclo_cyclo REAL, 
Pvalue_DexCyclo_cyclo_down REAL, 
Pvalue_DexCyclo_cyclo_up REAL);""")

cur.execute("""CREATE TABLE IF NOT EXISTS microarrays_GSE576 (
Locus_Identifier, 
ath1_probe, 
Annotation, 
FC_27_28_35_36_GSE576,
Pvalue__27_28_35_36_down,
Pvalue_27_28_35_36_up,
FC_29_30_37_38_GSE576,
Pvalue_29_30_37_38_down,
Pvalue_29_30_37_38_up, 
FC_31_32_39_40_GSE576,
Pvalue_31_32_39_40_down,
Pvalue_31_32_39_40_up, 
FC_33_34_41_42_GSE576,
Pvalue_33_34_41_42_down,
Pvalue_33_34_41_42_up);""")

cur.execute("""CREATE TABLE IF NOT EXISTS microarrays_GSE28062 (
Locus_Identifier, 
ath1_probe, 
Annotation, 
FC_LFYGR_WT REAL, 
Pvalue_LFYGR_WT_down REAL, 
Pvalue_LFYGR_WT_up REAL);""")

cur.execute("""CREATE TABLE IF NOT EXISTS microarrays_Chahtane (
Locus_Identifier, ath1_probe, 
Annotation, 
FC_SP1_col REAL,
Pvalue_SP1_col_down REAL,
Pvalue_SP1_col_up REAL, 
FC_SP3_col REAL,
Pvalue_SP3_col_down REAL,
Pvalue_SP3_col_up REAL);""")

cur.execute("""CREATE TABLE IF NOT EXISTS microarrays_GSE576 (
Locus_Identifier, 
ath1_probe, 
Annotation, 
FC_Col_5DAF_vs_lfy_5DAF REAL,
Pvalue_Col_5DAF_vs_lfy_5DAF_down REAL,
Pvalue_Col_5DAF_vs_lfy_5DAF_up REAL,
FC_Col_7DAF_vs_lfy_7DAF REAL,
Pvalue_Col_7DAF_vs_lfy_7DAF_down REAL,
Pvalue_Col_7DAF_vs_lfy_7DAF_up REAL, 
FC_Col3DAF_lfy3DAF REAL,
Pvalue_Col3DAF_lfy3DAF_down REAL,
Pvalue_Col3DAF_lfy3DAFup REAL, 
FC_Col_0DAF_vs_lfy_0DAF REAL,
Pvalue_Col_0DAF_vs_lfy_0DAF_down REAL,
Pvalue_Col_0DAF_vs_lfy_0DAF_up REAL);""")

cur.execute("""CREATE TABLE IF NOT EXISTS microarrays_GSE96799 (
Locus_Identifier, 
ath1_probe, 
Annotation, 
FC_1_2h REAL, 
PValue_1_2h REAL, 
FC_1_4h REAL, 
PValue_1_4h REAL, 
FC_1_8h REAL, 
PValue_1_8h REAL, 
FC_1_12h REAL, 
PValue_1_12h REAL, 
FC_4_2h REAL, 
PValue_4_2h REAL, 
FC_4_4h REAL, 
PValue_4_4h REAL, 
FC_4_8h REAL, 
PValue_4_8h REAL, 
FC_4_12h REAL, 
PValue_4_12h REAL, 
FC_2_2h REAL, 
PValue_2_2h REAL, 
FC_2_4h REAL, 
PValue_2_4h, 
FC_2_8h, 
PValue_2_8h, 
FC_2_12h, 
PValue_2_12h, 
FC_1_0h, 
PValue_1_0h, 
FC_2_0h, 
PValue_2_0h, 
FC_4_0h, 
PValue_4_0h, 
FC_5_2h, 
PValue_5_2h, 
FC_5_4h, 
PValue_5_4h, 
FC_5_8h, 
PValue_5_8h, 
FC_5_12h, 
PValue_5_12h, 
FC_5_0h, 
PValue_5_0h, 
FC_Infloresence_Cyclohexamide_treatment_3h_1, 
Pvalue_Infloresence_Cyclohexamide_treatment_3h_1, 
FC_Infloresence_Cyclohexamide_treatment_3h_2, 
Pvalue_Infloresence_Cyclohexamide_treatment_3h_2, 
FC_Infloresence_Cyclohexamide_treatment_3h_3, 
Pvalue_Infloresence_Cyclohexamide_treatment_3h_3, 
FC_Infloresence_Cyclohexamide_treatment_3h_4, 
Pvalue_Infloresence_Cyclohexamide_treatment_3h_4);""")

cur.execute("""CREATE TABLE IF NOT EXISTS ChIP_Seq_GSE96806 (
Chr, 
Start, 
End, 
Peak_Score, 
Annotation, 
Nearest_PromoterID );""")

### CREATE a table
#cur.execute("""CREATE TABLE IF NOT EXISTS ChIP_Seq_GSE20176 (
#lengthRead_AP1_GR_2h_1, 
#strand_AP1_GR_2h_1, 
#chr_AP1_GR_2h_1, 
#pos_AP1_GR_2h_1,
#lengthRead_AP1_GR_2h_2, 
#strand_AP1_GR_2h_2, 
#chr_AP1_GR_2h_2, 
#pos_AP1_GR_2h_2,
#lengthRead_AP1_GR_uninduced_1, 
#strand_AP1_GR_uninduced_1, 
#chr_AP1_GR_uninduced_1, 
#pos_AP1_GR_uninduced_1,
#lengthRead_AP1_GR_uninduced_2, 
#strand_AP1_GR_uninduced_2, 
#chr_AP1_GR_uninduced_2, 
#pos_AP1_GR_uninduced_2);""")

#cur.execute("""CREATE TABLE IF NOT EXISTS ChIP_Seq_GSE24568 (
#id,
#chr, 
#pos,
#size,
#orp_rank,
#log2_orp,
#fdr_bh_q1,
#fdr_bh_q2,
#rc_chip1,
#rc_chip2,
#rc_ctrl1,
#rc_ctrl2,
#overlap_names,
#overlap_types,
#up_names,
#up_dist,
#up_strands,
#down_names,
#down_dist,
#down_strands
#);""")

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

with open('tab_sep_LFY_regulated_genes_with_GSE96799.csv','rb') as fin: # `with` statement available in 2.5+
	# csv.DictReader uses first line in file for column headings by default
	dr = csv.DictReader(fin, delimiter='\t') # comma is default delimiter
	to_micGSE911_db = [(i['Locus.Identifier'], i['ath1_probe'], i['Annotation'], i['FC_35sLFY_LER'], i['P.value_35sLFY_LER_down'], i['P.value_35sLFY_LER_up'], i['FC_Dex_mock'], i['P.value_Dex_mock_down'], i['P.value_Dex_mock_up'], i['FC_DexCyclo_cyclo'], i['P.value_DexCyclo_cyclo_down'], i['P.value_DexCyclo_cyclo_up'] ) for i in dr]

with open('tab_sep_LFY_regulated_genes_with_GSE96799.csv','rb') as fin: # `with` statement available in 2.5+
	# csv.DictReader uses first line in file for column headings by default
	dr = csv.DictReader(fin, delimiter='\t') # comma is default delimiter
	to_micGSE28062_db = [(i['Locus.Identifier'], i['ath1_probe'], i['Annotation'], i['FC_LFYGR_WT_GSE28062'], i['P.value_LFYGR_WT_down'], i['P.value_LFYGR_WT_up'] ) for i in dr]

with open('tab_sep_LFY_regulated_genes_with_GSE96799.csv','rb') as fin: # `with` statement available in 2.5+
	# csv.DictReader uses first line in file for column headings by default
	dr = csv.DictReader(fin, delimiter='\t') # comma is default delimiter
	to_micChahtane_db = [(i['Locus.Identifier'], i['ath1_probe'], i['Annotation'], i['FC_SP1_col'],i['P.value_SP1_col_down'], i['P.value_SP1_col_up'], i['FC_SP3_col'],i['P.value_SP3_col_down'], i['P.value_SP3_col_up'] ) for i in dr]	

with open('tab_sep_LFY_regulated_genes_with_GSE96799.csv','rb') as fin: # `with` statement available in 2.5+
	# csv.DictReader uses first line in file for column headings by default
	dr = csv.DictReader(fin, delimiter='\t') # comma is default delimiter
	to_micGSE576_db = [(i['Locus.Identifier'], i['ath1_probe'], i['Annotation'], i['FC_Col_5DAF_vs_lfy_5DAF'],i['P.value_Col_5DAF_vs_lfy_5DAF_down'],i['P.value_Col_5DAF_vs_lfy_5DAF_up'],i['FC_Col_7DAF_vs_lfy_7DAF'],i['P.value_Col_7DAF_vs_lfy_7DAF_down'],i['P.value_Col_7DAF_vs_lfy_7DAF_up'], i['FC_Col3DAF_lfy3DAF'],i['P.value_Col3DAF_lfy3DAF_down'],i['P.value_Col3DAF_lfy3DAFup'], i['FC_Col_0DAF_vs_lfy_0DAF'],i['P.value_Col_0DAF_vs_lfy_0DAF_down'],i['P.value_Col_0DAF_vs_lfy_0DAF_up'] ) for i in dr]		
	
with open('tab_sep_LFY_regulated_genes_with_GSE96799.csv','rb') as fin: # `with` statement available in 2.5+
	# csv.DictReader uses first line in file for column headings by default
	dr = csv.DictReader(fin, delimiter='\t') # comma is default delimiter
	to_micGSE96799_db = [(i['Locus.Identifier'], i['ath1_probe'], i['Annotation'], i['LogRatio_Rep_1_2h'], i['PValueLogRatio_Rep_1_2h'], i['LogRatio_Rep_1_4h'], i['PValueLogRatio_Rep_1_4h'], i['LogRatio_Rep_1_8h'], i['PValueLogRatio_Rep_1_8h'], i['LogRatio_Rep_1_12h'], i['PValueLogRatio_Rep_1_12h'], i['LogRatio_Rep_4_2h'], i['PValueLogRatio_Rep_4_2h'], i['LogRatio_Rep_4_4h'], i['PValueLogRatio_Rep_4_4h'], i['LogRatio_Rep_4_8h'], i['PValueLogRatio_Rep_4_8h'], i['LogRatio_Rep_4_12h'], i['PValueLogRatio_Rep_4_12h'], i['LogRatio_Rep_2_2h'], i['PValueLogRatio_Rep_2_2h'], i['LogRatio_Rep_2_4h'], i['PValueLogRatio_Rep_2_4h'], i['LogRatio_Rep_2_8h'], i['PValueLogRatio_Rep_2_8h'], i['LogRatio_Rep_2_12h'], i['PValueLogRatio_Rep_2_12h'], i['LogRatio_Rep_1_0h'], i['PValueLogRatio_Rep_1_0h'], i['LogRatio_Rep_2_0h'], i['PValueLogRatio_Rep_2_0h'], i['LogRatio_Rep_4_0h'], i['PValueLogRatio_Rep_4_0h'], i['LogRatio_Rep_5_2h'], i['PValueLogRatio_Rep_5_2h'], i['LogRatio_Rep_5_4h'], i['PValueLogRatio_Rep_5_4h'], i['LogRatio_Rep_5_8h'], i['PValueLogRatio_Rep_5_8h'], i['LogRatio_Rep_5_12h'], i['PValueLogRatio_Rep_5_12h'], i['LogRatio_Rep_5_0h'], i['PValueLogRatio_Rep_5_0h'], i['LogRatio_Infloresence_Cyclohexamide_treatment_3h_1'], i['PvalueLogRatio_Infloresence_Cyclohexamide_treatment_3h_1'], i['LogRatio_Infloresence_Cyclohexamide.treatment_3h_2'], i['PvalueLogRatio_Infloresence_Cyclohexamide_treatment_3h_2'], i['LogRatio_Infloresence_Cyclohexamide.treatment_3h_3'], i['PvalueLogRatio_Infloresence_Cyclohexamide_treatment_3h_3'], i['LogRatio_Infloresence_Cyclohexamide.treatment_3h_4'], i['PvalueLogRatio_Infloresence_Cyclohexamide_treatment_3h_4'] ) for i in dr]		
	
with open('tab_sep_ChIP_Seq_GSE96806.csv','rb') as fin: # `with` statement available in 2.5+
	# csv.DictReader uses first line in file for column headings by default
	dr = csv.DictReader(fin, delimiter='\t') # comma is default delimiter
	to_chip_db = [(i['Chr'], i['Start'], i['End'], i['Peak_Score'], i['Annotation'], i['Nearest_PromoterID']) for i in dr]

cur.executemany("INSERT INTO microarrays_GSE911 (Locus_Identifier, ath1_probe, Annotation, FC_35sLFY_LER, Pvalue_35sLFY_LER_down, Pvalue_35sLFY_LER_up, FC_Dex_mock, Pvalue_Dex_mock_down, Pvalue_Dex_mock_up, FC_DexCyclo_cyclo, Pvalue_DexCyclo_cyclo_down, Pvalue_DexCyclo_cyclo_up) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_micGSE911_db)
con.commit()
cur.executemany("INSERT INTO microarrays_GSE28062 (Locus_Identifier, ath1_probe, Annotation, FC_LFYGR_WT, Pvalue_LFYGR_WT_down, Pvalue_LFYGR_WT_up) VALUES (?, ?, ?, ?, ?, ?);", to_micGSE28062_db)
con.commit()
cur.executemany("INSERT INTO microarrays_Chahtane (Locus_Identifier, ath1_probe, Annotation, FC_SP1_col,Pvalue_SP1_col_down,Pvalue_SP1_col_up, FC_SP3_col,Pvalue_SP3_col_down,Pvalue_SP3_col_up) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", to_micChahtane_db)
con.commit()
cur.executemany("INSERT INTO microarrays_GSE576 (Locus_Identifier, ath1_probe, Annotation, FC_Col_5DAF_vs_lfy_5DAF,Pvalue_Col_5DAF_vs_lfy_5DAF_down,Pvalue_Col_5DAF_vs_lfy_5DAF_up,FC_Col_7DAF_vs_lfy_7DAF,Pvalue_Col_7DAF_vs_lfy_7DAF_down,Pvalue_Col_7DAF_vs_lfy_7DAF_up, FC_Col3DAF_lfy3DAF,Pvalue_Col3DAF_lfy3DAF_down,Pvalue_Col3DAF_lfy3DAFup, FC_Col_0DAF_vs_lfy_0DAF,Pvalue_Col_0DAF_vs_lfy_0DAF_down,Pvalue_Col_0DAF_vs_lfy_0DAF_up) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_micGSE576_db)
con.commit()
cur.executemany("INSERT INTO microarrays_GSE96799 (Locus_Identifier, ath1_probe, Annotation, FC_1_2h, PValue_1_2h, FC_1_4h, PValue_1_4h, FC_1_8h, PValue_1_8h, FC_1_12h, PValue_1_12h, FC_4_2h, PValue_4_2h, FC_4_4h, PValue_4_4h, FC_4_8h, PValue_4_8h, FC_4_12h, PValue_4_12h, FC_2_2h, PValue_2_2h, FC_2_4h, PValue_2_4h, FC_2_8h, PValue_2_8h, FC_2_12h, PValue_2_12h, FC_1_0h, PValue_1_0h, FC_2_0h, PValue_2_0h, FC_4_0h, PValue_4_0h, FC_5_2h, PValue_5_2h, FC_5_4h, PValue_5_4h, FC_5_8h, PValue_5_8h, FC_5_12h, PValue_5_12h, FC_5_0h, PValue_5_0h, FC_Infloresence_Cyclohexamide_treatment_3h_1, Pvalue_Infloresence_Cyclohexamide_treatment_3h_1, FC_Infloresence_Cyclohexamide_treatment_3h_2, Pvalue_Infloresence_Cyclohexamide_treatment_3h_2, FC_Infloresence_Cyclohexamide_treatment_3h_3, Pvalue_Infloresence_Cyclohexamide_treatment_3h_3, FC_Infloresence_Cyclohexamide_treatment_3h_4, Pvalue_Infloresence_Cyclohexamide_treatment_3h_4) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_micGSE96799_db)
con.commit()
cur.executemany("INSERT INTO ChIP_Seq_GSE96806 (Chr, Start, End, Peak_Score, Annotation, Nearest_PromoterID ) VALUES (?, ?, ?, ?, ?, ?);", to_chip_db)
con.commit()


   
######### Display the names of the tables ############   
#res = con.execute("SELECT name FROM sqlite_master WHERE type='table';")
#for name in res:
	#print name[0]

########## Display the names of the columns from a table ############   
#cur.execute("SELECT * FROM microarrays_GSE911")
#col_name_list = [tuple[0] for tuple in cur.description]
#print(col_name_list)

###### UNION allows to remove duplicata
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
##print cur.fetchall()
##UNION 
##SELECT Locus_Identifier FROM microarrays_GSE28062 WHERE Pvalue_LFYGR_WT_down <'0.05' 
##UNION 
##SELECT Nearest_PromoterID FROM ChIP_Seq_GSE96806 WHERE Chr ='1'	
########## Display the names (+ other information) of the columns from a table ##########
##cur.execute("PRAGMA table_info(microarrays_GSE911)")
##print cur.fetchall()

######## Display some columns #############
##cur.execute("""SELECT Locus_Identifier, ath1_probe FROM microarrays_GSE911""")
##for row in cur:
	##print('{0} : {1}'.format(row[0], row[1]))

con.close()
