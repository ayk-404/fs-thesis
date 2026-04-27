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

# Recherche Gemini
Lineare Regression: Die Rechenkomplexität skaliert näherungsweise linear mit der Anzahl der Beobachtungen n, also O(n⋅p 
2
 ) für p Features.

TabPFN: Da es die gesamte Trainingsmenge als "Context" in einem Transformer verarbeitet, dominiert der Self-Attention-Mechanismus. Dieser skaliert quadratisch zur Anzahl der Datenpunkte (n):

Complexity≈O(n 
2
 ⋅d)
Modell,Trainingsphase,Inferenzphase (Vorhersage)
Dummy/Linear,Minimaler Aufwand.,Extrem schnell (einfache Matrix-Multiplikation).
XGBoost,Iteratives Finden von Splits (O(nlogn)).,Sehr schnell (Traversieren von Bäumen).
TabPFN,Entfällt. Das Modell ist vortrainiert.,Sehr rechenintensiv. Der gesamte Datensatz wird bei jeder Vorhersage durch den Transformer geschleust.

TabPFN ist für Small Data (typischerweise n<1.000) optimiert. In diesem Bereich bietet es State-of-the-Art Genauigkeit ohne Hyperparameter-Tuning. Sobald n jedoch steigt, wird der quadratische Rechenaufwand (O(n 
2
 )) zum Flaschenhals.
 TabPFN ist deshalb langsamer, weil es selbst bei großen Datensätzen versucht, eine hochkomplexe Transformer-Operation durchzuführen, während lineare Regressionen und Bäume die Datenmenge algorithmisch effizienter "verdauen".