# (name, $-income)
customers = [("John", 240000),
("Alice", 120000),
("Ann", 1100000),
("Zach", 44000)]
# your high-value customers earning >$1M
whales = [x for x,y in customers if y>1000000]
print(whales)
# ['Ann']