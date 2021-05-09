import requests
from bs4 import BeautifulSoup
from helper import replace_all


def parsetimetable():

    url1 = "https://www.timetable.ul.ie/UA/Default.aspx"
    url2 = "https://www.timetable.ul.ie/UA/CourseTimetable.aspx"
    d={"<td>": "", "</td>": ""}

    with requests.session() as s:
        # Loading Cookies
        s.get(url1)  
        soup = BeautifulSoup(s.get(url2).text, "html.parser")

        # Form Data to post
        data = {
            "__EVENTTARGET": "ctl00$HeaderContent$CourseDropdown",
            "ctl00$HeaderContent$CourseDropdown": ""
        }

        #Headers to post
        headers = {'User-Agent':'Mozilla/5.0','Referer': 'https://www.timetable.ul.ie/UA/CourseTimetable.aspx'}
        for inp in soup.select("input[value]"):
            data[inp["name"]] = inp["value"]

        # Get all Courses available from the Website
        courses = [
            opt["value"]
            for opt in soup.select("#HeaderContent_CourseDropdown option")
            if opt["value"] != "-1"
        ]

        # List Initialisation 
        l1=[]
        l2=[]

        # Traversing through Courses available
        for c in range(0,len(courses)):
            
            # Get Timetable for course 'c':
            data["ctl00$HeaderContent$CourseDropdown"] = courses[c]

            # Post request for selecting Course and parse
            soup = BeautifulSoup(s.post(url2, data=data, headers = headers).content, "html.parser")

            # Get all Years of a Course
            years = [
                opt["value"]
                for opt in soup.select("#HeaderContent_CourseYearDropdown option")
                if opt["value"] != "-1"
            ]

            # Traversing through years for a particular Course
            for y in range(0,len(years)):
                
                # Get Timetable for year 'y'
                data["ctl00$HeaderContent$CourseYearDropdown"] = years[y]
                for inp in soup.select("input[value]"):
                    data[inp["name"]] = inp["value"]

                # Post request for selecting Year and parse
                soup = BeautifulSoup(s.post(url2, data=data, headers = headers).text, "html.parser")
                
                #print some data:
                for i in soup.body.find_all('td'):
                    #print(str(i))    
                    l1.append(str(i))

                # Filtering and Gathering data
                for i in range(0,len(l1)):
                    temp=(i+1)%6
                    if l1[i] == "<td>\xa0</td>" or l1[i] == "<td> </td>":
                        pass
                    else:
                        try:
                            for j in l1[i].split("<br/> <br/>"):
                                # Replacing <td> and </td> with ''
                                new=replace_all(j,d)
                                if len(new.split("<br/>")) == 5:
                                    l2.append([courses[c],years[y],temp,new.split("<br/>")[0],new.split("<br/>")[1],new.split("<br/>")[2],new.split("<br/>")[3].split(':')[1]])
                                else:
                                    l2.append([courses[c],years[y],temp,new.split("<br/>")[0],new.split("<br/>")[1],new.split("<br/>")[2],new.split("<br/>")[4].split(':')[1]])
                        except IndexError:
                            print("Unexpected Data")    
                l1.clear()
    return(l2)        