def groupingDishes(dishes):
    dic = {}
    for dish in dishes:
        dish_name = dish[0]
        for ingredient in dish[1:]:
            if ingredient not in dic:
                dic[ingredient] = set()
            dic[ingredient].add(dish_name)


    res = []
    for key in keys:
        temp = []
        temp.append(key)
        temp += list(dic[key])
        res.append(temp)

    return res

dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
            ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
            ["Quesadilla", "Chicken", "Cheese", "Sauce"],
            ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]

groupingDishes(dishes)