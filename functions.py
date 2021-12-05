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

    list_tags = []
    for i in post_list:
        j = i["content"]
        j = j.split(" ") #разбиваем текст поста на слова по пробелу

        #перебираем все слова каждого поста, если там есть # то формируем список слов без любых символов
        for k in j:
            if "#" in k:
                list_tags.append("".join([letter.lower() for letter in k if letter.isalnum()]))
    #удаляем дубликаты
    list_tags = set(list_tags)

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



#print(is_tag("posts.json", "кот"))