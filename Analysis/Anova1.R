library(effectsize)

setwd("C:/Users/tmdck/Desktop/R/data_Exp/singleton")
data = read.csv("data_mpacc_long.csv", header = T)
data$sbj <- factor(data$sbj)


##1. three-way
#model1 <- aov(acc ~ (dist*offset*wm) + Error(sbj/(dist*offset*wm)), data)
#eta_squared(model1)



##2. WM -> two-way with trial type x similarity 
data_low = data[data$wm=="low" ,]
data_high = data[data$wm=="high" ,]

model1_low <- aov(acc ~ (dist*offset) + Error(sbj/(dist*offset)), data_low)
eta_squared(model1_low)

model1_high <- aov(acc ~ (dist*offset) + Error(sbj/(dist*offset)), data_high)
eta_squared(model1_high)



##3. low WM & similarity - one-way with trial type
#data_low_low = data_low[data_low$offset=="nooffset" ,]
#data_low_high = data_low[data_low$offset=="offset" ,]

#model1_low_low <- aov(rt ~ dist + Error(sbj/dist), data_low_low)
#eta_squared(model1_low_low)

#model1_low_high <- aov(rt ~ dist + Error(sbj/dist), data_low_high)
#eta_squared(model1_low_high)


## high WM & similarity - one-way with trial type
#data_high_low = data_high[data_high$offset=="nooffset" ,]
#data_high_high = data_high[data_high$offset=="offset" ,]

#model1_high_low <- aov(rt ~ dist + Error(sbj/dist), data_high_low)
#eta_squared(model1_high_low)

#model1_high_high <- aov(rt ~ dist + Error(sbj/dist), data_high_high)
#eta_squared(model1_high_high)
