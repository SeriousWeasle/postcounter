from lxml import html
import requests
import time

with open ("settings/start_time", 'r') as readStartTime:
    start_time = readStartTime.read()

with open ("settings/start_post", 'r') as readStartPost:
    start_posts = readStartPost.read()

while 1:
    for i in range (0, 60):
        page = requests.get("https://derpibooru.org")
        treepage = html.fromstring(page.content)
        postamount = treepage.xpath("//span/strong/text()")
        posts = int(postamount[2])
        currtime = time.time()

        made_posts = posts - int(start_posts)
        time_passed = float(currtime) - float(start_time)
        datapoint = str(made_posts) + ", " + str(time_passed)
        print(datapoint)
        
        if i == 0:
            with open ("output/dataset_60s", "a") as dcmt:
                dcmt.write(str(datapoint))
                dcmt.write("\n"
                "")
            
            with open ("output/dataset_60m", "a") as dcmt:
                dcmt.write(str(datapoint))
                dcmt.write("\n"
                "")
        
        else:
            with open ("output/dataset_60s", "a") as dcmt:
                dcmt.write(str(datapoint))
                dcmt.write("\n"
                "")
        
        i += 1
        time.sleep(60)