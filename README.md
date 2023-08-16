===========================================================================
# Scraping Amazon Products based on a User Search
An automated scraping tool that locates a particular product and, by utilizing the Selenium Webdriver, crawls and extracts all the information based on a user search. This is an updated version of the project with the new Selenium update as well as improvements in file organization, code refactoring, and improvements.    

</br></br> 

<div align="center">
    <img width="65%" src="img/amazon1.gif" alt="amazon.gif" >
</div>

</br></br>

## ◘ Navigation
- [Introduction](#-introduction)
    - [Background](#-background)
    - [Objective](#-objective)
- [Technical Preliminaries](#-technical-preliminaries)
    - [Approach](#-approach)
    - [Scraping Procedure](#-scraping-procedure)
- [System Design](#-system-design)
    - [Selenium](#-selenium)
    - [Methodologies & Concepts](#-methodologies-and-concepts)
- [Project Specifications](#-project-specifications)
    - [Project Organization](#-project-organization)
    - [Libraries & Technologies](#-libraries-and-technologies)
- [Installation](#-installation)
    - [Module Installation](#-module-installation)
    - [Library Installation](#-library-installation)
    - [Supplementary Resources](#-supplementary-resources)
- [License](#-license)

</br>

## ◘ Introduction  

### • Background
Amazon.com is an American multinational technology company focusing on e-commerce, cloud computing, online advertising, digital streaming, and artificial intelligence. It has been often referred to as "one of the most influential economic and cultural forces in the world," and is often regarded as one of the world's most valuable brands. Additionally, it is considered one of the Big Five American technology companies, alongside Alphabet (parent company of Google), Apple, Meta (formerly Facebook, Inc.), and Microsoft. Amazon was founded by Jeff Bezos from his garage in Bellevue, Washington.

However, it is essential to mention that browsing the site can pose some challenges as it is pretty confusing due to the lackluster layouts and inconsistent web page structure. Furthermore, the site can often be relatively slow to browse due to extensive traffic. As a result, comparing multiple products can be a much more difficult process than it seems as it affects the user's decision-making as it requires browsing all the links for the same type of products with different specifications. Therefore, it is imperative to bypass the inconvenience a user might face otherwise, by automating the search procedure on the Amazon site, scraping relevant information, and displaying comprehensively in a tabular format making it easy for the user to compare and analyze for a better purchase decision on Amazon.

</br></br>

![alt text](https://github.com/shahriar-rahman/Amazon-Product-Scraping/blob/main/img/amazon_products1.jpg)

</br>

### • Objective
* Automate web browsing for better convenience
* Utilize Selenium Webdriver to achieve the targeted goal
* Use concepts of web-scraping to find and traverse the correct Document Object Model (DOM) structure.
* Conduct extensive search till the end of pages
* Ensure the data scraped does not contain any missing values
* Briefly explore the acquired data

</br></br>

## ◘ Technical Preliminaries

### • Approach
The primary incentive of this research is to:
* Initiate a search for a user's preferred item (i.e. iPhone)
* Crawl to the Amazon site and locate all the links relevant to the target item
* Use the Pagination concept to transition between pages
* Scrape only the necessary tags such as title, ratings, price, descriptions, and total ratings
* Use Pandas and Matplotlib libraries to visualize and ensure the data stands out

</br>

### • Scraping Procedure
![alt text](https://github.com/shahriar-rahman/Amazon-Product-Scraping/blob/main/img/flowchart.png)

</br></br>

## ◘ System Design

### • Selenium 
Selenium is an open-source umbrella project for a range of tools and libraries aimed at supporting browser automation. It refers to a suite of tools that are widely used in the testing community when it comes to cross-browser testing. Selenium cannot automate desktop applications but can be used in browsers and is considered to be one of the most preferred tool suites for automation testing of web applications as it provides support for popular web browsers which makes it very powerful. It supports a number of browsers (Google Chrome 12+, Internet Explorer 7,8,9,10, Safari 5.1+, Opera 11.5, Firefox 3+) and operating systems (Windows, Mac, Linux/Unix).

</br>

The Selenium WebDriver drives a browser natively, as a user would, either locally or on a remote machine using the Selenium server, which marks a leap forward in terms of browser automation. WebDriver allows the user to choose a programming language to create test scripts and is an advancement over Selenium RC to overcome a few limitations. However, it is not capable of handling window components, but this exact drawback can be circumvented by using tools like Sikuli, Auto IT, etc.

</br>

### • Methodologies and Concepts
* Selenium Webdriver
* Expected Conditions
* Implicit and Explicit Waits
* Chrome and Chrome Options
* Nested Pagination
* Data Storage based on Excel, CSV, and JSON formats
* Pandas and Matplotlib for examining the Scraped data

</br></br>

## ◘ Project Specifications

### • Project Organization
---------------------------------------------------------

    ├── LICENSE
    |
    ├── README.md            # The top-level README for developers using this project
    ├── scraping_data        # Scraped Data stored in various formats
    │   ├── csv              
    │   ├── excel          
    │   └── json            
    │
    ├── img                    # Contains Project related files
    │   
    ├── graphs                # Graphs generated from the scraped data
    │
    ├── requirements.txt        # The requirements file for reproducing the analysis environment
    │                         			
    ├── test_environment.txt    # This is to inspect the correct version of Python
    │
    ├── setup.py                # Makes project pip installable (pip install -e .) so src can be imported
    │       
    ├── src                    # Source code for use in this project.
    │   ├── __init__.py        # Makes src a Python module
    │   │
    │   ├── crawler            # Primary Selenium script to initiate crawling
    │   │   └── crawler.py
    │   │   
    │   ├── controller            # Script that can be modified if the DOM structure receives any overhaul in future. Also contains user preferred items to scrape.
    │   │   └── controller.py
    │   │
    │   ├── visualization           # Script for data analysis and visualization
    │       └── visualize.py

--------

</br>

### • Libraries and Technologies
* selenium~=4.8.3
* pandas~=2.0.0
* openpyxl~=3.1.2
* matplotlib~=3.7.1
* seaborn~=0.12.2
* setuptools~=65.5.1
* Python 3.11
* PyCharm 2023.1

</br></br>

## ◘ Installation

### • Module Installation
Using setup.py:
1. To use the *setup.py* file in Python, the first objective is to have the *setuptools* module installed. It can be accomplished by running the following command:
```
pip install setuptools                                     
```
2. Once the setuptools module is installed, use the setup.py file to build and distribute the Python package by running the following command:
```
python setup.py sdist bdist_wheel
```
3. In order to install the my_package package, run the following command:
```
pip install my_package  
```
4. This command will install all the requirements:
```
pip install .                                 
```
5. This will install the my_package package and any of its dependencies that are not already installed on your system. Once the package is installed, you can use it in your Python programs by importing it like any other module. For example:
```
import my_package    
```

<br/>

### • Library Installation
Using pip:
In order to *install* the required packages on the local machine, Open pip and run the following commands separately:
```
> pip install selenium               

> pip install pandas                                                                                 

> pip install seaborn

> pip install matplotlib                  
```

<br/>

### • Supplementary Resources
For more details, visit the following links:
* https://pypi.org/project/setuptools/
* https://pypi.org/project/selenium/
* https://pypi.org/project/pandas/
* https://pypi.org/project/seaborn/
* https://pypi.org/project/matplotlib/

<br/><br/>

## ◘ License 
### • MIT License
Copyright (c) 2023 Shahriar Rahman

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

</br>

===========================================================================
