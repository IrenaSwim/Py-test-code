data = {}
while True:
    info = input('Type your user name, age and position via gaps or enter "stop" ').lower
    if info == 'stop':
        break
    else:
        info_list = info.split()
        for key in data.keys():
            if key == info_list[0]:
                new_name = input('This user name is occupied. Please, enter another one ').lower
                info_list[0] = new_name
                break
            