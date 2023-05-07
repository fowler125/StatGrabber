
This code was made for educational and personal purposes ONLY and was not designed for commercial use.

Welcome to my NFL stats project! This project is designed to collect and conglomerate NFL statistics for one week in the season. The project includes code for scraping data from various sources, cleaning and organizing the data, and creating visualizations to help users analyze the data. With this project, you'll be able to quickly and easily access a wide range of NFL stats for a given week in the season. Whether you're a football fan looking to dive deep into the numbers or a data analyst interested in exploring a new dataset, this project has something for you.

# **Installation**
To use this project, you'll need to install a few dependencies:

```
- bs4
- urlopen from urllib.request
- beautifulsoup
- datetime
- os
```
You can install these dependencies using pip, the Python package manager. First, make sure you have Python and pip installed on your system. Then, run the following command in your terminal:


```
'pip install bs4 urllib3 beautifulsoup4 datetime'
```
This will install all the required dependencies for the project.

Alternatively, you can also install the dependencies from the requirements.txt file included in the project. Simply run the following command in your terminal:


```pip install -r requirements.txt```
This will install all the required dependencies listed in the file.

With the dependencies installed, you're ready to start using the project!


# Usage
To use this project, follow these steps:

1. Download the project from GitHub.

2. Install the dependencies listed in the requirements.txt file using pip. You can do this by running the following command in your terminal:
```pip install -r requirements.txt```
3. Once the dependencies are installed, you can run the GrabLatestGameScores.py script to collect and conglomerate NFL stats for one week in the season. You can do this by running the following command in your terminal:
```python GrabLatestGameScores.py```
4. There is also the ```TopWeekStats.Py``` which will grab the top stat holders for that given week and export to a TXT file.
5. This will run the script and generate a TXT file with the NFL stats for the specified week.
6. Optionally, you can create a common file to run both at the same time, this has been tested and works perfectly fine as well, but for my use case I did not need to run them both at the same time.

7. You can also modify the **_GrabLatestGameScores.py_** script to collect stats for a different week or to customize the output format. The script is well-documented and easy to modify.

That's it! With these simple steps, you can collect and analyze NFL stats for any week in the season. Enjoy!

# Examples
![NFL STATS EXAMPLE](/Example%20Graphics/cha%20v%20den.png)