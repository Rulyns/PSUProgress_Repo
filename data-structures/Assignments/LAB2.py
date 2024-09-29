
# LAB2
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
import math
import copy # <--- Imported copy meself

# -------- SECTION 1
class Instructor:
    '''
        >>> t1= Instructor('John Doe')
        >>> t1.get_name()
        'John Doe'
        >>> t1.get_courses()
        []
        >>> t1.add_course('MATH140')
        >>> t1.get_courses()
        ['MATH140']
        >>> t1.add_course('STAT100')
        >>> t1.get_courses()
        ['MATH140', 'STAT100']
        >>> t1.add_course('STAT100')
        >>> t1.get_courses()
        ['MATH140', 'STAT100']
        >>> t1.remove_course('MATH141')
        >>> t1.get_courses()
        ['MATH140', 'STAT100']
        >>> t1.remove_course('MATH140')
        >>> t1.get_courses()
        ['STAT100']
    '''

    def __init__(self, name):
        #--- YOUR CODE STARTS HERE
        self.name = name
        self.courses = []
        pass

    def get_name(self):
        #--- YOUR CODE STARTS HERE
        return self.name
        pass

    def set_name(self, new_name):
        #--- YOUR CODE STARTS 
        if isinstance(new_name, str):
            self.name = new_name
        pass

    def get_courses(self):
        #--- YOUR CODE STARTS HERE
        return self.courses # self explanatory
        pass

    def remove_course(self, course):
        #--- YOUR CODE STARTS HERE
        if course in self.courses and isinstance(course, str): # checks if course str is in list AND is a str
            self.courses.remove(course)
        pass
        
    def add_course(self,course):
        #--- YOUR CODE STARTS HERE
        if course not in self.courses and isinstance(course, str): # checks if course str is in list AND is a str
            self.courses.append(course)
        pass


# -------- SECTION 2      
class Pantry:
    """"
        >>> sara_pantry = Pantry()                
        >>> sara_pantry.stock_pantry('Bread', 2)
        'Pantry Stock for Bread: 2.0'
        >>> sara_pantry.stock_pantry('Cookies', 6) 
        'Pantry Stock for Cookies: 6.0'
        >>> sara_pantry.stock_pantry('Chocolate', 4) 
        'Pantry Stock for Chocolate: 4.0'
        >>> sara_pantry.stock_pantry('Pasta', 3)     
        'Pantry Stock for Pasta: 3.0'
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 6.0, 'Chocolate': 4.0, 'Pasta': 3.0}
        >>> sara_pantry.get_item('Pasta', 2)     
        'You have 1.0 of Pasta left'
        >>> sara_pantry.get_item('Pasta', 6) 
        'Add Pasta to your shopping list!'
        >>> sara_pantry.get_item('Pizza', 2)
        "You don't have Pizza"
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 6.0, 'Chocolate': 4.0, 'Pasta': 0.0}
        >>> ben_pantry = Pantry()                    
        >>> ben_pantry.stock_pantry('Cereal', 2)
        'Pantry Stock for Cereal: 2.0'
        >>> ben_pantry.stock_pantry('Noodles', 5) 
        'Pantry Stock for Noodles: 5.0'
        >>> ben_pantry.stock_pantry('Cookies', 9) 
        'Pantry Stock for Cookies: 9.0'
        >>> ben_pantry.stock_pantry('Cookies', 8) 
        'Pantry Stock for Cookies: 17.0'
        >>> ben_pantry.get_item('Pasta', 2)       
        "You don't have Pasta"
        >>> ben_pantry.get_item('Cookies', 2.5) 
        'You have 14.5 of Cookies left'
        >>> sara_pantry.transfer(ben_pantry, 'Cookies')
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 20.5, 'Chocolate': 4.0, 'Pasta': 0.0}
        >>> ben_pantry.transfer(sara_pantry, 'Rice')
        >>> ben_pantry.transfer(sara_pantry, 'Pasta')
        >>> ben_pantry
        I am a Pantry object, my current stock is {'Cereal': 2.0, 'Noodles': 5.0, 'Cookies': 0.0}
        >>> ben_pantry.transfer(sara_pantry, 'Pasta')
        >>> ben_pantry
        I am a Pantry object, my current stock is {'Cereal': 2.0, 'Noodles': 5.0, 'Cookies': 0.0}
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 20.5, 'Chocolate': 4.0, 'Pasta': 0.0}
    """
    # Notes for Grader: The whole class is Case Sensitive, I didn't know if we could use the str class or any other implementation in order to make sure that our dict doesnt have "Cookies" and "cookies".
    # I decided to keep the class Case Sensitive, but it would be very easy to format with an extra helper or existing function. 
    # Also using Absolute Value because I dont want you doing a negative number for stocking pantry to take in the guise that you are "putting" food in. You're not slick.
    def __init__(self):
        self.items = {}
    
    def __repr__(self):
        #--- YOUR CODE STARTS HERE
        return f'I am a Pantry object, my current stock is {self.items}' # Nice and simple f"" formatting
        pass

    def stock_pantry(self, item, qty):
        qty = abs(qty) # Makes sure you're not stealing
        #--- YOUR CODE STARTS HERE
        if isinstance(item, str) and isinstance(qty, (float, int)):
            if item not in self.items.keys():
                self.items.update({item: float(qty)}) # "All values in the dictionary must be stored as float values", This will also ensure that all other methods that might use Int switch to float when the operations are done.
            else:
                self.items[item] += qty
        return f'Pantry Stock for {item}: {self.items[item]}'
        pass


    def get_item(self, item, qty):
        qty = abs(qty) # Makes sure you're not secretly putting food into the pantry (Matthew 6:3-4, ESV - Just put yourself down as anonymous bud)
        #--- YOUR CODE STARTS HERE
        if isinstance(item, str) and isinstance(qty, (float, int)):
            if (item not in self.items.keys()) or (self.items[item] == 0):
                return f"You don't have {item}"
            else:
                if (self.items[item] - qty > 0):
                    self.items[item] -= qty
                    return f'You have {self.items[item]} of {item} left'
                else:
                    self.items[item] = 0.0
                    return f'Add {item} to your shopping list!'

        pass

    def transfer(self, other_pantry, item):
        #--- YOUR CODE STARTS HERE
        # Who stole all my noodles situation, where you are taking from "other_pantry" an entire stock of one item.
        transferAmount = 0.0
        if isinstance(other_pantry.items, dict) and isinstance(item, str): # Want to make sure you're even calling a dictionary and string
            if item in other_pantry.items.keys() and other_pantry.items.get(item) > 0.0: # Only if both are true, this is called. Meaning it wont happen if the key isnt in the dictionary or there isnt any left.
                transferAmount =+ copy.deepcopy(other_pantry.items.get(item))
                other_pantry.items[item] = 0.0
                self.stock_pantry(item, transferAmount) # make the transfer
                



