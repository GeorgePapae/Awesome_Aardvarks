# Awesome_Aardvarks
Group 1 (Awesome_Aardvarks) groupwork.

## Overview
- code: contains the code worked on for our assignment.
- data: contains the data imported that our code uses.
- results: output files from code appear here. Contains a figure and compiled pdf displaying the results of TAutoCorr.R.
- sandbox: bin for code. Empty.
- CONTRIBUTIONS.md - shows the each group members contributions to the project.

## Code Contents

### align_seqs_better.py
**What it does:** Aligns sequences in .fasta format using a sequence alignment algorithm.

**Purpose:** Reads multiple sequences from a .fasta file, compares them, and outputs all possible best alignments by calculating similarity scores and gaps.

**Example usage:**
```bash
cd code
python3 align_seqs_better.py
```

### align_seqs_fasta.py
**What it does:** Aligns any two sequences from separate .fasta files provided as command-line arguments and outputs the best alignment with its score.

**Purpose:** Performs pairwise sequence alignment between two input sequences and writes results (best alignment and score) to a .txt file in the results directory.

**Example usage:**
```bash
cd code
# With specific files
python3 align_seqs_fasta.py ../data/407228326.fasta ../data/407228412.fasta

# Without arguments (uses first two .fasta files in ../data/)
python3 align_seqs_fasta.py
```

### oaks_debugme.py
**What it does:** Filters oak species (genus Quercus) from a CSV file and saves them to a new CSV file, with fuzzy matching to handle minor typos in genus names.

**Purpose:** Extracts oak species records from taxonomic data, including error tolerance for species name variations, and outputs filtered results to a new CSV file.

**Example usage:**
```bash
cd code
python3 oaks_debugme.py
```

### PP_Regress_loc.R
**What it does:** Performs predator-prey mass regression analysis by location, feeding interaction type, and predator life stage, calculating slopes, intercepts, correlation coefficients, and statistical significance.

**Purpose:** Analyzes the relationship between predator and prey mass across different ecological contexts using linear regression, converts mass units to grams for consistency, and outputs regression statistics to a CSV file.

**Example usage:**
```bash
cd code
Rscript PP_Regress_loc.R
# Or in R interactive session
source("PP_Regress_loc.R")
```

### TAutoCorr.R
**What it does:** Tests temporal autocorrelation in temperature data by comparing actual year to year temperature correlation with a null distribution to determine statistical significance.

**Purpose:** Analyzes whether annual mean temperatures in Key West, Florida are significantly correlated between successive years, using permutation testing to assess if observed correlations exceed random chance.

**Example usage:**
```bash
cd code
Rscript TAutoCorr.R
# Or in R interactive session
source("TAutoCorr.R")
```
