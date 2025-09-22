export = {
 "users": [
 { "_id" : "4ke83hsejs", "name" : "John", "role" : "developer"},
 { "_id" : "34rkmlqek2", "name" : "Kevin", "role" : "developer"},
 { "_id" : "83i2kkwwj3", "name" : "Joe", "role" : "developer"},
 { "_id" : "12kw4jwmcq", "name" : "Bob", "role" : "developer"},
 { "_id" : "4i5ii32313", "name" : "Robert", "role" : "developer"},
 { "_id" : "lkr3jwl4k5", "name" : "Mary", "role" : "manager"},

 ],
 "sprints": [
 { "_id": "2",
 "tasks":[ { "_id" : "T0005", "storypoint" : 60, "task" : "Seach", "hours": [ ("4ke83hsejs", 23), ("83i2kkwwj3", 15), ("4i5ii32313", 11)]},
 { "_id" : "T0006", "storypoint" : 20, "task" : "Filter",
 "hours": [ ("4ke83hsejs", 17), ("4i5ii32313", 12)]},
 { "_id" : "T0007", "storypoint" : 40, "task" : "List items",
 "hours": [ ("4i5ii32313", 3)]},
 ]
 },{ "_id": "3",
 "tasks":[ { "_id" : "T008", "storypoint" : 25, "task" : "Basket",
 "hours": [ ("4ke83hsejs", 6), ("83i2kkwwj3", 15), ("4i5ii32313", 23)]},
 { "_id" : "T0009", "storypoint" : 20, "task" : "Subscription",
 "hours": [ ("4ke83hsejs", 3), ("83i2kkwwj3", 24), ("4i5ii32313", 23)]},
 { "_id" : "T0010", "storypoint" : 35, "task" : "Order",
 "hours": [ ("83i2kkwwj3", 13), ("4i5ii32313", 5)]}
 ]
 },{ "_id": "1",
 "tasks":[ { "_id" : "T0001", "storypoint" : 50, "task" : "Login",
 "hours": [ ("4ke83hsejs", 13), ("83i2kkwwj3", 5), ("4i5ii32313", 11)]},
 { "_id" : "T0002", "storypoint" : 20, "task" : "Registration",
 "hours": [ ("4ke83hsejs", 28), ("4i5ii32313", 12)]},
 { "_id" : "T0003", "storypoint" : 30, "task" : "Menu",
 "hours": [ ("83i2kkwwj3", 7), ("4i5ii32313", 5)]},
 { "_id" : "T0004", "storypoint" : 40, "task" : "Design",
 "hours": [ ("4ke83hsejs", 17)]}
 ]
 },
 ]
}

# Minden osztályban legyen konstruktor (__init__())
# Minden osztályon belüli függvény első paramétere a self
class User:
    def __init__(self, id, password, name, role):
        self.id = id
        self.password = password
        self.name = name
        self.role = role

    def __str__(self):
        return f"{self.id}, {self.name} ({self.role})"
    
class Users:
    def __init__(self, users: list[dict]):
        self.users = []
        for user in users:
            példány = User(user["_id"], "", user["name"], user["role"])
            self.users.append(példány)
    
    def get_user(self, id: str) -> User:
        for user in self.users:
            if user.id == id:
                return user
        raise Exception(f"Did not find user with id: {id}.")
        

users = Users(export["users"])
print(users.get_user("83i2kkwwj3")) # 83i2kkwwj3, Joe (developer)
#print(users.get_user("83isadsaj3")) # HIBA








"""
myUser = User("myId1", "12345", "John", "Developer")
print(myUser.role)
print(myUser) # <__main__.User object at 0x000001F28F47F110>
szöveg = str(myUser)
print(szöveg) # <__main__.User object at 0x000001F28F47F110>
# Ahoz hogy ezt orvosulj, felül kell írnunk az str() függvény működését a User osztályban
"""