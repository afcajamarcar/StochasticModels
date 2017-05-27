library(bnlearn)
setwd("/home/japrietov/Documents/StochasticModels/Util/")
bn_df <- read.csv("learningBayesian.csv")
bn_df$Genuine[bn_df$Genuine==1] <- 1.0
bn_df$Genuine[bn_df$Genuine==0] <- 0.0
res <- hc(bn_df)
plot(res)
fittedbn <- bn.fit(res, data = bn_df)

