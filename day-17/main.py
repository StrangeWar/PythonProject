class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User('001', 'Vivek Sharma')
user_2 = User("002", "Anita Sharma")
user_1.follow(user_2)
user_2.follow(user_1)
print(f"User id: {user_1.id}")
print(f"User Name: {user_1.username}")
print(f"Followers count: {user_1.followers}")
print(f"User 2 followings: {user_2.following}")