# spark-streaming

In this project, I scraped data from instagram. The program "scrape.py" will go through a few hashtags and get the number of posts per hashtag.
This numbers are written to a text file in the data directory.
The scraping algorithm can be run in the terminal by navigating to the directory where the file scrape.py is situated and running following command:
```
python scrape.py
```
The algorithm will open a google chrome window, log in with the account I made for this project and start its scraping. The algorithm will sleep for 5 seconds and resume the scraping from the start.

The second algorithm is "streaming.py". This will use spark streaming to retrive the information from the text file and print it to the console.
The algorithm will wait for 5 seconds before checking if any files in the data-directaory have been changed.
The streaming algorithm should be run at the same time as the scrape algorithm in a seperate terminal with the following command:
```
python streaming.py
```
