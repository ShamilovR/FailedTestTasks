#1 Задание

time_values = '1h 45m,360s,25m,30m 120s,2h 60s'
total_minutes = 0
for time in time_values:
    time_items = time.split()
    hours = 0
    minutes = 0
    seconds = 0
    for item in time_items:
        if 'h' in item:
            hours = int(item.replace('h', ''))
        elif 'm' in item:
            minutes = int(item.replace('m', ''))
        elif 's' in item:
            seconds = int(item.replace('s', ''))
    total_minutes += hours * 60
    total_minutes += minutes
    total_minutes += seconds / 60

print(total_minutes)


#2 Задание

class Tester:
    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline

    def work_hard(self):
        if self.deadline:
            print(self.name, 'Что ж, ещё часок поработаю!')
        else:
            print(self.name, 'Можно отдыхать')


tester_1 = Tester(name='tester_1', deadline=False)
tester_1.work_hard()  # 'tester_1 Можно отдыхать'
tester_2 = Tester(name='tester_2', deadline=True)
tester_2.work_hard()  # 'tester_2 Что ж, ещё часок поработаю!'


#3 Задание

world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

world_champions[2022] = 'Аргентина'
print(world_champions.items())

country = 'Италия'
if country in world_champions.keys():
    print('Италия cтановилась чемпионом мира по футболу в 21 веке!')
else:
    print('Италия не выигрывала чемпионат мира по футболу в 21 веке.')


#4 Задание

new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']
completed_tasks.append(new_tasks.pop(-1))
new_tasks.remove('task_007')
print('task_015')


#5 Задание

class TestCase:
    def __init__(self, steps=None, result=None):
        if steps is None:
            steps = {}
        self.steps = steps
        self.result = result

    def set_step(self, step_number, step_text):
        self.steps[step_number] = step_text

    def set_result(self, result):
        result = result

    def delete_step(self, step_number, step_text: 0):
        self.steps[step_number] = step_text

    def get_test_case(self):
        test_case_info = {
            'Шаги': self.steps,
            'Ожидаемый результат': self.result
        }
        print(test_case_info)


test_case_1 = TestCase()
test_case_1.set_step(1, 'Перейти на сайт')
test_case_1.set_step(3, 'Перейти в раздел Товары')
test_case_1.delete_step(3)
test_case_1.set_step(2, 'Перейти в раздел Товары')
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине')
test_case_1.get_test_case()

test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case()
