def full_name(first, last):
    name = f'{first} {last}'
    return name


name = full_name('John', 'Doe')

print(name)

def famous_name(first,last,title,**addition):
    name = f'{title=} {first} {last} {addition}'
    return name

    name = famous_name(first='John', last='Doe', title='Mr.', addition='Jr.')

    print(name)