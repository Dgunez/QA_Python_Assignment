class Account: #creating a class called Account

    def __init__(self, username , password):
        self.__username= username #private variable using double _, self refers to the object being created
        self.__password =password #private variable, creating an attribute using self__password
    
    # Setter for username
    def set_username(self, username):
        self.__username = username

      # Method to display username
    def display_username(self):
        print("Username:", self.__username)      

# Create an Account object
acc = Account("dipendra", "mypassword123")

# Change username
acc.set_username("dipendra3")
acc.display_username()

# Try printing the password directly
print(acc.__password)  
# This will cause an AttributeError because we havent used setter &
#  method to display passwords