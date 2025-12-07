# TAutoCorr.R - Temperature Autocorrelation Analysis
# Tests if temperatures of one year are significantly correlated with the next year
# Author: Ziyang Wang (zw2425@ic.ac.uk), Shuqing Ren (sr1822@ic.ac.uk)
rm(list=ls())

# Load annual mean temperature data for Key West, Florida after file existence and extension check
filepath <- "../data/KeyWestAnnualMeanTemperature.RData"

if (!file.exists(filepath)) {
  stop("File not found: ", filepath, 
       "\nPlease check the file path and ensure the file exists.")
} # Check file existence

if (!grepl("\\.RData$", filepath, ignore.case = TRUE)) {
  warning("File extension is not .RData. Are you sure this is an RData file?")
} # Check file extension
load("../data/KeyWestAnnualMeanTemperature.RData")

# Data preparation
temps <- ats$Temp
n_years <- nrow(ats)
  
# Calculate the actual correlation between successive years
year_i <- temps[1:(n_years-1)]    # Years 1 to n-1
year_j <- temps[2:n_years]        # Years 2 to n
  
actual_cor <- cor(year_i, year_j, method = "pearson")
cat("Actual correlation between successive years:", round(actual_cor, 4), "\n")
  
# Permutation Analysis
permuted_cors <- matrix()
permutations <- 10000
  
set.seed(1)
for (i in 1:permutations) {
  permuted_temps <- sample(temps, replace = FALSE) # Randomly shuffle the temperature sequence
    
  # Calculate correlation for permuted time series sequence
  perm_year_i <- permuted_temps[1:(n_years-1)]
  perm_year_j <- permuted_temps[2:n_years]
  permuted_cors[i] <- cor(perm_year_i, perm_year_j, method = "pearson")
}

# Calculate p-value with an one-tailed test: fraction of permuted correlations > actual correlation
p_value <- sum(permuted_cors > actual_cor) / permutations

cat("Permutation p-value:", round(p_value, 4), "\n")
cat("Based on", permutations, "permutations\n")

# There is statistically significant evidence that temperatures show autocorrelation between successive 
# years over the past century in Key West, Florida. Temperatures in one year tend to predict temperatures
# in the next year better than random chance permuted for 10,000 times

# visualisation & save image 
pdf("../results/Fig1.pdf", width = 6, height = 4)  # open a pdf device (size in inches)
plot(year_i, year_j, xlab = "Previous Year Temp", ylab = "Following Year Temp")
dev.off()
