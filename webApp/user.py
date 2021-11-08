import uuid


class User:
    type_public = 'public'
    type_staff = 'staff'

    status_active = 1
    status_delete = 0

    # For real scenario use double underscore for variables
    def __init__(self, email, password, first_name, last_name, gender, membership=None, remarks=None):
        self.id = str(uuid.uuid4())
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.membership = membership
        self.remarks = remarks
        self.type = User.type_public
        self.status = User.status_active

    def __str__(self):
        return f'ID: {self.id}\nEmail: {self.email}\nFirst Name: {self.first_name}\nLast Name: {self.last_name}\nType: {self.type}\nStatus: {self.status}\n'


# user1 = User('user1@test.com', 'flaskwebapp', 'Alice')
# print(user1)
# user2 = User('user2@test.com', 'flaskwebapp', 'Bryan')
# print(user2)
