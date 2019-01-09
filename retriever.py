from lxml import html
import requests
import time

page = requests.get("https://derpibooru.org")
treepage = html.fromstring(page.content)
time_start = time.time()
postamount_start = treepage.xpath("//span/strong/text()")
posts_start = postamount_start[2]

while 1:
    page = requests.get("https://derpibooru.org")
    treepage = html.fromstring(page.content)
    postamount = treepage.xpath("//span/strong/text()")
    posts = int(postamount[2])
    currtime = time.time()
    made_posts = posts - int(posts_start) 
    timepassed = float(currtime) - float(time_start)
    time_passed = round(timepassed, 3)
    datapoint = str(made_posts) + ", " + str(time_passed)
    print(datapoint)
    with open ("dataset", 'a') as dcmt:
        dcmt.write(str(datapoint))
        dcmt.write("\n"
        "")
    time.sleep(60)
