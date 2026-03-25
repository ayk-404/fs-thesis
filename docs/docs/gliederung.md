
Zitat-Style: harvard
# Titel

### WIP
Benchmarking Tabular Foundation Models against Hyperparameter-Optimized Machine Learning in Clinical Risk Prediction



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
3.4 TabPFN tuning  
3.5 Evaluation Framework: Robustness Loop, Metrics, and Fair Comparison  

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
6.3 TabPFN lowers the barrier
    LLM lowers the barrier for AI in general, but there is no easy way to find high impact. With MCP, Agents, etc we still
    have the error of halluzination. But with tabpfn we focus on bayesian inference. No haluzination but math as a backbone.
    And the base for this backbone is not a prompt, a poem or a thesis. It is the data every industry has, in tabular format. 
    This algorithm will lower the barrier for industry usage of AI. It will maybe not outperform current ML-Pipelines, Teams 
    of Engineers and Agents. But it will leverage the current barrier and improve the impact for businesses in a massive way.

``` 
GPT Formulierung  
While Large Language Models (LLMs) rely on stochastic sequence generation—prone to inherent hallucinations—Tabular Foundation Models like TabPFN leverage approximated Bayesian inference to provide robust, calibrated probability estimates from structured data.

The empirical results of this thesis (see Sections 4.1 & 4.3) demonstrate that the performance gap between zero-shot foundation models and highly optimized ML pipelines in clinical risk prediction is often marginal. Consequently, the primary value proposition shifts from raw predictive power to operational efficiency and reduced expertise requirements (Section 5.2). By mitigating the high entry barriers of traditional HPO-driven workflows, Tabular Foundation Models serve as a scalable entry point for AI adoption across data-driven industries, offering a mathematically grounded alternative to the risks of unstructured generative AI.
```