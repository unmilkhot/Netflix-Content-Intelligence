import pandas as pd
import ast
import matplotlib.pyplot as plt
titles = pd.read_csv("titles.csv")
credits = pd.read_csv("credits.csv")


print("Titles dataset:", titles.shape)
print("Credits dataset:", credits.shape)

print("\nTitles columns:")
print(titles.columns)

print("\nCredits columns")
print(credits.columns)

print("\nTitles data types:")
print(titles.dtypes)

print("\nCredits data types:")
print(credits.dtypes)

print("\nMissing values in titles:")
print(titles.isnull().sum())

print("\nMissing values in Credits")
print(credits.isnull().sum())

print("\nDuplicate values in titles:")
print(titles.duplicated().sum())

print("\nDuplicate values in credits:")
print(credits.duplicated().sum())

print("\nUnique IDs in titles:")
print(titles["id"].nunique())

print("\nTotal rows in Titles:")
print(len(titles))

print("\nUnique IDs in credits:")
print(credits["id"].nunique())

titles_id = set(titles["id"])
credits_id = set(credits["id"])
missing_credits_id = titles_id - credits_id
print("\nTitles without credits:")
print(len(missing_credits_id))
print(missing_credits_id)

titles_without_credits = titles[titles["id"].isin(missing_credits_id)]

print("\ntitles_without_credits:")
print(titles_without_credits[["id", "title", "type", "release_year"]].head(20).to_string(index=False))

print(titles_without_credits["type"].value_counts())



print(titles_without_credits["release_year"].min())
print(titles_without_credits["release_year"].max())

print(titles_without_credits["release_year"].value_counts().sort_index())

print(titles_without_credits.groupby(["release_year", "type"]).size())

missing_percentage = (len(titles_without_credits)/len(titles))*100
print("missing_value_percentage:",missing_percentage)

print(titles["type"].value_counts())

show_overrepresentation = 76.50 / 37.57
print("show overrepresentation:", show_overrepresentation)

shows_missing_rate = (267/2306)*100
movie_missing_rate = (82/3831)*100
print("show missing rate",shows_missing_rate)
print("movie missing rate",movie_missing_rate)

print(titles["genres"].head(10).to_string(index=False))

print((titles["genres"] == "[]").sum())

print(titles["production_countries"].head(10).to_string(index=False))

print((titles["production_countries"] == "[]").sum())

print(titles[titles["age_certification"].isnull()]["type"].value_counts())

print(titles[titles["seasons"].isnull()]["type"].value_counts())

print(titles[titles["imdb_score"].isnull()]["type"].value_counts())

movie_imdb_missing_rate = (305/3831)*100
print("movie_imdb_missing_rate:", movie_imdb_missing_rate)

show_imdb_missing_rate = (163/2306)*100
print("show_imdb_missing_rate:", show_imdb_missing_rate)

print(titles[titles["tmdb_score"].isnull()]["type"].value_counts())

movie_tmdb_missing_rate = (158/3831)*100
print("movie_tmdb_missing_rate:", movie_tmdb_missing_rate)

show_tmdb_missing_rate = (94/2306)*100
print("show_tmdb_missing_rate:", show_tmdb_missing_rate)

print(titles[titles["tmdb_popularity"].isnull()]["type"].value_counts())

print(titles[titles["imdb_votes"].isnull()]["type"].value_counts())

movie_imdb_missing_vote_rate = (321/3831)*100
print("movie_imdb_missing_vote_rate:", movie_imdb_missing_vote_rate)

show_imdb_missing_vote_rate = (163/2306)*100
print("show_imdb_vote_missing_rate:", show_imdb_missing_vote_rate)

# print(type(titles["genres"].iloc[0]))

titles["genres"] = titles["genres"].apply(ast.literal_eval)
print(type(titles["genres"].iloc[0]))

print((titles["genres"].apply(len) == 0).sum())

genre_exploded = titles["genres"].explode()
print(genre_exploded.value_counts())

movie_genre = titles[titles["type"] == "MOVIE"]["genres"].explode()
print(movie_genre.value_counts())

