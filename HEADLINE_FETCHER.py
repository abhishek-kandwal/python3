# here importing all the required libraies for our program
from bs4 import BeautifulSoup
import requests
import csv

# here getting the homepage of the website 
r = requests.get("https://www.hindustantimes.com/")
soup = BeautifulSoup(r.content, "lxml")

#soup.prettify() code will indent the code
#print(soup.prettify())

# below code will create a file in which headline will be saved
csv_file = open('headlines.csv','w')
csv_writer = csv.writer(csv_file)

# this below line of code will create row heading 
csv_writer.writerow(['headlines']) 

# grabing all the headlines one by one 
for head in soup.find_all('div', class_='subhead4'):
    
    # here using exception blocks , if any block don't have the headines it will pass it and will not break the program 
    
    try:
        
        # grabing the headline and saving it in the variable headline
        
        headline = head.h2.a.text        
    
    except:
        
        # if above try block will not work it will jump in this block
        
        headline = None    
        
    # here saving the headlines in the csv file
    
    csv_writer.writerow([headline])
    
    # here printing the headlines 
    
    print(headline)
    print()
    
# here closing the csv file that we create     
csv_file.close()
