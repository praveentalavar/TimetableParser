from parsetimetable import parsetimetable
from transformdata import transformdata

if __name__ == "__main__":
    print("Getting Timetable")
    p = parsetimetable()
    DF = transformdata(p)

    print(DF)

    # Uncomment to store into csv
    #DF.to_csv('FINAL.csv', encoding='utf-8', index=False)
    
    # Counting Lectures in the whole sem
    #print(DF.loc[DF.ClassType == 'LEC','ClassType'].count())
    