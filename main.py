from view import create_human, get_human_info


def main():
    while True:
        client_action = input(""" 
            Press 1 to create human,
            Press 2 to find human,
            Press 3 to exit
            """)
        if client_action == '1':
            create_human()
        elif client_action == '2':
            get_human_info()
        else:
            print("I'm miss you")
            break


if __name__ == '__main__':
    main()
