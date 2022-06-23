# Python program to replace text in a file
x = input("enter text to be replaced: ").casefold()
y = input("enter text that will replace: ").casefold()

f = open("Resources/example.txt", "r+")

# each sentence becomes an element in the list l
l = f.readlines()

# acts as a counter to know the
# index of the element to be replaced
c = 0
for i in l:
    if x in i:
        # Replacement carries the value
        # of the text to be replaced
        Replacement = i.replace(x, y)

        # changes are made in the list
        l = Replacement
    c += 1

# The pre existing text in the file is erased
f.seek(0)
f.truncate(0)
# the modified list is written into the file thereby replacing the old text
f.writelines(l)
f.close()
print("Text successfully replaced.")