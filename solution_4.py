class RomanNumber:
    '''
    Description of RomanNumber

    This class helps deal with roman numbers

    Class attributes:
        all_roman: dictionary with all possible roman symbols

    Attributes:
        rom_value: string with roman number

    Methods:
        decimal_number: turns roman number into arabic

    Static methods:
        is_roman: checks roman number for correctness
    '''
    all_roman = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, \
                      'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

    def __init__(self, roman=None):
        '''
        Initializes numbers

        args:
            roman: roman number
        '''
        self.rom_value = roman
        if self.is_roman(self.rom_value) == False:
            self.rom_value = None
            print('ошибка')

    @staticmethod
    def is_roman(value):
        '''
        checks roman number for correctness

        returns True if number is correct, False - else
        '''
        count = 0
        flag = True
        if len(value) > 3:
            for itr in range(len(value)):
                if value[itr] in RomanNumber.all_roman.keys():
                    if itr + 1 != len(value):
                        if value[itr] == value[itr + 1]:
                            count += 1
                        else:
                            count = 0
                    if count == 3:
                        flag = False

        if len(value) > 1:
            for itr in range(len(value)):
                if itr in RomanNumber.all_roman.keys():
                    if itr + 1 != len(value):
                        if (value[itr] == 'D' and value[itr+1] == 'D') or\
                                (value[itr] == 'L' and value[itr+1] == 'L') or \
                                (value[itr] == 'V' and value[itr + 1] == 'V'):
                            flag = False

        if len(value) > 1:
            for itr in range(len(value)):
                if itr in RomanNumber.all_roman.keys():
                    if value[itr:itr+2] not in RomanNumber.all_roman.keys():
                        if len(value[itr:itr+2]) == 2:
                            if RomanNumber.all_roman[value[itr]] < RomanNumber.all_roman[value[itr+1]]:
                                flag = False
                    else:
                        if value[itr-1] == value[itr]:
                            flag = False

        value_CM = value.count('CM')
        value_M = value.count('M')
        if value_M - value_CM > 3:
            flag = False

        for itr in value:
            if itr not in RomanNumber.all_roman.keys():
                flag = False

        if flag == False:
            return False
        else:
            return True

    def decimal_number(self):
        '''
        turns roman number into arabic

        returns arabic number
        '''
        arab_value = None
        cnt = 0
        if self.rom_value != None:
            arab_value = 0
            for num in range(len(self.rom_value)):
                for k, v in self.all_roman.items():
                    if cnt == num:
                        if self.rom_value[num:num + 2] == k and len(self.rom_value[num:num + 2]) == 2:
                            arab_value += v
                            cnt += 2
                            break
                        if self.rom_value[num:num + 1] == k:
                            arab_value += v
                            cnt += 1
        return arab_value

    def __repr__(self):
        return f'{self.rom_value}'

    def __str__(self):
        return f'{self.rom_value}'