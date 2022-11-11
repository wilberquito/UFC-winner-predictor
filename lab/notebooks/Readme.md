# Read and execution fluxe

- info.ipynb
    
    gives you information about the meaning of the columns of the data

- backend.ipynb

    this notebooks is in charge of read data from Postgres and save to Mongo

- processing.ipynb

    this notebook is in charge of reading saved data from Mongo and parsing. Fixes missing values and drops unnecesary columns and also transform some categorical features to binary esparse matrix. Finally creates a model.

- visualization.ipynb

    Shows some diference between raw data and cleaned data from the pipeline of the processing notebook

- ensemble.ipynb

    Encodes some features, adjustes the distribution sample and creates 4 distinc models. Those that have biassed data are more acurasity than the others, but the true is that are overfitted becasuse the biass.


