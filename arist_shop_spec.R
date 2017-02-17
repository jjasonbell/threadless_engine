library(RColorBrewer)
blues = brewer.pal(9, 'Blues')
dark2 = brewer.pal(3, 'Dark2')
colors = c(blues, dark2)
set.seed(44)
N <- 2600
x <- runif(N)
y <- sin(rnorm(N)) + x + 1.05
y2 <- sin(rnorm(N)) - x - 1.05
#y <- runif(N)
symbols = c(0, 1, 2, 3, 4, 5, 6, 8)
sizes = c(1.4, 1.6, 1.8, 2)
#png('test.png', width = 2000, height = 2000)
png('test2.png', width = 4200, height = 4800)
par(bg = NA)
x_range <- c(min(x), max(x))
y_range <- c(min(y), max(y))
span <- abs(y_range[2] - y_range[1])
y_range <- c(y_range[1] - span * .0714, y_range[2] + span * .0714)
plot(x_range, y_range, type = 'n', axes = F, xlab = '', ylab = '')
points(x, y, pch = symbols, cex = sizes * 1.3 * 2.1, lwd = 3 * 2.1, 
     bg = 'black', col = colors)
#points(x, y2, pch = symbols, cex = sizes*1.3, lwd = 3,
#       bg = 'black', col = colors)
dev.off()
