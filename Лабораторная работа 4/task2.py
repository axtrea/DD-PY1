
def get_count_char(str_):
    dict_char = {}
    DEFAULT_COUNT = 0
    str_ = "".join(str_.split())
    str_ = str_.lower()
    for current_char in str_:
        if current_char.isalpha() == True:
            dict_char[current_char] = dict_char.get(current_char, DEFAULT_COUNT) + 1
    return dict_char
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
def al(dict_): # функция возвращает новый словарь, где кол-во элемента заменено на процентное соотношение ко всем символам
    b = sum(dict_.values())
    for current_char in dict_:
        dict_[current_char] = round(dict_.get(current_char) / b,3)
    return dict_
#print(al(get_count_char(main_str)))



