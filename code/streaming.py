import os
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

# set the directories
CODE_DIR = os.getcwd()
WORK_DIR = CODE_DIR.replace("/code", "")

if __name__ == "__main__":

  # set 10 seconds and make the algorithm run every 5 second
  sc = SparkContext(appName="PythonStreaming")
  ssc = StreamingContext(sc, 5)

  # get the lines of the file where the scraping data was stored
  lines = ssc.textFileStream(WORK_DIR+"/data")

  # print the lines to the console
  lines.pprint()
  
  ssc.start()
  ssc.awaitTermination()