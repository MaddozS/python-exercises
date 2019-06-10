command = input("> ")
while command.lower() != "quit":
    if command.lower() == "start":
        print("Car started")
    elif command == "help":
        print('''
        help: Shows the commands
        start: starts the car
        stop: stops the car
        quit: exits the program''')
    elif command == "stop":
        print("Car stopped")
    else:
        print("I don't understand...")
    command = input("> ").lower()
else:
    print("Goodbye :D ")