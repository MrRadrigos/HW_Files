with open('recipe.txt', 'r', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish_name = line.strip()
        dish_count = int(f.readline())
        ingredients = []
        for i in range(dish_count):
            ing = f.readline().strip()
            name, qnt, measure = ing.split(' | ')
            ingredients.append({
                'ingredient_name': name,
                'quantity': qnt,
                'measure': measure,
            })
        f.readline()
        cook_book[dish_name] = ingredients


# print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    dict_dishes = {}
    for dish in cook_book:
        if dish in dishes:
            for ingr in cook_book[dish]:
                ingr['quantity'] *= person_count
                tmp_dict = ingr.pop('ingredient_name')
                dict_dishes[tmp_dict] = ingr
    return dict_dishes


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
