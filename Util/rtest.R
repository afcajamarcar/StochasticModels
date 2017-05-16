bn_df <- data.frame(coronary)
res <- hc(bn_df)

res$arcs <- res$arcs[-which((res$arcs[,'from'] == "M..Work" & res$arcs[,'to'] == "Family")),]
plot(res)

fittedbn <- bn.fit(res, data = bn_df)



