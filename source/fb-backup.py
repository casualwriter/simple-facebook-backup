from facebook_scraper import get_posts

fb_name  = 'mrleeyee'
fb_title = 'Mr. LeeYee'

f = open( fb_name+'.js', 'w', encoding='UTF-8' )

print( "var fbKey='" + fb_name + "', fbName = '" + fb_title + "'", file=f );
print( "var None=null, False=false, True=true", file=f )
print( "var posts=[], i=0", file=f );

#### if fb required login, use below code
#for post in get_posts( fb_name, pages=99, credentials=('youemail@gmail.com', '???') )
for post in get_posts( fb_name, pages=99 ):
  print( "posts[i++] = ", post, file=f)

