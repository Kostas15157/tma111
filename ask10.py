
# coding: utf-8

# In[ ]:


#q4
from bs4 import BeautifulSoup#import beautiful soup library
import urllib2#used for  generation of GET query strings
import re

input_link=raw_input("Enter Link=")#only html pages 
html_page = urllib2.urlopen(input_link).read()
soup = BeautifulSoup(html_page)
for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    print link.get('href')
count_p=0
count_br=0
for linebreak in soup.findAll():#enable to find all tag
    if linebreak.name=='p':#only selects p tag
        count_p+=1
    if linebreak.name=='br':#only selects br tag
        count_br+=1
print "br tag in this page=",count_br
print "p tag in this page=",count_p

