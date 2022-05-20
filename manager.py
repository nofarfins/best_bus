from database import all_routes, get_route_by_line_number


def add_route():
    line_number = int(input("insert line number:"))

    if get_route_by_line_number(line_number) is not None:
        print('Line number already exists!')

        return

    origin = input('insert origin: ')
    destination = input('insert destination: ')
    list_of_stops = input('insert list of stops: ')

    new_route = {
        'line number': line_number,
        'origin': origin,
        'destination': destination,
        'list of stops': list_of_stops.split(',')
    }

    all_routes.append(new_route)


def delete_route():
    bus_number = input('choose between 47 or 16')
    for route in all_routes:
        if route['line number'] == bus_number:
            ask = input("Are you sure?")
            if ask.lower() == 'yes':
                all_routes.remove(route)
            else:
                print('Thank you')


def update_route():
    line_number = int(input("Line number: "))

    route = get_route_by_line_number(line_number)

    if route is None:
        print('Line number not recognized!')
        return

    print('Route info:', route)

    ask = input("What do you like to change?")
    if ask == 'origin':
        change = input("enter your change origin: ")
    elif ask == 'destination':
        change = input("enter your change destination:")
    elif ask == 'list of stops':
        change = input("enter your change list of stops:")
    else:
        print(f'Cannot change {ask}!')
        return

    route[ask] = change


def add_scheduled_ride():
    line_number = int(input("Please enter line number: "))

    route = get_route_by_line_number(line_number)

    if route is None:
        print('Line number not recognized!')
        return

    print(f'Rides for line {line_number}:', route['scheduled rides'])

    origin_time = input('insert origin time: ')
    destination_time = input('insert destination time: ')
    driver_name = input('insert driver name: ')

    new_ride = {
        'id': 0 if len(route['scheduled rides']) == 0 else route['scheduled rides'][-1]['id'] + 1,
        'origin time': origin_time,
        'destination time': destination_time,
        'driver name': driver_name,
        'delays': 0,
    }

    route['scheduled rides'].append(new_ride)
    print('Updated routes:', route['scheduled rides'])


def manager_login(attempts=3):
    for i in range(attempts):
        password = input("Please enter manager password: ")

        if password == 'RideWithUs!':
            return True
        else:
            print('Wrong password!')

    return False


def manager_menu():
    choose = input('Enter the best option for you: "add route" / "delete route" / "update route"/ "add scheduled ride": ')

    if choose == 'add route':
        add_route()
    elif choose == 'delete route':
        delete_route()
    elif choose == 'update route' :
        update_route()
    elif choose == 'add scheduled ride':
        add_scheduled_ride()
    else:
        print('Invalid option!')
