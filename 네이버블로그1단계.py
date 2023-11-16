import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

search_keyword = 'iPhone 15'

# create a new Excel workbook and select the active sheet
wb = Workbook()
ws = wb.active

# write the column names to the first row of the sheet
ws.append(["블로그명", "블로그주소", "글 제목", "포스팅 날짜"])

for page in range(1, 101):
    url = f'https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}&start={page * 10 - 9}'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    posts = soup.find_all('li', {'class': 'bx'})
    for post in posts:
        try:
            blog_address_elem = post.find("a", attrs={"class": "name"})            
            blog_address = blog_address_elem["href"]            
            blog_address_title_elem = post.find("a", attrs={"class": "name"})            
            blog_address_title = blog_address_title_elem.text
            blog_address_title.replace("\n","")
        except TypeError:
            blog_address = ""
            blog_address_title = ""

        post_date_elem = post.find('span', {'class': 'sub'})
        post_date = post_date_elem.text if post_date_elem else ""
        post_date.replace("\n","")
        post_title_elem = post.find('a', {'class': 'title_link _cross_trigger'})
        post_title = post_title_elem.text if post_title_elem else ""
        post_title.replace("\n","")

        print(blog_address)
        print(blog_address_title)
        print(post_title)
        print(post_date)

        ws.append([blog_address, blog_address_title, post_title, post_date])

# Save the workbook to a file
path = 'c:\\work\\'
file_path = f'{path}{search_keyword}_blog_data.xlsx'
wb.save(file_path)
