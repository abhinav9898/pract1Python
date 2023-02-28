entered_string = input('enter your query: ').lower()
started = False

while entered_string != 'quit':
    if entered_string == 'help':
        print("""
        start- To start the car
        Stop- To stop the car
        quit- To exit game
        """)
        entered_string = input('enter your query: ').lower()

    elif entered_string == 'start':
        if started:
            print("Car already started!!")
        else:
            print('Car started ... ready to go!')
            started= True

        entered_string = input('enter your query: ').lower()

    elif entered_string == 'stop':
        if not started:
            print("Car already stopped!")
        else:
            print('Car has stopped')
            started= False

        entered_string = input('enter your query: ').lower()

    else:
        print('I dont understand that')
        entered_string = input('enter your query again: ').lower()

else:
    print('You have exited the game')
