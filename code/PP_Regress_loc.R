##PP_Regress.R
##Author: Ekadh Ranganathan
##Date: 31st October 2025

library(tidyverse)
# Loading csv
ecol_archives <- read.csv("../data/EcolArchives-E089-51-D1.csv")

#Conversion
ecol_archives$Prey.mass[ecol_archives$Prey.mass.unit == "mg"] <- ecol_archives$Prey.mass[ecol_archives$Prey.mass.unit == "mg"] / 1000
ecol_archives$Prey.mass.unit[ecol_archives$Prey.mass.unit == "mg"] <- "g"

# Setting basic plot aesthetics
p <- ggplot(ecol_archives,
            aes(Prey.mass, Predator.mass,
                color = Predator.lifestage))
# Setting points and lm lines (plot raw masses but display axes on a log scale so labels are positive)
p <- p + geom_point(shape = I(3)) + geom_smooth(method = "lm", fullrange = TRUE, se = TRUE) +
  scale_x_log10() + scale_y_log10()
# Setting up facet wrap, labs and theme
p <- p + facet_wrap(Type.of.feeding.interaction ~., ncol = 1, strip.position = "right") +
  labs(x = "Prey mass in grams", y = "Predator mass in grams") +
  theme(
    legend.position = "bottom",
    legend.direction = "horizontal",
    legend.box = "horizontal",
    strip.placement = "outside",
    plot.margin = margin(10, 40, 10, 10),
    legend.text = element_text(size = 8),
    legend.title = element_text(size = 9),
    strip.text = element_text(size = 8)
  ) +
  guides(color = guide_legend(nrow = 1))
print(p)

ggsave(filename = "../results/Visualised_regression.pdf", plot = p)

regs <- ecol_archives %>%
  group_by(Type.of.feeding.interaction, Predator.lifestage) %>%
  summarise({
    model <- lm(log(Predator.mass) ~ log(Prey.mass), data = cur_data())
    fpstats <- summary(model)
    
    fstat <- fpstats$fstatistic
    
    if (!is.null(fstat) && all(is.finite(fstat))) {
      p_val <- pf(fstat[1], fstat[2], fstat[3], lower.tail = FALSE)
    } else {
      p_val <- NA_real_
    }
    
    tibble(
      slope = coef(model)[2],
      intercept = coef(model)[1],
      R = sqrt(fpstats$r.squared),
      F_stat = if (!is.null(fstat)) fstat[1] else NA_real_,
      p_value = p_val
    )
  }, .groups = "drop")

write.csv(regs, "../results/PP_Regress_Results.csv", row.names = FALSE)

