
# 11월 1일 쪽지 시험 보겠다. (정규화) - 과제점수에 반영

#설치는 python -m pip install beatifulsoup4 로 설치


from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urljoin

## html 파싱 예제 

#html_doc= """
#<html><head><title>The Dormouse's story</title></head>
#<body>
#<p class="title"><b>The Dormouse's story</b></p>
#<p class="story">Once upon a time there were three little sisters; and their names were
#<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
#<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
#<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
#and they lived at the bottom of a well.</p>
#<p class="story">...</p>
#"""

#soup = BeautifulSoup(html_doc, "html.parser") # 두번째 인자는 파서종류, 디폴트가 html parser
##print(soup.prettify())
##print(soup.title.prettify()) # 태그명을 지정해서 찾을 수 있다.
##print(soup.title.string) # 태그명의 아이템 값을 얻을 수 있다.
##print(soup.p['class']) # 태그의 애트리뷰트 값도 가져올수 있다.(가장 먼저 나오는 값을 가져옴)
##print(soup('a',{'id':'link1'})[0].contents) #태그의 애트리뷰트 값을 알면 해당 값을 가져올 수 있다.
#print(type(soup.find_all(id='link1'))) #리스트가 아닌 bs4의 result set이다.

## 웹사이트 파싱 예제 
#import webbrowser
#url = "http://comic.naver.com/webtoon/list.nhn?titleId=20853"

#data = urlopen(url)
#soup = BeautifulSoup(data,'html.parser')
#print(soup.title.string) # title 태그의 item을 가져옴
##cartoons = soup.find_all('td', {'class' : 'title'}) #td 로 되어있는 태그의 class가 title인 것들을 가져온다.

##for i in range(len(cartoons)):
##    title = cartoons[i].find('a').string
##    ref = cartoons[i].find('a')['href']
##    tempurl= urljoin(url, ref)
##    print(title, "\t" , tempurl)
##    #webbrowser.open_new(tempurl)

##웹 크롤러 만들기 예제

class crawler:
    def crawl(self, pages, depth=2):
        for i in range(depth):
            newpage= set()
            for page in pages:
                try:
                    c = urlopen(page)
                except:
                    print("Could not open %s" % page)
                    continue
                soup = BeautifulSoup(c.read(), 'html.parser')
                print('Found %s' % page)
                
                links = soup('a')
                for link in links:
                     if('href' in dict(link.attrs)):
                        url= urljoin(page, link['href'])
                        if url.find("'")!=-1 : continue
                        url= url.split("#")[0]
                        if url[0:4]=='http':
                            newpage.add(url)
                pages = newpage

pagelist=['http://www.naver.com']
crawler=crawler()
crawler.crawl(pagelist)
print(pagelist)
