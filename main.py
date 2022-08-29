import requests
# from pprint import pprint


def get_request():
    """this function return a list with hero's description in json format"""
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)  # делаем get запрос для получения данных о героях
    return response.json()  # возвращаем данные в json формате.


def get_three_hero_dict(hero_1, hero_2, hero_3):
    """this function return a dictionary with hero's name and value of intelligence"""
    super_list = get_request()
    three_dict = {}  # создаем пустой словарь для героев
    for hero_info in super_list:  # идем по json и по ключам выбираем значение интеллект, доб. в словарь
        if hero_info['name'] == hero_1.title():
            hero_1_intelligence = hero_info['powerstats']['intelligence']
            three_dict[hero_info['name']] = hero_1_intelligence
        elif hero_info['name'] == hero_2.title():
            hero_2_intelligence = hero_info['powerstats']['intelligence']
            three_dict[hero_info['name']] = hero_2_intelligence
        elif hero_info['name'] == hero_3.title():
            hero_3_intelligence = hero_info['powerstats']['intelligence']
            three_dict[hero_info['name']] = hero_3_intelligence
    return three_dict


def find_the_smartest(hero_1, hero_2, hero_3):
    """this function can find the smartest hero from a list"""
    three_hero_dict = get_three_hero_dict(hero_1, hero_2, hero_3)  # создаем словарь из трех героев.
    the_smartest = max(three_hero_dict.values())  # функция max для значений словаря (интеллект)
    for name, value in three_hero_dict.items():  # печатаем самого умного.
        if value == the_smartest:
            return f'Самый умный из троих - {name}. Очки его ума = {value}.'


if __name__ == '__main__':
    res = find_the_smartest('captain america', 'hulk', 'thanos')
    print(res)
