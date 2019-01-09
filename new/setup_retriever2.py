from lxml import html
import time
import requests

page = requests.get("https://derpibooru.org")
treepage = html.fromstring(page.content)
postamount_start = treepage.xpath("//span/strong/text()")

post_start = postamount_start[2]
time_start = time.time()

with open ("settings/start_time", 'w') as dcmt:
    dcmt.write(str(time_start))

with open ("settings/start_post", 'w') as dcmt:
    dcmt.write(str(post_start))