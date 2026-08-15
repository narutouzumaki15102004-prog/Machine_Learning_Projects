# Movie Recommender System

A basic machine learning project that recommends movies based on a selected movie.

## Live Demo

[Movie Recommender System](https://moviedekh.streamlit.app/)

## Features

* Select a movie from the available list
* Find similar movies using a similarity matrix
* Display the top 5 recommended movies
* Simple Streamlit web interface

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit
* Pickle

## Project Files

```text id="q7g4fx"
MovieRecommenderSystem/
│
├── app.py
├── movie_dict.pkl
├── similarity.pkl
├── requirements.txt
└── Movie_Recommender_System.ipynb
```

* `app.py` - Streamlit application
* `movie_dict.pkl` - Processed movie dataset
* `similarity.pkl` - Movie similarity matrix
* `requirements.txt` - Required Python packages
* `Movie_Recommender_System.ipynb` - Notebook used for developing the project

## How to Run Locally

Clone the repository and install the dependencies:

```bash id="r3q7jh"
pip install -r requirements.txt
```

Run the Streamlit application:

```bash id="b8v5cx"
streamlit run app.py
```

## Deployment

The application is deployed using **Streamlit Community Cloud**.


