class User:

    # Constructor
    def __init__(self, user_id, username):

        # self is the object being initialized (this kind of seems like .this)
        self.id = user_id
        self.username = username
        print('Hello!')

user_1 = User("001", "svierckl")
