from pprint import pprint
def custom_write(file_name, strings):
    with open(file_name, 'a+', encoding='utf8') as file:
        num_line = int()
        num_byte = int()
        returned_dict = {}
        file.seek(0)
        _fl = file.readlines()
        if len(_fl) == 0:
            file.seek(0)
            num_line = 1
            num_byte = 0
        else:
            num_line = len(_fl) + 1
            num_byte = file.tell()
            file.seek(num_byte)
        for l in strings:
            returned_dict[(num_line, num_byte)] = l
            file.write(l + '\n')
            num_byte = file.tell()
            num_line = num_line + 1
        return returned_dict


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
