Dict = {}
print("Empty Dictionary: ")
print(Dict)

Dict = {1: 'Hour', 2: 'Of', 3: 'Code'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)

Dict = {'Name': 'HourOfCode', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)

Dict = dict({1: 'Hour', 2: 'Of', 3: 'Code'})
print("\nDictionary with the use of dict(): ")
print(Dict)

Dict = dict([(1, 'Hour'), (2, 'Of')])
print("\nDictionary with each item as a pair: ")
print(Dict)

Dict = {1: 'Hour', 'name': 'Of', 3: 'Code'}
print("Accessing a element using key:")
print(Dict['name'])
print("Accessing a element using get:")
print(Dict.get(3))