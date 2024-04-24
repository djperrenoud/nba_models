data <- read.csv("21_22_data.csv")
library(ggplot2)
library(ggrepel)
library(plotly)

# Create scatterplot with customized aesthetics
scatter_plot <- ggplot(data, aes(x = FG., y = PTS)) +
  geom_point(aes(size = PTS), fill = "black", color = "black", alpha = 0.6) +  # Filled black points with black outline
  scale_size_continuous(range = c(0.5, 3)) +  # Adjusted range of circle sizes based on PTS
  labs(title = "FG% vs PTS for NBA Players (2021-2022 Season)",
       x = "Field Goal Percentage",
       y = "Points Per Game") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
  xlab("Field Goal Percentage") +  # Adding x-axis label
  ylab("Points Per Game") +        # Adding y-axis label +
  annotate("text", x = 0.9, y = 0, label = "High FG%", color = "red") +
  annotate("text", x = 0, y = 30, label = "High PTS", color = "red", angle = 90)

# Setting the y-axis limit to 35
scatter_plot <- scatter_plot + scale_y_continuous(limits = c(0, 35))

# Print scatterplot
print(scatter_plot)
