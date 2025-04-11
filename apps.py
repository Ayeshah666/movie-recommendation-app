import streamlit as st
import pandas as pd

# Load your data (make sure to update the paths)
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")
movie_ratings = pd.merge(ratings, movies, on="movieId")
user_ratings = movie_ratings.pivot_table(index=["userId"], columns=["title"], values="rating")

def get_recommendations(movie_title):
    movie_ratings_input = user_ratings[movie_title]
    similar_to_movie = user_ratings.corrwith(movie_ratings_input)
    similar_movies_output = pd.DataFrame(similar_to_movie, columns=["correlation"])
    similar_movies_output = similar_movies_output.dropna().sort_values("correlation", ascending=False)
    return similar_movies_output.head(10)

st.title("Movie Recommendation App")

movie_list = movies["title"].values
selected_movie = st.selectbox("Select a movie", movie_list)

if st.button("Get Recommendations"):
    recommendations = get_recommendations(selected_movie)
    st.write("Movies you might like:")
    st.write(recommendations)