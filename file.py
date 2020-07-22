from bs4 import BeautifulSoup
import requests
from datetime import date

today = str(date.today())


page=requests.get('https://www.worldometers.info/coronavirus/')
soup=BeautifulSoup(page.content, 'html.parser')
soup
#L=[i.findAll('td') for i in soup.find('tbody').findAll('tr')]
L=[i for i in soup.find('tbody').findAll('td')]
"""
    if i.text.strip()=='' :
        continue
    else :
"""
S=[]
for i in L :
    S.append(i.text.strip())
f=open("Cache//fichier_base"+today+".csv", 'w')
f.write("index,Country,Tot cases,New cases,Tot Deaths,New Deaths,Total Recovered,New Recov,Active Cases,Serious,Tot C par million,Deaths par million,Total Test,Tot T par million,population,Continent,col1,col2,col3\n")
WR=False
GR=False
c=1
g=0
for i in S:
    g+=1
    if g==S.index('All')+4:
        WR=True
        continue
            
            
    if WR==True :
        #print(i+'\n')
        if i!='' and i!='N/A' :
            if c%19==0:
                f.write(i)
                f.write('\n')
                c+=1
                continue
            else :
                if i[-1].isdigit() :
                    i=i.replace(',','')
                    f.write(i.replace('+', '')+',')
                    c+=1
                elif i[0].isalpha() :
                    c+=1
                    f.write(i+',')

        else :
            if c%19==0:
                f.write('\n')
                c+=1
                continue           
            else :
                c+=1
                f.write('-1,')
                

f.close()    
