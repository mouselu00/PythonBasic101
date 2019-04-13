# lib import
import urllib.request as req
# import beautiful suoup to resutructure the html plan code to batter code view
import bs4

# set url (target website link)
url =  "https://www.ptt.cc/bbs/NBA/M.1552012857.A.A2F.html"

# create a request object, set the request Header info (the taget website header information)
request = req.Request(url , headers  = {
# set target webiste user-agent
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"

})

# request the target website and set to "response" object 
with req.urlopen(request) as response:
# use the object method "read" to read the website structure and set to data variable
# the website decode format set to utf-8
    data = response.read().decode("utf-8")

# print out the html structure
# use to test success to fatch website structure
# print(data)

# restructure plan html code to readable and become a objected
root = bs4.BeautifulSoup(data , "html.parser")

# print out the html tag
print(root.title)
# print out the html tag title content
print(root.title.string)

# finding target content with html tag and class parent and children tag
targetValue = root.find("a" , class_  =  "board")
print(targetValue) # <a class="board" href="/bbs/NBA/index.html">返回看板</a>
# get targetValue children tag
print(targetValue.span)
# get targetValue children tag content
print(targetValue.span.string)

# find all the tag with "find_all"
listRoot = root.find_all("span" , class_="push-content")
# print(lists)
for listValue in listRoot:
# if listValue contain a content and none dalete
    if listValue !=  None:
        print(listValue.string)