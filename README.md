<img src="img/lexiguard_logo.png" height="400" alt="LexiGuard logo">

# LexiGuard

*Detecting toxicity in online comments using an LSTM recurrent neural network*

Capstone group project for [neue fische Data Science Bootcamp](https://www.neuefische.de/bootcamp/data-science):  
[Presentation slides (PDF)](lexiguard_presentation.pdf)  
[Presentation video](https://www.youtube.com/watch?v=uQ_HnZWJMs8)

## Installation

The most convenient way to run the notebooks contained in this repo is probably running them in the cloud, e.g. on [Google Colab](https://colab.research.google.com/). To do so open a notebook and click on the Colab badge at the top.

If you would like to run the notebooks locally on your own machine, you may want to install [Anaconda distribution](https://www.anaconda.com/) and create a virtual environment using the included `environment.yml` (`conda env create -f environment.yml`).

To run the Streamlit prototype dashboard, use this command: `python -m streamlit run lstm_dashboard.py`.

## Repo Contents

| File | Description |
| --- | --- |
| eda.ipynb | Initial exploratory data analysis |
| data_preprocessing.ipynb | Create data file(s) |
| baseline_model.ipynb | Baseline model (BOW + logistic regression) |
| random_forest.ipynb | Random forest experiments |
| xgboost.ipynb | XGBoost experiments |
| lstm.ipynb | LSTM final model (TensorFlow) |
| lstm_dashboard.py | Very basic prototype dashboard using Streamlit |
| functions.ipynb | Utitlity functions |

## Notes

The project was the group's first trip into the field of NLP. It was thus foremost about learning and trying out things. Many of these things did not make it into the final project version. Some examples of what we also tinkered around with:

- SpaCy (for vectorization)
- BERT / Hugging Face Transformers
- fastText (for vectorization)
- Gensim
- Naive Bayes
- random undersampling
- POS tagging
- stemming

## Credits

Code based on collaborative work by:  
André Oliveira ([Bambuzera](https://github.com/Bambuzera))  
Eric Martinez ([ericmartinez1189](https://github.com/ericmartinez1189))  
Purvi Parmar ([PurviDParmar](https://github.com/PurviDParmar))  
Michael Schickenberg ([CalleRosa40](https://github.com/CalleRosa40))
