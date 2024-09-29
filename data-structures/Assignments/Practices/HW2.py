# HW2
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

import random, os

class Course:
    '''
        >>> c1 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c2 = Course('CMPSC360', 'Discrete Mathematics', 3)
        >>> c1 == c2
        False
        >>> c3 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c1 == c3
        True
        >>> c1
        CMPSC132(3): Programming in Python II
        >>> c2
        CMPSC360(3): Discrete Mathematics
        >>> c3
        CMPSC132(3): Programming in Python II
        >>> c1 == None
        False
        >>> print(c1)
        CMPSC132(3): Programming in Python II
    '''
    def __init__(self, cid, cname, credits):
        # YOUR CODE STARTS HERE
        self.id = cid
        self.cname = cname
        self.credit = credits
        pass


    def __str__(self):
        # YOUR CODE STARTS HERE
        return f"{self.id}({self.credit}): {self.cname}" #in id(credit): Name format
        pass

    __repr__ = __str__

    def __eq__(self, other):
        # YOUR CODE STARTS HERE
        if isinstance(other, Course): # In any case where its not a course, return false
            return self.id == other.id 
        else:
            return False
        pass



class Catalog:
    ''' 
        >>> C = Catalog()
        >>> C.courseOfferings
        {}
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> C.courseOfferings
        {'CMPSC 132': CMPSC 132(3): Programming and Computation II, 'MATH 230': MATH 230(4): Calculus and Vector Analysis, 'PHYS 213': PHYS 213(2): General Physics, 'CMPEN 270': CMPEN 270(4): Digital Design, 'CMPSC 311': CMPSC 311(3): Introduction to Systems Programming, 'CMPSC 360': CMPSC 360(3): Discrete Mathematics for Computer Science}
        >>> C.removeCourse('CMPSC 360')
        'Course removed successfully'
        >>> C.courseOfferings
        {'CMPSC 132': CMPSC 132(3): Programming and Computation II, 'MATH 230': MATH 230(4): Calculus and Vector Analysis, 'PHYS 213': PHYS 213(2): General Physics, 'CMPEN 270': CMPEN 270(4): Digital Design, 'CMPSC 311': CMPSC 311(3): Introduction to Systems Programming}
        >>> isinstance(C.courseOfferings['CMPSC 132'], Course)
        True
    '''

    def __init__(self):
        # YOUR CODE STARTS HERE
        self.courseOfferings = {}
        pass

    def addCourse(self, cid, cname, credits):
        # YOUR CODE STARTS HERE
        if cid in self.courseOfferings.keys():
            return "Course already added"
        else:
            tempCourse = Course(cid, cname, credits)
            self.courseOfferings.update({tempCourse.id : tempCourse})
        pass

    def removeCourse(self, cid):
        # YOUR CODE STARTS HERE
        if cid not in self.courseOfferings.keys():
            return "Course not found"
        else:
            self.courseOfferings.pop(cid)
            return "Course removed successfully"
        pass

    def _loadCatalog(self, file):
        target_path = os.path.join(os.path.dirname(__file__), file)
        with open(target_path, "r") as f:
            course_info = f.readlines()
        # YOUR CODE STARTS HERE
        
        for x in course_info:
            x = x.strip()
            info = x.split(",")
            cid = info[0]
            cname = info[1]
            credit = info[2]
            self.addCourse(cid, cname, credit)


