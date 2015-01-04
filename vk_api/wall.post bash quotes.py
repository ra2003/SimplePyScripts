import vk_api
import sys
import requests
from grab import Grab
import time
import urllib.parse

__author__ = 'ipetrash'


# Скрипт получает цитату с сайта bash.im и помещает ее на стену пользователя vk.com
# The script receives a quote from the site bash.im and puts it on the wall by vk.com


def unescape(s):
    s = s.replace("&lt;", "<")
    s = s.replace("&gt;", ">")
    s = s.replace("&quot;", '"')
    s = s.replace("&apos;", "'")
    s = s.replace("&amp;", "&")
    return s


def bash_quote():
    rs = requests.get('http://bash.im/random')
    g = Grab(rs.text)

    quote = g.doc.select('//div[@class="quote"]')

    html_quote = quote.select('div[@class="text"]').html()

    quote_text = html_quote.replace('<div class="text">', '').replace('</div>', '')
    quote_text = unescape(quote_text)
    quote_text = quote_text.replace('<br>', '\n').strip()

    quote_href = quote.select('div/a[@class="id"]').attr('href')
    quote_href = urllib.parse.urljoin('http://bash.im/', quote_href)

    return quote_text, quote_href


if __name__ == '__main__':
    # Логин и пароль к аккаунту и id человека, на стену которого будем постить сообщения
    login, psw, owner_id = 'USER_LOGIN', 'USER_PASSWORD', 'OWNER_ID'

    try:
        vk = vk_api.VkApi(login, psw)  # Авторизируемся
    except vk_api.AuthorizationError as error_msg:
        print(error_msg)  # В случае ошибки выведем сообщение
        sys.exit()

    while True:
        # Получаем текст цитаты и ее адрес
        quote_text, quote_href = bash_quote()

        # Добавление сообщения на стену пользователя id равным OWNER_ID
        # Если не указывать owner_id, сообщения себе на стену поместится
        rs = vk.method('wall.post', {
            'owner_id': owner_id,
            'message': quote_text,
            'attachments': quote_href,
        })
        print(rs, quote_href)

        time.sleep(60 * 60)  # Задержка в 1 час