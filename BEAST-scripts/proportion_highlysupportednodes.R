library(ggplot2)
library(dplyr)
library(lubridate)

# visualiuze prop of internal nodes with high posterior support for state 
setwd("~/Documents/HPAI/HPAI_2344b/DTA-BEAST/RF/results/RF-wild2/")
df_high_prob <- read.csv("df_high_prob-100.csv")


df_high_prob$date <- format(date_decimal(df_high_prob$date), "%Y-%m-%d")
df_high_prob$date <- as.Date(df_high_prob$date)

df_high_prob$yearweek <- format(df_high_prob$date, "%Y-%U")



# Calculate the proportion of each discrete trait for each year-week
proportion_data <- df_high_prob %>%
  group_by(yearweek, host) %>%
  summarise(count = n()) %>%
  group_by(yearweek) %>%
  mutate(proportion = count/sum(count))



host_colors <- c("Domestic" = "#5CA7A4",
                 "Wild" = "#2664A5",
                 "Backyard_bird" = "#D1BA56")   

# Plot the proportion using ggplot2
ggplot(proportion_data, aes(x = yearweek, y = proportion, fill = host)) +
  geom_bar(stat = "identity", position = "stack") +
  scale_fill_manual(values = host_colors) +
  labs(title = "Proportion of highly supported nodes (>0.9 pp) by Year-Week - 100% Wild",
       x = "Year-Week",
       y = "Proportion") +
  theme_minimal() +
  theme(legend.position = "bottom", 
        axis.text.x = element_text(size = 14),
        axis.text.y = element_text(size = 14),
        plot.title = element_text(size = 14)) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

ggsave("prop_highsupp_100.pdf", plot = last_plot(), width = 8.5, height = 11, units = "in", dpi = 300)



