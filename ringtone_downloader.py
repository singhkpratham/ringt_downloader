import os
import re
from pathlib import Path
##os.chdir('/Users/ShazAka/Downloads/Understanding SSH')

import urllib.request
##urllib.request.urlretrieve('http://9xmasti.in/data/file/13338/.html?download',
##                           'test.mp3')

##a = str(urllib.request.urlopen(
##    'http://9xmasti.in/data/3474/MP3-Ringtones.html').read())
##
##b = str(urllib.request.urlopen(
##    'http://9xmasti.in/data/3475/Bollywood-Movie-Ringtones.html').read())
##
##c = str(urllib.request.urlopen(
##    'http://9xmasti.in/data/3476/A-to-Z-Movies-Ringtones.html').read())
##
##d = str(urllib.request.urlopen(
##    'http://9xmasti.in/data/3478/A---B---C.html').read())
##
##e = str(urllib.request.urlopen(
##    'http://9xmasti.in/data/3479/A.html').read())
##
##f = str(urllib.request.urlopen(
##    'http://9xmasti.in/data/11879/Aksar-2-2017-Movie-MP3-Ringtones.html').read())
##
##g = str(urllib.request.urlopen(
##    'http://9xmasti.in/data/file/11897/Aksar-2-Mohabbat-Karte-Rehna-Re-Mp3-Ringtone-mp3.html').read())

##re.findall('href=.{1,5}(http.{1,30}data\/\d{4,6}.{5,50}\.html)',a)

all_fld = set()
all_file = set()
def dwnld(link,dir_name=""):
    breakpoint()
    global all_fld,all_file
    dir_name = Path.cwd() if dir_name is None else Path.cwd()/dir_name
    dir_name.mkdir(exist_ok=True)
    src = str(urllib.request.urlopen(link).read())
    fld_links = set(re.findall('href=.{1,5}(http.{1,30}data\/\d{4,6}.{5,50}\.html)',src)).difference(all_fld)
    file_links = set(re.findall('href=.{1,5}(http.{1,30}data\/file\/\d{4,6}.{5,50}\.html)',src)).difference(all_file)
    all_fld = all_fld.update(fld_links)
    all_file = all_file.update(file_links)

    if file_links:
        for link in file_links:
            file_name = ''.join(re.findall( '\/([^\/]*?)\.html',link))
            urllib.request.urlretrieve(link+'?download',
                           dir_name/(file_name+'.mp3'))
            print(dir_name/(file_name+'.mp3'))
    
    for link in fld_links:
        folder_name = ''.join(re.findall( '\/([^\/]*?)\.html',link))
        new_path = Path.cwd()/dir_name/folder_name
        print(new_path)
        dwnld(link,new_path)
