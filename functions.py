import json

def search_unique_tag(text):
    """
    функция перебирает спикой словарей и ищет в них слова с #
    после чего выводит список этих слов без #
    :param text: list whith elements dict
    :return: set
    """
    with open(text, "r") as file:
        post_list = json.load(file)

    list_tags = []
    for i in post_list:
        j = i["content"]
        j = j.split(" ") #разбиваем текст поста на слова по пробелу

        #перебираем все слова каждого поста, если там есть # то вормируем список слов без любых символов
        for k in j:
            if "#" in k:
                list_tags.append("".join([letter for letter in k if letter.isalnum()]))
    #удаляем дубликаты
    list_tags = set(list_tags)

    return list_tags
