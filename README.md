### Description

`simple-facebook-backup` is a simple html/js program to represent the facebook posts into a static web site. 

first, please use [facebook-scraper](https://pypi.org/project/facebook-scraper/) to backup facebook posts int a **javascript file**, 
then simple upload the index.html with the javascript file to web-hosting, a static web site is ready.

**Features**

* single html file ([index.html](source/index.html)) in 118 lines
* vanilla JS, without any dependance
* support multiple facebook accounts (by #account-name)
* mobile support with responsive design
* content searchable
* nice printout

### How to use

For example, to backup the facebook posts of https://www.facebook.com/mrleeyee

1. install [facebook-scraper](https://pypi.org/project/facebook-scraper/) from https://pypi.org/project/facebook-scraper/
2. open and revise python script fb-backup.py, simple revise the facebook name and title

~~~
from facebook_scraper import get_posts

fb_name  = 'mrleeyee'
fb_title = 'Mr. LeeYee'

f = open( fb_name+'.js', 'w', encoding='UTF-8' )

print( "var fbKey='" + fb_name + "', fbName = '" + fb_title + "'", file=f );
print( "var None=null, False=false, True=true", file=f )
print( "var posts=[], i=0", file=f );

#### if fb required login, use below code
#for post in get_posts( fb_name, pages=99, credentials=('youemail@gmail.com', '???') )
for post in get_posts( fb_name, pages=99 )
  print( "posts[i++] = ", post, file=f)
~~~

 

3. run script fb-fb-backup.py to backup posts to file `{fb_name}.js`
4. upload to web-hosting (e.g. https://casualwriter.github.io/facebook)

then a static web site is ready on https://casualwriter.github.io/facebook/#mrleeyee

### Sample Sites

**Hosted on github-page**
* backup for facebook.com/mrleeyee: https://casualwriter.github.io/facebook/#mrleeyee
* backup for facebook.com/nganshunkau: https://casualwriter.github.io/facebook/#nganshunkau
* backup for facebook.com/nganshunkau: https://casualwriter.github.io/facebook/#epinoia2020

**Self-hosted on github**

As github source can be directly accessed as a web page by githack or RawGit, so it is self-hosted. 

* gitHack for fb:mrleeyee: https://raw.githack.com/casualwriter/simple-facebook-backup/main/source/index.html#mrleeyee
* gitHack for fb:nganshunkau: https://raw.githack.com/casualwriter/simple-facebook-backup/main/source/#nganshunkau
* gitHack for fb:epinoia2020: https://raw.githack.com/casualwriter/simple-facebook-backup/main/source/#epinoia2020


### Modification History

* 2022/01/18 v0.50, initial version
* 2022/03/31 v0.60, cater multiple facebook accounts.
