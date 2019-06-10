command = ""
while command.lower() != "quit":
    command = input("> ").lower()
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
else:
    print("Goodbye :D ")