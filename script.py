import praw
from config_bot import *
from random import choice
from time import sleep
r=praw.Reddit(client_id=rid,client_secret=rsecret,user_agent=ua,password=REDDIT_PASS,username=REDDIT_USERNAME)
print(r.user.me())
sub=r.subreddit('GooglePorn')
with open('American.txt','r') as f:
    words=list(f)
while True:
    try:
        word=str(choice(words)).strip('\n').strip('\r')
        word2=list(word)
        word2=['+' if x==' ' else x for x in word2]
        word2=''.join(word2)
        word=list(word)
        word[0]=word[0].upper()
        word=''.join(word)
        title=word+' Porn'
        s=sub.submit(title,url='https://www.google.com/search?q='+word2+'+porn')
        s.reply("[Definition of \""+word+"\"](http://dictionary.com/browse/"+word+")")
        print('Posted '+title)
        sleep(0.5*60*60)
    except:
        r=praw.Reddit(client_id=rid,client_secret=rsecret,user_agent=ua,password=REDDIT_PASS,username=REDDIT_USERNAME)
