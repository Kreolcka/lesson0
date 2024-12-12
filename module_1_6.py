#phone_book = {'Olga': 89773664758, 'Max': 89768465738}
#phone_book['Olga'] = 939374747
#phone_book['Robby'] = 988483948
#print(phone_book['Robby'])
#print(phone_book)
#del phone_book['Max']
#print(phone_book)
#phone_book.update({'Denis': 474747474,
#                  'Nata': 6666677777,
#                  'Kim': 30494949})
#print(phone_book.get('Lisiy', 'Такого ключа нет'))
#r = phone_book.pop('Robby')
#print(r)
#print(phone_book.keys())
#print(phone_book.values())
#print(phone_book.items())
#set_ = {1, 2, 3, 4, 5, 1, 2, 3, 'Johe', True, (4, 3, 4)}
#print(set_)
#list_ = [1, 3, 3, 1, 4, 5, 4]
#list_ = set(list_)
#print(list_)
#print(list_.remove(5))
#print(list_)
#print(list_.add(7))
#print(list_)


my_dict = {'Vobla': 1990, 'Lesh': 2023, 'Kambala': 2012, }
print('Dict:', my_dict)
print('Existing value:', my_dict.get('Kambala'))
print('Not existing value:', my_dict.get('Bro', 'здесь нет братьев, только рыба'))
my_dict.update({'Skumbria': 1780,
                'Putasu': 2015})
print(my_dict)
l = my_dict.pop('Lesh')
print('Deleted value:', l)
print('Modified dictionary:', my_dict)

my_set = {2, 2, 5, 7, 9, 7, 9, 12, 'Kilka', False, 2.0 }
print('Set:', my_set)
my_set.add('Akula')
my_set.add(90)
my_set.add('Akula')
my_set.remove(False)
print('Modified set:', my_set)