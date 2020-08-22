import csv
import pandas as pd
import os
import sys
import shutil

'''Check each file name and size that are downloaded. This will help make a determination
   of files which may be null or empty'''
my_dir = 'C:\\Users\\yching\\Desktop\\Assignments\\testfiles\\'

for f in os.listdir(my_dir):
    path = os.path.join(my_dir, f)
    if os.path.isfile(path):
        #print(f)
        print ( f + " with size in bytes:" +  str(os.path.getsize(path)))

'''Files downloaded can sometimes be in a nonconventional extension.
  Check filesname extensions-web scraper selenium took csv_ files'''
path = 'C:\\Users\\yching\\Desktop\\Assignments\\testfiles\\'

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

for file in files("."):
    print (file)


'''Renaming file extensions from csv_ to csv'''
#############   
'''dir_path = 'C:/Users/yching/Desktop/Assignments/'

for filename in os.listdir(dir_path):
    filename_splitext = os.path.splitext(filename)
    if filename_splitext[1] in ['.csv_','.txt']:
        print(filename_splitext)
        os.rename(os.path.join(dir_path, filename), 
                os.path.join(dir_path,filename_splitext[0] +  '.csv'))
'''
#############
'''Declare global variable and set to path of directory'''
arrival_folder = 'C:/Users/yching/Desktop/Assignments/webscraper/'
'''Clean, parse L_AIRLINE_ID file'''
airid_output = r'C:/Users/yching/Desktop/Assignments/webscraper/L_AIRLINE_ID.csv'
airid_destination = r'C:/Users/yching/Desktop/Assignments/webscraper/L_AIRLINE_ID_OUTCOME.csv'
df = pd.read_csv(airid_output)

# new data frame with split value columns 
new = df["Description"].str.split(":", n = 1, expand = True) 
# making separate first name column from new data frame 
df["Airline_Name"]= new[0] 
  
# making separate last name column from new data frame 
# also strip away leading and trailing spaces
df["Airline_Initial"]= new[1].str.strip()


#Display the first 200 rows-just as a test to display on screen
result = df.head(200)

#Testing only first 10 rows of data
#print("First 10 rows of the DataFrame:")
#print(result)

# save dataframe- take out index
result.to_csv(airid_destination, index = False)

'''Clean, parse L_YESNO_RESP file'''

yesnoresp_output = r'C:/Users/yching/Desktop/Assignments/webscraper/L_YESNO_RESP.csv'
yesnoresp_destination = r'C:/Users/yching/Desktop/Assignments/webscraper/L_YESNO_RESP_OUTCOME.csv'
df2 = pd.read_csv(yesnoresp_output)

# also strip away leading and trailing spaces
df2['Description']= df2['Description'].str.strip()


#Display the first 200 rows-just as a test to display on screen
result2 = df2.head(200)

# save dataframe- take out index
result2.to_csv(yesnoresp_destination, index = False)

'''Clean, parse L_WORLD_AREA_CODES'''
wrldareacode_output = r'C:/Users/yching/Desktop/Assignments/webscraper/L_WORLD_AREA_CODES.csv'
wrldareacode_destination = r'C:/Users/yching/Desktop/Assignments/webscraper/L_WORLD_AREA_CODES_OUTCOME.csv'
df3 = pd.read_csv(wrldareacode_output)

# also strip away leading and trailing spaces
df3['Description']= df3['Description'].str.strip()


#Display the first 200 rows-just as a test to display on screen
result3 = df3.head(200)

# save dataframe- take out index
result3.to_csv(wrldareacode_destination, index = False)

'''Clean, parse L_WEEKDAYS'''

weekdays_output = r'C:/Users/yching/Desktop/Assignments/webscraper/L_WEEKDAYS.csv'
weekdays_destination = r'C:/Users/yching/Desktop/Assignments/webscraper/L_WEEKDAYS_OUTCOME.csv'
df4 = pd.read_csv(weekdays_output)

# also strip away leading and trailing spaces
df4['Description']= df4['Description'].str.strip()


#Display the first 200 rows-just as a test to display on screen
result4 = df4.head(200)

# save dataframe- take out index
result4.to_csv(weekdays_destination, index = False)


