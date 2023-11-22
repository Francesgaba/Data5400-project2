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

class SitemapParser:
    def __init__(self, robots_url):
        self.robots_url = robots_url  # URL of the robots.txt file
        self.sitemaps = self.get_sitemaps()  # List of sitemap URLs found in the robots.txt

    def get_sitemaps(self):
        try:
            response = requests.get(self.robots_url)
            response.raise_for_status()
            # splitting the text into lines and filtering for those that start with 'Sitemap:'
            sitemaps = [line.split(' ')[1] for line in response.text.split('\n') if line.startswith('Sitemap:')]
            return sitemaps
        except requests.RequestException as e:
            print(f"Error fetching robots.txt: {e}")
            return []

    def parse_sitemap(self, sitemap_url):
        try:
            response = requests.get(sitemap_url)  # Fetching the sitemap
            response.raise_for_status()  # raise an exception for HTTP errors
            root = ET.fromstring(response.content)  # parsing XML content
            # Handling namespaces in XML
            namespace = '{' + root.tag.split('}')[0].strip('{') + '}'
            urls = []
            for sitemap in root.findall('.//' + namespace + 'url'):
                # extracting URL information and removing namespace from tags
                url_info = {child.tag[len(namespace):]: child.text for child in sitemap}
                urls.append(url_info)
            return urls
        except (requests.RequestException, ET.ParseError) as e:
            print(f"Error parsing sitemap: {e}")
            return []

    def dataframe(self):
        all_urls = []
        for sitemap_url in self.sitemaps:
            urls = self.parse_sitemap(sitemap_url)  # Parsing each sitemap
            all_urls.extend(urls)  # Aggregating all URLs
        return pd.DataFrame(all_urls)  

parser = SitemapParser('https://www.nytimes.com/robots.txt') 
df = parser.dataframe()  # Converting the parsed sitemap to a DataFrame
print(df)


# In[ ]:




