class NavalBattle:
    '''
       Description of game naval battle

       This class helps to play game

       Class attributes:
           playing_field: list of lists with field (0 - none, 1 - ship)

       Attributes:
            shot_marker: symbol of each player that marks their shots

       Methods:
             shot: selected player shots at playing filed. Player can either shot or miss

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
        new_field = [[],[],[],[],[],[],[],[],[],[]]
        for item in range(len(NavalBattle.playing_field)):
            for itr in range(len(NavalBattle.playing_field[item])):
                if NavalBattle.playing_field[item][itr] == 1 or NavalBattle.playing_field[item][itr] == 0:
                    new_field[item].append('~')
                else:
                    new_field[item].append(NavalBattle.playing_field[item][itr])
        for item in range(len(new_field)):
            for itr in new_field[item]:
                print(itr,end='')
            print('')

    def shot(self, x, y):
        '''
        selected player shots at playing filed. Player can either shot or miss

        args:
            x: x coordinate
            y: y coordinate
        '''
        if self.playing_field[y-1][x-1] == 1:
            self.playing_field[y-1][x-1] = self.shot_marker
            print('попал')
        if self.playing_field[y-1][x-1] == 0:
            self.playing_field[y-1][x-1] = 'o'
            print('мимо')