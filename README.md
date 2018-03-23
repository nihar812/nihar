# nihar
> dataset=read.csv("PersonenSchaden.csv",header=T,na.strings="?")
> attach(dataset)
> mean(total)
[1] 38367.22
> var(total)
[1] 8277562110
> sd(total)
[1] 90981.11
> summary(total)
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
     10    6297   13854   38367   35123 4485797 
> C=hist(total,col="Green",breaks=200,xlab="Dollar value of claims",main="Histogram of the dollar value of claims")
> D=hist(finmonth-repmonth,col="Blue",xlab="Settlement delay",main="Histogram of the settlement delay")
> E=hist(legrep,freq=FALSE,breaks=100,col="Pink",xlab="Legal representative",ylab="Percentage of total claims",main="The proportion of cases which are legally represented (and not)")
> f=c(inj1,inj2,inj3,inj4,inj5)
> fsol=hist(f,col="brown",freq=FALSE,xlab="Various code of Injuries",ylab="Percentage of total claims",main="Proportion of various injury code")
> H=hist(log(total),xlab="log Dollar value of the claims",main="Histogram of the log dollar value of claims",col="Yellow")
> I1=plot(op_time,total,xlab="Operational time",ylab="Size of claims",main="Plot of claim size against operation time")
> I2=plot(op_time,log(total),xlab="Operational time",ylab="log of claim size",main="Plot of log claim size against operation time")
> legrepcolour=as.factor(dataset[,7])
> K=plot(op_time,log(total),col=legrepcolour,xlab="Operational time",ylab="log of claim size",main="Plot of log claim size against operation time")
