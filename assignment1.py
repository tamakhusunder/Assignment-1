badgeRecord =[ ["111", "exit"],
["222", "enter"],
["111", "enter"],
["111", "exit"],
["222", "enter"],
["222", "enter"],
["333", "exit"],
["333", "enter"],
["222", "exit"],
["111", "enter"],
["111", "exit"],
["222", "exit"],
["222", "enter"],
["222", "enter"],
["111", "exit"],
]

def getBadgeAccess(records):
    did_not_exit = set()
    did_not_enter = set()
    room = set()

    for name, swipe in records:
        if swipe == 'enter':
            if name in room:
                did_not_exit.add(name)
            else:
                room.add(name)
        elif swipe == 'exit':
            if name not in room:
                did_not_enter.add(name)
            else:
                room.discard(name)
    
    for person in list(room):
        did_not_exit.add(person)
        
    return did_not_exit, did_not_enter

x,y=getBadgeAccess(badgeRecord)
print("Person who did not exit are :",x)
print("Person who did not enter are :",y)