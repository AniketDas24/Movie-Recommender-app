import streamlit as str
import pickle
import requests

str.title("Movie Recomender")

movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    ind = movies['title'][movies['title'] == movie].index[0]
    lst = sorted(list(enumerate(similarity[ind])), key = lambda x: x[1], reverse=1)[1:6]
    res = []
    res_poster = []
    for i in lst:
        movie_ids = movies['id'][i[0]]
        res_poster.append(fetch_poster(movie_ids))
        res.append(movies['title'][i[0]])
    return res,res_poster

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

selected_movie = str.selectbox(
     'Select Your Movie',
     movies['title'].values)

if str.button('Recomend'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = str.columns(5)
    with col1:
        str.text(recommended_movie_names[0])
        str.image(recommended_movie_posters[0])
    with col2:
        str.text(recommended_movie_names[1])
        str.image(recommended_movie_posters[1])

    with col3:
        str.text(recommended_movie_names[2])
        str.image(recommended_movie_posters[2])
    with col4:
        str.text(recommended_movie_names[3])
        str.image(recommended_movie_posters[3])
    with col5:
        str.text(recommended_movie_names[4])
        str.image(recommended_movie_posters[4])

