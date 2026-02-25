import itertools

def info_store(input_str):
    info_list = info_store.split()
    return info_list

data = {}
inf_gen = (x for x in itertools.count())

while True:
    user = input('Введите имя, возраст и профессию через пробел ')
    if user == 'stop':
        break
    else:
        user_info = info_store(user)
        data.setdefault(next(inf_gen), user_info)

for key, value in data.items():
    print(f'Идентификатор {value[0]}: {key}')