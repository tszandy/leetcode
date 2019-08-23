class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        self.game_string = board[0]+board[1]+board[2]

        X_win = len(list(filter(lambda x:x,map(lambda x:self.check_equal(x,'X'),self.win_sequences()))))>=1
        O_win = len(list(filter(lambda x:x,map(lambda x:self.check_equal(x,'O'),self.win_sequences()))))>=1

        if X_win and O_win:
            print(1)
            return False

        count_X = len(list(filter(lambda x:x=='X',self.game_string)))
        count_O = len(list(filter(lambda x:x=='O',self.game_string)))
        if (X_win and count_X==count_O) or (O_win and count_X == count_O+1) :
            print(2)
            return False

        if not (count_X==count_O or count_X==count_O+1):
            print(3)
            return False

        count_move = len(list(filter(lambda x:x!=' ',self.game_string)))
        if not(count_move<8 and (X_win or O_win)):
            print(4)
            return False


        return True

    def win_sequences(self):
        return [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

    def check_equal(self,sequence,target):
        a,b,c = sequence
        if self.game_string[a]==self.game_string[b] and self.game_string[b]==self.game_string[c] and self.game_string[a]==target:
            return True
        else:
            return False
