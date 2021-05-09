import pandas as pd
from helper import expand_week

def transformdata(l2):
    # List to Dataframe for easy transformations
    df=pd.DataFrame(l2)
    df.columns = df.columns.astype(str)

    # Dictionary for Replacing
    weekDays = {0:"Saturday",1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday"}

    #df = pd.read_csv('sample.csv')

    # Column transformations
    df[['CourseCode','Course']] = df['0'].str.split('-', 1, expand=True)
    df['Year'] = df['1']
    df['2'].replace(weekDays, inplace=True)
    df['Day'] = df['2']
    df[['StartTime','EndTime']] = df['3'].str.split(' - ', 1, expand=True)
    df['4']=df['4'].apply(lambda x: str(x)+" - NA" if(len(str(x)) <= 12) else str(x))
    df[['ModuleName','ClassType','ClassGroup']] = df['4'].str.split(' - ', 2, expand=True)
    df['Professor'] = df['5']
    df['Week'] = expand_week(df['6'])

    # Dropping repeated and unwanted Columns
    df=df.drop(['0','1','2','3','4','5','6'], axis = 1)
    
    # Split Explode to have unique week value
    df= df.set_index(['CourseCode','Course','Year','Day','StartTime','EndTime','ModuleName','Professor','ClassType','ClassGroup']).apply(lambda x: x.str.split(',').explode()).reset_index()
    
    return df
    
    
    