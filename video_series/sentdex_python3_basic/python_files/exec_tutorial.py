#! python3

# Exec compiles and evaluates whatever you pass into it in string form.
# A compiler in a compiler. If you have any kind of dynamic data being passed
# to this by users, it oculd be dangereous.

exec("print('so this works like eval?')")

list_str = "[5,6,2,1,6]"

# This will return None
list_str = exec(list_str)
print(list_str)

exec("list_str2 = [5,6,2,1,1]")
print(list_str2)

exec("def test(): print('o sniiiiip snap')")
test()


exec("""
def test2():
    print('lets see if multiline works')
""")

test2()
