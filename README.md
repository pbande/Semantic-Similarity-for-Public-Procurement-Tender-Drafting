# Semantic-Similarity-for-Public-Procurement-Tender-Drafting

## Structure of the directory:

### Data Directory:
- [insiders_with_preprocessed_descriptions.csv](data/insiders_with_preprocessed_descriptions.csv) : training data preprocessed.
- [insiders_downloaded.csv](data/insiders_downloaded.csv) : training data.
- [minors_with_preprocessed_descriptions.csv](data/minors_with_preprocessed_descriptions.csv) : testing data preprocessed.
- [minors_downloaded.csv](data/minors_downloaded.csv) : testing data.
- [cpv.csv](data/cpv.csv) : contains each code and its description.

### Code Directory:

#### General
- [distances.ipynb](src/general/distances.ipynb) : understanding cosine and euclidean distance.
- [insiders_preprocessing.ipynb](src/general/insiders_preprocessing.ipynb) : training data preprocessing.
- [minors_preprocessing.ipynb](src/general/minors_preprocessing%20copy.ipynb) : testing data preprocessing.
- [text_preprocessing.py](src/general/text_preprocessing.py) : Data preprocessing script.
- [visualization.ipynb](src/general/visualization.ipynb) : Data analysis.
- [visualization_complex.ipynb](src/general/visualization_complex.ipynb)  : Data clustering analysis.

#### Non-Processing
- [embedding.ipynb](src/non_preprocessing/embedding.ipynb) : Build models.
- [embedding_eval.ipynb](src/non_preprocessing/embedding_eval.ipynb) : Evaluate .embeddings.

#### Preprocessing
- [embedding.ipynb](src/preprocessing/embedding.ipynb) : Build models.
- [embedding_eval.ipynb](src/preprocessing/embedding_eval.ipynb) : Evaluate embeddings.

### Models Directory:
Models generated are stored in the "non_preprocessing" and "preprocessing" folders depending on the data used.
