class User:
    
    def __init__(self, user_id, username, password):
        print("creating new user...")
        self.id= user_id 
        self.name= username
        self.pword= password
        self.followers=0
        self.following=0

    def follow(self, user):
        user.followers +=1
        self.following +=1

user_1=User("001", "ohwane", "unique")
# print(user_1.id)

user_2= User("002", "seme", "theworld")
# print(user_2.pword)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.following)
print(user_2.followers)