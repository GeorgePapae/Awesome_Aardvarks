##PP_Regress_loc.R
##Author: Ekadh Ranganathan & George Papaeracleous
##Date: 25th November 2025

library(tidyverse)
# Loading csv
ecol_archives <- read.csv("../data/EcolArchives-E089-51-D1.csv")

#Conversion
ecol_archives$Prey.mass[ecol_archives$Prey.mass.unit == "mg"] <- ecol_archives$Prey.mass[ecol_archives$Prey.mass.unit == "mg"] / 1000 # nolint: line_length_linter.
ecol_archives$Prey.mass.unit[ecol_archives$Prey.mass.unit == "mg"] <- "g"

regs <- ecol_archives %>%
  group_by(Location, Type.of.feeding.interaction, Predator.lifestage) %>%
  summarise({
    model <- lm(log(Predator.mass) ~ log(Prey.mass), data = pick(everything()))
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

write.csv(regs, "../results/PP_Regress_Results_loc.csv", row.names = FALSE)

