Command to run the application: python app.py
Dataset consists of two csv files:
One file containing the phenotypic values for 280 genotypes for GWPS(gram), PH(cm), GY(gram) from five different locations(Dharwad, Delhi, Jharkhand, Karnal, Ludhiana), DH(days) and GFD(days) from four different locations(Dharwad, Delhi, Jharkhand, Karnal), and GNPS(number) from two different locations(Dharwad, Jharkhand) along with their pooled values.
The second csv file contains the processed SNP genotypic information obtained through Axiom Wheat Breeder’s Genotyping Array. It has 14790 SNPs and corresponding pair of alleles for all the genotypes, along with mention of primary allele/ secondary allele , chromosome (1A-7D), etc. 
After preprocessing, the final dataset will consist of Allele Sequence,GFD(Grain Filling Duration),PH(Plant Height),GWPS (Grain Weight Per Spike),DH(Days to Heading).
Random Forest was used to train the model.
The model is stored in a joblib file named random_forest_model_avg .joblib that can be loaded in the app.py file.
