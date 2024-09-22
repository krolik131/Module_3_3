def print_params(a=1, b='строка', c=True):
    print(a,b,c)

print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, 'Hello World', True]
values_dict = {'a' : 1, 'b' : 'Hello', 'c' : True}
print_params(**values_dict)

values_list_2 = [1, 'Hello man']
print_params(*values_list_2, 42)