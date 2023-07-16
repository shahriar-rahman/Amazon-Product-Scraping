from setuptools import find_packages, setup

setup(
    name='selenium_amazon2',
    version='1.2.0',
    description="An automated scraping tool which locates a particular product and, by utilizing Selenium Webdriver, "
                "crawls and extracts all the information.",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    author='Shahriar Rahman',
    license='MIT',
    author_email='shahriarrahman1101@gmail.com',
    python_requires='>=3.11, <4',
    extras_requires={
        "dev": ["pytest>=7.0", "twine>=4.0.2"]
    },
    install_requires=[
        'selenium~=4.8.3',
        'pandas~=2.0.0',
        'openpyxl~=3.1.2',
        'matplotlib~=3.7.1',
        'seaborn~=0.12.2',
        'setuptools~=65.5.1',
    ],

)
