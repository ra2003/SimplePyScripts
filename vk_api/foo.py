import sys
import time
import datetime

import vk_api


__author__ = 'ipetrash'


# https://github.com/python273/vk_api
# https://vk.com/dev/methods


def vk_auth(login, password):
    try:
        vk = vk_api.VkApi(login, password)  # Авторизируемся
    except vk_api.AuthorizationError as error_msg:
        print(error_msg)  # В случае ошибки выведем сообщение
        sys.exit()

    return vk


LOGIN = ''
PASSWORD = ''


if __name__ == '__main__':
    # Авторизируемся
    vk = vk_auth(LOGIN, PASSWORD)



    def vk_bdate_to_bdate_this_year(bdate):
        # bdate может быть в формате: %d.%m.%Y или %d.%m
        parts = bdate.split('.')
        d, m, y = int(parts[0]), int(parts[1]), datetime.datetime.today().year
        return datetime.date(y, m, d)


    # Получим и выведем списк друзей с указанными днями рождения
    rs = vk.method('friends.get', {'fields': 'bdate'})

    for i, friend in enumerate(rs.get('items'), 1):
        id_user = friend.get('id')
        first_name = friend.get('first_name')
        last_name = friend.get('last_name')
        bdate = friend.get('bdate')
        if bdate:
            # Дата дня рождения в текущем году
            birthday_this_year = vk_bdate_to_bdate_this_year(bdate)

            # Сколько осталось дней до дня рождения
            remained_days = birthday_this_year - datetime.datetime.today().date()
            remained_days = remained_days.days

            if remained_days > 0:
                print(str(i) + ". " + "id" + str(id_user) + "  " + first_name + " " + last_name
                      + " до дня рождения осталось: " + str(remained_days) + " дней")



    # # Написание сообщения пользователю с id=170968205 на стену:
    # rs = vk.method('wall.post', {'owner_id': '170968205', 'message': message})
    # print(rs)



    # # Написание сообщения пользователю с id=170968205 в диалог:
    # rs = vk.method('messages.send', {'user_id': '170968205', 'message': paste_url})
    # print(rs)



    # rs = vk.method('friends.get')
    # # rs = vk.method('friends.get', {'user_id': '59628698'})
    #
    # print("Всего друзей: {}".format(rs['count']))
    #
    # friends = [str(i) for i in rs['items']]
    #
    # rq_params = {
    #     'user_ids': ','.join(friends),
    #     'fields': 'relation'
    # }
    #
    # rs = vk.method('users.get', rq_params)
    # # print(rs)
    #
    # for i, f in enumerate(rs, 1):
    #     print(i, f)


    # ## Получение инфы о пользователе
    # # Получение инфы о текущем пользователе
    # rs = vk.method('users.get')
    #
    # # # Получение больше инфы о текущем пользователе
    # # rs = vk.method('users.get', {'fields': 'sex, city, online, screen_name'})
    #
    # # # Получение инфы о пользователе creeddevilmaycry
    # # rs = vk.method('users.get', {'user_ids': 'creeddevilmaycry'})
    # print(rs)


    # rs = vk.method('utils.getServerTime')
    # print(rs)


    # # # Получение инфы о пользователе
    # rs = vk.method('users.get', {'user_ids': 'arthur_iskuzhin'})
    # print(rs)


    # # # Получение инфы о пользователе или приложении по короткому имение
    # rs = vk.method('utils.resolveScreenName', {'screen_name': 'arthur_iskuzhin'})
    # print(rs)



    ## Печатаем текст последнего поста со стены
    # values = {
    #     'count': 1  # Получаем только один пост
    # }
    # response = vk.method('wall.get', values)  # Используем метод wall.get
    #
    # if response['items']:
    #     # Печатаем текст последнего поста со стены
    #     print(response['items'][0]['text'])


    # # Получение статуса
    # # http://vk.com/dev/status.get
    # rs = vk.method('status.get')
    # print(rs)
    #
    # # Установка статуса
    # # http://vk.com/dev/status.set
    # rs = vk.method('status.set', {'text': '*Задумал злобный план*'})
    # print(rs)


    # ## Написание сообщения на стену
    # # Написание сообщения себе на стену:
    # response = vk.method('wall.post', {'message': 'Hello World! Привет Мир!'})
    # print(response)
    #
    # # Написание сообщения пользователю с id=170968205 на стену:
    # response = vk.method('wall.post', {'owner_id': '170968205', 'message': 'Даров, чувак!'})
    # print(response)


    # rs = vk.method('wall.post', {
    #     'owner_id': '123810316',
    #     'message': 'vk_api!',
    #     # 'attachments': 'http://doghusky.ru/wp-content/uploads/2012/02/Siberian-Husky-Puppy-Photo_002-600x375.jpg',
    # })
    # print(rs)


    # rs = vk.method('wall.post', {
    #     # 'owner_id': '4033640',
    #     # 'message': 'Щенята!',
    #     'attachments': 'http://bash.im/quote/144613',
    # })
    # print(rs)