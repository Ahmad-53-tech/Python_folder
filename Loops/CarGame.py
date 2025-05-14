command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started🚘..............Ready to Go")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped🚗.................skrrrrrr")
    elif command == "help":
        print("""
start - To start the car
stop - To stop the car
quit - To exit""")
    elif command == "quit":
        break
    else:
        print("I don't understand this")    