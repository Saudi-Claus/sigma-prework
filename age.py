from datetime import date, datetime


def age_finder(birth_date: date) -> int:
    '''
    Return the age in years, based on the provided birth date.
    '''
    current_date = date.today()
    age = current_date.year - birth_date.year
    if (birth_date.month, birth_date.day) < (current_date.month, current_date.day):
        return age
    return age - 1


def input_birthday() -> date:
    '''
    Prompt the user for their birth day and validates it.
    '''
    while True:
        birth_time = input(
            'Please input the day you were born in the form DD-MM-YYYY: ')

        # Validation
        try:
            birth_date = datetime.strptime(birth_time, '%d-%m-%Y').date()

            if birth_date > date.today():
                raise ValueError('You were not born in the future')

            return birth_date

        except ValueError as e:
            print(
                f'Error: {e}. Input is not correctly formatted. Please try again.')


if __name__ == '__main__':
    birth_date = input_birthday()
    print(age_finder(birth_date))
