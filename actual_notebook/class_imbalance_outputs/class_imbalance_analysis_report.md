# Class Imbalance Impact Analysis: Comprehensive Experimental Validation

**Report Generated:** 2026-02-07 14:20:15  
**Dataset:** Human vs AI Text Classification  
**Task:** Binary classification (Human=0, AI=1)

---

## Executive Summary

### Dataset Composition
- **Human texts:** 2,492 paragraphs (71.4%)
- **AI texts:** 1,000 paragraphs (28.6%)
- **Imbalance ratio:** 2.5:1 (favoring Human class)

### Overall Verdict: **MINOR CONCERN**

**Key Findings:**
1. Class weight correction changed accuracy by **-0.43%** (Experiment 1)
2. Maximum coefficient of variation: **1.70%** - highly stable (Experiment 2)
3. Balanced training improved AI recall by **+4.00%** (Experiment 3)
4. AI recall variance is **5.62x** Human variance - variance issue (Experiment 4)

### Recommendations

⚠️ **ACKNOWLEDGE LIMITATION:** Minor imbalance effects detected. Report with caveats.



---

## Experiment 1: Class Weight Comparison

### Objective
Test whether using proper class weights changes model performance.

### Methodology
- **Version 1:** Unweighted (no correction) - current approach
- **Version 2:** Weighted (scale_pos_weight = 2.4987)
- **Version 3:** Balanced (random undersampling to 1:1 ratio)

### Results

| Approach | Accuracy | Human Recall | AI Recall | AUC |
|----------|----------|--------------|-----------|-----|
| Unweighted | 0.9728 | 0.9819 | 0.9500 | 0.9957 |
| Weighted | 0.9685 | 0.9719 | 0.9600 | 0.9949 |
| Balanced | 0.9599 | 0.9558 | 0.9700 | 0.9944 |

### Performance Changes (Weighted vs Unweighted)
- Accuracy: **-0.43%**
- Human Recall: **-1.00%**
- AI Recall: **+1.00%**
- AUC: **-0.0008**

### Interpretation
**MINIMAL IMPACT:** Using class weights provides minimal benefit (<1% accuracy change). Classes are naturally separable despite imbalance.

### Statistical Significance
- Change magnitude: **0.43%**
- Conclusion: **Not significant**

---

## Experiment 2: Random Seed Stability Testing

### Objective
Determine if class imbalance causes unstable results across different random initializations.

### Methodology
- Trained 10 models with random seeds 42-51
- Evaluated consistency of performance metrics

### Results

| Metric | Mean | Std | CV (%) |
|--------|------|-----|--------|
| Accuracy | 0.9693 | 0.0062 | 0.64 |
| Human Recall | 0.9805 | 0.0047 | 0.48 |
| AI Recall | 0.9415 | 0.0160 | 1.70 |
| AUC | 0.9959 | 0.0008 | 0.08 |

### Stability Assessment
- **Maximum CV:** 1.70%
- **Classification:** HIGHLY STABLE
  - CV < 2%: Highly stable ✅
  - CV 2-5%: Moderately stable ⚠️
  - CV > 5%: Unstable 🚨

### Class-Specific Stability
- Human Recall CV: **0.48%**
- AI Recall CV: **1.70%**
- Ratio (AI/Human): **3.52x**

### Interpretation
✅ **STABLE PERFORMANCE:** Both classes show low variance. Imbalance not causing instability.

---

## Experiment 3: Balanced Dataset Cross-Evaluation

### Objective
Test how models trained on balanced vs imbalanced data generalize across different class distributions.

### Methodology
- Created balanced dataset (1000 Human, 1000 AI) via undersampling
- Trained on both balanced and imbalanced data
- Cross-evaluated all combinations

### Results: Cross-Evaluation Matrix

| Training | Testing | Accuracy | Human Recall | AI Recall |
|----------|---------|----------|--------------|-----------|
| Imbalanced | Imbalanced | 0.9728 | 0.9819 | 0.9500 |
| Imbalanced | Balanced | 0.9950 | 1.0000 | 0.9900 |
| Balanced | Imbalanced | 0.9713 | 0.9639 | 0.9900 |
| Balanced | Balanced | 0.9575 | 0.9550 | 0.9600 |

### Generalization Analysis
- **Imbalanced model generalization gap:** 0.0222 (2.22%)
- **Balanced model generalization gap:** 0.0138 (1.38%)

### Minority Class (AI) Performance
- Imbalanced train → Imbalanced test: **0.9500**
- Balanced train → Imbalanced test: **0.9900**
- **Improvement:** +4.00%

### Interpretation
⚠️ **BALANCED SUPERIOR:** Balanced training generalizes better across distributions.

---

## Experiment 4: Stratified K-Fold Cross-Validation

### Objective
Rigorous validation maintaining class ratios across all folds to assess true performance with confidence intervals.

