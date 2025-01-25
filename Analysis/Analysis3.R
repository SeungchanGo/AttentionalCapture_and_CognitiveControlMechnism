rm(list = ls())
datafiles = list.files(pattern = ".txt")
nSubj = length(datafiles)
root=getwd()



# making matrix colum names
dist_type = c("absent", "present")
offset_type = c("nooffset", "offset")
whole_cond =c()

rt_all = matrix(NA,nSubj, 4)
acc_all = matrix(NA,nSubj, 4)
mpacc_all = matrix(NA,nSubj, 4)

for (IV_2 in offset_type){
  for (IV_1 in dist_type){
      curCOND = sprintf("%s_%s",IV_1, IV_2)
      whole_cond <- c(whole_cond, curCOND)
  }
}

colnames(rt_all) <- whole_cond
colnames(acc_all) <- whole_cond


for(sbj in 1:nSubj){
  data = read.table(datafiles[sbj], header = T)
  data=data[data$trt > 0.2, ]
 
  condition_number = 1
  
  for (offset in 0:1){
    for (dist in 0:1) {
          
        rt_all[sbj, condition_number] = mean(data[data$block == offset & data$trialtype == dist & data$tacc ==1, ]$trt)
        acc_all[sbj, condition_number] = mean(data[data$block == offset & data$trialtype == dist, ]$tacc)
          
          condition_number = condition_number + 1
          
    }
  }
}




write.csv(rt_all, "dataRT.csv")
write.csv(acc_all, "dataACC.csv")


library(tidyr)
library(lattice)
library(plyr)
library(Rmisc)
#library(ggplot2)


rt_data = read.csv("dataRT.csv", header = T)
rt_data_long <- gather(rt_data, cond, rt, absent_nooffset:present_offset)
data_long = separate(rt_data_long, col=cond, sep="_", into = c("dist", "offset"))
colnames(data_long)[1] = "sbj"
write.csv(data_long, "data_long.csv")

acc_data = read.csv("dataACC.csv", header = T)
acc_data_long <- gather(acc_data, cond, acc, absent_nooffset:present_offset)
data_acc_long = separate(acc_data_long, col=cond, sep="_", into = c("dist", "offset"))
colnames(data_acc_long)[1] = "sbj"
write.csv(data_acc_long, "data_acc_long.csv")
