#!/usr/bin/env python
# coding: utf-8

# The dataset created by this script is a collection of URLs from the sitemaps listed in the robots.txt file of the New York Times website. Each row in the dataset represents a URL, and the columns contain various pieces of information about these URLs, such as their location, last modification date, change frequency, and priority. This information is typically used by search engines for indexing.
# 
# ##### Potential Uses of the Dataset:
# SEO Analysis: The dataset can be used for search engine optimization (SEO) analysis. By understanding the structure and content of the website's URLs, SEO strategies can be developed or improved.

# In[4]:


import requests
import pandas as pd
import xml.etree.ElementTree as ET

import requests
import xml.etree.ElementTree as ET
import pandas as pd

class SitemapParser:
    """
    A parser for extracting sitemap URLs from a robots.txt file and parsing the sitemaps to collect URLs.
    
    Attributes:
        robots_url (str): The URL of the robots.txt file.
        sitemaps (list): A list of sitemap URLs found in the robots.txt file.
    """

    def __init__(self, robots_url):
        """
        Initializes the SitemapParser with a given robots.txt URL.

        Args:
            robots_url (str): The URL of the robots.txt file.
        """
        self.robots_url = robots_url
        self.sitemaps = self.get_sitemaps()

    def get_sitemaps(self):
        """
        Retrieves and parses the robots.txt file to extract sitemap URLs.

        Returns:
            list: A list of sitemap URLs.
        """
        try:
            response = requests.get(self.robots_url)
            response.raise_for_status()
            sitemaps = [line.split(' ')[1] for line in response.text.split('\n') if line.startswith('Sitemap:')]
            return sitemaps
        except requests.RequestException as e:
            print(f"Error fetching robots.txt: {e}")
            return []

    def parse_sitemap(self, sitemap_url):
        """
        Parses a given sitemap URL and extracts URLs from it.

        Args:
            sitemap_url (str): The URL of the sitemap to parse.

        Returns:
            list: A list of dictionaries containing the parsed URL data.
        """
        try:
            response = requests.get(sitemap_url)
            response.raise_for_status()
            root = ET.fromstring(response.content)
            namespace = '{' + root.tag.split('}')[0].strip('{') + '}'
            urls = []
            for sitemap in root.findall('.//' + namespace + 'url'):
                url_info = {child.tag[len(namespace):]: child.text for child in sitemap}
                urls.append(url_info)
            return urls
        except (requests.RequestException, ET.ParseError) as e:
            print(f"Error parsing sitemap: {e}")
            return []

    def dataframe(self):
        """
        Converts the parsed sitemap URLs into a Pandas DataFrame.

        Returns:
            DataFrame: A DataFrame containing all URLs from the parsed sitemaps.
        """
        all_urls = []
        for sitemap_url in self.sitemaps:
            urls = self.parse_sitemap(sitemap_url)
            all_urls.extend(urls)
        return pd.DataFrame(all_urls)

parser = SitemapParser('https://www.nytimes.com/robots.txt') 
df = parser.dataframe()  # Converting the parsed sitemap to a DataFrame
print(df)


# In[ ]:




