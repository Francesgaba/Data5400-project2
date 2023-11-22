#!/usr/bin/env python
# coding: utf-8

# I interacts with "The Dog API" to retrieve information about dog breeds. The code uses the requests library to make HTTP requests to the API and the pandas library to manipulate and store the data in a DataFrame.

# In[1]:


# Import the necessary libraries for making HTTP requests and working with data in tabular format.
import requests
import pandas as pd

class DogAPI:
    def __init__(self):
        # Initialize the class with the base URL of the API.
        self.base_url = "https://api.thedogapi.com/v1"

    # Method to retrieve information about dog breeds from the API.
    def get_breeds(self):
        # Construct the API endpoint URL for fetching breed information.
        url = f"{self.base_url}/breeds"
        
        # Send a GET request to the API.
        response = requests.get(url)
        
        # Check if the response status code is not 200 (OK).
        if response.status_code != 200:
            # Print an error message and return an empty DataFrame.
            print(f"Error: {response.status_code}")
            return pd.DataFrame()
        
        try:
            # Try to parse the JSON response into a list of dog breeds.
            breeds = response.json()
        except ValueError:
            # If JSON parsing fails, print an error message and return an empty DataFrame.
            print("Invalid JSON response")
            return pd.DataFrame()

        # Convert the list of dog breeds into a DataFrame and return it.
        return pd.DataFrame(breeds)
.
dog_api = DogAPI()
breeds_df = dog_api.get_breeds()
print(breeds_df.head())


# In[ ]:





# In[ ]:




