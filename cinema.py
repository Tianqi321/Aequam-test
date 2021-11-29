
"""
The page shown at the link below contains movies with some metadata of interest to our friend Quentin, a budding movie director.

https://www.listchallenges.com/100-must-see-movies-for-more-advanced-cinephiles

title
year
ranking
no_of_votes


Task
Using your preferred language and/or tools - write a program that parses this page and extracts the following data into two possible file formats

1 - A CSV file
2 - A HTML file with some style formatting applied - You can use a CSS framework like https://tailwindcss.com/docs to complete this task.


Include instructions on how to run your program including installing any dependencies.

Usage:

python cinema.py --format [ CSV | HTML ]

"""

from bs4 import BeautifulSoup
import urllib.request
import requests
import csv
import pandas as pd
import re





def transform():
    def getHTMLText(url):
        try: 
            for i in range(0,20):            
                r = requests.get(url, timeout=30)
                r.raise_for_status() 
                r.encoding = 'utf-8' 
                return r.text
        except:
            return ""
    url_vote='https://www.listchallenges.com/100-must-see-movies-for-more-advanced-cinephiles/vote'


    html=getHTMLText(url_vote)
    soup_vote=BeautifulSoup(html,'html.parser')
    movie=soup_vote.select('div[class="item-name"]')
    rank=soup_vote.select('td[class="listVoteItem-rank"]')
    no_of_vote=soup_vote.select('span[class="listVote-combinedVoteCount"]')
    year_re = re.compile(r'[(](.*?)[)]', re.S)  
    name=[]
    year=[]
    for i in range(100):
    
        name.append(re.sub(r'[(](.*?)[)]', '',movie[i].string.strip())  )
        year.append(re.findall(year_re,str(movie[i].string.strip()) ))
        rank=[]
    for i in range(100):
        rank.append(i+1)
        vote=[]
    for i in range(100):
        vote.append(no_of_vote[i].string)
    df=pd.DataFrame()
    df['name']=name
    df['year']=year
    df['rank']=rank
    df['no_of_vote']=vote
    df.to_csv("./result.csv",index=True)
    print(df)
pass
transform()


'''
    I dont understand should i also do it with the format HTML/CSS because i am
    not very good at web desgine,but i think the main idea is the same expect with 
    csv format i use RE to remove all the HTML part
'''