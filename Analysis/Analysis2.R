library(tidyr)
library(lattice)
library(plyr)
library(Rmisc)
library(ggplot2)
library(effectsize)

## 그래프 그리기
plotdata=read.csv("data_long.csv") 
plotdata$sbj = factor(plotdata$sbj) # 변인으로 피험자 지정
#plotdata = plotdata[plotdata$sbj != "5",]

## 그래프에서 쓰일 컬러 지정
palette1<- c('absent'='#d9e254','present'='#805ba5')

## nooffset low
plotdata1 = plotdata[plotdata$offset=="nooffset" & plotdata$wm=="low" ,]

plotdataerror1=summarySEwithin(plotdata1, idvar="sbj", measurevar="rt", withinvars =c("dist"))

aa=ggplot(plotdataerror1, aes(x=factor(dist, levels=c('absent', 'present')),fill=dist, y=rt, )) + 
  geom_bar(position=position_dodge(), stat="identity", width=0.8) +
  geom_errorbar(aes(ymin=rt-se, ymax=rt+se, width=.3), position=position_dodge(.9))+
  theme_classic(base_size=10)+coord_cartesian(ylim = c(0.5, 1.0)) + 
  xlab("Dist") + ylab("Reaction time (sec)") + scale_fill_manual(values=palette1) + theme(legend.position=c(0.3, 0.9), legend.key.height=unit(0.5, 'cm'))

## offset low
plotdata2 = plotdata[plotdata$offset=="offset" & plotdata$wm=="low" ,]

plotdataerror2=summarySEwithin(plotdata2, idvar="sbj", measurevar="rt", withinvars =c("dist"))

bb=ggplot(plotdataerror2, aes(x=factor(dist, levels=c('absent', 'present')), fill=dist, y=rt, )) + 
  geom_bar(position=position_dodge(), stat="identity", width=0.8) +
  geom_errorbar(aes(ymin=rt-se, ymax=rt+se, width=.3), position=position_dodge(.9))+
  theme_classic(base_size=10)+coord_cartesian(ylim = c(0.5, 1.7)) + 
  xlab("Dist") + ylab("Reaction time (sec)") + scale_fill_manual(values=palette1) + theme(legend.position=c(0.4, 20))

## nooffset high
plotdata3 = plotdata[plotdata$offset=="nooffset" & plotdata$wm=="high" ,]

plotdataerror3=summarySEwithin(plotdata3, idvar="sbj", measurevar="rt", withinvars =c("dist"))

cc=ggplot(plotdataerror3, aes(x=factor(dist, levels=c('absent', 'present')),fill=dist, y=rt, )) + 
  geom_bar(position=position_dodge(), stat="identity", width=0.8) +
  geom_errorbar(aes(ymin=rt-se, ymax=rt+se, width=.3), position=position_dodge(.9))+
  theme_classic(base_size=10)+coord_cartesian(ylim = c(0.5, 1.0)) + 
  xlab("Dist") + ylab("Reaction time (sec)") + scale_fill_manual(values=palette1) + theme(legend.position=c(1, 20))


## offset high
plotdata4 = plotdata[plotdata$offset=="offset" & plotdata$wm=="high" ,]

plotdataerror4=summarySEwithin(plotdata4, idvar="sbj", measurevar="rt", withinvars =c("dist"))

dd=ggplot(plotdataerror4, aes(x=factor(dist, levels=c('absent', 'present')),fill=dist, y=rt, )) + 
  geom_bar(position=position_dodge(), stat="identity", width=0.8) +
  geom_errorbar(aes(ymin=rt-se, ymax=rt+se, width=.3), position=position_dodge(.9))+
  theme_classic(base_size=10)+coord_cartesian(ylim = c(0.5, 1.7)) + 
  xlab("Dist") + ylab("Reaction time (sec)") + scale_fill_manual(values=palette1) + theme(legend.position=c(1, 20))

multiplot(aa,cc,bb,dd, cols=2)
