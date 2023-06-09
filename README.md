
# Twitter-Sentiment-Analysis

Twitter Sentiment Analysis is a project aimed at analyzing the sentiment of tweets containing a particular keyword. The project uses a machine learning model trained on a dataset of labeled tweets to classify the sentiment of incoming tweets as positive, negative or neutral.


## Prerequisites

- Python 3.11
- NLTK
- Scikit-Learn
- Matplotlib
- Django
- Streamlit


## Installation

#### Clone the repository to your local machine

```bash
git clone https://github.com/chetan-droid/sentiment-analysis.git
```

#### Create Virtutal environment

```bash
  python -m venv./env
```

#### Activate Virtutal environment

```bash
source env/Scripts/Activate
```

#### Command to deactivate the Virtutal environment

```bash
deactivate
```

#### Install packages

```bash
pip install -r requirements.txt
```

### To migrate

```bash
python manage.py migrate
```

### To run application

```bash
python manage.py runserver
```
### To run web application

```bash
streamlit run quickstart.py
```

### While running the web application, firstly you have to run "python manage.py runserver" in one terminal and in other terminal you have to run "streamlit run quickstart.py" simultaneously.
