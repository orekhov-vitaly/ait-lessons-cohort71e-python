def can_bay_groceries(is_lidl_open, is_kaufland_open):
    return is_lidl_open or is_kaufland_open


is_lidl_open = True
is_kaufland_open = True
print("Можно ли сейчас купить продукты -", can_bay_groceries(is_lidl_open, is_kaufland_open))

is_lidl_open = True
is_kaufland_open = False
print("Можно ли сейчас купить продукты -", can_bay_groceries(is_lidl_open, is_kaufland_open))

is_lidl_open = False
is_kaufland_open = True
print("Можно ли сейчас купить продукты -", can_bay_groceries(is_lidl_open, is_kaufland_open))

is_lidl_open = False
is_kaufland_open = False
print("Можно ли сейчас купить продукты -", can_bay_groceries(is_lidl_open, is_kaufland_open))