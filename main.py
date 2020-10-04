
clients = 'pablo,ricardo,'

def create_client(client_name):
    global clients
    clients += client_name


def _add_comma():
    global clients
    clients += ','

def list_clients():
    global clients
    print(clients)

def _print_welcome():
    print('WELCOME TO AXEL VENTAS')
    print('*'* 50 )
    print('what would you like to do today')
    print('[C]reate client')
    print('[D]elete client')


if __name__ == "__main__":
    _print_welcome()

    command = input ('What is the client name ? ')
    if command == 'C':
        client_name = str(input('Dame el nombre: '))
        create_client(client_name)
        list_clients() 
