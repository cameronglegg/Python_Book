# This gets the list with the ending I want but it doesn't accomplish what the questions asked.
# print('Enter a list')
# spam = input()
# eggs = spam[-1]
# foo = 'and ' + eggs
# del spam[-1]
# spam.append(foo)
# print(spam)

def addAnd(list):
    finalListItem = list[-1]
    andAddedtoListItem = 'and ' + finalListItem
    del list[-1]
    list.append(andAddedtoListItem)
    return list

list = []
while True:
    print('Enter items into the list ' + str(len(list) + 1)+ '(Or enter nothing to finish.): ')
    listItem = input()
    if listItem == '':
        break
    list = list + [listItem] # This should be the concat.

addAnd(list)
print('The list items are: ')
print(list)