class Semester:
    '''
        >>> cmpsc131 = Course('CMPSC 131', 'Programming in Python I', 3)
        >>> cmpsc132 = Course('CMPSC 132', 'Programming in Python II', 3)
        >>> math230 = Course("MATH 230", 'Calculus', 4)
        >>> phys213 = Course("PHYS 213", 'General Physics', 2)
        >>> econ102 = Course("ECON 102", 'Intro to Economics', 3)
        >>> phil119 = Course("PHIL 119", 'Ethical Leadership', 3)
        >>> spr22 = Semester()
        >>> spr22
        No courses
        >>> spr22.addCourse(cmpsc132)
        >>> isinstance(spr22.courses['CMPSC 132'], Course)
        True
        >>> spr22.addCourse(math230)
        >>> spr22
        CMPSC 132; MATH 230
        >>> spr22.isFullTime
        False
        >>> spr22.totalCredits
        7
        >>> spr22.addCourse(phys213)
        >>> spr22.addCourse(econ102)
        >>> spr22.addCourse(econ102)
        'Course already added'
        >>> spr22.addCourse(phil119)
        >>> spr22.isFullTime
        True
        >>> spr22.dropCourse(phil119)
        >>> spr22.addCourse(Course("JAPNS 001", 'Japanese I', 4))
        >>> spr22.totalCredits
        16
        >>> spr22.dropCourse(cmpsc131)
        'No such course'
        >>> spr22.courses
        {'CMPSC 132': CMPSC 132(3): Programming in Python II, 'MATH 230': MATH 230(4): Calculus, 'PHYS 213': PHYS 213(2): General Physics, 'ECON 102': ECON 102(3): Intro to Economics, 'JAPNS 001': JAPNS 001(4): Japanese I}
    '''


    def __init__(self):
        # --- YOUR CODE STARTS HERE
        self.tool = Catalog() # uses the catalog object, since i want to reuse code
        self.courses = self.tool.courseOfferings

        pass



    def __str__(self):
        # YOUR CODE STARTS HERE
        retrnstr = ""
        for x in self.courses.keys():
            retrnstr += f"; {x}"
        if retrnstr == "":
            return "No courses"
        else:
            return retrnstr.removeprefix("; ")
        pass

    __repr__ = __str__

    def addCourse(self, course):
        # YOUR CODE STARTS HERE
        if isinstance(course, Course):
            return self.tool.addCourse(course.id, course.cname, course.credit) # no need to check if course is already in or not, we are using the previous class
        pass

    def dropCourse(self, course):
        # YOUR CODE STARTS HERE
        if isinstance(course, Course):
            if self.tool.removeCourse(course.id) == "Course not found":
                return "No such course"
            else:
                self.tool.removeCourse(course.id)
        pass

    @property
    def totalCredits(self):
        # YOUR CODE STARTS HERE
        sum = 0
        for x in self.courses.keys():
            sum += int(self.courses.get(x).credit)
        return sum
        pass

    @property
    def isFullTime(self):
        # YOUR CODE STARTS HERE
        return self.totalCredits >= 12
        pass

    
class Loan:
    '''
        >>> import random
        >>> random.seed(2)  # Setting seed to a fixed value, so you can predict what numbers the random module will generate
        >>> first_loan = Loan(4000)
        >>> first_loan
        Balance: $4000
        >>> first_loan.loan_id
        17412
        >>> second_loan = Loan(6000)
        >>> second_loan.amount
        6000
        >>> second_loan.loan_id
        22004
        >>> third_loan = Loan(1000)
        >>> third_loan.loan_id
        21124
    '''
    

    def __init__(self, amount):
        # YOUR CODE STARTS HERE
        self.amount = amount
        self.__getloanID
        pass


    def __str__(self):
        # YOUR CODE STARTS HERE
        return f"Balance: ${self.amount}"
        pass

    __repr__ = __str__


    @property
    def __getloanID(self):
        # YOUR CODE STARTS HERE
        self.loan_id = random.randrange(10000, 100000) # from 10,000 to 99,999
        pass


class Person:
    '''
        >>> p1 = Person('Jason Lee', '204-99-2890')
        >>> p2 = Person('Karen Lee', '247-01-2670')
        >>> p1
        Person(Jason Lee, ***-**-2890)
        >>> p1.get_ssn()
        '204-99-2890'
        >>> p2
        Person(Karen Lee, ***-**-2670)
        >>> p3 = Person('Karen Smith', '247-01-2670')
        >>> p3
        Person(Karen Smith, ***-**-2670)
        >>> p2 == p3
        True
        >>> p1 == p2
        False
    '''

    def __init__(self, name, ssn):
        # YOUR CODE STARTS HERE
        self.name = name
        self.__ssn = ssn 
        pass

    def __str__(self):
        # YOUR CODE STARTS HERE
        tempssn = self.get_ssn()
        return f"Person({self.name}, ***-**-{tempssn[-4:]})"
        pass

    __repr__ = __str__

    def get_ssn(self):
        # YOUR CODE STARTS HERE
        return self.__ssn
        pass

    def __eq__(self, other):
        # YOUR CODE STARTS HERE
        if isinstance(other, Person):
            return self.get_ssn() == other.get_ssn()
        else:
            return False
        pass

