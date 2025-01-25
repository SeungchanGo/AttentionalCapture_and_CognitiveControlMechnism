setwd("C:/Users/tmdck/Desktop/R/data_Exp/onset")
data = read.csv("data_long.csv", header = T)
data$sbj <- factor(data$sbj)

model2 <- aov(rt ~ (dist*offset*wm) + Error(sbj/(dist*offset*wm)), data)
eta_squared(model2)