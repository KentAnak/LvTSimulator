library(tidyverse)
library(sqldf)

getwd()

dat <- read.csv("data.csv")
# Check talent distribution
ggplot(data = dat, aes(x = talent)) +
geom_histogram(binwidth = 0.01, fill = "white", colour = "black")

# Check wealth distribution
# log-lin
ggplot(data = dat, aes(x = wealth)) +
geom_histogram(binwidth = 50, fill = "white", colour = "black") +
scale_y_log10()

# Check Pareto's "80-20" rule
sum(sqldf("SELECT wealth FROM dat 
    ORDER BY wealth DESC
    LIMIT (SELECT 0.20 * COUNT(*) FROM dat)")) /
sum(sqldf("SELECT SUM(wealth) FROM dat"))

sum(sqldf("SELECT wealth FROM dat
       ORDER BY wealth
       LIMIT (SELECT 0.80 * COUNT(*) FROM dat)")) /
sum(sqldf("SELECT SUM(wealth) FROM dat"))

sqldf("SELECT * FROM dat 
    ORDER BY wealth DESC
    LIMIT (SELECT 0.004 * COUNT(*) FROM dat)")

# Check wealth distribution with talent
ggplot(data = dat, aes(x = wealth, y = talent)) +
geom_point() +
scale_x_log10()

ggplot(data = dat, aes(x = talent, y = wealth)) +
geom_point()

# Check wealth distribution with luck
ggplot(data = dat, aes(x = wealth, y = lucky_cnt)) +
geom_point() +
scale_x_log10()

# Check wealth distribution with unluck
ggplot(data = dat, aes(x = wealth, y = unlucky_cnt)) +
geom_point() +
scale_x_log10()
