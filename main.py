from manager import manager_login, manager_menu
from passenger import passenger_menu


def main():
    print('Hello to best bus ever app!')
    select = ''

    while select not in ('passenger', 'manager'):
        select = input('Please choose between "passenger" or "manager": ')

    if select == 'manager':
        success = manager_login()

        if not success:
            print('Failed to login as manager. Goodbye!')
            return

    while True:
        print(f'Welcome {select}!')

        if select == 'manager':
            manager_menu()
        else:
            passenger_menu()


if __name__ == '__main__':
    main()
