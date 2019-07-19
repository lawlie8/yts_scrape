from bs4 import BeautifulSoup
import requests
import time
import sys
import os




tmp_list = []   #list to store magnet links
x = open('yts_magnet.txt','r+')
hu = x.readlines()
try:
    list = hu[3].split('title=')
    str = list[-1].split('"')
    last = str[1]
except:
    list = hu[6].split('title=')
    str = list[-1].split('"')
    last = str[1]

print('Found last magnet link at line 3  ' + last)



def check(no_time_to_think_about_new_variable,last):

    if no_time_to_think_about_new_variable.split(' ') == last.split(' '):
        fw = open('yts_magnet.txt','r+')
        con = fw.readlines()
        open('yts_magnet.txt','w').close()
        fw = open('yts_magnet.txt','w+')

        for run in tmp_list:
            if len(tmp_list) > 1:

                fw.write(run)

            else:
                for hj in con:
                    fw.write(hj)
                print("Your List is up to date \nExiting yts.py")
                time.sleep(3)
                os.system('taskkill  /f /im  py.exe')
        fw = open('yts_magnet.txt','a')

        for hj in con:

            fw.write(hj)
        print('Last Magnet Reached')
        time.sleep(5)
        os.system('taskkill  /f /im  py.exe')
        fw.close()


for i in range(1,2000):  #why 2000? just because
    print("\n\n{}\n\n".format(i))
    def first_page(source , soup):

        for movie_link in soup.find_all('a',class_='browse-movie-link', href=True):
            link_visit = movie_link['href']
            source1 = requests.get(link_visit).text
            soup1 = BeautifulSoup(source1,features='html.parser')
            try:
                magnet_link = soup1.find('a',class_='magnet-download download-torrent magnet',href=True)
            except:
                magnet_link = "NO MAGNET LINK FOUND"
            try:
                print_data = "\n\nmovie-->{}\n{}".format(link_visit,magnet_link)
                no_time_to_think_about_new_variable = magnet_link['title']
                tmp_list.append(print_data)
                check(no_time_to_think_about_new_variable,last)
            except:
                print("Error at magnet link side")
            try:
                #no_time_to_think_about_new_variable = magnet_link['href']
                print(no_time_to_think_about_new_variable)
                #print('\n' + print_data)
            except:
                print("NONE")

    source = requests.get("https://yts.lt/browse-movies?page={}".format(i)).text
    soup = BeautifulSoup(source,features='html.parser')

    if source == "":
        print('end of the line mate\nBYE BYE ')
        fw.close()
        time.sleep(5)
        os.system('taskkill  /f /im  yts.exe')


    #print("Error with Get Requests")
    first_page(source ,soup)
