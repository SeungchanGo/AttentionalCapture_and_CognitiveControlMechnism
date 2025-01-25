## 공통 스크립트
rm(list = ls())
datafiles = list.files(pattern = ".txt")
nSubj = length(datafiles) #DATA 개수
#nSubj = 7
root=getwd()

## Working Directory 지정
setwd("C:/Users/tmdck/Desktop/R/data_Exp/onset")
## making matrix column names
dist_type = c("absent", "present") 
offset_type = c("nooffset", "offset")
wm_type = c("low", "high")
whole_cond =c()

## 행은 피험자 수, 열은 8개인 행렬 생성
rt_all = matrix(NA,nSubj, 8)
acc_all = matrix(NA,nSubj, 8) 
mpacc_all = matrix(NA,nSubj, 8)

## 조건별 열 라벨링링
for (IV_3 in wm_type){
  for (IV_2 in offset_type){
    for (IV_1 in dist_type){
      curCOND = sprintf("%s_%s_%s",IV_1, IV_2, IV_3)
      whole_cond <- c(whole_cond, curCOND)
      
    }
  }
}

## 만들었던 매트릭스에 열 라벨링 집어넣기
colnames(rt_all) <- whole_cond
colnames(acc_all) <- whole_cond
colnames(mpacc_all) <- whole_cond

## 완성된 빈 행렬에 실제 피험자 데이터 집어넣기
for(sbj in 1:nSubj){
  data = read.table(datafiles[sbj], header = T)
  data=data[data$trt > 0.2, ] #rt가 너무 빠른 데이터는 버림

  condition_number = 1 #열(조건)의 순서
  for (wm in 0:1){
    for (offset in 0:1){
      for (dist in 0:1) {
        #sbj 행, condition 열에 있는 데이터에 각 조건에 해당하는 수치의 평균을 삽입
        rt_all[sbj, condition_number] = mean(data[data$wmload == wm & data$block == offset & data$trialtype == dist & data$tacc ==1 & data$mpacc ==1, ]$trt)
        acc_all[sbj, condition_number] = mean(data[data$wmload == wm & data$block == offset & data$trialtype == dist, ]$tacc)
        mpacc_all[sbj, condition_number] = mean(data[data$wmload == wm & data$block == offset & data$trialtype == dist, ]$mpacc)

        condition_number = condition_number + 1
      }
    }
  }
}

## 완성된 매트릭스를 엑셀파일로 저장
write.csv(rt_all, "dataRT.csv")
write.csv(acc_all, "dataACC.csv")
write.csv(mpacc_all, "dataMPACC.csv")

## 필요한 라이브러리 불러오기
library(tidyr)
library(lattice)
library(plyr)
library(Rmisc)
library(ggplot2)
library(effectsize)

# # 분석 용이하게 만들기
rt_data = read.csv("dataRT.csv", header = T) #RT data
rt_data_long <- gather(rt_data, cond, rt, absent_nooffset_low:present_offset_high)
data_long = separate(rt_data_long, col=cond, sep="_", into = c("dist", "offset", "wm"))
colnames(data_long)[1] = "sbj"
write.csv(data_long, "data_long.csv")

acc_data = read.csv("dataACC.csv", header = T) #ACC data
acc_data_long <- gather(acc_data, cond, acc, absent_nooffset_low:present_offset_high)
data_acc_long = separate(acc_data_long, col=cond, sep="_", into = c("dist", "offset", "wm"))
colnames(data_acc_long)[1] = "sbj"
write.csv(data_acc_long, "data_acc_long.csv")

mpacc_data = read.csv("dataMPACC.csv", header = T) #mpACC data
mpacc_data_long <- gather(mpacc_data, cond, acc, absent_nooffset_low:present_offset_high)
data_mpacc_long = separate(mpacc_data_long, col=cond, sep="_", into = c("dist", "offset", "wm"))
colnames(data_mpacc_long)[1] = "sbj"
write.csv(data_mpacc_long, "data_mpacc_long.csv")