show_genre = titles[titles["type"] == "SHOW"]["genres"].explode()
print(show_genre.value_counts())

movie_genre_percentage = (movie_genre.value_counts()/ (titles["type"] == "MOVIE").sum())* 100
print(movie_genre_percentage)

show_genre_percentage = (show_genre.value_counts()/ (titles["type"] == "SHOW").sum())* 100
print(show_genre_percentage)

genre_comparison = pd.DataFrame({
    "Movie (%)" : movie_genre_percentage,
    "Show (%)" : show_genre_percentage
    })

print(genre_comparison)

# plt.figure(figsize =(10,8))
# genre_comparison.plot(kind="bar", figsize =(10,8))

# plt.xlabel("genre")
# plt.ylabel("percentage")
# plt.title("Genre Distribution: Movies Vs Shows")
# plt.legend(title="content type")
# plt.xticks(rotation=45)
# plt.tight_layout()

# plt.show()

yearly_content = titles[["release_year", "type"]].value_counts().unstack(fill_value=0)
yearly_content = yearly_content.sort_index()
movie_growth = yearly_content["MOVIE"].pct_change()*100
print(movie_growth)
show_growth = yearly_content["SHOW"].pct_change()*100
print(show_growth)
print(yearly_content)
titles["decade"] = (titles["release_year"]//10)*10
print(titles[["release_year", "decade"]].head())
decade_content = titles[["decade","type"]].value_counts().unstack(fill_value=(0))
decade_content = decade_content.sort_index()
print(decade_content)

# yearly_content.plot(kind="line", figsize=(10,6))
# plt.xlabel("release_year")
# plt.ylabel("number of titles")
# plt.title("Movies Vs Shows release by year")
# plt.legend(title="content type")
# plt.tight_layout

# plt.show()

# movie_growth.plot(kind ="line", figsize=(10,6))
# plt.plot(movie_growth, label = "MOVIES")
# plt.plot(show_growth, label="SHOWS")

# plt.xlabel("release year")
# plt.ylabel("growth %")
# plt.title("year by year movie release growth")
# plt.tight_layout()

# plt.show()

# decade_content.plot(kind="bar", figsize=(10,6))
# plt.xlabel("decade")
# plt.ylabel("number of titles")
# plt.title("Movies Vs Shows by Decade")
# plt.legend(title="content type")

# plt.tight_layout()

# plt.show()

print(titles["runtime"].describe())

print((titles["runtime"] == 0).sum())

print(titles[titles["runtime"]==0][["title", "type", "release_year", "runtime"]])

runtime_valid = titles[titles["runtime"]>0]["runtime"]
print(runtime_valid.describe())

movie_runtime = titles[titles["type"]=="MOVIE"]["runtime"]
show_runtime = titles[titles["type"]=="SHOW"]["runtime"]

print(movie_runtime)
print(movie_runtime.describe())

print(show_runtime)
print(show_runtime.describe())

show_runtime_valid = titles[(titles["type"]=="SHOW") & (titles["runtime"]!=0)]["runtime"]
print(show_runtime_valid.describe())


# plt.figure(figsize=(8,6))
# plt.boxplot(
#     [movie_runtime, show_runtime_valid,],
#     tick_labels = ["MOVIES", "SHOWS"])
# plt.ylabel("runtime (minutes)")
# plt.title("Runtime Distribution : Movies Vs Shows")
# plt.tight_layout()
# plt.show()

show_long_runtime = titles[(titles["type"]=="SHOW")
                           & (titles["runtime"]>150)]
print("show_long_runtime",show_long_runtime[["title","release_year","runtime"]])
# print(" CODE RUN HO GAYA")

print(show_long_runtime[
    ["title","type","release_year","runtime","genres","seasons","description"]
     ].to_string(index=False))

documentation_shows = titles[
    (titles["type"]=="SHOW")&
    (titles["genres"].apply(lambda x : "documentation" in x))
]

print("documentation_shows",documentation_shows["runtime"].describe())

documentation_shows_valid = documentation_shows[
    documentation_shows["runtime"] != 0
]

print("documentation_shows_valid", documentation_shows_valid["runtime"].describe())

print("documentation_shows_valid", documentation_shows_valid["runtime"].value_counts().loc[[178,209]])


# plt.figure(figsize=(10,6))
# plt.hist(movie_runtime, bins = 30)
# plt.xlabel("Runtime (minutes)")
# plt.ylabel("Number of Titles")
# plt.title("Movie Runtime Distribution")
# plt.tight_layout()
# plt.show()


# plt.figure(figsize=(10,6))
# plt.hist(show_runtime_valid,bins=30)
# plt.xlabel("Runtime (minutes)")
# plt.ylabel("Number of Titles")
# plt.title("Show Runtime Distribution")
# plt.tight_layout()
# plt.show()


movie_runtime_category = pd.cut(
    movie_runtime,
    bins=[0,30,60,90,120,150, float("inf")],
    labels = ["0-30", "31-60", "61-90", "91-120", "121-150", "150+"]
)

print("movie_runtime_category",movie_runtime_category.value_counts().sort_index())


show_runtime_category = pd.cut(
    show_runtime_valid,
    bins=[0,30,60,90,120,150, float("inf")],
    labels = ["0-30", "31-60", "61-90", "91-120", "121-150", "150+"]
)

print("show_runtime_category",show_runtime_category.value_counts().sort_index())


runtime_comparison = pd.DataFrame({
    "Movies" : movie_runtime_category.value_counts().sort_index(),
    "Shows"  : show_runtime_category.value_counts().sort_index()
    })
print(runtime_comparison)


runtime_percentage = runtime_comparison.copy()

runtime_percentage["Movies"]=(
runtime_percentage["Movies"]/len(movie_runtime)*100)

runtime_percentage["Shows"]=(
    runtime_percentage["Shows"]/len(show_runtime_valid)*100)

print("runtime_percentage",runtime_percentage)


# runtime_percentage.plot(kind="bar",figsize=(10,6))

# plt.xlabel("Runtime (minutes)")
# plt.ylabel("percentage of titles")
# plt.title("Runtime Distribution: Movies Vs Shows")
# plt.legend(title= "content type")
# plt.xticks(rotation = 0)
# plt.tight_layout()
# plt.show()

print(titles["imdb_score"].describe())

movie_imdb = titles[titles["type"] == "MOVIE"]["imdb_score"]
show_imdb = titles[titles["type"] == "SHOW"]["imdb_score"]

print("Movie IMDB score:")
print(movie_imdb.describe())

print("\nShow IMDB score")
print(show_imdb.describe())


# plt.figure(figsize=(10,6))

# plt.hist(movie_imdb, bins=20)
# plt.xlabel("IMDB score")
# plt.ylabel("Number of movies")
# plt.title("IMDB score distribution : Movies")
# plt.tight_layout()
# plt.show()

movie_9_score = movie_imdb[movie_imdb == 9.0]
print(movie_9_score.count())


# plt.figure(figsize=(10,6))

# plt.hist(show_imdb, bins=20)
# plt.xlabel("IMDB score")
# plt.ylabel("Number of shows")
# plt.title("IMDB score distribution : shows")
# plt.tight_layout()
# plt.show()


# plt.figure(figsize=(10,6))

# plt.hist(movie_imdb, bins=20, alpha=0.5, label="movies")
# plt.hist(show_imdb, bins=20, alpha=0.5, label="shows")
# plt.xlabel("IMDB score")
# plt.ylabel("Number of shows")
# plt.title("IMDB score distribution : movies vs shows")
# plt.legend()
# plt.tight_layout()
# plt.show()


high_rated_movies = titles[
    (titles["type"] == "MOVIE") &
    (titles["imdb_score"]>=8)
]

print(high_rated_movies[["title","release_year","imdb_score"]])


high_rated_shows = titles[
    (titles["type"] == "SHOW") &
    (titles["imdb_score"]>=8)
]

print(high_rated_shows[["title","release_year","imdb_score"]])


movie_high_rated_percentage = len(high_rated_movies)/ len(movie_imdb)*100
show_high_rated_percentage = len(high_rated_shows)/ len(show_imdb)*100

print("movie 8+",movie_high_rated_percentage)
print("show 8+", show_high_rated_percentage)

top_movies = titles[
    titles["type"] == "MOVIE"
    ].sort_values(
        "imdb_score", ascending=False
    )

print(top_movies[["title", "release_year", "imdb_score"]].head(10))


top_shows = titles[
    titles["type"] == "SHOW"
    ].sort_values(
        "imdb_score", ascending=False
    )

print("top_shows",top_shows[["title", "release_year", "imdb_score"]].head(20))


print(titles["imdb_votes"].describe())


imdb_analysis = titles[["title","imdb_score","imdb_votes"]].dropna()
print(imdb_analysis.head())
print(imdb_analysis.shape)

# plt.figure(figsize=(10,6))
# plt.scatter(
#     imdb_analysis["imdb_score"],
#     imdb_analysis["imdb_votes"],
#     alpha=0.5

# )

# plt.xlabel("IMDB score")
# plt.ylabel("IMDB votes")
# plt.title("IMDB score Vs IMDB votes")

# plt.tight_layout()
# plt.show()


print(imdb_analysis["imdb_score"].corr(imdb_analysis["imdb_votes"]))

print(titles[["imdb_score", "tmdb_score"]].describe())

rating_comparison = titles[["title","imdb_score","tmdb_score"]].dropna()
print(rating_comparison)


print(rating_comparison["imdb_score"].corr(rating_comparison["tmdb_score"]))


# plt.figure(figsize=(10,6))

# plt.scatter(
#     rating_comparison["imdb_score"],
#     rating_comparison["tmdb_score"],
#     alpha=0.5
# )
# plt.xlabel("IMDB score")
# plt.ylabel("TMDB score")
# plt.title("IMDB score vs TMDB score")
# plt.tight_layout()
# plt.show()


print(credits["role"].value_counts())

print("unique people:", credits["person_id"].nunique())
print("unique actor:", credits[credits["role"]=="ACTOR"]["person_id"].nunique())
print("unique director:", credits[credits["role"]=="DIRECTOR"]["person_id"].nunique())

actor_counts = credits[
    credits["role"]=="ACTOR"
]["name"].value_counts()

print(actor_counts.head(10))

actor_title_counts = credits[
    credits["role"]== "ACTOR"

].groupby("name")["id"].nunique()

print(actor_title_counts.sort_values(ascending=False).head(10))


top_actors = actor_title_counts.sort_values(
    ascending = False
).head(10)

top_actor_data = credits[
    (credits["role"]== "ACTOR") &
    (credits["name"].isin(top_actors.index))
]

top_actor_content = top_actor_data.merge(
    titles[["id", "type"]],
    on = "id",
    how = "left"
)

print(top_actor_content.groupby(["name", "type"])["id"].nunique())


director_title_counts = credits[
    credits["role"]== "DIRECTOR"
    ].groupby("name") ["id"].nunique()

print(
    director_title_counts.sort_values(ascending=False).head(10)
)


top_directors = director_title_counts.sort_values(
    ascending = False
).head(10)

top_director_data = credits[
    (credits["role"]== "DIRECTOR") &
    (credits["name"].isin(top_directors.index))
]

top_director_content = top_director_data.merge(
    titles[["id", "type"]],
    on = "id",
    how = "left"
)

print(top_director_content.groupby(["name", "type"])["id"].nunique())



# Prepare genre data for Power BI

genre_data = titles[["id", "title", "type", "genres"]].explode("genres")

genre_data = genre_data[
    genre_data["genres"].notna() &
    (genre_data["genres"] != "")
].copy()

genre_data = genre_data.rename(columns={"genres": "genre"})

genre_data.to_csv("genre_distribution.csv", index=False)

print("Genre data saved:", genre_data.shape)
print(genre_data[["title", "type", "genre"]].head(10))