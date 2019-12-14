from bs4 import BeautifulSoup
import requests
import time
import sys
import os

tmp_list = []   #list to store magnet links
dir_files = []
error_lines2 = []
tmp_list2 = []
for files in os.listdir():
    dir_files.append(files)
    if files == 'error.txt':
        print(files)
        error_file = open('error.txt','r+')
        error_lines = error_file.readlines()
        i = error_lines[0]
        i = i[7]
        i = int(i)
        for ljokj in range(0,len(error_lines)):
            error_lines2.append(error_lines[ljokj].strip('\n'))
        error_lines.clear()
        for error_links in error_lines2[4:]:
            tmp_list.append(error_links)
        #############opti##########
        '''
        i1,i2,i3 = 0,0,1
        print(len(tmp_list))
        while True:
            if i1 <= len(tmp_list):
                try:
                    tmp_list2.append(tmp_list[i2] + tmp_list[i3])
                    #print(tmp_list2)
                    i1 = i1 + 1
                    i2 = i2 + 2
                    i3 = i3 + 2
                except:
                    break
        tmp_list = tmp_list2
        print(tmp_list2)
        '''
alshdjad = input()

try:
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
except:
    print('Check yts_magnet.txt')
    time.sleep(2)
    exit()

def check(no_time_to_think_about_new_variable,last):#check Function to check last magnet link
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
                os.system('del error.txt')
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
                print(no_time_to_think_about_new_variable)
            except:
                print("NONE")
    source = requests.get("https://yts.lt/browse-movies?page={}".format(i)).text
    soup = BeautifulSoup(source,features='html.parser')
    if source == "":
        print('end of the line mate\nBYE BYE ')
        fw.close()
        time.sleep(5)
        os.system('taskkill  /f /im  yts.exe')
    try:
        first_page(source ,soup)
    except:
        print('\n\nErrot Occured creating errror file\n\n')
        time.sleep(2)
        error_file = open('error.txt','w+')
        error_file.write('page = {}\n\n'.format(i))
        for magnet_link in tmp_list:
            error_file.write(magnet_link)
            print(magnet_link)
