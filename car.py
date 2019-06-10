command = input(">")
while command.lower() != "quit":
    if command.lower() == "start":
        print("The car's running")
    elif command.lower() == "help":
        print('''
        help: Shows the commands
        start: starts the car
        stop: stops the car
        quit: exits the program
        ''')
    elif command.lower() == "stop":
        print("The car stopped")
    else:
        print("I don't understand...")
    command = input(">")
else:
    print("Goodbye :D ")