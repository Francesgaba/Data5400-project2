#!/usr/bin/env python
# coding: utf-8

# In[13]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

class BoxOfficeMojoScraper:
    def __init__(self):
        self.base_url = "https://www.boxofficemojo.com/year/world/2022/"
"""The class initializes with a base URL, which is set to the 2022 worldwide box office page on Box Office Mojo."""
    
    def scrape_movies(self):
        response = requests.get(self.base_url)
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return pd.DataFrame()
"""This def fetches the page content from the base URL using the requests library.
If the HTTP response status is not 200 (OK), it prints an error message and returns an empty pandas DataFrame.
The method then uses BeautifulSoup to parse the HTML content."""

        soup = BeautifulSoup(response.content, 'html.parser')
        # Find the table rows
        rows = soup.find_all('tr')[1:]  # Skipping the header row   """The method then uses BeautifulSoup to parse the HTML content.It finds all table rows and iterates over them to extract data"""

        movie_data = []
        for row in rows:
            #For each row, extract various pieces of movie data such as rank, title
            rank = row.find('td', class_='a-text-right mojo-header-column mojo-truncate mojo-field-type-rank mojo-sort-column').get_text(strip=True)
            title_cell = row.find('td', class_='a-text-left mojo-field-type-release_group')  
            title = title_cell.get_text(strip=True) if title_cell else 'No title'
            
            world_money_cell = row.find('td', class_='a-text-right mojo-field-type-money')
            world_money = world_money_cell.get_text(strip=True) if world_money_cell else 'No data'

            dom_money_cell = row.find_next('td', class_='a-text-right mojo-field-type-money')
            dom_money = dom_money_cell.get_text(strip=True) if dom_money_cell else 'No data'

            percent_cell = row.find_next('td', class_='a-text-right mojo-field-type-percent')
            percent = percent_cell.get_text(strip=True) if percent_cell else 'No data'

            For_money_cell = row.find_next('td', class_='a-text-right mojo-field-type-money')
            For_money = For_money_cell.get_text(strip=True) if For_money_cell else 'No data'
            
            For_percent_cell = row.find_next('td', class_='a-text-right mojo-field-type-percent') # website selector 
            For_percent = For_percent_cell.get_text(strip=True) if For_percent_cell else 'No data'   
            
            movie_data.append({
                'Rank': rank,
                'Title': title,
                'Worldwide Gross': world_money,
                'Domestic Gross': dom_money,
                'Domestic %': percent,
                'Foreign Gross': For_money,
                'Foreign %': For_percent
            })
            
"""The extracted data for each movie is stored in a dictionary and appended to a list
then convert the list of movie data dictionaries into a pandas DataFrame and returns it """

        # Return the DataFrame created from the movie_data list
        return pd.DataFrame(movie_data)


# ### PART 4 
# #### EAD

# In[14]:

scraper = BoxOfficeMojoScraper()
movies_df = scraper.scrape_movies()
movies_df.head()


# In[15]:


movies_df.info()


# In[16]:


movies_df.describe()


# In[17]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[21]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

movies_df['Worldwide Gross'] = movies_df['Worldwide Gross'].replace('[\$,]', '', regex=True).astype(float)
movies_df['Domestic Gross'] = movies_df['Domestic Gross'].replace('[\$,]', '', regex=True).astype(float)
movies_df['Foreign Gross'] = movies_df['Foreign Gross'].replace('[\$,]', '', regex=True).astype(float) # convert to float 

variabele = ['Domestic Gross', 'Worldwide Gross','Foreign Gross']

plt.figure(figsize=(12, 8))

for i, col in enumerate(variabele):

    plt.subplot(3, 2, 2*i + 1)
    sns.histplot(movies_df[col], kde=True)
    plt.title(f'Histogram of {col}')

    plt.subplot(3, 2, 2*i + 2)
    sns.boxplot(y=movies_df[col])
    plt.title(f'Boxplot of {col}')

plt.tight_layout()
plt.show()


# In[22]:


def convert_percentage(value):
    if isinstance(value, str):
        value = value.replace('%', '').replace('<', '').strip() #remove % and -
        if value == '-' or value == '': 
            return 0.0
        return float(value) / 100  # covert by /100
    return value

movies_df['Domestic %'] = movies_df['Domestic %'].apply(convert_percentage)
movies_df['Foreign %'] = movies_df['Foreign %'].apply(convert_percentage)

percent_vars = ['Domestic %','Foreign %']

plt.figure(figsize=(12, 12))

for i, col in enumerate(percent_vars):
    #histogram
    plt.subplot(2, 2, 2*i + 1)
    sns.histplot(movies_df[col], kde=True)
    plt.title(f'Histogram of {col}')
    #boxplot
    plt.subplot(2, 2, 2*i + 2)
    sns.boxplot(y=movies_df[col])
    plt.title(f'Boxplot of {col}')

plt.tight_layout()
plt.show()


# #### research question:
# 
# "Is there a correlation between a movie's worldwide gross revenue and the balance of its domestic and foreign gross revenues?"
# 
# 

# In[23]:


# Create a scatter plot
plt.figure(figsize=(12, 6))
sns.scatterplot(x='Worldwide Gross', y='Domestic %', data=movies_df, color='blue', label='Domestic %')
sns.scatterplot(x='Worldwide Gross', y='Foreign %', data=movies_df, color='red', label='Foreign %')
plt.title('Worldwide Gross vs Domestic and Foreign Revenue Proportions')
plt.xlabel('Worldwide Gross ($)')
plt.ylabel('Revenue Proportion (%)')
plt.legend()
plt.grid(True)
plt.show()


# The scatter plot suggests that there is no strong correlation between a movie's worldwide gross revenue and the balance of its domestic and foreign gross revenues. High-grossing movies do not necessarily have a balanced revenue ratio.instead, they can be skewed towards either market, but with a tendency for foreign markets to contribute significantly to the worldwide gross

# In[ ]:




