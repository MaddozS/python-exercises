command = input("> ")
started = False
while command.lower() != "quit":
    if command.lower() == "start":
        if started:
            print("The car is already started!")
        else:
            started = True
            print("Car started")
    elif command == "help":
        print('''
help: Shows the commands        
start: starts the car
stop: stops the car
quit: exits the program
''')
    elif command == "stop":
        if started:
            started = False
            print("Car stopped")
        else:
            print("The car is already stopped")
    else:
        print("I don't understand...")
    command = input("> ").lower()
else:
    print("Goodbye :D ")