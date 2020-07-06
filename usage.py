from decorator import logger

path = input()

@logger(path)
def adv_print(*args, **kwargs):
    text = list(*args)
    for key, value in kwargs.items():
        if key == 'start':
            start_offset = 0
            for letter in value:
                text.insert(start_offset, letter)
                start_offset += 1
        if key == 'max_line':
            max_line_offset = value
            while len(text)>value:
                text.insert(value, '\n')
                value+=max_line_offset
        if key == 'in_file':
            if value == True:
                with open('test.txt', 'w', encoding='utf-8') as file:
                    file.write(''.join(text))
  print(''.join(text))
