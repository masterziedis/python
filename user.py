class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"The are {cls.active_users} active users"

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))


    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def __repr__(self):
            return f"{self.first} is {self.age}"

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th birthday, {self.first}"

# print(user2.full_name())
# print(user1.initials())
# print(user2.initials())
# print(user1.likes("Alutis"))


# print(user1.age)
# print(user2.is_senior())
# print(user1.birthday())
# print(user1.age)
# print(User.display_active_users())

# user1 = User("Jose", "Narkata", 28)
# user2 = User("Longa", "Prastitutka", 97)

# print(User.display_active_users())

tom = User.from_string("Tom,Jones,89")
print(tom)