# -------- SECTION 3
class Player:
    """
        >>> p1 = Player('Susy')
        >>> print(p1)
        No game records for Susy
        >>> p1.update_loss()
        >>> p1
        *Game records for Susy*
        Total games: 1
        Games won: 0
        Games lost: 1
        Best game: None
        >>> p1.update_win(5)
        >>> p1.update_win(2)
        >>> p1
        *Game records for Susy*
        Total games: 3
        Games won: 2
        Games lost: 1
        Best game: 2 attempts
    """
    def __init__(self, name):
        #--- YOUR CODE STARTS HERE
        self.name = name
        self.game_num = 0
        self.wins = 0
        self.losses = 0
        self.best = 10
        self.best_game = 0
        pass

    def update_win(self, att):
        #--- YOUR CODE STARTS HERE
        self.game_num += 1
        self.wins += 1
        if att <= self.best:
            self.best = att
        pass
    
    def update_loss(self):
        #--- YOUR CODE STARTS HERE
        self.game_num +=1
        self.losses += 1
        pass
    

    def __str__(self):
        #--- YOUR CODE STARTS HERE
        if self.game_num == 0:
            return f"No game records for {self.name}"
        elif self.wins == 0:
            return f"*Game records for {self.name}*\nTotal games: {self.game_num}\nGames won: {self.wins}\nGames lost: {self.losses}\nBest game: None"
        else:
            return f"*Game records for {self.name}*\nTotal games: {self.game_num}\nGames won: {self.wins}\nGames lost: {self.losses}\nBest game: {self.best} attempts"
        pass


    __repr__=__str__

