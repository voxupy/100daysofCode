n = int(input())


for x in range(n):
    if x % 5 and x % 7:
        print('FooBar')
    elif x % 5:
        print("Foo")
    elif x % 7:
        print("Bar")
    else:
        print(x)