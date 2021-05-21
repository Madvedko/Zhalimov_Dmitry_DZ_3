thesaurus = ["Иван", "Мария", "Петр", "Илья"]

names_dict_set = dict()
names_dict_list = dict()

for name in thesaurus:
  first_letter = name[0].upper()
  names_dict_set[first_letter] = names_dict_set.setdefault(first_letter, set()) | {name.capitalize()}

print(names_dict_set)
