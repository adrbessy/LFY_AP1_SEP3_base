## try http:// if https:// URLs are not supported
source("https://bioconductor.org/biocLite.R")
## browseVignettes("package_name") for package information
biocLite("affy") ## contains methods for Affymetrix arrays
biocLite("gcrma") ## gcrma adjusts for background intensities in Affymetrix array data which include optical noise and non-specific binding.
biocLite("RankProd") ## contains the Rank Product method that is a non-parametric method for identifying differentially expressed (up- or down- regulated) genes based on the estimated percentage of false predictions (pfp).
library(affy) 
library(gcrma)
library(RankProd) 

data0<-read.table('GSE576_33_34_41_42.csv', header = TRUE, sep = "\t", quote = '"')
data <- data0[,-1]
rownames(data) <- data0[,1]
data.cl<-c(0,0,1,1)

data.gnames<-rownames(data)
# RP.out <- RankProducts(data,data.cl,gene.names=data.gnames, logged=TRUE,na.rm=FALSE,plot=FALSE, rand=123)
RP.out<-RP(data,data.cl,gene.names=data.gnames,rand=123) ## we chose to set rand to 123 to make this pipeline reproducible.
result_0.1<-topGene(RP.out,num.gene=22810,gene.names=data.gnames,logged=FALSE) ## create a table with FC, pfp and P.value for all the genes (22810 genes here)
data1<-result_0.1$Table1
data1<-data1[,-2] ## suppress the RP/Rsum column
data1=cbind(rownames(data1),data1)

colnames(data1)[c(1,4,5)]=c('ath1_probe','pfp_GSE576_33_34_41_42_down','P.value_GSE576_33_34_41_42_down')
data2<-result_0.1$Table2
data2<-data2[,c(1,4,5)]
data2=cbind(rownames(data2),data2)
colnames(data2)[c(1,3,4)]=c('ath1_probe','pfp_33_34_41_42_up','P.value_33_34_41_42_up')
tables<-merge(data1, data2, by=c('ath1_probe','gene.index'),all=T)
colnames(tables)[c(2,3)]=c('probe_target_number','FC_33_34_41_42_GSE576')
write.table(tables,file='GSE576_33_34_41_42_2.csv',sep='\t',row.names=F)

multmerge = function(){
filenames=list.files(full.names=TRUE)
datalist = lapply(filenames, function(x){read.csv(file=x,, header = TRUE, sep = "\t", quote = '"')})
Reduce(function(x,y) {merge(x,y, by=c('ath1_probe','probe_target_number'),all=T)}, datalist)
}
all<-multmerge()
write.table(all,file="all.csv",sep="\t",row.names=F)