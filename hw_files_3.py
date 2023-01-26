import operator

dict_sum = {}
dict_text = {}


def name_files(name):
    with open(name, 'r', encoding='utf-8') as f:
        name_ = name
        sum_str = 0
        str_ = []
        for line in f:  # подсчет строк в файле
            sum_str += 1
            str_.append(line)
            dict_text[name] = str_
        return dict_sum.setdefault(name, sum_str)


name_files('1.txt')
name_files('2.txt')
name_files('3.txt')

sorted_dict = dict(sorted(dict_sum.items(), key=operator.itemgetter(1)))  # сортируем dict_text по значениям

with open('final.txt', 'w', encoding='utf-8') as f:
    for key, value in sorted_dict.items():
        name_f = f.write(f"{key}\n")
        values_str = f.write(f"{value}\n")
        for i in dict_text[key]:
            text = i.strip()
            f.write(f"{text}\n")

# print(dict_sum)
# print(dict_text)
# print(sorted_dict)
