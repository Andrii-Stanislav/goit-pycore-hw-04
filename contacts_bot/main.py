def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added."

def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        return f"Contact {name} not found."
    
    contacts[name] = phone
    return f"Contact {name} updated."

def show_all(contacts):
    if not contacts:
        return "No contacts added yet."
    
    res = 'All contacts:'
    for name, phone in contacts.items():
        res += f"\n - {name}: {phone}"
    return res

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        
        elif command == "hello":
            print("How can I help you?")
            
        elif command == "add":
            if len(args) < 2:
                print("Give me name and phone please. Example: add John 1234567890")
                continue
            print(add_contact(args, contacts))
            
        elif command == "change":
            if len(args) != 2:
                print("Give me name and phone please. Example: change John 1234567890")
                continue
            print(change_contact(args, contacts))
            
        elif command == "all":
            print(show_all(contacts))
            
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
