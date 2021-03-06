class flight:
    def __init__(self,number):
        if not number[:2].isalpha():
            raise ValueError("No airline code in {}".format(number))
        if not number[:2].isupper():
            raise ValueError("invaild airline code {}".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("invaild route number {}".format(number))

        self._number = number

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

class aircraft:
    def __init__(self, registeration, model, num_rows, num_seats_per_row):
        self._registeration = registeration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registeration(self):
        return self._registeration

    def model(self):
        return self._model
    def seating_plan(self):
        return (range(1,self._num_rows +1), "ABCDEFGHJK"[:self._num_seats_per_row])
