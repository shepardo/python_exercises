calories = {'apple' : 52, 'banana' : 89, 'choco' : 546}
print(calories['apple'] < calories['choco'])
calories['cappu'] = 74
print(calories['banana'] < calories['cappu'])
# False
print('apple' in calories.keys())
# True
print(52 in calories.values())
# True
for k, v in calories.items():
    print(k) if v > 500 else None
# 'choco'
