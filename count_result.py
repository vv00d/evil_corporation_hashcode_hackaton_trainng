
def check_likes(ingredients, likes_list):
    for ingredient in likes_list:
        if ingredient not in ingredients:
            return False
    return True

def check_dislikes(ingredients, dislike_list):
    for ingredient in likes_list:
        if ingredient in ingredients:
            return False
    return True

def is_client(ingredients, person):
    return check_likes(ingredients, person[0]) and check_dislikes(ingredients, person[1])

def get_result(ingredients, people):
    count = 0
    for person in people:
        if is_client(ingredients, person):
            count += 1
