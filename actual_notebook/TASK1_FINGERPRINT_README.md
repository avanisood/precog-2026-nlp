# Task1_The_Fingerprint_EDA_COMPLETE.ipynb

## 📋 Overview

This is a **research-grade exploratory data analysis notebook** for stylometric analysis of human vs AI-generated text. The notebook implements all content from cells 1-10 of the original Task1.ipynb, reorganized into clean, well-documented phases.

## 🎯 Objective

Distinguish between:
- **Class 1 (Human)**: Human-written texts from precog.csv
- **Class 2 (AI Generic)**: AI-generated texts from class_2_combined.csv
- **Class 3 (AI Mimic)**: AI-generated texts mimicking specific authors from class_3_combined.csv

## 📊 Analysis Structure (33 Cells Total)

### **Phase 0: Data Loading** (Cells 4-7)
- **Cell 4**: Markdown - Phase 0 introduction
- **Cell 5**: Code - Load CSVs with TTR analysis functions
- **Cell 6**: Markdown - Visualization description
- **Cell 7**: Code - Plot basic TTR comparison

**Purpose**: Load and perform initial Type-Token Ratio analysis on all three datasets.

---

### **Phase 1: Rolling TTR Function** (Cells 8-11)
- **Cell 8**: Markdown - Phase 1 hypothesis and approach
- **Cell 9**: Code - Core rolling TTR functions (`preprocess_text()`, `calculate_rolling_ttr_signal()`)
- **Cell 10**: Markdown - Validation test description
- **Cell 11**: Code - Validation tests on synthetic and real data

**Key Functions**:
```python
def calculate_rolling_ttr_signal(text: str, window_size: int = 50) -> List[float]:
    """Computes rolling TTR with sliding window (stride=1)"""
```

**Expected Outcome**: Function validated on repetitive text (low TTR), diverse text (high TTR), and actual CSV data.

---

### **Phase 2: Signal Analysis - Roughness Metrics** (Cells 12-15)
- **Cell 12**: Markdown - Phase 2 objectives and metrics
- **Cell 13**: Code - `compute_roughness_metrics()` and `apply_roughness_analysis()` functions
- **Cell 14**: Markdown - CSV loading description
- **Cell 15**: Code - Load all CSVs, combine, and apply roughness analysis

**Key Metrics Computed**:
- `mean_ttr`: Average lexical diversity
- `ttr_variance`: **PRIMARY DISCRIMINATOR** - lexical roughness
- `ttr_std`: Standard deviation of TTR signal
- `ttr_range`: Max - Min TTR
- `signal_length`: Number of windows analyzed
- `token_count`: Total tokens in text

**Expected Outcome**: DataFrame with roughness metrics added row-by-row (each text processed independently).

---

### **Phase 3: Visualization** (Cells 16-19)
- **Cell 16**: Markdown - Phase 3 visualization objectives
- **Cell 17**: Code - `plot_signal_comparison()` and `plot_roughness_distribution()` functions
- **Cell 18**: Markdown - Generate visualizations description
- **Cell 19**: Code - Create all visualizations

**Visualizations**:
1. **Signal Comparison**: Line plots showing rolling TTR "jaggedness" (roughness) vs "smoothness"
2. **Roughness Distribution**: Violin plots comparing TTR variance across classes

**Expected Outcome**: Visual evidence of higher roughness in human texts vs AI texts.

---

### **Phase 4: Syntactic Analysis** (Cells 20-31)
- **Cell 20**: Markdown - Phase 4 hypothesis (syntactic variation)
- **Cell 21**: Code - Load spaCy model (`en_core_web_sm`)
- **Cell 22**: Markdown - Helper functions description
- **Cell 23**: Code - `levenshtein_distance()` and `get_pos_sequences()` functions
- **Cell 24**: Markdown - Structural drift description
- **Cell 25**: Code - `calculate_structural_drift()` function
- **Cell 26**: Markdown - POS entropy description
- **Cell 27**: Code - `get_pos_trigrams()` and `calculate_pos_entropy()` functions
- **Cell 28**: Markdown - Apply analysis description
- **Cell 29**: Code - Compute syntactic metrics for all texts
- **Cell 30**: Markdown - Visualization description
- **Cell 31**: Code - Create syntactic visualizations (scatter plots, violin plots)

