import itertools

def info_store(input_str):
    info_list = input_str.split()
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
print()
for key, value in data.items():
    print(f'Сотрудник {value[0]}: идентификатор {key}, возраст {value[1]}, должность {value[2]}')