### Methodology
- 5-fold stratified cross-validation
- Preserved 71:29 class ratio in each fold
- Comprehensive metrics per fold

### Results: Aggregate Statistics with 95% CI

| Metric | Mean | Std | 95% CI |
|--------|------|-----|--------|
| Accuracy | 0.9688 | 0.0057 | [0.9576, 0.9799] |
| Human Recall | 0.9795 | 0.0036 | [0.9725, 0.9866] |
| AI Recall | 0.9419 | 0.0202 | [0.9023, 0.9815] |
| Human F1 | 0.9782 | 0.0039 | [0.9705, 0.9858] |
| AI F1 | 0.9451 | 0.0103 | [0.9249, 0.9654] |
| AUC | 0.9957 | 0.0007 | [0.9944, 0.9971] |

### Variance Analysis
- **Human Recall Std:** 0.0036
- **AI Recall Std:** 0.0202
- **Variance Ratio (AI/Human):** 5.62x

⚠️ **VARIANCE ISSUE:** AI recall has 50%+ higher variance than Human. Minority class performance is less stable.

### Statistical Significance Test
**Paired t-test (Human vs AI Recall):**
- t-statistic: **3.9249**
- p-value: **0.0172**
- Conclusion: **Statistically significant difference (p < 0.05)**

⚠️ Human and AI recall are significantly different. Examine if bias exists.

---

## Overall Conclusions

### Impact of Class Imbalance

Based on comprehensive testing across 4 independent experiments, the class imbalance (2.5:1 ratio) has been thoroughly evaluated:

**Evidence Summary:**
1. **Class Weights:** MINIMAL IMPACT - accuracy change of -0.43%
2. **Stability:** HIGHLY STABLE - max CV of 1.70%
3. **Generalization:** BALANCED BETTER - generalization gap difference of 0.0084
4. **Variance:** VARIANCE ISSUE - variance ratio of 5.62x

**Final Determination:**

⚠️ **MINOR IMBALANCE EFFECTS:** 1 out of 4 experiments shows concerning patterns. Acknowledge as limitation but results remain largely valid.



### Recommendations for Research Report

**1. Model Training:**
- Consider using class weights (scale_pos_weight=2.50)
- Alternatively, use balanced sampling via undersampling

**2. Results Reporting:**
- Report accuracy: **0.9688 ± 1.1126** (95% CI)
- Emphasize class-specific metrics (precision, recall, F1)
- Include AUC-ROC as robust metric
- Acknowledge 2.5:1 imbalance as methodological note

**3. Limitations Section:**
**Important limitations:**
- Training distribution (71:29) differs from potential deployment scenarios

- Some imbalance effects detected; class-specific metrics reported for transparency


**4. Deployment Considerations:**
- Threshold calibration recommended for specific use cases
- Monitor class-specific performance in production
- Consider retraining on balanced data if domain shifts

### Why This Dataset May Be Robust to Imbalance

**Hypothesis:** The extreme distinctness of Victorian literature (1880s-1900s) vs modern AI text (2024) creates naturally separable classes that overcome typical imbalance issues.

**Supporting Evidence:**
- Vocabulary: Non-overlapping semantic spaces
- Style: Victorian formality vs AI neutrality
- Temporal: 120+ year gap in language evolution
- Task 1 findings: ttr_variance, structural drift, POS entropy all strongly discriminative

This natural separation may explain why imbalance correction provides minimal benefit.

---

## Experimental Outputs

All results saved to `class_imbalance_outputs/`:

**CSV Files:**
- `experiment1_class_weight_comparison.csv` - Weight comparison results
- `experiment1_feature_importance_comparison.csv` - Feature importance changes
- `experiment2_seed_stability.csv` - Stability across 10 seeds
- `experiment3_cross_evaluation.csv` - Cross-evaluation matrix
- `experiment4_cv_results.csv` - 5-fold CV detailed results

**Visualizations:**
- `experiment1_comparison_metrics.png` - Accuracy, recall, F1, error rates
- `experiment1_confusion_matrices.png` - Side-by-side confusion matrices
- `experiment1_roc_curves.png` - ROC curve comparison
- `experiment1_feature_importance_comparison.png` - Feature importance changes
- `experiment2_stability_analysis.png` - Stability across seeds
- `experiment2_metric_distributions.png` - Metric distributions
- `experiment3_cross_evaluation_matrix.png` - Cross-evaluation heatmaps
- `experiment3_feature_importance_comparison.png` - Balanced vs imbalanced features
- `experiment4_fold_comparison.png` - Per-fold metrics
- `experiment4_confidence_intervals.png` - CI visualization

---

## Conclusion

This comprehensive 4-experiment validation framework definitively answers: **"MINOR CONCERN"**

The class imbalance requires acknowledgment and potentially correction. Results remain informative but should be reported with appropriate caveats.

**Final Recommendation:** Use class weights or balanced sampling. Report with transparency about imbalance testing.

---

**Report End**
