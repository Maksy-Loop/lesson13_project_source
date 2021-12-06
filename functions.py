import json

def search_unique_tag(jsonefile):
    """
    функция перебирает спикой словарей и ищет в них слова с #
    после чего выводит список этих слов без #
    :param jsonefile: list whith elements dict
    :return: set
    """
    with open(jsonefile, "r") as file:
        post_list = json.load(file)

    list_tags = set()
    for dict in post_list:
        content = dict["content"]
        content = content.split(" ") #разбиваем текст поста на слова по пробелу

        #перебираем все слова каждого поста, если там есть # то формируем список слов без любых символов
        for word in content:
            if word.startswith("#"):
                #тут мы перебираем буквы каждого слова, если есть спец символы их удаляем
                list_tags.add("".join([letter.lower() for letter in word if letter.isalnum()]))

    return list_tags


def is_tag(jsonefile, tag):
    """
    функция отбирает в списке словари где есть теги
    :param jsonefile:
    :param tag:
    :return: list  возвращает список словарей
    """
    with open(jsonefile, "r") as file:
        post_list = json.load(file)
    hashtag = f'#{tag}'
    post_with_tags = [post for post in post_list if hashtag.lower() in post.get("content").lower()  and hashtag != "#"]

    return post_with_tags


def add_value(dict, jsonfile):
    """
    функция добавляес словарь в список, который храниться в json файле в виде словаря
    :param dict:
    :param json:
    :return: bool
    """
    with open(jsonfile, "r") as f:
        list_date = json.load(f)

    list_date.append(dict)

    with open(jsonfile, "w") as f:
        json.dump(list_date, f, ensure_ascii=False, indent=4)

    return True
