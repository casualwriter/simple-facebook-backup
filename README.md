### Description

`simple-facebook-backup` is a simple html/js program to represent the facebook posts into a static web site. 

first, please use [facebook-scraper](https://pypi.org/project/facebook-scraper/) to backup facebook posts int a **javascript file**, 
then simple upload the index.html with the javascript file to web-hosting, a static web site is ready.

**Features**

* a single html file ([index.html](index.html)) in 115 lines
* vanilla JS, without any dependance
* support multiple facebook accounts (by #account-name)
* mobile support with responsive design

### How to use

For example, to backup the facebook posts of https://www.facebook.com/mrleeyee

1. install [facebook-scraper](https://pypi.org/project/facebook-scraper/) from https://pypi.org/project/facebook-scraper/
2. create/revise python script mrleeyee.py, like below

~~~
from facebook_scraper import get_posts

f = open('mrleeyee.js','w',encoding='UTF-8')

for post in get_posts('mrleeyee', pages=999):
  print(post, file=f)
~~~

3. run script fb-mrleeyee.py to backup posts to file fb-mrleeyee.js
4. upload to web-hosting (e.g. https://casualwriter.github.io/facebook)

then a static web site is ready on https://casualwriter.github.io/facebook/#mrleeyee

### Sample Sites

**Hosted on github-page**
* backup for facebook.com/mrleeyee: https://casualwriter.github.io/facebook/#mrleeyee
* backup for facebook.com/nganshunkau: https://casualwriter.github.io/facebook/#nganshunkau

**Self-hosted on github**

As github account can be directly accessed as a web page by githack or RawGit, so it is self-hosted. 

* gitHack for fb:mrleeyee: https://raw.githack.com/casualwriter/simple-facebook-backup/main/#mrleeyee
* gitHack for fb:nganshunkau: https://raw.githack.com/casualwriter/simple-facebook-backup/main/#nganshunkau



### Modification History

* 2022/01/18 v0.50, initial version 