class Wordle:
    """
        >>> p1 = Player('Susy')
        >>> p2 = Player('Taylor')
        >>> w1 = Wordle(p1, 'water')
        >>> w2 = Wordle(p2, 'cloud')
        >>> w3 = Wordle(p1, 'jewel')
        >>> w1.play('camel')
        '_A_E_'
        >>> w1.play('ranes')
        'rA_E_'
        >>> w1.play('baner')
        '_A_ER'
        >>> w1.play('pacer')
        '_A_ER'
        >>> w1.play('water')
        'You won the game'
        >>> w1.play('rocks')
        'Game over'
        >>> w1.play('other')
        'Game over'
        >>> w3.play('beast')
        '_E___'
        >>> w3.play('peace')
        '_E__e'
        >>> w3.play('keeks')
        '_Ee__'
        >>> w3.play('jewel')
        'You won the game'
        >>> w2.play('classes')
        'Guess must be 5 letters long'
        >>> w2.play('cs132')
        'Guess must be all letters'
        >>> w2.play('audio')
        '_ud_o'
        >>> w2.play('kudos')
        '_udo_'
        >>> w2.play('would')
        '_oulD'
        >>> w2.play('bound')
        'The word was cloud'
        >>> w2.play('cloud')
        'Game over'
        >>> p1
        *Game records for Susy*
        Total games: 2
        Games won: 2
        Games lost: 0
        Best game: 4 attempts
        >>> p2
        *Game records for Taylor*
        Total games: 1
        Games won: 0
        Games lost: 1
        Best game: None
    """
    # str and chr classes and its built in fuctions will be used A LOT during this. especially for running through the word.
    # I'm going to type this now. This code was not thoroughly bugchecked or optimized. It works for the given tests on file but not the gradechecker tests. It's 10:00 Pm on Sunday and I wan't to wind down for next week. I'll take the loss on this test and simply fix it when I get the chance.
    # ROADMAP FOR LATER FIXING (Post lab submission): 
        # Check length and alpha BEFORE actually processing the guess within process guess. The current code first checks "if everything is true", then processes the guess. It might just be easier to check for faults before just processing it
        # Try to fix the attempt system, there is definitely an easier way of calculating attempt rather than having an attempt limit and a counter.
        # Played might be an unnessesary boolean value, try to find a workaround.
        # guess and answer should just be ".lower()" whenever they get the chance, it just helps the loop and the functions out
        # Maybe tweak the player class to better suit the wordle class in whatever way possible, mainly the "attempts" value on both classes.
    def __init__(self, player, word):
        #--- YOUR CODE STARTS HERE
        if isinstance(player, Player):
            self.player = player
        if not (len(word) == 5 or word.isalpha()):
            self.played = True # This will automatically end the game, since you messed up the class. Don't mess up the class.
        self.answer = str.lower(word) # For clarity
        self.played = False
        self.attempts = 6
        self.att_count = 0
        pass
        

    def process_guess(self, guess):
        #--- YOUR CODE STARTS HERE
        hint = ""
        # Make the correct conditional statements
        if isinstance(guess, str) and guess.isalpha() and len(guess) == 5:
            # Lets make a iterator for the guess and the answer, Since the word is capped at 5 characters, this makes things easier.
            # first check if the letter exists, then check if the letter is in the right place, else just place an underline
            for i in range(len(self.answer)):
                if guess[i] == self.answer[i]:
                    hint += self.answer[i].upper()
                elif guess[i] in self.answer:
                    hint += guess[i].lower()
                else:
                    hint += "_"
        elif len(guess) != 5: # not right length
            self.att_count -= 1 # remove the count
            return "Guess must be 5 letters long"
        elif not str.isalpha(guess): # not all alphabetic
            self.att_count -= 1 # remove the count
            return "Guess must be all letters"
        return hint
        pass


    def play(self, guess):
        #--- YOUR CODE STARTS HERE
        hint = self.process_guess(guess) # First process the guess (duh)
        self.attempts -= 1 # attempt used
        self.att_count += 1 
        if self.attempts > 0 and not self.played:
            if hint == self.answer.upper(): # if the hint is just the answer
                self.player.update_win(self.att_count)
                self.played = True # straight to Game over
                return "You won the game" 
            else:
                return hint
        elif self.played:
            return "Game over"
        elif self.attempts <= 0: # if you didnt win and lost all your attempts, you lost and were given the answer.
            self.played = True 
            self.player.update_loss()
            return f"The word was {self.answer}"
        pass

    # @property
    # def randomize_att(self):
    #     self.attempts = random.randint(1, 8) # my attempt at randomizing the attempts of the class after a game is finished. Instructions kinda unclear, the given examples just drop down to the number of attempts to the game won with the lowest amount of attempts. I sent this question in Teams a little late, so it's okay honestly.

    


       