'''Clean, parse L_AIPORT_ID data'''

airport_output = r'C:/Users/yching/Desktop/Assignments/webscraper/L_AIRPORT_ID.csv'
airport_destination = r'C:/Users/yching/Desktop/Assignments/webscraper/L_AIRPORT_ID_OUTCOME.csv'
df5 = pd.read_csv(airport_output)

# new data frame with split value columns 
new5 = df5["Description"].str.split(":", n = 1, expand = True) 
# making separate first name column from new data frame 
df5["Airport_Location"]= new5[0] 
  
# making separate last name column from new data frame 
# also strip away leading and trailing spaces
df5["Airport_Name"]= new5[1].str.strip()


#Display the first 200 rows-just as a test to display on screen
result5 = df5.head(200)

#Testing only first 10 rows of data
#print("First 10 rows of the DataFrame:")
#print(result)

# save dataframe- take out index
result5.to_csv(airport_destination, index = False)

'''Clean, parse L_AIPORT_SEQ_ID data'''

airportseq_output = r'C:/Users/yching/Desktop/Assignments/webscraper/L_AIRPORT_SEQ_ID.csv'
airportseq_destination = r'C:/Users/yching/Desktop/Assignments/webscraper/L_AIRPORT_SEQ_ID_OUTCOME.csv'
df6 = pd.read_csv(airportseq_output)

# new data frame with split value columns 
new6 = df6["Description"].str.split(":", n = 1, expand = True) 
# making separate first name column from new data frame 
df6["Airport_Location"]= new6[0] 
  
# making separate last name column from new data frame 
# also strip away leading and trailing spaces
df6["Airport_Name"]= new6[1].str.strip()


#Display the first 200 rows-just as a test to display on screen
result6 = df6.head(200)

#Testing only first 10 rows of data
#print("First 10 rows of the DataFrame:")
#print(result)

# save dataframe- take out index
result6.to_csv(airportseq_destination, index = False)

'''Clean, parse L_CITY_MARKET_ID data'''

citymarket_output = r'C:/Users/yching/Desktop/Assignments/webscraper/L_CITY_MARKET_ID.csv'
citymarket_destination = r'C:/Users/yching/Desktop/Assignments/webscraper/L_CITY_MARKET_ID_OUTCOME.csv'
df7 = pd.read_csv(citymarket_output)

# new data frame with split value columns 
new7 = df7["Description"].str.split(",", n = 1, expand = True) 
# making separate first name column from new data frame 
df7["Airport_Region"]= new7[0] 
  
# making separate last name column from new data frame 
# also strip away leading and trailing spaces
df7["Airport_State_Country"]= new7[1].str.strip()


#Display the first 200 rows-just as a test to display on screen
result7 = df7.head(200)

#Testing only first 10 rows of data
#print("First 10 rows of the DataFrame:")
#print(result)

# save dataframe- take out index
result7.to_csv(citymarket_destination, index = False)

'''Clean, parse 960972689_T_ONTIME_REPORTING'''

ontime_output = r'C:/Users/yching/Desktop/Assignments/webscraper/960972689_T_ONTIME_REPORTING.csv'
ontime_destination = r'C:/Users/yching/Desktop/Assignments/webscraper/L_ONTIME_OUTCOME.csv'
df8 = pd.read_csv(ontime_output)


# Remove all duplicates rows based on all columns
result_df = df8.drop_duplicates(keep=False)

#Display the first 200 rows-just as a test to display on screen
result_df = result_df.head(200)

#Need to add list comprehension and create an unique hash keys
result_df['hash_key'] = [[i for i in row if i == i] for row in result_df.values]

# save dataframe- take out index
result_df.to_csv(ontime_destination, index = False)

#Copy cleaned and parsed files into a new directory for ingestion
dir_src = ("C:\\Users\\yching\\Desktop\\Assignments\\webscraper\\")
dir_dst = ("C:\\Users\\yching\\Desktop\\Assignments\\dbinteraction\\")

for filename in os.listdir(dir_src):
    if filename.endswith('OUTCOME.csv'):
        shutil.copy( dir_src + filename, dir_dst)
    print(filename)