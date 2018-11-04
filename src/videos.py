import random


def get_random(cache):
    try:
        video_id = random.choice(list(cache['videos'].keys()))
        if video_id:
            return 'https://youtu.be/' + video_id
    except IndexError:
        print('Videos dict is empty')


x = get_random({'videos': {'test1': {'id_1': 'test_1', 'id_2': 'test_2'}, 'test2': {'id_3': 'test_3', 'id_4': 'test_4'}}})
print(x)