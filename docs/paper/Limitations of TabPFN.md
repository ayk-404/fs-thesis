# From the paper
Limitations of TabPFN. The limitations of TabPFN are as follows:  
(1) the inference speed of TabPFN may be slower than highly optimized 
approaches such as CatBoost; (2) the memory usage of TabPFN scales 
linearly with dataset size, which can be prohibitive for very large data-
sets; and (3) our evaluation focused on datasets with up to 10,000 
samples and 500 features; scalability to larger datasets requires further 
study (p.327)

The author (Hollmann) is not talking about wheter they look into the tabpfn algo if there is a smaller dataset.

# When to use TabPFN
When to use TabPFN. TabPFN excels in handling small- to medium-sized 
datasets with up to 10,000 samples and 500 features (Fig. 4 and Extended  
Data Table 1). For larger datasets and highly non-smooth regression 
datasets, approaches such as CatBoost9, XGB7 or AutoGluon40 are likely 
to outperform TabPFN. (p.326)

In my show case the TabPFN is basically equal to the state-of-art algorithms. 

