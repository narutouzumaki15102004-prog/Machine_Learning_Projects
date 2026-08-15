import streamlit as st
import pickle
import pandas as pd

movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    for i in movies_list:
        movie_id=i[0]
        # fetch poster from API

        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


st.title('Movie Recommender System')

Selected_Movie_name = st.selectbox(
    "Name of the movie that u watched recently and liked?",
    movies['title'].values,
)

if st.button("Top 5 Recommended Movies for u"):
    recommendations=recommend(Selected_Movie_name)
    for i in recommendations:
        st.write(i)





