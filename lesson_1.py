'''Каждое из слов «разработка», «сокет», «декоратор» представить в строковом
 формате и проверить тип и содержание соответствующих переменных. Затем с помощью
 онлайн-конвертера преобразовать строковые представление в формат Unicode и также
 проверить тип и содержимое переменных.
'''

import locale
import subprocess
words: list = ["разработка", "сокет", "декоратор"]


for word in words:
    print(f'Тип переменной: {type(word)}')
    print(f'Содержимое переменной: {word}')
    print(f'Длина перменной: {len(word)}')
    print("*"*25)


words_UC: list = [
    b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0',
    b'\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82',
    b'\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80'
]

for word in words_UC:
    print(f'Тип переменной: {type(word)}')
    print(f'Содержимое переменной: {word}')
    print(f'Длина перменной: {len(word)}')
    print("*"*25)

'''Каждое из слов «class», «function», «method» записать в байтовом типе
 без преобразования в последовательность кодов 
 (не используя методы encode и decode) и определить тип, содержимое и длину
  соответствующих переменных.
'''

words: list = [b"class", b"function", b"method"]

for word in words:
    print(f'Тип переменной: {type(word)}')
    print(f'Содержимое переменной: {word}')
    print(f'Длина перменной: {len(word)}')


'''Определить, какие из слов «attribute», «класс», «функция», «type» 
невозможно записать в байтовом типе'''

# var2 = b'attribute'
# var3 = b'класс'
# var4 = b'функция'
# var5 = b'type'

"""невозможно преобразовать строки с Кириллицей - вылетает исключение"""

'''Преобразовать слова «разработка», «администрирование», «protocol»,
 «standard» из строкового представления в байтовое и выполнить обратное
  преобразование (используя методы encode и decode).'''

words: list = ['разработка', 'администрирование', 'protocol', 'standard']
for i in words:
    a = i.encode('utf-8')
    print(a, type(a))
    b = bytes.decode(a, 'utf-8')
    print(b, type(b))
    print('#'*15)


'''Выполнить пинг веб-ресурсов yandex.ru, youtube.com 
и преобразовать результаты из байтовового в строковый тип на кириллице'''
print('#'*30)


ping_resource: list = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]

for ping_now in ping_resource:

    ping_process = subprocess.Popen(ping_now, stdout=subprocess.PIPE)

    i = 0

    for line in ping_process.stdout:

        if i < 10:
            print(line)
            line = line.decode('cp866').encode('utf-8')
            print(line.decode('utf-8'))
            i += 1
        else:
            print('#'*30)
            break

'''Создать текстовый файл test_file.txt, заполнить его тремя строками: 
«сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию. Принудительно открыть файл
в формате Unicode и вывести его содержимое'''


resource_string = ['сетевое программирование', 'сокет', 'декоратор']

# Создаем файл
with open('resourse.txt', 'w+') as f_n:
    for i in resource_string:
        f_n.write(i + '\n')
    f_n.seek(0)

print(f_n)  # печатаем объект файла, что бы узнать его кодировку

file_coding = locale.getpreferredencoding()

# Читаем из файла
with open('resourse.txt', 'r', encoding=file_coding) as f_n:
    for i in f_n:
        print(i)

    f_n.seek(0)
