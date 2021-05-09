from datetime import datetime
from pyspark.context import SparkContext
from pyspark.sql import SparkSession



def countlectures(sc):
    
    #Getting the input data
    df = sc.read.csv("file:///home/praveentalavar/Downloads/timetabledataset.csv",header=True)
    
    # Printing 1st 10 records of the table
    df.show(10)

    # Printing the count of Lectures in the timetbale data 
    # which shows total number of lectures in the current sem
    print("Lecture Count: ",df.filter(df["ClassType"]=="LEC").count())
    
    # Getting Count of all Class Types
    print("Count of all Class Types in the Timetable")
    df.groupBy("ClassType").count().show()
       

if __name__ == "__main__":
    sc = SparkSession.builder.appName("TimeTableLectures")\
            .config("spark.sql.shuffle.partitions", "50")\
            .config("spark.driver.maxResultSize","5g")\
            .config ("spark.sql.execution.arrow.pyspark.enabled", "true")\
            .getOrCreate()
    countlectures(sc)

