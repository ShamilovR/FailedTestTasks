#1 Задание

class Case:

    def __init__(self, test_case_id, name, step_description, expected_result):
        self.test_case_id = test_case_id
        self.name = name
        self.step_description = step_description
        self.expected_result = expected_result

    def print_test_case_info(self):
        print(f"ID тест-кейса:  {self.test_case_id}"
              f"\nНазвание: {self.name}"
              f"\nОписание шага: {self.step_description}"
              f"\nОжидаемый результат: {self.expected_result}")

class ExtendedCase(Case):

    def __init__(self, test_case_id, name, step_description, expected_result, precondition, environment):
        self.precondition = precondition
        self.environment = environment
        super().__init__(test_case_id, name, step_description, expected_result)

    def print_test_case_info(self):
        print(f"ID тест-кейса:  {self.test_case_id}"
              f"\nНазвание: {self.name}"
              f"\nОписание шага: {self.step_description}"
              f"\nОжидаемый результат: {self.expected_result}"
              f"\nПредусловие: {self.precondition}"
              f"\nОкружение: {self.environment}")

case = ExtendedCase('1', 'Наличие кнопки Принять', '1. Открыть вкладку приёма документов 2. Проверить наличие кнопки ',
                    'Кнопка доступна', 'Открыть сервис', 'Яндекс Браузер')
case.print_test_case_info()


#2 Задание

class Movies:

    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

class Comedy(Movies):

    def add_movie(self, movie):
        sself.movies.append(movie)
        return f'Комедии: {self.movies}'

class Drama():

    def add_movie(self, movie):
        self.movies.append(movie)
        return f'Драмы: {self.movies}'


print(Comedy().add_movie('Большой куш'))
print(Drama().add_movie('Оружейный барон'))


#3 Задание

class PointsForPlace:

    @staticmethod
    def get_points_for_place(place):
        points = 0
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
        else:
            points = 100 - place
        return points

class PointsForMeters:

    @staticmethod
    def get_points_for_meters(meters):
        points = 0
        if meters < 0:
            print('Количество метров не может быть отрицательным')
        else:
            points = meters * 0.5
        return points

class TotalPoints(PointsForPlace, PointsForMeters):

    @staticmethod
    def get_total_points(meters, place):
        total = PointsForPlace.get_points_for_place(place) + PointsForMeters.get_points_for_meters(meters)
        return total

points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))
points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))
total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))

#4 Задание

class EmployeeSalary:

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
        self.hourly_payment = 400

    @classmethod
    def get_hours(cls, name, hours, rest_days, email):
        if hours is None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days, email):
        if email is None:
            email = f'{name}@email.com'
        return cls(name, hours, rest_days, email)

    def set_hourly_payment(self):
        self.hourly_payment = 500

    def salary(self, hours):
        return hours * EmployeeSalary.hourly_payment


#5 Задание

class Results:

    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses

class Football():

    def __init__(self, victories, draws, losses):
        super().__init__(victories, draws, losses)

    def number_of_wins(self):
        return f'Футбольных побед: {self.victories}'

    def number_of_draws(self):
        return f'Футбольных ничьих: {self.draws}'

    def number_of_losses(self):
        return f'Футбольных поражений: {self.losses}'

    def total_points(self):
        return f'Общее количество очков: {3 * self.victories + self.draws}'


class Hockey():

    def __init__(self, victories, draws, losses):
        super().__init__(victories, draws, losses)

    def number_of_wins(self):
        return f'Хоккейных побед: {self.victories}'

    def number_of_draws(self):
        return f'Хоккейных ничьих: {self.draws}'

    def number_of_losses(self):
        return f'Хоккейных поражений: {self.losses}'

    def total_points(self):
        return f'Общее количество очков: {3 * self.victories + self.draws}'
