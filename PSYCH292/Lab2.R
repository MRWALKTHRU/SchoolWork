IQ = c(141, 97, 107, 127, 108, 87, 124, 110, 114, 92, 115
       , 118, 101, 112, 102, 91, 146, 129, 114, 102, 
       96, 108, 109, 139, 134, 92, 106, 83, 109, 104, 
       118, 135, 127, 102, 101, 98, 97, 116, 113, 131
       , 101, 108, 113, 106, 86, 107, 129, 105, 89, 123)

IQ[order(IQ)]
Participants <- data.frame(IQ)
scale_x_continuous(breaks=seq(80,150, by=10))

breaks <- seq(80,150, by=10)
hist(IQ, breaks=breaks)


ggplot(Participants, aes(x=IQ)) + geom_histogram(bindwidth=10,colour="black",
    "fill"="red",) + labs(x="IQ Scores", y="Frequency", 
  title="Frequency of IQ Scores") + theme_bw() +
  theme(panel.grid = element_blank()) + 


class_intervals <- c('140-149', '130-139', '120-129', '110-119', '100-109',
                     '90-99', '80-89')
freq <- c(2, 4, 6, 10, 17, 7, 4)
midpoints <-c(145, 135, 125, 115, 105, 95, 85)

plot(midpoints, freq, type ="o", col="gray",
     xlab="IQ Scores", ylab="Frequency", main="IQ Grouped Scores Polygon",
     lwd = 2, pch = 16, xaxt="n")

axis(1, at=midpoints, labels=class_intervals)