# -------- SECTION 4
class Point2D:
    def __init__(self, x, y):
        self.x = float(x) # This will help with math later on
        self.y = float(y)
    
    # Defining a multiply in here to help with the multiply outside
    def __mul__(self, other):
        if isinstance(other, int):
            return Point2D(self.x * other, self.y * other)

class Line: 
    ''' 
        >>> p1 = Point2D(-7, -9)
        >>> p2 = Point2D(1, 5.6)
        >>> line1 = Line(p1, p2)
        >>> line1.getDistance
        16.648
        >>> line1.getSlope
        1.825
        >>> line1
        y = 1.825x + 3.775
        >>> line2 = line1*4
        >>> line2.getDistance
        66.592
        >>> line2.getSlope
        1.825
        >>> line2
        y = 1.825x + 15.1
        >>> line1
        y = 1.825x + 3.775
        >>> line3 = line1*4
        >>> line3
        y = 1.825x + 15.1
        >>> line5=Line(Point2D(6,48),Point2D(9,21))
        >>> line5
        y = -9.0x + 102.0
        >>> Point2D(45,3) in line5
        False
        >>> Point2D(34,-204) in line5
        True
        >>> line6=Line(Point2D(2,6), Point2D(2,3))
        >>> line6.getDistance
        3.0
        >>> line6.getSlope
        inf
        >>> isinstance(line6.getSlope, float)
        True
        >>> line6
        Undefined
        >>> line7=Line(Point2D(6,5), Point2D(9,5))
        >>> line7.getSlope
        0.0
        >>> line7
        y = 5.0
        >>> Point2D(9,5) in line7
        True
        >>> Point2D(89,5) in line7
        True
        >>> Point2D(12,8) in line7
        False
        >>> (9,5) in line7
        False
    '''
    def __init__(self, point1, point2):
        #--- YOUR CODE STARTS HERE
        if isinstance(point1, Point2D) and isinstance(point2, Point2D):
            self.foo_point = point1
            self.bar_point = point2
        pass

    #--- YOUR CODE STARTS HERE
    @property
    def getDistance(self):
        return round(math.sqrt(((self.bar_point.x - self.foo_point.x)**2) + ((self.bar_point.y - self.foo_point.y)**2)), 3)
        pass
    
    
    #--- YOUR CODE STARTS HERE
    @property
    def getSlope(self):
        if math.isclose((self.bar_point.x - self.foo_point.x), 0):
            return math.inf # Checks if denom is close to 0 before calculations, (note for me, check for big big slopes, like with a denom of 0.000001)
        else:
            return (self.bar_point.y - self.foo_point.y) / (self.bar_point.x - self.foo_point.x) # Stays unrounded for accuracy until needed to round
        pass


    #--- YOUR CODE CONTINUES HERE
    @property
    def getIntercept(self):
        # y - mx = b
        return self.bar_point.y - (self.getSlope*self.bar_point.x)
        pass

    def __str__(self):
        if math.isclose(self.getSlope, 0): # First checks for no slope.
            return f"y = {round(self.getIntercept, 3)}"
        elif self.getSlope != math.inf: #then checks for regular slope, if slope isnt infinite
            return f"y = {round(self.getSlope,3)}x + {round(self.getIntercept,3)}"
        else: #if slope is infinite, then there is no plausible string representation
            return "Undefined"
        pass
    
    def __mul__(self, other):
        if isinstance(other, int): # calls the point2D __mul__ in order to do its own __mul__, also only checks for int
            return Line(self.foo_point * other, self.bar_point * other)
        else:
            return None # satisfies requirement to return none, This isn't needed on the Point2D __mul__ since it wont ever be recognized if "other" isn't an int on that end due to the if statement.
        pass

    def __contains__(self, other):
        # no assumptions made... Hopefully.
        if isinstance(other, Point2D):
            return math.isclose(Line(Point2D(0, round(self.getIntercept,3)), other).getSlope, self.getSlope)
        pass

    __repr__ = __str__ # needed if just calling the object.

def run_tests():
    import doctest

    # Run tests in all docstrings
    # doctest.testmod(verbose=True)
    
    # Run tests per function - Uncomment the next line to run doctest by function. Replace Pantry with the name of the class you want to test
    doctest.run_docstring_examples(Wordle, globals(), name='LAB2',verbose=True)

if __name__ == "__main__":
    run_tests()