**Key Metrics Computed**:
- `mean_drift`: Normalized Levenshtein distance between consecutive sentence POS sequences
- `pos_entropy`: Shannon entropy of POS trigram distributions

**Expected Outcome**: Human texts show higher syntactic variation and grammatical diversity.

---

### **Phase 5: Save Results** (Cells 32-33)
- **Cell 32**: Markdown - Save results description
- **Cell 33**: Code - Save complete DataFrame to CSV

**Output File**: `/home/avani/precog/reports/ttr_syntactic_analysis_results.csv`

---

## 🔬 Key Findings Expected

1. **TTR Variance** (Lexical Roughness):
   - Human: Higher variance (~0.0015-0.0020)
   - AI: Lower variance (~0.0008-0.0012)

2. **Structural Drift** (Syntactic Variation):
   - Human: More variation between consecutive sentences
   - AI: More uniform syntactic structures

3. **POS Entropy** (Grammatical Diversity):
   - Human: Higher entropy (more diverse grammar)
   - AI: Lower entropy (more repetitive patterns)

## 📁 Input Files

```
/home/avani/precog/content/
├── precog.csv                           # Class 1 (Human)
├── class_2_pro_vanilla_combined.csv     # Class 2 (AI Generic)
└── class_3_pro_combined.csv             # Class 3 (AI Mimic)
```

## 📈 Output Files

```
/home/avani/precog/reports/
├── ttr_analysis.png                     # Basic TTR comparison
├── ttr_roughness_distribution.png       # Roughness metrics
├── syntactic_analysis.png               # Syntactic metrics
└── ttr_syntactic_analysis_results.csv   # Complete results
```

## 🚀 Usage

Run cells sequentially from top to bottom. Each phase builds on the previous one:

```python
# Phase 0: Load data
# Phase 1: Validate rolling TTR function
# Phase 2: Compute roughness metrics → df_with_roughness
# Phase 3: Visualize roughness patterns
# Phase 4: Add syntactic metrics → df_with_roughness (updated)
# Phase 5: Save final results
```

## 📦 Dependencies

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
import spacy
import re
from typing import List, Tuple
from collections import Counter
from tqdm import tqdm
from scipy.spatial.distance import hamming
```

**spaCy Model Required**:
```bash
python -m spacy download en_core_web_sm
```

## 🔧 Configuration

Window sizes and parameters can be adjusted in the code:
- **Rolling TTR window**: 50 words (default)
- **Basic TTR window**: 10,000 words
- **Step size**: 1 word (rolling), 1000 words (basic)

## ✨ Features

✅ **Research-Grade Structure**: Clear phases with markdown documentation  
✅ **Independent Processing**: Each text analyzed separately (no concatenation)  
✅ **Comprehensive Metrics**: 8 stylometric features computed  
✅ **Professional Visualizations**: Publication-ready plots with seaborn  
✅ **Progress Tracking**: tqdm progress bars for long computations  
✅ **Error Handling**: NaN handling for texts that are too short  
✅ **Complete Documentation**: Every function has docstrings and explanations  

## 📝 Notes

- **Original Source**: Content extracted from Task1.ipynb cells 1-10
- **Processing Strategy**: Row-by-row processing preserves individual text characteristics
- **Validation**: Synthetic tests ensure functions work correctly before applying to real data
- **Performance**: spaCy pipes disabled for faster POS tagging (ner, lemmatizer not needed)

## 🎓 Academic Context

This analysis forms the foundation for:
- Feature engineering (Task 2 Tier A)
- XGBoost classification
- Human vs AI text detection
- Author attribution analysis

## 🔗 Related Files

- **Task1.ipynb**: Original messy notebook (4707 lines, 36 cells)
- **Task1_The_Fingerprint_EDA_COMPLETE_OLD.ipynb**: Previous version (45 cells, archived)
- **Task2_1_Tier_A_The_Statistician.ipynb**: Feature engineering notebook (uses this output)

---

**Status**: ✅ Complete - Ready for execution  
**Last Updated**: 2024  
**Cells**: 33 (11 markdown, 22 code)  
**Lines**: ~1247
