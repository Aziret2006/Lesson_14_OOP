
class Human:
    def __init__(self, first_name: str, last_name: str,  data_of_birth: str, hair_color: str,
                 nationaly: str, is_married: bool, place_of_birthday: str, hands_count=2):
        self.first_name = first_name
        self.last_name = last_name
        self.data_of_birth = data_of_birth
        self.place_of_birthday = place_of_birthday
        self.nationaly = nationaly
        self.is_married = is_married
        self.hands_count = hands_count


    def think(self):
        print("I'm thinking")


    def remember(self):
        print("I'm remember!")

    def saying(self):
        print("I'm say Hi!")