from database import all_routes, get_route_by_line_number


def input_bus_line():
    bus_line = ''
    all_bus_lines = [item['line number'] for item in all_routes]

    print(f"Bus lines: {', '.join([str(i) for i in all_bus_lines])}")
    while not bus_line.isdigit() or int(bus_line) not in all_bus_lines:
        bus_line = input("Please enter bus line: ")
    bus_line = int(bus_line)

    return bus_line


def search_route():
    search_by = input("choose line number or origin or destination or bus stop:")
    if search_by == 'line number':
        bus_line = input_bus_line()

        for route in all_routes:
            if route['line number'] == bus_line:
                print(route)
    elif search_by == 'origin':
        origin = input("Origin please: ")

        for route in all_routes:
            if route['origin'] == origin:
                print(route)
    elif search_by == 'destination':
        destination = input("Destination please: ")

        for route in all_routes:
            if route['destination'] == destination:
                print(route)
    elif search_by == 'bus stop':
        stop = input('Stop please: ')

        for route in all_routes:
            if stop in route['list of stops']:
                print(route)

    else:
        print('Invalid option!')


def report_delay():
    bus_line = input_bus_line()

    route = get_route_by_line_number(bus_line)

    delay = ''
    while delay not in ('destination', 'origin'):
        delay = input("Is the delay at the destination or origin: ")

    new_time = input("Enter new hour: ")
    print(f'Bus line {bus_line} is delayed at {delay}. New arrival time: {new_time}')




def passenger_menu():
    choose = input('Enter the best option for you: "search route" / "report delay": ')

    if choose == 'search route':
        search_route()
    elif choose == 'report delay':
        report_delay()
    else:
        print('Invalid option!')
