# Name: Nikitha Donthi (100953192)
# Date: 11-10-2024

def create_user(users, username, storage):
    #Create a new user if the username is unique and storage is valid.
    if not username or username in users:
        return False, "Username must be unique and not empty."
    if storage <= 0:
        return False, "Storage must be a positive number."
    
    users[username] = {'available_storage': storage, 'used_storage': 0}
    return True, "User created successfully."

def delete_user(users, username):
    #Delete a user if they exist.
    if username in users:
        del users[username]
        return True, "User deleted."
    return False, "User not found."

def upload_file(users, username, file_name, filesize):
    #Upload a file if the user exists and has enough available storage
    if username not in users:
        return False, "User not found."
    if filesize <= 0:
        return False, "File size must be positive."
    
    user = users[username]
    free_space = user['available_storage'] - user['used_storage']
    
    if free_space >= filesize:
        user['used_storage'] += filesize
        return True, f"File '{file_name}' uploaded successfully."
    return False, "Not enough storage space."

def display_users(users):
    #Display all users and their available storage.
    if not users:
        print("No users found.")
    else:
        for username, info in users.items():
            free_space = info['available_storage'] - info['used_storage']
            print(f"{username} - Available storage: {free_space} MB")

def main():
    users = {}
    while True:
        print("\nMenu:")
        print("1. Create User")
        print("2. Delete User")
        print("3. Upload File")
        print("4. Display Users")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")

        if choice == '1':
            username = input("Enter a username: ")
            try:
                storage = int(input("Enter storage (MB): "))
            except ValueError:
                print("Please enter a valid number for storage.")
                continue
            success, msg = create_user(users, username, storage)
            print(msg)
        elif choice == '2':
            username = input("Enter the username to delete: ")
            success, msg = delete_user(users, username)
            print(msg)
        elif choice == '3':
            username = input("Enter a username: ")
            file_name = input("Enter the file name: ")
            try:
                filesize = int(input("Enter file size (MB): "))
            except ValueError:
                print("Please enter a valid number for file size.")
                continue
            success, msg = upload_file(users, username, file_name, filesize)
            print(msg)
        elif choice == '4':
            display_users(users)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()

