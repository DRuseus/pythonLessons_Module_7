from time import sleep

team1_num = 6
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = int()
time_avg = int()
challenge_result = 'Победа команды Волшебники данных!'
print('В команде "Мастера кода" участников: %s!' % team1_num)
print('В команде "Волшебники данных" участников: %s!' % team2_num)
print('Итого сегодня в командах участников: %d и %d!' % (team1_num, team2_num))
print('Команда Волшебники данных решила задач: {}!'.format(score2))
print('{team} решили задачи за {time} секунд!'.format(time=team2_time, team='Волшебники данных'))
print(f'Команды решили {score1} и {score2} задач.')
if score1 > score2 or score1 == score2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
print(f'Результат битвы: победа команды {result}!')
print(
    f'Сегодня было решено {score1 + score2} задач, в среднем по {(team2_time + team1_time) / (score2 + score1)} '
    f'секунды на задачу!')
print(result)
print()












# Моё балаовство
from random import randint


def gen_shape():
    shape_var = randint(0, 2)
    shape = str()
    match shape_var:
        case 0:
            shape = 'Ножницы'
        case 1:
            shape = "Камень"
        case 2:
            shape = "Бумага"
    shape = str('{name}'.format(name=shape))
    return shape


class RockPepperScissors:
    __player_index = 0

    __ROCK = 'Камень'
    __PEPPER = 'Бумага'
    __SCISSORS = 'Ножницы'

    def __new__(cls, *args, **kwargs):
        cls.__player_index += 1
        return super().__new__(cls)

    def __gen_firstname(self):
        rand_pre_name = randint(0, 3)
        rand_post_name = randint(0, 3)
        pre_name = ['Анд', 'Па', 'Се', 'Алесанд']
        post_name = ['рус', 'рэ', 'вел', 'вард']
        firstname = '{}{}'.format(pre_name[rand_pre_name], post_name[rand_post_name])
        return firstname

    def __init__(self, shape=None):
        self.index = self.__player_index
        self.firstname = self.__gen_firstname()
        value = int()
        if shape == None:
            self.shape = gen_shape()
        else:
            if shape == self.__SCISSORS:
                self.shape = self.__SCISSORS
            if shape == self.__ROCK:
                self.shape = self.__ROCK
            if shape == self.__PEPPER:
                self.shape = self.__PEPPER

    def __lt__(self, other):
        if self.shape == self.__PEPPER and other.shape == self.__SCISSORS:
            return True
        if self.shape == self.__SCISSORS and other.shape == self.__ROCK:
            return True
        if self.shape == self.__ROCK and other.shape == self.__PEPPER:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.shape == self.__PEPPER and other.shape == self.__ROCK:
            return True
        if self.shape == self.__SCISSORS and other.shape == self.__PEPPER:
            return True
        if self.shape == self.__ROCK and other.shape == self.__SCISSORS:
            return True
        else:
            return False

    def __eq__(self, other):
        return self.shape == other.shape

    def __str__(self):
        return 'Игрок \033[3%sm%s\033[0m под номером \033[3%sm%s\033[0m' % (
            self.index, self.firstname, self.index, self.index)


def refery(*plrs):
    plrs_list = list(plrs)
    if len(plrs_list) >= 2:
        print('Игрок %s выкинул %s против игрока %s, а тот показал %s' %
              (plrs[0].firstname, plrs[0].shape, plrs[1].firstname, plrs[1].shape))
        if plrs[0] > plrs[1] and not plrs[0] == plrs[1]:
            print(plrs[0], 'побеждает', plrs_list.pop(1), 'и проходит дальше')
            refery(*plrs_list)
        elif plrs[0] < plrs[1] and not plrs[0] == plrs[1]:
            print(f'{plrs[1]} побеждает {plrs_list.pop(0)} и проходит дальше')
            refery(*plrs_list)
        elif plrs[0] == plrs[1]:
            print('{} и {} показали одинаковую фигуру и схлестнутся в следующем поединке'.format(plrs[0], plrs[1]))
            plrs[0].shape = gen_shape()
            plrs[1].shape = gen_shape()
            refery(*plrs_list)
    else:
        print('%s побеждает в ожесточённой схватке' % plrs_list[0])
        return plrs_list[0]


def post_fix(num):
    num = round(num / 10000, 0) * 10000
    return int(num)


sleep(5)
player1 = RockPepperScissors()
player2 = RockPepperScissors()
player3 = RockPepperScissors()
player4 = RockPepperScissors()
print(player1)
print(player2)
print(player3)
print(player4)
winner = refery(player1, player2, player3, player4)
print(f'После всех матчей "Камень ножницы бумага", {winner} доказал, что он номер один в этой игре и забирает свой приз'
      f'в {post_fix(randint(10000, 1000000))}')
