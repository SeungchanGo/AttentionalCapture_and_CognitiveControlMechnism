library(effectsize)

setwd("C:/Users/tmdck/Desktop/R/data_Exp/baseline")
data = read.csv("data_long.csv", header = T)
data$sbj <- factor(data$sbj)

model <- aov(rt ~ (dist*offset) + Error(sbj/(dist*offset)), data)
eta_squared(model)
summary(model)


#model2 <- aov(rt ~ (dist*offset*wm) + Error(sbj/(dist*offset*wm)), data)
#eta_squared(model2)

# anova_test 함수 사용
#model2_low <- anova_test(data = data_low, dv = rt, wid = sbj, within = c(dist, offset))
#model2_high <- anova_test(data = data_high, dv = rt, wid = sbj, within = c(dist, offset))

# 소수점 세째 자리까지 반올림된 partial eta-squared 출력
#round(model2_low$ANOVA$partial_eta_squared, 3)
#round(model2_high$ANOVA$partial_eta_squared, 3)