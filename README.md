<img src="img/lexiguard_logo.png" height="400" alt="LexiGuard logo">

# LexiGuard

Detecting toxicity in online comments.

Capstone project for neue fische Data Science bootcamp (neuefische.de).

Code based on collaborative work by:  
André Oliveira ([Bambuzera](https://github.com/Bambuzera))  
Eric Martinez ([ericmartinez1189](https://github.com/ericmartinez1189))  
Purvi Parmar ([PurviDParmar](https://github.com/PurviDParmar))  
Michael Schickenberg ([CalleRosa40](https://github.com/CalleRosa40))

## Repo Contents

| File | Description |
| --- | --- |
| eda.ipynb | Initial exploratory data analysis to get us started |
| data_preprocessing.ipynb | Create data file(s)
| baseline_model.ipynb | Baseline model (BOW + logistic regression)
| random_forest.ipynb | Random forest experiments
| xgboost.ipynb | XGBoost experiments
| lstm.ipynb | LSTM final model (TensorFlow)
| lstm_dashboard.py | Very basic prototype dashboard using Streamlit
| functions.ipynb | Utitlity functions
| lexiguard_presentation.pdf | Capstone project presentation slides |

A video of the group's capstone presentation will be available soon.

## Installing

Preferably create and activate a virtual Python environment. run the Jupyter notebooks of this project by running the following at the command prompt (Windows):

```
python -m venv .venv --prompt="lexiguard"
.venv\Scripts\activate
pip install -r requirements.txt
```

Downloads required??? (eg !python -m spacy download en_core_web_md)

Code for Streamlit


## Notes

Bias!!!

The project was our first trip into the field of NLP. It was thus foremost about learning and trying out things. Many of these things did not make it into the final project version but can still be found in the /archive folder. Some examples of what we have tinkered around with:

[[See funnel graphic!]]

- POS tagging
- SpaCy vectors
- TF-IDF
- BERT
- Transformers lib
- Pickle
- SMOTE
- fastText

[[Move this section to README in /archive?]]

## Outlook / To do

...
