import streamlit as st
import pandas as pd
import plotly.express as px

# Charger les données
df = pd.read_csv("netflix_titles.csv",encoding='latin1')

# Nettoyage des données
df=df.drop(df.columns[12:26],axis=1) #pour supprimer les colonnes inutile a partir de leur indexe
df=df.drop(["director","cast"], axis=1) #pour supprimer les colonne director et cast que j'ai juger inutile
df.loc[2,"country"]="France"   #TO REPLACE VALUES LINE BY LINE
df.loc[3,"country"]="United States"
df.loc[5,"country"]="United States"
df.loc[6,"country"]="United States"
df.loc[10,"country"]="United Kingdom"
df.loc[8718,"country"]="United States"
df.loc[8760,"country"]="United States"
df.loc[8784,"country"]="United Kingdom"
df.loc[8786,"country"]="India"
df.loc[8803,"country"]="South Korea"
df.loc[11,"country"]="Thailand" #to replace line by line 
df.loc[13,"country"]="Brazil"
df.loc[16,"country"]="Germany"
df.loc[18,"country"]="United States"
df.loc[8679,"country"]="India"
df.loc[8690,"country"]="United States"
df.drop([8759,8783,8785],axis=0)
df=df.dropna(subset=["country"])
df=df.dropna(subset=["date_added","rating","duration"]) #pour supprimer ls lignes contenant des valeurs manquante des colonnes suivantes 
df = df.copy()
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
df["year_added"] = df["date_added"].dt.year
df["month_added"] = df["date_added"].dt.month
df["day_added"] = df["date_added"].dt.day
df["genre"] = df["listed_in"].str.split(",").str[0].str.strip() #pour avoir le genre des films et series
df=df.drop(["listed_in","description"],axis=1)

# --- Titre du dashboard ---
st.set_page_config(page_title="Analyse Netflix", layout="wide")
st.title("Dashboard Analyse Netflix")

# --- KPIs ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Nombre total de titres", df.shape[0])
col2.metric("Nombre de films", df[df["type"]=="Movie"].shape[0])
col3.metric("Nombre de séries", df[df["type"]=="TV Show"].shape[0])
col4.metric("Pays uniques", df["country"].nunique())

st.markdown("---")

# --- Filtres ---
st.sidebar.header("Filtres")
genre_filter = st.sidebar.text_input("Filtrer par genre (ex: Drama)")
country_filter = st.sidebar.selectbox("Choisir un pays", ["Tous"] + sorted(df["country"].dropna().unique().tolist()))
year_filter = st.sidebar.slider("Année", int(df["release_year"].min()), int(df["release_year"].max()), (2000, 2021))

df_filtered = df.copy()
if genre_filter:
    df_filtered = df_filtered[df_filtered["genre"].str.contains(genre_filter, case=False, na=False)]
if country_filter != "Tous":
    df_filtered = df_filtered[df_filtered["country"] == country_filter]
df_filtered = df_filtered[(df_filtered["release_year"] >= year_filter[0]) & (df_filtered["release_year"] <= year_filter[1])]

# --- Graphes ---
col1, col2 = st.columns(2)

# Répartition par type
fig_type = px.pie(df_filtered, names="type", title="Répartition Films vs Séries")
col1.plotly_chart(fig_type, use_container_width=True)

# Répartition par genre
df_genre = df_filtered["genre"].str.split(", ", expand=True).stack().reset_index(level=1, drop=True).to_frame("genre")
fig_genre = px.bar(df_genre["genre"].value_counts().head(10), title="Top 10 Genres")
col2.plotly_chart(fig_genre, use_container_width=True)

# Évolution par année
fig_year = px.histogram(df_filtered, x="release_year", nbins=30, title="Nombre de titres par année")
st.plotly_chart(fig_year, use_container_width=True)

# Carte des pays
df_country = df_filtered.groupby("country").size().reset_index(name="counts")
fig_map = px.choropleth(df_country, locations="country", locationmode="country names",
                        color="counts", title="Répartition par pays")
st.plotly_chart(fig_map, use_container_width=True)

# --- Insights ---
st.subheader(" Insights")
st.write("""
-  Le catalogue Netflix a 𝐞𝐱𝐩𝐥𝐨𝐬é à 𝐩𝐚𝐫𝐭𝐢𝐫 𝐝𝐞 𝐥’𝐚𝐧𝐧é𝐞 2019-2022 (sûrement à cause de la pandémie ) avec une nette augmentation de contenu,
- 𝐋𝐞𝐬 𝐟𝐢𝐥𝐦𝐬 𝐫𝐞𝐬𝐭𝐞𝐧𝐭 𝐩𝐥𝐮𝐬 𝐧𝐨𝐦𝐛𝐫𝐞𝐮𝐱 𝐪𝐮𝐞 𝐥𝐞𝐬 𝐬é𝐫𝐢𝐞𝐬, même si les séries prennent de plus en plus de place,
- 𝐔𝐧𝐞 𝐠𝐫𝐚𝐧𝐝𝐞 𝐩𝐚𝐫𝐭𝐢𝐞 𝐝𝐞𝐬 𝐩𝐫𝐨𝐝𝐮𝐜𝐭𝐢𝐨𝐧𝐬 𝐯𝐢𝐞𝐧𝐭 𝐝𝐞𝐬 É𝐭𝐚𝐭𝐬-𝐔𝐧𝐢𝐬, mais on observe une 𝐦𝐨𝐧𝐭é𝐞 𝐝’𝐚𝐮𝐭𝐫𝐞𝐬 𝐩𝐚𝐲𝐬 𝐜𝐨𝐦𝐦𝐞 𝐥’𝐈𝐧𝐝𝐞, 𝐥𝐚 𝐂𝐨𝐫é𝐞 𝐝𝐮 𝐒𝐮𝐝, 
- Les 𝐠𝐞𝐧𝐫𝐞𝐬 𝐥𝐞𝐬 𝐩𝐥𝐮𝐬 𝐫𝐞𝐩𝐫é𝐬𝐞𝐧𝐭é𝐬 tournent autour du Drame, Comédie, action et Documentaire.
- 𝐥𝐚 𝐝𝐮𝐫é𝐞 𝐝𝐞 𝐟𝐢𝐥𝐦 𝐥𝐞𝐬 𝐩𝐥𝐮𝐬 𝐨𝐛𝐬𝐞𝐫𝐯é𝐞𝐬 dans le catalogue Netflix est de 100mins
- Les contenus proposés par Netflix sont pour la plupart pour des +17ans ce qui veut dire Netflix cible plus les adultes
""")
# Let the user select Genre and Country
genres = sorted(set([g.strip() for sublist in df["genre"].dropna().str.split(",") for g in sublist]))
countries = sorted(df["country"].dropna().unique())

selected_genre = st.selectbox("Select a Genre", options=genres)
selected_country = st.selectbox("Select a Country", options=countries)

if st.button("Recommend"):
    # Filter dataset
    recommendations = df[
        (df["genre"].str.contains(selected_genre, case=False, na=False)) &
        (df["country"] == selected_country)
    ]

    if recommendations.empty:
        st.warning("Sorry, no recommendations found for your selection.")
    else:
        st.success(f"Here are some recommendations in {selected_country} for {selected_genre}:")
        for title in recommendations["title"].head(10).tolist():
            st.write("✅", title)
