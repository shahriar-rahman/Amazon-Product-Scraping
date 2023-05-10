# Amazon Product Scraping
==============================

Scraping amazon products based on a user search.

## Introduction
Browsing Amazon can be very confusing due to inconsistent layouts and web page structure. 
More importantly, the site can often be quite slow to browse due to so much traffic. 
Furthermore, comparing multiple products is much more difficult to infer as it requires browsing 
all the links for different products. 

The primary incentive of this project is to bypass the inconvenience a user would face by 
automating the search procedure on the Amazon site, scraping relevant information, and 
displaying comprehensively in a tabular format making it easy for the user to compare 
and analyze for a better purchase decision on Amazon.

![alt text](https://github.com/shahriar-rahman/Amazon-Product-Scraping/blob/main/img/amazon_products.JPG)

## Project Organization
---------------------------------------------------------

    ├── LICENSE
    ├── Makefile             <- Makefile with various commands
    ├── README.md        <- The top-level README for developers using this project.
    ├── scraping_data
    │   ├── csv              <- Data in csv format compatible with pandas dataframe.
    │   ├── excel           <- Data in xlsx format for better data analysis.
    │   ├── xml             <- Data in xml format.
    │   └── json            <- Data in Json format for better utilization.
    │
    ├── img                 <- Contains project image files.
    │   
    ├── figures                 <- Graphs generated from the scraped data.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         			generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── main            <- Contains scripts for automating web scraping using Selenium
    │   │   └── amazon.py
    │   │
    │   ├── visualization   <- Scripts folder for data analysis and visualization
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------
## Methods used:
• Selenium 4.8.3

• Webdriver and Expected Conditions

• System queue, Implicit and Explicit Waits

• Chrome and Chrome Options

• Nested Pagination

• DataFrame Manipulation using Pandas

• Data Storage using CSV, Excel, JSON and XML format
