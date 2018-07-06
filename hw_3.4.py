import requests
from urllib.parse import urlencode

# Создайте страничку с помощью GitHub Pages.
# Установите счётчик.
# Реализуйте класс доступа к API Яндекс.Метрика, который принимает токен и предоставляет информацию о визитах, просмотрах и посетителях.

# Алгоритм решения:
# Создаем сайт, подключаем счетчик яндекс метрики  -- ВЫПОЛНЕНО --
# Получаем токен от нового приложения в яндекс Метрики -- ВЫПОЛНЕНО --
# Создаем класс YaMetrikaReports, который по примеру в лекции получает
# номер актуального счетчика и данные пр
# Зная номер счетчика получаем информацию о визитах, просмотрах и посетителях.


APP_ID = 'abb2f6ad43ae4298838a1a02b19f04e8'
APP_ID = 'abb2f6ad43ae4298838a1a02b19f04e8'
AUTH_URL = 'https://oauth.yandex.ru/authorize'

auth_data = dict(
    response_type='token',
    client_id=APP_ID
)

# print('?'.join((AUTH_URL, urlencode(auth_data))))
# Получили access_token=AQAAAAAoHhM3AAUYiy6WRE56oUX4nBwZ64SinqA


TOKEN1 = 'AQAAAAAoHhM3AAUYiy6WRE56oUX4nBwZ64SinqA'


class YaMetrikaReports():
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {'Authorization': 'OAuth {0}'.format(self.token)}

    # @property
    def counters(self):
        response = requests.get(
            'https://api-metrika.yandex.ru/management/v1/counters',
            headers=self.get_headers()
        )

        return [c['id'] for c in response.json()['counters']]

    def get_statistics(self):
        for counter in self.counters():
            response = requests.get(
                'https://api-metrika.yandex.ru/stat/v1/data?metrics={0}&id={1}&oauth_token={2}'.format(
                    'ym:s:visits,ym:s:users,ym:s:pageviews', counter, self.token)
            )
            return response.json()['totals']


ya_user_2 = YaMetrikaReports(TOKEN1)
visits, users, pageviews = ya_user_2.get_statistics() # Получили инфо о визитах, просмотрах и посетителях и сразу распаковали.
print('Всего {} визитов.'.format(int(visits)))
print('Всего {} посетителей.'.format(int(users)))
print('Всего {} просмотров.'.format(int(pageviews)))

