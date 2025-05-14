def add(a,  *b):
    c = a
    for i in b:
        c += i
    print(f"C: {c}")

add(20, 15, 2, 12, 3, 1)

def person(name, **data):
    for key,value in data.items():
        print(key, value)

person("Ahmad", age=19, city='lagos', mobile=+2349123852253)