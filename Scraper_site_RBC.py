# Импортируем библиотеки requests и BeautifulSoup
# Import the requests and BeautifulSoup libraries
import requests
from bs4 import BeautifulSoup

# Указываем URL сайта, который хотим распарсить
# Specify the URL of the website that we want to parse.
url = "https://www.rbc.ru/"

# Отправляем GET-запрос к указанному URL и сохраняем ответ в переменной response
# Send a GET request to the specified URL and save the response in the variable 'response'
response = requests.get(url)

# Создаем объект BeautifulSoup, передавая в качестве аргументов текст ответа и парсер
# Create a BeautifulSoup object, passing the response text and parser as arguments
soup = BeautifulSoup(response.text, "html.parser")

# Ищем все элементы a с классом main__feed__link на странице
# Find all 'a' elements with the class 'main__feed__link' on the page
articles = soup.find_all("a", class_="main__feed__link")

# Для каждого найденного элемента a извлекаем заголовок новости, используя метод find и указывая класс main__feed__title
# For each found 'a' element, extract the news headline using the find method and specifying the 'main__feed__title' class
for article in articles:
    title = article.find("span", class_="main__feed__title").text.strip()


    # Выводим заголовок на новость с помощью функции print
    # Output the news headline with the print
    print(title)

    # Добавляем пустую строку, чтобы отделить одну новость от другой
    # Add an empty line to separate one news from another
    print()

# Добавляем input() чтобы после выполнения скрипта
# окно командной строки не закрылось и ожидало нажатия клавиши Enter,
# тк скрипт будет запакован в .exe файл через утилиту pyinstaller

# Add input() so that the command line window doesn't close after the script execution
# and waits for the Enter key to be pressed. This is necessary because
# the script will be packaged into a .exe file using the pyinstaller utility

input()
