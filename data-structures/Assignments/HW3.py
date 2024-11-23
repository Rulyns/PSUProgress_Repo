# HW3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

#NOTE: NOTICE!!!!! Exponentiation is still bugged, meaning that some calculations that require repeated exponents dont work yet. Aka 2^3^5
class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__
                          

#=============================================== Part I ==============================================

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
        >>> y = Stack()
        >>> y.push(-2)
        >>> y.push("+")
        >>> y.push(6)
        >>> y.push("*")

        # Check for what a "Mathmatical" Stack should look like. Remove any straggling spaces from the code

        >>> y.push(55)
        >>> y
        Top:Node(55)
        Stack:
        55
        *
        6
        +
        -2
        >>> Node(x.pop()).next
        >>> len(y)
        5
    '''
    def __init__(self):
        self.top = None
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__


    def isEmpty(self):
        # YOUR CODE STARTS HERE
        return self.top == None
        pass

    def __len__(self): #NOTE: Double check bugfix, but I thinks this is okay.
        # YOUR CODE STARTS HERE
        if self.isEmpty():
            return 0
        else:
            temp = self.top
            count = 0
            while temp is not None:
                count += 1
                temp = temp.next
        return count
        pass

    def push(self,value):
        # YOUR CODE STARTS HERE
        if self.isEmpty():
            self.top = Node(value)
        else:
            temp = self.top
            self.top = Node(value)
            self.top.next = temp
        pass

     
    def pop(self):
        # YOUR CODE STARTS HERE # Doubt in this code check for connection to newest head node NOTE: Doubt quenched!
        if self.isEmpty(): # if its empty, just dont do anything.
            return None
        else: # if its not empty, Make sure you grab the values you need, sever the Node, and return the value! NOTE: You might be able to del the node too.
            rtnValue = self.top.value
            newTop = self.top.next
            self.top.next = None
            self.top = newTop
            return rtnValue
        pass

    def peek(self):
        # YOUR CODE STARTS HERE NOTE: Uh..... Yeah!
        return self.top.value
        pass


#=============================================== Part II ==============================================

class Calculator:
    '''
        >>> x=Calculator()
        >>> x._isNumber(' 2.560 ')
        True
        >>> x._isNumber('7 56')
        False
        >>> x._isNumber('2.56p')
        False
        >>> x._isNumber("Supercalifragilisticexpialadocious") #NOTE: Eh? Eh?? I think I spelt it wrong though.
        False
        >>> x._isNumber("Supercalifragilisticexpialidocious") #NOTE: This is the right way of spelling
        False
        >>> x._isNumber("55 + 46") # I wonder if this would try to do the operation? #NOTE: Nooope.
        False
        >>> float(" 794732.8291     ") #NOTE: Have to check if just node works. Can never be too sure
        794732.8291
    '''
    def __init__(self):
        self.__expr = None


    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

    def _isNumber(self, txt):
        # YOUR CODE STARTS HERE
        try: #NOTE: Didn't know you could do this! Or at least I forgot, this is super useful!
            float(txt)
            return True
        except: 
            return False
        pass
    
    def _isAllowed(self, txt):
        '''
            >>> x=Calculator()
            >>> x._isAllowed(' 2 * ( 5 + 3 ) ^  2 + ) 1 + 4 (')
            True
            >>> x._isAllowed('( ( 2 ) )')
            True
            >>> x._isAllowed('2 * (( 5 +-3 ) ^ 2 + (1 + 4 ))')
            True
            >>> x._isAllowed('2 * + 4 - 5')
            False
            >>> x._isAllowed('2 -( -4 * 5) + 6')
            True
            >>> x._isAllowed('2*5.34+3^2+1+4')
            True
            >>> x._isAllowed('2 * 5 + 3 ^ + -2 + 1 + 4')
            False
            >>> x._isAllowed('     2 * 5 + 3  ^ * 2 + 1 + 4')
            False
            >>> x._isAllowed('2    5')
            False
            >>> x._isAllowed('25 +')
            False
            >>> x._isAllowed('2 *      5% + 3       ^ + -2 +1 +4')
            False
            >>> x._isAllowed('(2)-4')
            True
        '''
        # This method checks for operators next to operators and digits next to digits, and if the expression ends in an operator. Also removes parenthesis, This is okay because there should still be operators in between parenthesis, like (5) + (5), so strings like (5) (5) would instead return False instead of true.
        if isinstance(txt, str):
            txt = txt.replace("-", " - ") 
            txt = txt.replace("(", " ") # parenthesis removal
            txt = txt.replace(")", " ") # parenthesis removal
            txt = txt.replace("+", " + ")
            txt = txt.replace("/", " / ")
            txt = txt.replace("*", " * ")
            txt = txt.replace("^", " ^ ")
            txt = txt.split()
            qualifiedOperations = ["^", "+", "/", "*"] #"-" not in here because its a special case
            previous = ""
            for x in range(1, len(txt)):
                previous_minus = txt[x-1]
                if previous_minus in qualifiedOperations and txt[x] is "-" and self._isNumber(txt[x+1]):
                    txt[x] = txt[x] + txt[x+1]
                    del txt[x+1]
            for token in txt[:]:
                if token in qualifiedOperations and previous in qualifiedOperations:
                    return False
                if self._isNumber(token) and self._isNumber(previous):
                    return False
                previous = token
            if txt[-1] in qualifiedOperations:
                return False
            return True

    def _isBalanced(self, txt):
        '''
            >>> x = Calculator()
            >>> x._isBalanced(' 2 * ( 5 + 3 ) ^  2 + ) 1 + 4 (')
            False
            >>> x._isBalanced('2 * (           ( 5 +-3 ) ^ 2 + (1 + 4 ))')
            True
            
        '''
        # this function checks for the balancing of the parenthesis in the expression.
        if isinstance(txt, str):
            txt = txt.replace("-", " -") 
            txt = txt.replace("(", " ( ")
            txt = txt.replace(")", " ) ")
            txt = txt.replace("+", " + ")
            txt = txt.replace("/", " / ")
            txt = txt.replace("*", " * ")
            txt = txt.replace("^", " ^ ")
            txt = txt.split()
            parenthesis_count = 0
            for token in txt[:]:
                if token is "(":
                    parenthesis_count += 1
                if token is ")":
                    parenthesis_count -= 1
                if parenthesis_count < 0:
                    return False
            return parenthesis_count == 0

    def _getPostfix(self, txt):
        '''
            Required: _getPostfix must create and use a Stack for expression processing
            >>> x=Calculator()
            >>> x._getPostfix('     2 ^       4')
            '2.0 4.0 ^'
            >>> x._getPostfix('          2 ')
            '2.0'
            >>> x._getPostfix('2.1        * 5        + 3       ^ 2 +         1 +             4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('2*5.34+3^2+1+4')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('( .5 )')
            '0.5'
            >>> x._getPostfix ('( ( 2 ) )')
            '2.0'
            >>> x._getPostfix ('2 * (           ( 5 +-3 ) ^ 2 + (1 + 4 ))')
            '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('(2 * ( ( 5 + 3) ^ 2 + (1 + 4 )))')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('((2 *((5 + 3) ^ 2 + (1 +4 ))))')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('2* (       -5 + 3 ) ^2+ ( 1 +4 )')
            '2.0 -5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'
            >>> x._getPostfix('-2 +          3.5')
            '-2.0 3.5 +'

            # In invalid expressions, you might print an error message, adjust doctest accordingly
            # If you are veryfing the expression in calculate before passing to postfix, this cases are not necessary

            >>> x._getPostfix('2 * 5 + 3 ^ + -2 + 1 + 4')
            False
            >>> x._getPostfix('     2 * 5 + 3  ^ * 2 + 1 + 4')
            False
            >>> x._getPostfix('2    5')
            False
            >>> x._getPostfix('25 +')
            False
            >>> x._getPostfix(' 2 * ( 5      + 3 ) ^ 2 + ( 1 +4 ')
            False
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^  2 + ) 1 + 4 (')
            False
            >>> x._getPostfix('2 *      5% + 3       ^ + -2 +1 +4')
            False
            >>> x._getPostfix('2 *      $5 + 3       ^ + -$2 +1 +4')
            False
            >>> x._getPostfix("( -2/6) + ( 5$ *( 9.4 ))")
            False
        '''
        # YOUR CODE STARTS HERE
        postfixStack = Stack()  # method must use postfixStack to compute the postfix expression
        postfixExpression = ""
        qualifiedOperations = {"(": -1, "+" : 1, "-": 1, "/" : 2, "*" : 2,"^" : 3} #"-" is a special case so most of the operations will be fine except for when we encounter a negative
        #NOTE: Might have to change where this is, but check the string representation for where theres a random operator at the end of the inorder stack. There should never be something like that by the TOP of the stack, except for negative.
        if len(txt) == 0 or not self._isBalanced(txt) or not self._isAllowed(txt): # Both helper methods are called HERE to check viability.
            return False
        if isinstance(txt, str): #NOTE: Should be a string already
            txt = txt.replace("-", " - ") # Makes sure negatives arent connecting with other operators
            txt = txt.replace("(", " ( ")
            txt = txt.replace(")", " ) ")
            txt = txt.replace("+", " + ")
            txt = txt.replace("/", " / ")
            txt = txt.replace("*", " * ")
            txt = txt.replace("^", " ^ ")
            txt = txt.split() # Removes any trailing whitespace we began with (and added)
            #NOTE: Get rid of ALL unneccesary whitespace with this one, We wont need it for where we're going.
            #NOTE: txt is now a list you can iterate over, this is going to get pushed/popped into the stack until we get the postfix.
            # Parenthesis is a special case, so we should simply push it first into the stack
            for x in range(1, len(txt)):
                previous = txt[x-1]
                if previous in qualifiedOperations.keys() and txt[x] is "-" and self._isNumber(txt[x+1]):
                    txt[x] = txt[x] + txt[x+1]
                    del txt[x+1]
                if previous == "-" and self._isNumber(txt[x]) and x == 1:
                    txt[1] = "-"+txt[x]
                    del txt[0]
                    
            for token in txt[:]:
                # Any token thats a number automatically goes into the postfix.
                if self._isNumber(token):
                   postfixExpression += f"{float(token)} "
                # Any token thats not an operand has to go Through a process where it 1. Checks the stack for higher operations 2. Sees if the token can get added to the stack. 3. What needs to be removed from the stack in order for precidence to work.
                elif token in qualifiedOperations.keys() and postfixStack.isEmpty():
                    # if token is an operator and the stack is empty
                    postfixStack.push(token)
                elif token in qualifiedOperations.keys() and not postfixStack.isEmpty():
                    # is token is an operator and there are items in the stack
                    while not postfixStack.isEmpty() and 0 < qualifiedOperations.get(token) <= qualifiedOperations.get(postfixStack.peek()):
                        # while there are items in the stack, pop out any items that need to leave the stack in order for the new token to get placed into the stack
                        postfixExpression += f"{postfixStack.pop()} "
                    postfixStack.push(token)
                    # ^ this push above me is for the token to finally go into the stack after all other operations have been done
                elif token is ")":
                    while postfixStack.peek() is not "(":
                        # while there are items in the stack, pop out any items that need to leave the stack in order for the new token to get placed into the stack
                        postfixExpression += f"{postfixStack.pop()} "
                    postfixStack.pop()
                else:
                    return False
            while not postfixStack.isEmpty():
                    # add any straggling operations to the end of the stack.
                    postfixExpression += f"{postfixStack.pop()} "
            return postfixExpression.strip()
        pass

    @property
    def calculate(self):
        '''
            calculate must call _getPostfix
            calculate must create and use a Stack to compute the final result as shown in the video lecture
            
            >>> x=Calculator()
            >>> x.setExpr('4        + 3 -       2')
            >>> x.calculate
            5.0
            >>> x.setExpr('-2 +          3.5')
            >>> x.calculate
            1.5
            >>> x.setExpr('      4 +           3.65  - 2        / 2')
            >>> x.calculate
            6.65
            >>> x.setExpr('23 / 12 - 223 + 5.25      * 4 * 3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr('2-3*4')
            >>> x.calculate
            -10.0
            >>> x.setExpr('4-5^2-6-2')
            >>> x.calculate
            -29.0
            >>> x.setExpr('7^2^3')
            >>> x.calculate
            5764801.0
            >>> x.setExpr(' 3 * ((( 10 - 2*3 )) )')
            >>> x.calculate
            12.0
            >>> x.setExpr('      8 / 4 * (3 - 2.45 * ( 4   - 2 ^ 3 )       ) + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr('2 * ( 4 +        2 * (         5 - 3 ^ 2 ) + 1 ) + 4')
            >>> x.calculate
            -2.0
            >>> x.setExpr(' 2.5 +         3 * (2 + ( 3.0) * ( 5^2-2 * 3 ^ ( 2 )         ) * ( 4 ) ) * ( 2 / 8 + 2 * ( 3 - 1 /3 ) ) - 2 / 3^ 2')
            >>> x.calculate
            1442.7777777777778
            

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            >>> x.setExpr(" 4 ++ 3+ 2") 
            >>> x.calculate
            >>> x.setExpr("4  3 +2")
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 *( 2 - 3 * 2 ) )')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * / ( 2 - 3 * 2 )')
            >>> x.calculate
            >>> x.setExpr(' ) 2 ( *10 - 3 * ( 2 - 3 * 2 ) ')
            >>> x.calculate
            >>> x.setExpr('(    3.5 ) ( 15 )') 
            >>> x.calculate
            >>> x.setExpr('3 ( 5) - 15 + 85 ( 12)') 
            >>> x.calculate
            >>> x.setExpr("( -2/6) + ( 5 ( ( 9.4 )))") 
            >>> x.calculate
            >>> x.setExpr("( -2/6) + ( 5$ *( 9.4 ))") 
            >>> x.calculate
        '''

        if not isinstance(self.__expr,str) or len(self.__expr)<=0 or not self._getPostfix(self.__expr):
            return None
        else:
            qualifiedOperations = ["^", "+", "-", "/", "*"]
            calcStack = Stack()   # method must use calcStack to compute the  expression

            # YOUR CODE STARTS HERE
            # calculates expressions based of pop, pop, push. 
            PostExpression = self._getPostfix(self.getExpr)
            PostList = PostExpression.split(" ")
            for x in PostList:
                if self._isNumber(x):
                    calcStack.push(float(x))
                elif x in qualifiedOperations:
                    token1 = calcStack.pop()
                    token2 = calcStack.pop()
                    if x == "+":
                        ans = token2 + token1
                    elif x == "-":
                        ans = token2 - token1
                    elif x == "*":
                        ans = token2 * token1
                    elif x == "/":
                        ans = token2 / token1
                    elif x == "^":
                        ans = token2 ** token1
                    calcStack.push(float(ans))
            return calcStack.peek()
        pass

#=============================================== Part III ==============================================

class AdvancedCalculator:
    '''
        >>> C = AdvancedCalculator()
        >>> C.states == {}
        True
        >>> C.setExpression('a = 5;b = 7 + a;a = 7;c = a + b;c = a * 0;return c')
        >>> C.calculateExpressions() == {'a = 5': {'a': 5.0}, 'b = 7 + a': {'a': 5.0, 'b': 12.0}, 'a = 7': {'a': 7.0, 'b': 12.0}, 'c = a + b': {'a': 7.0, 'b': 12.0, 'c': 19.0}, 'c = a * 0': {'a': 7.0, 'b': 12.0, 'c': 0.0}, '_return_': 0.0}
        True
        >>> C.states == {'a': 7.0, 'b': 12.0, 'c': 0.0}
        True
        >>> C.setExpression('x1 = 5;x2 = 7 * ( x1 - 1 );x1 = x2 - x1;return x2 + x1 ^ 3')
        >>> C.states == {}
        True
        >>> C.calculateExpressions() == {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        True
        >>> print(C.calculateExpressions())
        {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        >>> C.states == {'x1': 23.0, 'x2': 28.0}
        True
        >>> C.setExpression('x1 = 5 * 5 + 97;x2 = 7 * ( x1 / 2 );x1 = x2 * 7 / x1;return x1 * ( x2 - 5 )')
        >>> C.calculateExpressions() == {'x1 = 5 * 5 + 97': {'x1': 122.0}, 'x2 = 7 * ( x1 / 2 )': {'x1': 122.0, 'x2': 427.0}, 'x1 = x2 * 7 / x1': {'x1': 24.5, 'x2': 427.0}, '_return_': 10339.0}
        True
        >>> C.states == {'x1': 24.5, 'x2': 427.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;C = A + B;A = 20;D = A + B + C;return D - A')
        >>> C.calculateExpressions() == {'A = 1': {'A': 1.0}, 'B = A + 9': {'A': 1.0, 'B': 10.0}, 'C = A + B': {'A': 1.0, 'B': 10.0, 'C': 11.0}, 'A = 20': {'A': 20.0, 'B': 10.0, 'C': 11.0}, 'D = A + B + C': {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}, '_return_': 21.0}
        True
        >>> C.states == {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;2C = A + B;A = 20;D = A + B + C;return D + A')
        >>> C.calculateExpressions() is None
        True
        >>> C.states == {}
        True
    '''
    def __init__(self):
        self.expressions = ''
        self.states = {}

    def setExpression(self, expression):
        self.expressions = expression
        self.states = {}

    def _isVariable(self, word):
        '''
            >>> C = AdvancedCalculator()
            >>> C._isVariable('volume')
            True
            >>> C._isVariable('4volume')
            False
            >>> C._isVariable('volume2')
            True
            >>> C._isVariable('vol%2')
            False
        '''
        # YOUR CODE STARTS HERE
        # checks if the first char is part of alphabet and not a number, the rest can be alphabet or a number.
        return str.isalpha(word[0]) and str.isalnum(word)
        pass
       

    def _replaceVariables(self, expr):
        '''
            >>> C = AdvancedCalculator()
            >>> C.states = {'x1': 23.0, 'x2': 28.0}
            >>> C._replaceVariables('1')
            '1'
            >>> C._replaceVariables('105 + x')
            >>> C._replaceVariables('7 * ( x1 - 1 )')
            '7 * ( 23.0 - 1 )'
            >>> C._replaceVariables('x2 - x1')
            '28.0 - 23.0'
        '''
        # YOUR CODE STARTS HERE
        if not isinstance(expr, str):
            return None
        checkexpr = expr.split()
        rtnexpr = ""
        for x in checkexpr[:]:
            if self._isVariable(f'{x}') and x not in self.states.keys():
                return None
            elif x in self.states.keys():
                rtnexpr += f"{self.states.get(x)} "
            else:
                rtnexpr += f"{x} "
        return rtnexpr.strip()
        pass

    
    def calculateExpressions(self):
        self.states = {} 
        calcObj = Calculator()     # method must use calcObj to compute each expression
        # YOUR CODE STARTS HERE
        expression_dict = {}
        expressionlst = self.expressions.split(";")
        for expression in expressionlst[:]:
            tokens = expression.split("=")
            if expression[0:6].lower() == "return":
                tokens = expression.split(" ", 1) # splits only once for return, since the expression isnt return = expression
            if tokens[0].lower() == "return":
                # only for return
                calcObj.setExpr(self._replaceVariables(tokens[1].strip()))
                expression_dict.update({"_return_": calcObj.calculate})
            elif self._isVariable(tokens[0].strip()) and tokens[0] != "return":
                # specifically only for expressions that arent the return statement.
                calcObj.setExpr(self._replaceVariables(tokens[1].strip()))
                self.states.update({tokens[0].strip(): calcObj.calculate})
            else:
                # wipe states and return none in case of error
                self.states = {} 
                return None
            dict_snapshot = dict(self.states)
            if not expression.startswith("return"):
                expression_dict.update({expression: dict_snapshot})
        return expression_dict
        pass


def run_tests():
    import doctest

    # Run tests in all docstrings
    #doctest.testmod(verbose=True)
    
    # Run tests per function - Uncomment the next line to run doctest by function. Replace Stack with the name of the function you want to test
    doctest.run_docstring_examples(Calculator.calculate, globals(), name='HW3',verbose=True)   

if __name__ == "__main__":
    run_tests()