class Staff(Person):
    '''
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Staff('Jane Doe', '214-49-2890')
        >>> s1.getSupervisor
        >>> s2 = Staff('John Doe', '614-49-6590', s1)
        >>> s2.getSupervisor
        Staff(Jane Doe, 905jd2890)
        >>> s1 == s2
        False
        >>> s2.id
        '905jd6590'
        >>> p = Person('Jason Smith', '221-11-2629')
        >>> st1 = s1.createStudent(p)
        >>> isinstance(st1, Student)
        True
        >>> s2.applyHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        'Unsuccessful operation'
        >>> s2.removeHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        >>> st1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> st1.semesters
        {1: CMPSC 132}
        >>> s1.applyHold(st1)
        'Completed!'
        >>> st1.enrollCourse('CMPSC 360', C)
        'Unsuccessful operation'
        >>> st1.semesters
        {1: CMPSC 132}
        >>> print(StudentAccount.CREDIT_PRICE)
        1000
    '''
    def __init__(self, name, ssn, supervisor=None):
        # YOUR CODE STARTS HERE
        super().__init__(name, ssn)
        self.setSupervisor(supervisor)
        pass


    def __str__(self):
        # YOUR CODE STARTS HERE
        return f"Staff({self.name}, {self.id})"
        pass

    __repr__ = __str__


    @property
    def id(self):
        # YOUR CODE STARTS HERE
        name_pieces = self.name.split(" ")
        initials = ""
        for x in name_pieces:
            initials += x[0].lower()
        return f"905{initials}{self.get_ssn()[-4:]}"
        pass

    @property   
    def getSupervisor(self):
        # YOUR CODE STARTS HERE
        if not self.__supervisor == None:
            return self.__supervisor
        pass

    def setSupervisor(self, new_supervisor):
        # YOUR CODE STARTS HERE
        if isinstance(new_supervisor, Staff):
            self.__supervisor = new_supervisor
            return "Completed!"
        elif new_supervisor == None:
            self.__supervisor = new_supervisor # to complement the constructor case of None
        pass


    def applyHold(self, student):
        # YOUR CODE STARTS HERE
        if isinstance(student, Student):
            student.hold = True
            return "Completed!"
        pass

    def removeHold(self, student):
        # YOUR CODE STARTS HERE
        if isinstance(student, Student):
            student.hold = False
            return "Completed!"
        pass

    def unenrollStudent(self, student):
        # YOUR CODE STARTS HERE
        if isinstance(student, Student):
            student.active = False
            return "Completed!"
        pass

    def createStudent(self, person):
        # YOUR CODE STARTS HERE
        if isinstance(person, Person): # if not person class then not made
            newstudent = Student(person.name, person.get_ssn(), 'Freshman') #starts as freshmen as stated
            return newstudent
        pass




class Student(Person):
    '''
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1
        Student(Jason Lee, jl2890, Freshman)
        >>> s2 = Student('Karen Lee', '247-01-2670', 'Freshman')
        >>> s2
        Student(Karen Lee, kl2670, Freshman)
        >>> s1 == s2
        False
        >>> s1.id
        'jl2890'
        >>> s2.id
        'kl2670'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC 132}
        >>> s1.enrollCourse('CMPSC 360', C)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC 465', C)
        'Course not found'
        >>> s1.semesters
        {1: CMPSC 132; CMPSC 360}
        >>> s2.semesters
        {}
        >>> s1.enrollCourse('CMPSC 132', C)
        'Course already enrolled'
        >>> s1.dropCourse('CMPSC 360')
        'Course dropped successfully'
        >>> s1.dropCourse('CMPSC 360')
        'Course not found'
        >>> s1.semesters
        {1: CMPSC 132}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC 132, 2: No courses}
        >>> s1.enrollCourse('CMPSC 360', C)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC 132, 2: CMPSC 360}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC 132, 2: CMPSC 360, 3: No courses}
        >>> s1
        Student(Jason Lee, jl2890, Sophomore)
        >>> s1.classCode
        'Sophomore'
    '''
    def __init__(self, name, ssn, year):
        random.seed(1)
        # YOUR CODE STARTS HERE
        super().__init__(name, ssn)
        self.hold = False
        self.active = True
        self.__createStudentAccount()
        self.semesters = {}
        self.classCode = year



    def __str__(self):
        # YOUR CODE STARTS HERE
        return f"Student({self.name}, {self.id}, {self.classCode})"
        pass

    __repr__ = __str__

    def __createStudentAccount(self):
        # YOUR CODE STARTS HERE
        if self.active :
            self.account = StudentAccount(self)
        pass


    @property
    def id(self):
        # YOUR CODE STARTS HERE
        name_pieces = self.name.split(" ")
        initials = ""
        for x in name_pieces:
            initials += x[0].lower()
        return f"{initials}{self.get_ssn()[-4:]}" # abc1234 format
        pass

    def registerSemester(self):
        # YOUR CODE STARTS HERE
        if not self.active or self.hold:
            return "Unsuccessful operation"
        else:
            temp_sem = Semester()
            if len(self.semesters.keys()) == 0:
                i = 1
            else:
                i = max(self.semesters.keys()) + 1 # might need to add [:]
            self.semesters.update({i : temp_sem})
            if i > 2 :
                self.classCode = "Sophomore"
            elif i > 4 :
                self.classCode = "Junior"
            elif i > 6:
                self.classCode = "Senior"
        pass



    def enrollCourse(self, cid, catalog):
        # YOUR CODE STARTS HERE
        # Reads through a catalog object in order to pick out courses. The catalog object uses "cid" as keys in order to pick out certain classes. 
        # All that you need to do is add the Course obj to the Semester obj within the "semesters" dict.
        # Plan of action is to first check for all things that wouldn't allow the student to add a course, 
        # AKA if the account is not active or if the account has a hold, and also to check if the course is even within the catalogs keys.
        if isinstance(catalog, Catalog):
            if not self.active or self.hold:
                return "Unsuccessful operation"
            elif cid not in catalog.courseOfferings:
                return "Course not found"
            elif cid in  self.semesters.get(max(self.semesters.keys())).courses.keys():
                return "Course already enrolled"
            else:
                self.account.chargeAccount(int(catalog.courseOfferings.get(cid).credit) * int(StudentAccount.CREDIT_PRICE))
                self.semesters.get(max(self.semesters.keys())).addCourse(catalog.courseOfferings[cid])
                return "Course added successfully"
        pass

    def dropCourse(self, cid):
        # YOUR CODE STARTS HERE
        if not self.active or self.hold:
            return "Unsuccessful operation"
        elif cid not in self.semesters[max(self.semesters.keys())].courses.keys():
            return "Course not found"
        else:
            self.account.makePayment(int(self.semesters.get(max(self.semesters.keys())).courses.get(cid).credit) * int(StudentAccount.CREDIT_PRICE) / 2)
            self.semesters.get(max(self.semesters.keys())).tool.removeCourse(cid)
            return "Course dropped successfully"
        pass

    def getLoan(self, amount):
        # YOUR CODE STARTS HERE
        if not self.active:
            return "Unsuccessful operation"
        elif not self.semesters[max(self.semesters.keys())].isFullTime:
            return "Not full-time"
        else:
            newLoan = Loan(amount)
            self.account.makePayment(amount)
            self.account.loans.update({newLoan.loan_id : newLoan})
        pass




