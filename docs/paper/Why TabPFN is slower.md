# Why TabPFN is slower then the other algos in the prediction.

Transformer-based ICL algorithms, however, receive train and 
test data in a single pass and thus perform training and prediction at 
once. Thus, when a fitted model is reused, it has to redo computations 
for the training set. (P.321)

the data is trained in a single pass and ...

Limitations of TabPFN. The limitations of TabPFN are as follows:  
(1) the inference speed of TabPFN may be slower than highly optimized 
approaches such as CatBoost; (2) the memory usage of TabPFN scales 
linearly with dataset size, which can be prohibitive for very large data-
sets; and (3) our evaluation focused on datasets with up to 10,000 
samples and 500 features; scalability to larger datasets requires further 
study (p.327)

the secound point is the reason why the performance is pretty bad compared. The memory usage of TabPFN scales with the data size.