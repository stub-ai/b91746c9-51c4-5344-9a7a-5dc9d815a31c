import requests
from bs4 import BeautifulSoup

def get_book_info(title):
    base_url = "https://book.naver.com/search/search.nhn"
    params = {
        "query": title
    }

    response = requests.get(base_url, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')

    book_info = soup.find('div', class_='basic_info_area')
    if book_info:
        title = book_info.find('a', class_='N=a:bel.title').text.strip()
        author = book_info.find('a', class_='txt_name N=a:bel.author').text.strip()
        price = book_info.find('em', class_='price').text.strip()
        isbn = book_info.find('div', class_='book_info_inner').find_all('div')[3].text.split(':')[1].strip()

        print(f"Title: {title}")
        print(f"Author: {author}")
        print(f"Price: {price}")
        print(f"ISBN: {isbn}")
    else:
        print("No book found with the given title.")

if __name__ == "__main__":
    book_title = input("Enter the title of the book: ")
    get_book_info(book_title)