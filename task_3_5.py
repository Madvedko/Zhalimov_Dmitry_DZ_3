from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

"""Реализованная функция get_jokes(), возвращающая n шуток, сформированные из трех случайных слов, взятых из трёх списков"""

def get_jokes(n):
    for i in range(n):
        random = choice(nouns)
        random_1 = choice(adverbs)
        random_2 = choice(adjectives)
        joke = f'{random}, {random_1}, {random_2}'
        print(joke)




get_jokes(2)
