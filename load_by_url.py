#!/usr/bin/env python3
import sys
import os
import shutil
import requests
from bs4 import BeautifulSoup
color = sys.argv[2]
icon =sys.argv[3]
url = sys.argv[4]
folder = './'+sys.argv[1]

if not os.path.exists(folder):
    os.makedirs('./'+sys.argv[1])

if not os.path.exists(sys.argv[1]+'/css'):
    os.makedirs(sys.argv[1]+'/css')

with open(sys.argv[1]+'/css/style.css','w') as cssFile:
    cssFile.close


req = requests.get(url)
soup = BeautifulSoup(req.text, "lxml")
titleContent = soup.find(id="title-page").find_next('h2')
presentationContent = soup.find(id="presentation")
durationContent = soup.find(id="content").find_all('p')[0]
programmeContent = soup.find("div",id="tab1")
programmeContent["class"]=""
programmeContent.find("h4")["class"] ="notdisplayed"
footers = soup.find("div",id="tab3").find_all("p")
competenceContent = footers[1]
skillContent = footers[3]
technologyContent = footers[2]
practicalContent = footers[0]
priceContent = footers[4]

 

os.chdir(folder)
fIn = open(r"./../generic-template.html")  # use raw strings for windows file names
fOut = open(r"index.html", "w")
for line in fIn:
    fOut.write(line)
fIn.close()
fOut.close()
with open('index.html','r') as myFile:
    fileSoup = BeautifulSoup(myFile,'lxml')
    titleHead = fileSoup.find("title")
    titleHead.clear()
    titleHead.append(titleContent.text)

## presentation content
    presentation = fileSoup.find("div",id="presentationContent")
    presentation["class"]="presentation"
    presentation.clear()
    presentation.append(presentationContent)

## footer
    skill = fileSoup.find("h6",id="skill")
    skill.clear()
    skill.append(skillContent.text)


    title = fileSoup.find("h5",class_="titlePage")
    title.clear()
    title.append(titleContent.text)

    competence = fileSoup.find("h6",id="competence")
    competence.clear()
    competence.append(competenceContent.text)


    technology = fileSoup.find("h6",id="technology")
    technology.clear()
    technology.append(technologyContent.text)

    practical = fileSoup.find("h6",id="practical")
    practical.clear()
    practical.append(practicalContent.text)

    price = fileSoup.find("h6",id="price")
    price.clear()
    price.append(priceContent.text)


    duration = fileSoup.find("h6",id="duration")
    duration.clear()
    duration.append(durationContent.text)

# Contenu content
    programme = fileSoup.find("div",id="tabContent")
    changeClasses = programmeContent.find_all("div",class_="span5") 
    changeh5classes = programmeContent.find_all("h5") 
   
    for someCls in changeClasses:
        someCls["class"] ="col-sm-6"
   
   
    for someCls5 in changeh5classes:
        someCls5["class"] ="orangeColor"

    programme.clear()
    programme.append(programmeContent)

    #change backgroundColor
    mainDiv1 = fileSoup.find("div",id="main1")
    mainDiv1['class'] = "row "+color+"Background whiteColor"
    mainDiv2 = fileSoup.find("div",id="main2")
    mainDiv2['class'] = "circle "+color+"Background"
    mainDiv3 = fileSoup.find("div",id="main3")
    mainDiv3['class'] = "whiteColor "+color+"Background"   


    ##iconLogo
    iconTag = fileSoup.find('i',id="iconLogo")
    
    iconTag["class"]=str(icon)
    myFile.close

with open('index.html','wb') as myFile:
    myFile.write(fileSoup.prettify("utf-8"))
    myFile.close