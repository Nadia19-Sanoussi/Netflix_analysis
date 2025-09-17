# Netflix Content Analysis and Interactive Recommendation System Dashboard

## Live Demo

## Overview
This projects does two things:
1. **Analyzes** Netflix's content library to uncover trends in genres, countries, release years.
2. **Serves** the results through an interactive web dashboard wher users can get personalized content recommendations based on **genre** and **country**.

## Features
- **Exploratory Data Analysis (EDA):**visualized the distribution of movies vs. TV shoxs, content growth over time, and top producing countries.
- **Interactive Dashboard:**Visualize key metrics from the Netflix dataset.
- **Content-Based Filtering:** Built a recommendation engine that suggests titles of similar genre, and country of production.
-**Content-Based Recommander:**Get a list of 10 suggested titles similar to your preferences.

## Dataset
The dataset used in is NEtflix_titles, available on [kaggle](https://www.kaggle.com/datasets/shivamb/netflix_titles). It contains information about titles, director, cast, country, release_year, date_added,rating and more.

## Installation
1. Clone this repository: 'gitclone https://github.com/nadia19-sanoussi/netflix_analysis.git.
2. Install the required dependencies:'pip install -r requirements.txt'.

## Usage
1. Open the Jupyter Notebook:'juputer notebook notebooks/Netflix_Analysis.ipynb
2. Run the cells to see the analysis.
3. To get recommendations, modify the genre and country in the last cell of he notebook and run it.

## Key Insights
- Le catalogue Netflix a 𝐞𝐱𝐩𝐥𝐨𝐬é à 𝐩𝐚𝐫𝐭𝐢𝐫 𝐝𝐞 𝐥’𝐚𝐧𝐧é𝐞 2019-2022 (sûrement à cause de la pandémie ) avec une nette augmentation de contenu,
-Over 70% of Netflix's content is movies.
-𝐔𝐧𝐞 𝐠𝐫𝐚𝐧𝐝𝐞 𝐩𝐚𝐫𝐭𝐢𝐞 𝐝𝐞𝐬 𝐩𝐫𝐨𝐝𝐮𝐜𝐭𝐢𝐨𝐧𝐬 𝐯𝐢𝐞𝐧𝐭 𝐝𝐞𝐬 É𝐭𝐚𝐭𝐬-𝐔𝐧𝐢𝐬, mais on observe une 𝐦𝐨𝐧𝐭é𝐞 𝐝’𝐚𝐮𝐭𝐫𝐞𝐬 𝐩𝐚𝐲𝐬 𝐜𝐨𝐦𝐦𝐞 𝐥’𝐈𝐧𝐝𝐞, 𝐥𝐚 𝐂𝐨𝐫é𝐞 𝐝𝐮 𝐒𝐮𝐝, 
- Les 𝐠𝐞𝐧𝐫𝐞𝐬 𝐥𝐞𝐬 𝐩𝐥𝐮𝐬 𝐫𝐞𝐩𝐫é𝐬𝐞𝐧𝐭é𝐬 tournent autour du Drame, Comédie, action et Documentaire.
- 𝐥𝐚 𝐝𝐮𝐫é𝐞 𝐝𝐞 𝐟𝐢𝐥𝐦 𝐥𝐞𝐬 𝐩𝐥𝐮𝐬 𝐨𝐛𝐬𝐞𝐫𝐯é𝐞𝐬 dans le catalogue Netflix est de 100mins
-Les contenus proposés par Netflix sont pour la plupart pour des +17ans ce qui veut dire Netflix cible plus les adultes.

## Technologies Used
- Python
- Pandas
- Numpy
- Scikit-learn
- Matplotlib/seaborn
- plotly
- Streamlit

