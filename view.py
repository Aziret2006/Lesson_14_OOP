from classwork import Human
from database import PEOPLE


def create_human():
    first_name = input("Enter name:").strip().capitalize()
    last_name = input("Enter surname:").strip().capitalize()
    date_of_birth = input("Enter your date of birth (01.01.2022): ")
    place_of_birth = input("Enter your place of birth: ")
    nationallaty = input("Enter your nationallaty: ")
    is_married = input("""Choose 1 if you married
                       Choose 2 if you not married
                       """)
    if is_married == '1':
        is_married = True
    else:
        is_married = False

    hair_color = input("""Choice 1 if you have black hair
                       Choice 2 if you have blond hair
                       Choice 3 if you have brown hair
                       Choice 4 if you have other color
                       """)
    if hair_color in ['1', '2', '3']:
        hair_colors = {
            '1': 'black',
            '2': 'blond',
            '3': 'brown'
        }
        hair_color = hair_colors[hair_color]
    else:
        pass


    hand_count = input('Enter your count hands: ')
    Human(first_name=first_name,
          last_name=last_name,
          data_of_birth=date_of_birth,
          place_of_birthday=place_of_birth,
          nationaly=nationallaty,
          is_married=is_married,
          hair_color=hair_color,
          hands_count=hand_count)
    PEOPLE.append(Human)
    print("Human created succes!")


def get_human_info():
    for human in PEOPLE:
        print(human)
        print(human.first_name)
        print(human.last_name)
        human.think()
        human.remember()
        print(human.first_name, human.is_married)