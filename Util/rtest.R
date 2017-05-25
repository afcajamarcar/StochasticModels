library(bnlearn)
bn_df <- read.csv("learningBayesian.csv")
res <- hc(bn_df)
plot(res)
fittedbn <- bn.fit(res, data = bn_df)

