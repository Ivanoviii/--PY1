def get_count_char(str_):

    dct_ = {}
    str_ = str_.lower()

    for letter in str_:
       if letter.isalpha():
           if letter in dct_:
               dct_[letter] += 1
           else:
            dct_[letter] = 1
    return dct_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
