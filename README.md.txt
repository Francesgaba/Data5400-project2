Ziqi Huang

Part 1: Sitemap Parser

I defines a class called SitemapParser that can be used to parse sitemap files and extract URLs from them. The init() method takes a URL to a robots.txt file as input and stores it in the robots_url attribute. The get_sitemaps() method fetches the robots.txt file and extracts the sitemap URLs from it. The parse_sitemap() method takes a sitemap URL as input and parses the XML content to extract URLs from it. The dataframe() method converts all the extracted URLs into a Pandas DataFrame.

Part 2: Dog Breeds API

In this part,I defines a class called DogAPI that can be used to interact with the Dog Breeds API. The init() method takes the base URL of the API as input and stores it in the base_url attribute. The get_breeds() method sends a GET request to the API to fetch information about dog breeds. It parses the JSON response into a list of dog breeds and returns a Pandas DataFrame containing the breed information.

Part 3: Box Office Mojo Scraper

In part 3 , I create a class called BoxOfficeMojoScraper that can be used to scrape movie data from the Box Office Mojo website. The init() method takes the base URL of the website as input and stores it in the base_url attribute. The scrape_movies() method sends a GET request to the website to fetch the movie data. I uses BeautifulSoup to parse the HTML content and extract the movie data into a Pandas DataFrame.