class StudentAccount:
    '''
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> s1.account.balance
        3000
        >>> s1.enrollCourse('CMPSC 360', C)
        'Course added successfully'
        >>> s1.account.balance
        6000
        >>> s1.enrollCourse('MATH 230', C)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C)
        'Course added successfully'
        >>> print(s1.account)
        Name: Jason Lee
        ID: jl2890
        Balance: $12000
        >>> s1.account.chargeAccount(100)
        12100
        >>> s1.account.balance
        12100
        >>> s1.account.makePayment(200)
        11900
        >>> s1.getLoan(4000)
        >>> s1.account.balance
        7900
        >>> s1.getLoan(8000)
        >>> s1.account.balance
        -100
        >>> s1.enrollCourse('CMPEN 270', C)
        'Course added successfully'
        >>> s1.account.balance
        3900
        >>> s1.dropCourse('CMPEN 270')
        'Course dropped successfully'
        >>> s1.account.balance
        1900.0
        >>> s1.account.loans
        {27611: Balance: $4000, 84606: Balance: $8000}
        >>> StudentAccount.CREDIT_PRICE = 1500
        >>> print(StudentAccount.CREDIT_PRICE)
        1500
        >>> s2 = Student('Thomas Wang', '123-45-6789', 'Freshman')
        >>> s2.registerSemester()
        >>> s2.enrollCourse('CMPSC 132', C)
        'Course added successfully'

        >>> s2.account.balance
        4500
        >>> s1.enrollCourse('CMPEN 270', C)
        'Course added successfully'
        >>> s1.account.balance
        7900.0
        
    '''
    
    CREDIT_PRICE = 1000


    def __init__(self, student):
        # YOUR CODE STARTS HERE
        self.student = student
        self.balance = 0
        self.loans = {}
        pass


    def __str__(self):
        # YOUR CODE STARTS HERE
        return f"Name: {self.student.name}\nID: {self.student.id}\nBalance: ${self.balance}"
        pass

    __repr__ = __str__


    def makePayment(self, amount):
        # YOUR CODE STARTS HERE
        self.balance -= amount
        return self.balance
        pass


    def chargeAccount(self, amount):
        # YOUR CODE STARTS HERE
        self.balance += amount
        return self.balance
        pass


def run_tests():
    import doctest

    # Run tests in all docstrings
    doctest.testmod(verbose=True)
    
    # Run tests per function - Uncomment the next line to run doctest by function. Replace Course with the name of the function you want to test
   # doctest.run_docstring_examples(Student, globals(), name='HW2',verbose=True)   

if __name__ == "__main__":
    run_tests()