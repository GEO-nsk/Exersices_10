import random

class NavalBattle:
    '''
    Description of game naval battle

       This class helps to play game

       Class attributes:
           playing_field: list of lists with field (0 - none, 1 - ship)

       Attributes:
            shot_marker: symbol of each player that marks their shots

       Methods:
             shot: selected player shots at playing filed. Player can either shot or miss. Can print error message.
             new_game: creates new random generated field

       Static methods:
           show: shows the playing field to players
    '''
    playing_field = None

    def __init__(self, shot_marker):
        '''
        Initializes players

        args:
            shot_marker: symbol of each player that marks their shots
        '''
        self.shot_marker = shot_marker

    @staticmethod
    def show():
        '''
        shows the playing field to players

        returns new playing filed
        '''
        new_field = [[], [], [], [], [], [], [], [], [], []]
        for item in range(len(NavalBattle.playing_field)):
            for itr in range(len(NavalBattle.playing_field[item])):
                if NavalBattle.playing_field[item][itr] == 1 or NavalBattle.playing_field[item][itr] == 0:
                    new_field[item].append('~')
                else:
                    new_field[item].append(NavalBattle.playing_field[item][itr])
        for item in range(len(new_field)):
            for itr in new_field[item]:
                print(itr, end='')
            print('')

    def shot(self, x, y):
        '''
        selected player shots at playing filed. Player can either shot or miss. Can print error message

        args:
            x: x coordinate
            y: y coordinate
        '''
        if self.playing_field == None:
            print('игровое поле не заполнено')
        else:
            if self.playing_field[y - 1][x - 1] == 1:
                self.playing_field[y - 1][x - 1] = self.shot_marker
                print('попал')
            elif self.playing_field[y - 1][x - 1] == 0:
                self.playing_field[y - 1][x - 1] = 'o'
                print('мимо')
            else:
                print('ошибка')

    @classmethod
    def new_game(cls):
        '''
        creates new random generated field
        '''

        num_ship_2 = 3
        num_ship_3 = 2
        num_ship_4 = 1

        cls.playing_field = \
            [['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']]

        while num_ship_4 > 0:
            line = random.randint(0, 1)
            if line == 0:
                index_y = []
                index_x = []
                num_ship_4 -= 1

                for item in range(1, 11):
                    for itr in range(1, 8):
                        if cls.playing_field[item - 1][itr - 1] == '0' and cls.playing_field[item - 1][
                            itr] == '0' and cls.playing_field[item - 1][itr + 1] == '0' and \
                                cls.playing_field[item - 1][itr + 2] == '0':
                            index_y.append(item)
                            break
                ship_y = random.choice(index_y)

                for itr in range(1, 8):
                    if cls.playing_field[ship_y - 1][itr - 1] == '0' and cls.playing_field[ship_y - 1][itr] == '0' and \
                            cls.playing_field[item - 1][itr + 1] == '0' and cls.playing_field[item - 1][
                        itr + 2] == '0':
                        index_x.append(itr)
                ship_x = random.choice(index_x)

                for item in range(18):
                    cls.playing_field[ship_y - 1][ship_x - 1] = '4'
                    cls.playing_field[ship_y - 1][ship_x] = '4'
                    cls.playing_field[ship_y - 1][ship_x + 1] = '4'
                    cls.playing_field[ship_y - 1][ship_x + 2] = '4'
                    if 0 <= ship_y - 2 <= 9 and 0 <= ship_x - 2 <= 9:
                        cls.playing_field[ship_y - 2][ship_x - 2] = '#'
                    if 0 <= ship_y - 2 <= 9 and 0 <= ship_x - 1 <= 9:
                        cls.playing_field[ship_y - 2][ship_x - 1] = '#'
                    if 0 <= ship_y - 2 <= 9 and 0 <= ship_x <= 9:
                        cls.playing_field[ship_y - 2][ship_x] = '#'
                    if 0 <= ship_y - 2 <= 9 and 0 <= ship_x + 1 <= 9:
                        cls.playing_field[ship_y - 2][ship_x + 1] = '#'
                    if 0 <= ship_y - 2 <= 9 and 0 <= ship_x + 2 <= 9:
                        cls.playing_field[ship_y - 2][ship_x + 2] = '#'
                    if 0 <= ship_y - 2 <= 9 and 0 <= ship_x + 3 <= 9:
                        cls.playing_field[ship_y - 2][ship_x + 3] = '#'
                    if 0 <= ship_y - 1 <= 9 and 0 <= ship_x - 2 <= 9:
                        cls.playing_field[ship_y - 1][ship_x - 2] = '#'
                    if 0 <= ship_y - 1 <= 9 and 0 <= ship_x + 3 <= 9:
                        cls.playing_field[ship_y - 1][ship_x + 3] = '#'
                    if 0 <= ship_y <= 9 and 0 <= ship_x - 2 <= 9:
                        cls.playing_field[ship_y][ship_x - 2] = '#'
                    if 0 <= ship_y <= 9 and 0 <= ship_x - 1 <= 9:
                        cls.playing_field[ship_y][ship_x - 1] = '#'
                    if 0 <= ship_y <= 9 and 0 <= ship_x <= 9:
                        cls.playing_field[ship_y][ship_x] = '#'
                    if 0 <= ship_y <= 9 and 0 <= ship_x + 1 <= 9:
                        cls.playing_field[ship_y][ship_x + 1] = '#'
                    if 0 <= ship_y <= 9 and 0 <= ship_x + 2 <= 9:
                        cls.playing_field[ship_y][ship_x + 2] = '#'
                    if 0 <= ship_y <= 9 and 0 <= ship_x + 3 <= 9:
                        cls.playing_field[ship_y][ship_x + 3] = '#'

            else:
                index_y = []
                index_x = []
                num_ship_4 -= 1

                for item in range(10):
                    for itr in range(7):
                        if cls.playing_field[itr][item] == '0' and cls.playing_field[itr + 1][item] == '0' and \
                                cls.playing_field[itr + 2][item] == '0' and cls.playing_field[itr + 3][item] == '0':
                            if itr not in index_y:
                                index_y.append(itr)
                ship_y = random.choice(index_y) + 1

                for item in range(1, 11):
                    if cls.playing_field[ship_y - 1][item - 1] == '0' and cls.playing_field[ship_y][
                        item - 1] == '0' and cls.playing_field[ship_y + 1][item - 1] == '0' and \
                            cls.playing_field[ship_y + 1][item - 1] == '0':
                        index_x.append(item)

                ship_x = random.choice(index_x)

                for item in range(18):
                    cls.playing_field[ship_y - 1][ship_x - 1] = '4'
                    cls.playing_field[ship_y][ship_x - 1] = '4'
                    cls.playing_field[ship_y + 1][ship_x - 1] = '4'
                    cls.playing_field[ship_y + 2][ship_x - 1] = '4'
                    if 0 <= ship_y - 2 <= 9 and 0 <= ship_x - 2 <= 9:
                        cls.playing_field[ship_y - 2][ship_x - 2] = '#'
                    if 0 <= ship_y - 2 <= 9 and 0 <= ship_x - 1 <= 9:
                        cls.playing_field[ship_y - 2][ship_x - 1] = '#'
                    if 0 <= ship_y - 2 <= 9 and 0 <= ship_x <= 9:
                        cls.playing_field[ship_y - 2][ship_x] = '#'
                    if 0 <= ship_y - 1 <= 9 and 0 <= ship_x - 2 <= 9:
                        cls.playing_field[ship_y - 1][ship_x - 2] = '#'
                    if 0 <= ship_y - 1 <= 9 and 0 <= ship_x <= 9:
                        cls.playing_field[ship_y - 1][ship_x] = '#'
                    if 0 <= ship_y <= 9 and 0 <= ship_x - 2 <= 9:
                        cls.playing_field[ship_y][ship_x - 2] = '#'
                    if 0 <= ship_y <= 9 and 0 <= ship_x <= 9:
                        cls.playing_field[ship_y][ship_x] = '#'
                    if 0 <= ship_y + 1 <= 9 and 0 <= ship_x - 2 <= 9:
                        cls.playing_field[ship_y + 1][ship_x - 2] = '#'
                    if 0 <= ship_y + 1 <= 9 and 0 <= ship_x <= 9:
                        cls.playing_field[ship_y + 1][ship_x] = '#'
                    if 0 <= ship_y + 2 <= 9 and 0 <= ship_x - 2 <= 9:
                        cls.playing_field[ship_y + 2][ship_x - 2] = '#'
                    if 0 <= ship_y + 2 <= 9 and 0 <= ship_x <= 9:
                        cls.playing_field[ship_y + 2][ship_x] = '#'
                    if 0 <= ship_y + 3 <= 9 and 0 <= ship_x - 2 <= 9:
                        cls.playing_field[ship_y + 3][ship_x - 2] = '#'
                    if 0 <= ship_y + 3 <= 9 and 0 <= ship_x - 1 <= 9:
                        cls.playing_field[ship_y + 3][ship_x - 1] = '#'
                    if 0 <= ship_y + 3 <= 9 and 0 <= ship_x <= 9:
                        cls.playing_field[ship_y + 3][ship_x] = '#'

        while num_ship_3 > 0:
            line = random.randint(0, 1)
            if line == 0:
                index_y = []
                index_x = []
                num_ship_3 -= 1

                for item in range(1, 11):
                    for itr in range(1, 9):
                        if cls.playing_field[item - 1][itr - 1] == '0' and cls.playing_field[item - 1][itr] == '0' and \
                                cls.playing_field[item - 1][itr + 1] == '0':
                            index_y.append(item)
                            break
                ship_y = random.choice(index_y)

                for itr in range(1, 9):
                    if cls.playing_field[ship_y - 1][itr - 1] == '0' and cls.playing_field[ship_y - 1][itr] == '0' and \
                            cls.playing_field[ship_y - 1][itr + 1] == '0':
                        index_x.append(itr)
                ship_x = random.choice(index_x)

                for item in range(15):
                    cls.playing_field[ship_y - 1][ship_x - 1] = '3'
                    cls.playing_field[ship_y - 1][ship_x] = '3'
                    cls.playing_field[ship_y - 1][ship_x + 1] = '3'
                    if 0 <= ship_y - 2 <= 9 and 0 <= ship_x - 2 <= 9:
                        cls.playing_field[ship_y - 2][ship_x - 2] = '#'
                    if 0 <= ship_y - 2 <= 9 and 0 <= ship_x - 1 <= 9:
                        cls.playing_field[ship_y - 2][ship_x - 1] = '#'
                    if 0 <= ship_y - 2 <= 9 and 0 <= ship_x <= 9:
                        cls.playing_field[ship_y - 2][ship_x] = '#'
                    if 0 <= ship_y - 2 <= 9 and 0 <= ship_x + 1 <= 9:
                        cls.playing_field[ship_y - 2][ship_x + 1] = '#'
                    if 0 <= ship_y - 2 <= 9 and 0 <= ship_x + 2 <= 9:
                        cls.playing_field[ship_y - 2][ship_x + 2] = '#'
                    if 0 <= ship_y - 1 <= 9 and 0 <= ship_x - 2 <= 9:
                        cls.playing_field[ship_y - 1][ship_x - 2] = '#'
                    if 0 <= ship_y - 1 <= 9 and 0 <= ship_x + 2 <= 9:
                        cls.playing_field[ship_y - 1][ship_x + 2] = '#'
                    if 0 <= ship_y <= 9 and 0 <= ship_x - 2 <= 9:
                        cls.playing_field[ship_y][ship_x - 2] = '#'
                    if 0 <= ship_y <= 9 and 0 <= ship_x - 1 <= 9:
                        cls.playing_field[ship_y][ship_x - 1] = '#'
                    if 0 <= ship_y <= 9 and 0 <= ship_x <= 9:
                        cls.playing_field[ship_y][ship_x] = '#'
                    if 0 <= ship_y <= 9 and 0 <= ship_x + 1 <= 9:
                        cls.playing_field[ship_y][ship_x + 1] = '#'
                    if 0 <= ship_y <= 9 and 0 <= ship_x + 2 <= 9:
                        cls.playing_field[ship_y][ship_x + 2] = '#'

            else:
                index_y = []
                index_x = []
                num_ship_3 -= 1

                for item in range(10):
                    for itr in range(8):
                        if cls.playing_field[itr][item] == '0' and cls.playing_field[itr + 1][item] == '0' and \
                                cls.playing_field[itr + 2][item] == '0':
                            if itr not in index_y:
                                index_y.append(itr)
                ship_y = random.choice(index_y) + 1

                for item in range(1, 11):
                    if cls.playing_field[ship_y - 1][item - 1] == '0' \
                            and cls.playing_field[ship_y][item - 1] == '0' \
                            and cls.playing_field[ship_y + 1][item - 1] == '0':
                        index_x.append(item)

                ship_x = random.choice(index_x)

                for item in range(15):
                    cls.playing_field[ship_y - 1][ship_x - 1] = '3'
                    cls.playing_field[ship_y][ship_x - 1] = '3'
                    cls.playing_field[ship_y + 1][ship_x - 1] = '3'
                    if 0 <= ship_y - 2 <= 9 and 0 <= ship_x - 2 <= 9:
                        cls.playing_field[ship_y - 2][ship_x - 2] = '#'
                    if 0 <= ship_y - 2 <= 9 and 0 <= ship_x - 1 <= 9:
                        cls.playing_field[ship_y - 2][ship_x - 1] = '#'
                    if 0 <= ship_y - 2 <= 9 and 0 <= ship_x <= 9:
                        cls.playing_field[ship_y - 2][ship_x] = '#'
                    if 0 <= ship_y - 1 <= 9 and 0 <= ship_x - 2 <= 9:
                        cls.playing_field[ship_y - 1][ship_x - 2] = '#'
                    if 0 <= ship_y - 1 <= 9 and 0 <= ship_x <= 9:
                        cls.playing_field[ship_y - 1][ship_x] = '#'
                    if 0 <= ship_y <= 9 and 0 <= ship_x - 2 <= 9:
                        cls.playing_field[ship_y][ship_x - 2] = '#'
                    if 0 <= ship_y <= 9 and 0 <= ship_x <= 9:
                        cls.playing_field[ship_y][ship_x] = '#'
                    if 0 <= ship_y + 1 <= 9 and 0 <= ship_x - 2 <= 9:
                        cls.playing_field[ship_y + 1][ship_x - 2] = '#'
                    if 0 <= ship_y + 1 <= 9 and 0 <= ship_x <= 9:
                        cls.playing_field[ship_y + 1][ship_x] = '#'
                    if 0 <= ship_y + 2 <= 9 and 0 <= ship_x - 2 <= 9:
                        cls.playing_field[ship_y + 2][ship_x - 2] = '#'
                    if 0 <= ship_y + 2 <= 9 and 0 <= ship_x - 1 <= 9:
                        cls.playing_field[ship_y + 2][ship_x - 1] = '#'
                    if 0 <= ship_y + 2 <= 9 and 0 <= ship_x <= 9:
                        cls.playing_field[ship_y + 2][ship_x] = '#'

        while num_ship_2 > 0:
            line = random.randint(0, 1)
            if line == 0:
                index_y = []
                index_x = []
                num_ship_2 -= 1

                for item in range(1, 11):
                    for itr in range(1, 10):
                        if cls.playing_field[item - 1][itr - 1] == '0' and cls.playing_field[item - 1][itr] == '0':
                            index_y.append(item)
                            break
                ship_y = random.choice(index_y)

                for itr in range(1, 10):
                    if cls.playing_field[ship_y - 1][itr - 1] == '0' and cls.playing_field[ship_y - 1][itr] == '0':
                        index_x.append(itr)
                ship_x = random.choice(index_x)

                for item in range(12):
                    cls.playing_field[ship_y - 1][ship_x - 1] = '2'
                    cls.playing_field[ship_y - 1][ship_x] = '2'
                    if 0 <= ship_y - 2 <= 9 and 0 <= ship_x - 2 <= 9 and cls.playing_field[ship_y - 2][
                        ship_x - 2] != '1':
                        cls.playing_field[ship_y - 2][ship_x - 2] = '#'
                    if 0 <= ship_y - 2 <= 9 and 0 <= ship_x - 1 <= 9 and cls.playing_field[ship_y - 2][
                        ship_x - 1] != '1':
                        cls.playing_field[ship_y - 2][ship_x - 1] = '#'
                    if 0 <= ship_y - 2 <= 9 and 0 <= ship_x <= 9 and cls.playing_field[ship_y - 2][ship_x] != '1':
                        cls.playing_field[ship_y - 2][ship_x] = '#'
                    if 0 <= ship_y - 2 <= 9 and 0 <= ship_x + 1 <= 9 and cls.playing_field[ship_y - 2][
                        ship_x + 1] != '1':
                        cls.playing_field[ship_y - 2][ship_x + 1] = '#'
                    if 0 <= ship_y - 1 <= 9 and 0 <= ship_x - 2 <= 9 and cls.playing_field[ship_y - 2][
                        ship_x - 2] != '1':
                        cls.playing_field[ship_y - 1][ship_x - 2] = '#'
                    if 0 <= ship_y - 1 <= 9 and 0 <= ship_x + 1 <= 9 and cls.playing_field[ship_y - 2][
                        ship_x + 1] != '1':
                        cls.playing_field[ship_y - 1][ship_x + 1] = '#'
                    if 0 <= ship_y <= 9 and 0 <= ship_x - 2 <= 9 and cls.playing_field[ship_y][ship_x - 2] != '1':
                        cls.playing_field[ship_y][ship_x - 2] = '#'
                    if 0 <= ship_y <= 9 and 0 <= ship_x - 1 <= 9 and cls.playing_field[ship_y][ship_x - 1] != '1':
                        cls.playing_field[ship_y][ship_x - 1] = '#'
                    if 0 <= ship_y <= 9 and 0 <= ship_x <= 9 and cls.playing_field[ship_y][ship_x] != '1':
                        cls.playing_field[ship_y][ship_x] = '#'
                    if 0 <= ship_y <= 9 and 0 <= ship_x + 1 <= 9 and cls.playing_field[ship_y][ship_x + 1] != '1':
                        cls.playing_field[ship_y][ship_x + 1] = '#'

            else:
                index_y = []
                index_x = []
                num_ship_2 -= 1

                for item in range(10):
                    for itr in range(9):
                        if cls.playing_field[itr][item] == '0' and cls.playing_field[itr + 1][item] == '0':
                            if itr not in index_y:
                                index_y.append(itr)
                ship_y = random.choice(index_y) + 1

                for item in range(1, 11):
                    if cls.playing_field[ship_y - 1][item - 1] == '0' and cls.playing_field[ship_y][item - 1] == '0':
                        index_x.append(item)
                ship_x = random.choice(index_x)

                for item in range(12):
                    cls.playing_field[ship_y - 1][ship_x - 1] = '2'
                    cls.playing_field[ship_y][ship_x - 1] = '2'
                    if 0 <= ship_y - 2 <= 9 and 0 <= ship_x - 2 <= 9:
                        cls.playing_field[ship_y - 2][ship_x - 2] = '#'
                    if 0 <= ship_y - 2 <= 9 and 0 <= ship_x - 1 <= 9:
                        cls.playing_field[ship_y - 2][ship_x - 1] = '#'
                    if 0 <= ship_y - 2 <= 9 and 0 <= ship_x <= 9:
                        cls.playing_field[ship_y - 2][ship_x] = '#'
                    if 0 <= ship_y - 1 <= 9 and 0 <= ship_x - 2 <= 9:
                        cls.playing_field[ship_y - 1][ship_x - 2] = '#'
                    if 0 <= ship_y - 1 <= 9 and 0 <= ship_x <= 9:
                        cls.playing_field[ship_y - 1][ship_x] = '#'
                    if 0 <= ship_y <= 9 and 0 <= ship_x - 2 <= 9:
                        cls.playing_field[ship_y][ship_x - 2] = '#'
                    if 0 <= ship_y <= 9 and 0 <= ship_x <= 9:
                        cls.playing_field[ship_y][ship_x] = '#'
                    if 0 <= ship_y + 1 <= 9 and 0 <= ship_x - 2 <= 9:
                        cls.playing_field[ship_y + 1][ship_x - 2] = '#'
                    if 0 <= ship_y + 1 <= 9 and 0 <= ship_x - 1 <= 9:
                        cls.playing_field[ship_y + 1][ship_x - 1] = '#'
                    if 0 <= ship_y + 1 <= 9 and 0 <= ship_x <= 9:
                        cls.playing_field[ship_y + 1][ship_x] = '#'

        for itr in range(4):
            index_y = []
            index_x = []

            for item in range(1, 11):
                if cls.playing_field[item - 1].count('0') > 0:
                    index_y.append(item)
            ship_y = random.choice(index_y)

            for item in range(1, 11):
                if cls.playing_field[ship_y - 1][item - 1] == '0':
                    index_x.append(item)
            ship_x = random.choice(index_x)

            for item in range(9):
                cls.playing_field[ship_y - 1][ship_x - 1] = '1'
                if 0 <= ship_y - 2 <= 9 and 0 <= ship_x - 2 <= 9 and cls.playing_field[ship_y - 2][ship_x - 2] != '1':
                    cls.playing_field[ship_y - 2][ship_x - 2] = '#'
                if 0 <= ship_y - 2 <= 9 and 0 <= ship_x - 1 <= 9 and cls.playing_field[ship_y - 2][ship_x - 1] != '1':
                    cls.playing_field[ship_y - 2][ship_x - 1] = '#'
                if 0 <= ship_y - 2 <= 9 and 0 <= ship_x <= 9 and cls.playing_field[ship_y - 2][ship_x] != '1':
                    cls.playing_field[ship_y - 2][ship_x] = '#'
                if 0 <= ship_y - 1 <= 9 and 0 <= ship_x - 2 <= 9 and cls.playing_field[ship_y - 1][ship_x - 2] != '1':
                    cls.playing_field[ship_y - 1][ship_x - 2] = '#'
                if 0 <= ship_y - 1 <= 9 and 0 <= ship_x <= 9 and cls.playing_field[ship_y - 1][ship_x] != '1':
                    cls.playing_field[ship_y - 1][ship_x] = '#'
                if 0 <= ship_y <= 9 and 0 <= ship_x - 2 <= 9 and cls.playing_field[ship_y][ship_x - 2] != '1':
                    cls.playing_field[ship_y][ship_x - 2] = '#'
                if 0 <= ship_y <= 9 and 0 <= ship_x - 1 <= 9 and cls.playing_field[ship_y][ship_x - 1] != '1':
                    cls.playing_field[ship_y][ship_x - 1] = '#'
                if 0 <= ship_y <= 9 and 0 <= ship_x <= 9 and cls.playing_field[ship_y][ship_x] != '1':
                    cls.playing_field[ship_y][ship_x] = '#'

        for item in range(len(cls.playing_field)):
            for itr in range(len(cls.playing_field)):
                if cls.playing_field[item][itr] == '#':
                    cls.playing_field[item][itr] = 0
                elif cls.playing_field[item][itr] == '0':
                    cls.playing_field[item][itr] = 0
                else:
                    cls.playing_field[item][itr] = 1