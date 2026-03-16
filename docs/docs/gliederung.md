
# Titel
### Option 1 
Performance vs. Accessibility: Benchmarking Tabular Foundation Models against Hyperparameter-Optimized Machine Learning in Clinical Risk Prediction

### Option 2 
Evaluating TabPFN's Out-of-the-Box Utility vs. Optimized Gradient Boosting for Medical Screening

### Option 3 
Zero-Shot vs. Optimized: Benchmarking Tabular Foundation Models as Low-Barrier Alternatives to Hyperparameter-Tuned Machine Learning in Clinical Risk Prediction

### Option 4 fav
Performance vs. Accessibility: Benchmarking Tabular Foundation Models against Hyperparameter-Optimized Machine Learning — Evidence from Clinical Risk Prediction



# Outline

### 1. Introduction *(2–3 pages)*  
1.1 Motivation: Laverage AI in Clinical Screening Methods  
1.2 Research Question: Can TabPFN or TabICL predict a heart failure better, then a classic ML on demographic clinical data?  
1.3 Thesis Structure  

### 2. Theoretical Foundation *(4–5 pages)*
2.1 Tabular Data in Healthcare: Characteristics and Challenges  
2.2 Classical Methods: Random Forest and Gradient Boosting  
2.3 The Role of HPO: Why Tuning Matters for Classical Models  
2.4 Tabular Foundation Models: TabPFN and TabICL  
2.5 The Accessibility Argument: Zero-Shot Learning as a Paradigm Shift (no training, only pre-training)

### 3. Methodology & Experimental Setup *(4–5 pages)*
3.1 Dataset: MIMIC-IV Heart Failure Cohort and Target Definition  (predict 1/0 for heart failure or keep it?)
3.2 Data Pipeline: Preprocessing, Balancing, and Feature Engineering  
3.3 Model Configurations: Zero-Shot Baselines vs. HPO-Tuned Models  
3.4 Evaluation Framework: Robustness Loop, Metrics, and Fair Comparison  

### 4. Results *(5–6 pages)*
4.1 Benchmark Performance: F1 Macro and ROC-AUC Across All Models  
4.2 The HPO Effect: What Full Training Actually Adds  
4.3 The Speed-Scale Trade-off: Where Hollmann's Claims Meet Real Data  
4.4 Feature Analysis: Confounders, True Drivers, and Model Disagreement  (notwendig?)

### 5. Discussion *(4 pages)*
5.1 TabPFN as a Zero-Shot Approach: What It Can and Cannot Do  
5.2 The Real Barrier for AI implementation: Not Performance, But Expertise and Setup Cost for AI
5.3 Generalizability: From Medicine to Finance and Marketing  
5.4 Limitations: Dataset Size, Feature Space, and HPO Approximation  

### 6. Conclusion *(2–3 pages)*
6.1 Summary of Findings  
6.2 Practical Recommendations: When to Use Foundation Models  
6.3 Future Work with clinical data scope: Add more features, like habits and other factors a patient would know w/o tests, to improve the F1-Score and use the full potential of TabPFN/TabICL
