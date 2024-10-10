# Author: Vikhyat Srivastava
# Date: 23/09/2023
from pyspark.python.pyspark.shell import spark


# This program reads file written in text format and counts number of lines and number of words in each line.

def readFile():
    print('Enter the full path of the file.')
    data = [('asas','asdasd'),('a','b','c'),('r','t')]
    columns=['name','hobby']
    df = spark.createDataFrame(data,columns)
    display(df)

if __name__ == '__main__':
    readFile