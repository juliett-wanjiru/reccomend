import http
from bs4 import BeautifulSoup
import re
import requests as http

def  main(emotion):
    if (emotion=="sad"):
        urlhere='http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'

    elif(emotion=="contempt"):
        urlhere='http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'

    elif(emotion=="angry"):
        urlhere='http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'

    elif(emotion=="hope"):
        urlhere='http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'

    elif(emotion=="fear"):
        urlhere='http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'

    elif(emotion=="fun"):
        urlhere='http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'

    elif(emotion=="trust"):
        urlhere='http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'
         
    elif(emotion=="shock"):
        urlhere='http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'


    response= http.get(urlhere)
    data= response.text
    soup = SOUP(data, "lxml")

    title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})
    return title

if __name__=='__main__':
    emotion=input("enter the emotion: ")
    a=main(emotion)
    count=0
    if(emotion =="contempt" or emotion=="angry" or emotion=="shock"):
        for i in a:
            tmp=str(i).split('>;')
            if(len(tmp) == 3):
                print(tmp[1][:-3])
            if (count>13):
                break
            count+=1
    else:
        for i in a:
            tmp=str(i).split('>;')
            if(len(tmp)==3):
                print(tmp[1][:-3])
            if (count>11):
                break
            count+=1



    



  



