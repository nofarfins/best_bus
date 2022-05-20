all_routes = [
    {
        "line number": 47,
        "origin": "Ra'anana",
        "destination": "Kfar Saba",
        "list of stops": ["Ra'anana - Lev Hapark", "Ra'anana - Ahuza", "kfar Saba - Mish'ol Gil"],
        "scheduled rides": [
            {
                "id": 1,
                "origin time": '7:00',
                "destination time": '7:40',
                "driver name": "aviv levi",
                "delays": 1,
            }
        ]
    },
    {
        "line number": 16,
        "origin": "Ra'anana",
        "destination": "Ra'anana",
        "list of stops": ["Ra'anana - Park", "Ra'anana - Weissman", "Ra'anana - Rennanim Mall"],
        "scheduled rides": [
            {
                "id": 1,
                "origin time": 6,
                "destination time": '6:30',
                "driver name": "David cohen",
                "delays": 3,
            }
        ]
    }
]


def get_route_by_line_number(line_number):
    for route in all_routes:
        if route['line number'] == line_number:
            return route

    return None
