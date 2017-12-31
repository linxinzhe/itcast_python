# -*- coding:utf-8 -*-
import requests
import bs4

blog_list = []
page_range = range(1, 178)
# page_range = range(1, 3)
page = 1
for page in page_range:
    html = requests.get("http://www.matrix67.com/blog/page/" + str(page))
    bs_html = bs4.BeautifulSoup(html.text)
    blog_list.extend(bs_html.select("h1 a"))

html_head = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
"""
html_footer = """
</body>
</html>
"""
with open("matrix67.html", "w", encoding="utf-8") as f:
    f.write(html_head)
    for blog in blog_list:
        f.write(str(blog) + "<br/>\n")
    f.write(html_footer)
