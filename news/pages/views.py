from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup


# Create your views here.

def index(request):
    # Football news for index.html
    target_url="https://nf.com.tr/kategori/futbol/"
    resp = requests.get(target_url).content
    soup = BeautifulSoup(resp, "html.parser")

    list = soup.find("div", {"class":"mag-box-container clearfix"}).find_all("div", {"class":"post-details"})
    list2 = soup.find("div", {"class":"mag-box-container clearfix"}).find_all("a", {"class":"post-thumb"})

    postlist = []

    for div, a in zip(list, list2):
        title = div.find("h2", {"class":"post-title"}).find("a").text
        link = div.h2.a.get("href")
        date = div.find("span", {"class":"date meta-item tie-icon"}).text
        image = a.img.get("data-src")
        postlist.append({'title': title, 'date': date, 'link': link, 'image': image})
        
    title1 = postlist[0]['title']
    title2 = postlist[1]['title']
    title3 = postlist[2]['title']
    link1 = postlist[0]['link']
    link2 = postlist[1]['link']
    link3 = postlist[2]['link']
    date1 = postlist[0]['date']
    date2 = postlist[1]['date']
    date3 = postlist[2]['date']
    image1 = postlist[0]['image']
    image2 = postlist[1]['image']
    image3 = postlist[2]['image']
        
    # Formula1 news for index.html
    
    target_url="https://nf.com.tr/kategori/f1/"
    resp = requests.get(target_url).content
    soup = BeautifulSoup(resp, "html.parser")

    list = soup.find("div", {"class":"mag-box-container clearfix"}).find_all("div", {"class":"post-details"})
    list2 = soup.find("div", {"class":"mag-box-container clearfix"}).find_all("a", {"class":"post-thumb"})
    
    postlist1 = []

    for div, a in zip(list, list2):
        title = div.find("h2", {"class":"post-title"}).find("a").text
        link = div.h2.a.get("href")
        date = div.find("span", {"class":"date meta-item tie-icon"}).text
        image = a.img.get("data-src")
        postlist1.append({'title': title, 'date': date, 'link': link, 'image': image})
        
    title11 = postlist1[0]['title']
    title12 = postlist1[1]['title']
    title13 = postlist1[2]['title']
    link11 = postlist1[0]['link']
    link12 = postlist1[1]['link']
    link13 = postlist1[2]['link']
    date11 = postlist1[0]['date']
    date12 = postlist1[1]['date']
    date13 = postlist1[2]['date']
    image11 = postlist1[0]['image']
    image12 = postlist1[1]['image']
    image13 = postlist1[2]['image']
    
    # Basketball news for index.html
    
    target_url="https://nf.com.tr/kategori/nba/"
    resp = requests.get(target_url).content
    soup = BeautifulSoup(resp, "html.parser")
    
    list = soup.find("div", {"class":"mag-box-container clearfix"}).find_all("div", {"class":"post-details"})
    list2 = soup.find("div", {"class":"mag-box-container clearfix"}).find_all("a", {"class":"post-thumb"})

    postlist2 = []

    for div, a in zip(list, list2):
        title = div.find("h2", {"class":"post-title"}).find("a").text
        link = div.h2.a.get("href")
        date = div.find("span", {"class":"date meta-item tie-icon"}).text
        image = a.img.get("data-src")
        postlist2.append({'title': title, 'date': date, 'link': link, 'image': image})
        
    title21 = postlist2[0]['title']
    title22 = postlist2[1]['title']
    title23 = postlist2[2]['title']
    link21 = postlist2[0]['link']
    link22 = postlist2[1]['link']
    link23 = postlist2[2]['link']
    date21 = postlist2[0]['date']
    date22 = postlist2[1]['date']
    date23 = postlist2[2]['date']
    image21 = postlist2[0]['image']
    image22 = postlist2[1]['image']
    image23 = postlist2[2]['image']
    
    # Twitch news for index.html
    
    target_url="https://onedio.com/twitch-haberleri"
    resp = requests.get(target_url).content
    soup = BeautifulSoup(resp, "html.parser")
    extension = "https://onedio.com"

    list = soup.find("div", {"class":"flex flex-wrap mt-6 space-y-6 sm:space-y-0 tag-ternate-columns"}).find_all("article", {"class":"article-card relative bg-white w-full sm:w-[350px] rounded-none sm:rounded-md flex flex-col"})
    list2 = soup.find("div", {"class":"flex flex-wrap mt-6 space-y-6 sm:space-y-0 tag-ternate-columns"}).find_all("div", {"class":"flex flex-col p-4 flex-grow"})

    postlist3 = []

    for article, div in zip(list, list2):
            title = div.a.find("h3", {"class":"font-semibold o-linkbox__overlay"}).text
            link = div.find("a", {"class": "hover:text-link-primary line-clamp-3 mb-3"}).get("href")
            # date = div.find("span", {"class":"date meta-item tie-icon"})
            image = article.div.find("div",{"class":"absolute inset-0"}).img.get("src")
            postlist3.append({'title': title,'link': link, 'image': image})
            
    title31 = postlist3[0]['title']
    title32 = postlist3[1]['title']
    title33 = postlist3[2]['title']
    link31 = extension+postlist3[0]['link']
    link32 = extension+postlist3[1]['link']
    link33 = extension+postlist3[2]['link']
    # date11 = postlist3[0]['date']
    # date12 = postlist3[1]['date']
    # date13 = postlist3[2]['date']
    image31 = postlist3[0]['image']
    image32 = postlist3[1]['image']
    image33 = postlist3[2]['image']
    
    return render(request, 'pages/index.html', {'title1': title1, 'title2': title2, 'title3': title3, 'link1': link1, 'link2': link2, 'link3': link3, 'date1': date1, 'date2': date2, 'date3': date3, 'image1': image1, 'image2': image2, 'image3': image3,
                                                'title11': title11, 'title12': title12, 'title13': title13, 'link11': link11, 'link12': link12, 'link13': link13, 'date11': date11, 'date12': date12, 'date13': date13, 'image11': image11, 'image12': image12, 'image13': image13, 
                                                'title21': title21, 'title22': title22, 'title23': title23, 'link21': link21, 'link22': link22, 'link23': link23, 'date21': date21, 'date22': date22, 'date23': date23, 'image21': image21, 'image22': image22, 'image23': image23,
                                                'title31': title31, 'title32': title32, 'title33': title33, 'link31': link31, 'link32': link32, 'link33': link33, 'image31': image31, 'image32': image32, 'image33': image33})
