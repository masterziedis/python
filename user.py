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


class Moderator(User):
    total_mods = 0
    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
        Moderator.total_mods += 1

    @classmethod
    def display_active_mods(cls):
        return f"The are {cls.total_mods} active moderators"

    def remove_post(self):
        return f"{self.full_name()} removed a post from the {self.community} community"



user1 = User("Jose", "Narkata", 28)
user2 = User("Jose", "Narkata", 28)
user3 = User("Jose", "Narkata", 28)

jasmine1 = Moderator("Jasmine", "Radzi", 52, "Piano")
jasmine2 = Moderator("Jasmine", "Radzi", 52, "Piano")
print(User.display_active_users())
print(Moderator.display_active_mods())
