rm(list=ls())

# Load annual mean temperature data for Key West, FL
load("../data/KeyWestAnnualMeanTemperature.RData")

# Inspect the data
ls()
class(ats)
head(ats)
plot(ats)

# Observed correlation between Year and Temp
obs_corr <- cor(ats$Year, ats$Temp)

# Permutation test for cor between Year and reshuffled Temp (n=10k)
n_permutations <- 10000
perm_corrs <- matrix()
for (i in 1:n_permutations) {
  perm_temps <- sample(ats$Temp, replace = FALSE) 
  perm_corrs[i] <- cor(ats$Year, perm_temps)
}

# Two sided p-value as the fraction of permutation larger or equal to observed correlation coefficient 
p_value <- mean(abs(perm_corrs) >= abs(obs_corr))

