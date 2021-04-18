

def fixed_string(str_ua):

    #словарь разрешенных символов

    symbol_map = {ord("А"): "A", ord("Б"): "B", ord("В"): "V",
                  ord("Г"): "H", ord("Ґ"): "G", ord("Д"): "D",
                  ord("Е"): "E", ord("Є"): "Ye", ord("Ж"): "Zh",
                  ord("З"): "Z", ord("И"): "Y", ord("І"): "I",
                  ord("Ї"): "Yi", ord("Й"): "Y", ord("К"): "K",
                  ord("Л"): "L", ord("М"): "M", ord("Н"): "N",
                  ord("О"): "O", ord("П"): "P", ord("Р"): "R",
                  ord("С"): "S", ord("Т"): "T", ord("У"): "U",
                  ord("Ф"): "F", ord("Х"): "Kh", ord("Ц"): "Ts",
                  ord("Ч"): "Ch", ord("Ш"): "Sh", ord("Щ"): "Shch",
                  ord("Ю"): "Yu", ord("Я"): "Ya", ord("а"): "а",
                  ord("б"): "b", ord("в"): "v", ord("г"): "h",
                  ord("ґ"): "g", ord("д"): "d", ord("е"): "е",
                  ord("є"): "ie", ord("ж"): "zh", ord("з"): "z",
                  ord("и"): "y", ord("і"): "i", ord("ї"): "i",
                  ord("й"): "i", ord("к"): "k", ord("л"): "l",
                  ord("м"): "m", ord("н"): "n", ord("о"): "o",
                  ord("п"): "p", ord("р"): "r", ord("с"): "s",
                  ord("т"): "t", ord("у"): "u", ord("ф"): "f",
                  ord("х"): "kh", ord("ц"): "ts", ord("ч"): "ch",
                  ord("ш"): "sh", ord("щ"): "shch", ord("ю"): "іu",
                  ord("я"): "ia", ord("ь"): "",
                  ord("1"): "1", ord("2"): "2", ord("3"): "3",
                  ord("4"): "4", ord("5"): "5", ord("6"): "6",
                  ord("7"): "7", ord("8"): "8", ord("9"): "9",
                  ord("0"): "0"}


    #создаем список разрешенных символов из ключей словаря
    allowed_symbols=[]
    for elem in symbol_map.keys():
        allowed_symbols.append(chr(elem))
    #--------------------

    #переводим элементы строки str_ua в список list_str_ua 
    list_str_ua=[]
    list_str_ua[:0]=str_ua
    #--------------
   
    
    #находим неразрешенные символы odd_symbols
    latin_alphabet=['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z']
    set_str_ua = set(list_str_ua)
    odd_symbols = set_str_ua - set(allowed_symbols).union(set(latin_alphabet))
    #---------------

    #добавляем в словарь неразрешенные символы 
    for i in odd_symbols:
        symbol_map[ord(i)] = '_'
    #---------------
    

    translated_string = str_ua.translate(symbol_map)
    return translated_string


if __name__ == "__main__":

    str_ua = input('Для транслітерації введіть текст на українській мові')

    print('Текст -->')   
    print(str_ua)
    print('-----------------------')
    
    print('Результат транслітерації -->')
    print(fixed_string(str_ua))
    print('-----------------------')


