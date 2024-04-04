print("===Global Scope===")

x = 'text global'

def foo():
    print(x)

foo()
print(x)

print("===local Scope===")

def test_local_scope():
    n = 99 # variabel local
    print(n)

# print(n) # error n is not defined

test_local_scope()

print("===GLobal and Local Scope===")

point = 10
score = 0

def tambah_score():
    global score
    global point
    score += 1
    point += 10
    print('score : ', score)
    print('point : ', point)

tambah_score()
tambah_score()
tambah_score()
print(score)
print(point)

print("===Overlapping Variable===")

a = 8 # global variable

def my_function():
    a = 23 # local variable
    print('local', a)

print('global', a)
my_function()

