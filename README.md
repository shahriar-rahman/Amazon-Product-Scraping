# Scraping Amazon Products based on a User Search
===========================================================================

An automated scraping tool that locates a particular product and, by utilizing the Selenium Webdriver, crawls and extracts all the information based on a user search. This is an updated version of the project with the new Selenium update as well as improvements in file organization, code refactoring, and improvements.

</br></br>

<div align="center">
    <img width="65%" src="img/amazon1.gif" alt="amazon.gif" >
</div>

</br></br>

### Introduction
Amazon.com is an American multinational technology company focusing on e-commerce, cloud computing, online advertising, digital streaming, and artificial intelligence. It has been often referred to as "one of the most influential economic and cultural forces in the world," and is often regarded as one of the world's most valuable brands. Additionally, it is considered one of the Big Five American technology companies, alongside Alphabet (parent company of Google), Apple, Meta (formerly Facebook, Inc.), and Microsoft. Amazon was founded by Jeff Bezos from his garage in Bellevue, Washington.

However, it is important to mention that browsing the site can pose some challenges as it is quite confusing due to the lackluster layouts and inconsistent web page structure. Furthermore, the site can often be quite slow to browse due to extensive traffic. As a result, comparing multiple products can be a much more difficult process than it seems as it affects the user's decision-making as it requires browsing all the links for the same type of products with different specifications. Therefore, it is imperative to bypass the inconvenience a user might face otherwise, by automating the search procedure on the Amazon site, scraping relevant information, and displaying comprehensively in a tabular format making it easy for the user to compare and analyze for a better purchase decision on Amazon.

</br></br>

![alt text](https://github.com/shahriar-rahman/Amazon-Product-Scraping/blob/main/img/amazon_products1.jpg)

</br></br>

### ◘ Objective
* Automate web browsing for better convenience
* Utilize Selenium Webdriver to achieve the targeted goal
* Use concepts of web-scraping to find and traverse the correct Document Object Model (DOM) structure.
* Conduct extensive search till the end of pages
* Ensure the data scraped does not contain any missing values
* Briefly explore the acquired data

### ◘ Approach
The primary incentive of this research is to:
* Initiate a search for a user's preferred item (i.e. iPhone)
* Crawl to the Amazon site and locate all the links relevant to the target item
* Use the Pagination concept to transition between pages
* Scrape only the necessary tags such as title, ratings, price, descriptions, and total ratings
* Use Pandas and Matplotlib libraries to visualize and ensure the data stands out


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

• Data Storage using CSV, Excel, and JSON format

===========================================================================
