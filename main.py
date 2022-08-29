import requests
# from pprint import pprint


def get_request():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)
    return response.json()


def get_three_hero_dict(hero_1, hero_2, hero_3):
    super_list = get_request()
    three_dict = {}
    for hero_info in super_list:
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
    three_hero_dict = get_three_hero_dict(hero_1, hero_2, hero_3)
    the_smartest = max(three_hero_dict.values())
    for name, value in three_hero_dict.items():
        if value == the_smartest:
            return f'Самый умный из троих - {name}. Очки его ума = {value}.'


if __name__ == '__main__':
    res = find_the_smartest('captain america', 'hulk', 'thanos')
    print(res)
