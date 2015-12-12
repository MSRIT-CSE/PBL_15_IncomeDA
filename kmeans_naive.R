 df<-read.csv("C:/Users/ravi/Downloads/New folder/pums/finalhusa.csv")[,c('FINCP','HINCP','RNTP','VEH','ST','FES','WKEXREL')]
  d<-df[complete.cases(df),]
 (kc <- kmeans(d[1:2], 6)) 
 plot(d[c("FINCP", "HINCP")], col=kc$cluster)
points(kc$centers[,c("FINCP", "HINCP")], col=1:3, pch=8, cex=2)
d$cluster_no<-kc$cluster 
d$cluster_no<-factor(d$cluster_no)
library(class) 
library(e1071)
classifier<-naiveBayes(d[,1:7], d[,8])
table(predict(classifier, d[,-8]), d[,8])

