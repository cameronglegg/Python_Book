# This section has been commented out as it is old, and bad...

# print('Enter name of Cat 1: ')
# catName1 = input()
# print('Enter name of Cat 2: ')
# catName2 = input()
# print('Enter name of Cat 3: ')
# catName3 = input()
# print('Enter name of Cat 4: ')
# catName4 = input()
# print('Enter name of Cat 5: ')
# catName5 = input()
# print('Enter name of Cat 6: ')
# catName6 = input()
# print("The cat names are: ")
# print(catName1+', '+catName2+', '+catName3+', '+catName4+', '+catName5+', '+catName6)

catNames = []
while True:
    print('Enter the name of the cat ' + str(len(catNames) + 1) +
    ' (Or enter Nothing to stop.) :')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concat
print('The cat names are: ')
for name in catNames:
    print(' '+ name)