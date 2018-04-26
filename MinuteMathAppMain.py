import kivy
kivy.require('1.10.0')
from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition
from kivy.uix.label import Label
from kivy.app import App
from kivy.clock import Clock
import random
import datetime

#Issues
'''
1. When the game is over, the timer says "Game Over!" as expected, but the user still has to ask another question to
actually trigger the screen to change in 5 seconds. I need to figure out how to prevent the user from answering anything.
One solution is to take all of the keypad values and make them "blank". I could Also edit the Button to say "continue",
and this would dynamically force the screen to once pressed. Make all of the buttons blank except for the continue Button,
or "Get results" Button, and dynamically have the screen revert back to the options screen.
'''





class Easy_Addition_Level(Screen):
    '''
    #Docstring: Class that will generate random questions
    in the easy addition section of the application. It can
    generate numbers from 1, 20 for the user to add. It will
    generate a neatly formatted question in the application.
    I will pass this parent class to the main application class.
    '''

    def __init__(self, **kwargs):
        '''
        #Docstring: in this init method, set the attributes
        that can be passed to children as the first number
        that we want to generate, the second number that
        needs to be generated, the users score, the number
        of questions they've been asked, the number of
        correct answers they give, the number of minutes
        they have to complete the problems and the number
        of seconds they have to complete the problems. We
        can increment these values later when we call instances
        of this class
        '''
        super(Easy_Addition_Level, self).__init__(**kwargs)
        self.easy_addition_first_num = random.randint(1, 20)
        self.easy_addition_second_num = random.randint(1, 20)
        self.easy_addition_score = 0
        self.easy_addition_questions = 0
        self.easy_addition_correct_answers = 0
        self.easy_addition_minutes = 1
        self.easy_addition_seconds = 0
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def easy_addition_generate_numbers(self, *args):
        '''
        #Docstring: This function will generate the random numbers using
        the random.randint() function. The numbers will be
        between 1, 20 since this is the easy level.

        param: *args: I pass *args as the parameter because we will call
        this function with the Clock.schedule_interval function. Since we
        will repeatedly call this function, this means that there will be
        an arbitrary number of arguments made to this function call, which
        is why I pass *args
        '''
        self.easy_addition_first_num = random.randint(1, 20)
        self.easy_addition_second_num = random.randint(1, 20)
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_addition(self):
        '''
        #Docstring: This method will enable us to call
        the generate_numbers() method in order to generate
        random numbers to add together for the easy addition
        questions. I use the Clock.schedule_interval function
        to make calls to the generate_number() function so that
        we can get new numbers each time the user clicks the Button
        to get a new question.
        '''
        Clock.schedule_interval(self.easy_addition_generate_numbers, 1)
        self.easy_addition_question = '{} + {}'.format(self.easy_addition_first_num, self.easy_addition_second_num)
        self.easy_addition_answer = self.easy_addition_first_num + self.easy_addition_second_num
        self.easy_addition_answer = str(self.easy_addition_answer)
######################################################################################################################################################################

class Easy_Subtraction_Level(Screen):
    '''
    #Docstring: Class that will generate random questions
    in the easy subtraction section of the application. It can
    generate numbers from 1, 20 for the user to subtract. It will
    generate a neatly formatted question in the application.
    I will pass this parent class to the main application class.
    '''

    def __init__(self, **kwargs):
        '''
        #Docstring: in this init method, set the attributes
        that can be passed to children as the first number
        that we want to generate, the second number that
        needs to be generated, the users score, the number
        of questions they've been asked, the number of
        correct answers they give, the number of minutes
        they have to complete the problems and the number
        of seconds they have to complete the problems. We
        can increment these values later when we call instances
        of this class
        '''
        super(Easy_Subtraction_Level, self).__init__(**kwargs)
        self.easy_subtraction_first_num = random.randint(1, 20)
        self.easy_subtraction_second_num = random.randint(1, 20)
        self.easy_subtraction_score = 0
        self.easy_subtraction_questions = 0
        self.easy_subtraction_correct_answers = 0
        self.easy_subtraction_minutes = 1
        self.easy_subtraction_seconds = 0
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def easy_subtraction_generate_numbers(self, *args):
        '''
        #Docstring: This function will generate the random numbers using
        the random.randint() function. The numbers will be
        between 1, 20 since this is the easy level.

        param: *args: I pass *args as the parameter because we will call
        this function with the Clock.schedule_interval function. Since we
        will repeatedly call this function, this means that there will be
        an arbitrary number of arguments made to this function call, which
        is why I pass *args
        '''
        self.easy_subtraction_first_num = random.randint(1, 20)
        self.easy_subtraction_second_num = random.randint(1, 20)

        #If statement, specifies that if the first number is less than the second number,
        #I will call the function again. This will ensure that the user will never have to,
        #answer a negative value. This will keep the questions 'easy'...
        if self.easy_subtraction_first_num < self.easy_subtraction_second_num:
            self.easy_subtraction_generate_numbers()
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_subtraction(self):
        '''
        #Docstring: This method will enable us to call
        the generate_numbers() method in order to generate
        random numbers to add together for the easy subtraction
        questions. I use the Clock.schedule_interval function
        to make calls to the generate_number() function so that
        we can get new numbers each time the user clicks the Button
        to get a new question.
        '''
        Clock.schedule_interval(self.easy_subtraction_generate_numbers, 1)

        #If the first number is smaller than the second number, call the function to get a new number
        if self.easy_subtraction_first_num < self.easy_subtraction_second_num:
            self.easy_subtraction_generate_numbers()

        self.easy_subtraction_question = '{} - {}'.format(self.easy_subtraction_first_num, self.easy_subtraction_second_num)
        self.easy_subtraction_answer = self.easy_subtraction_first_num - self.easy_subtraction_second_num
        self.easy_subtraction_answer = str(self.easy_subtraction_answer)
#######################################################################################################################################################################

class Easy_Multiplication_Level(Screen):
    '''
    #Docstring: Class that will generate random questions
    in the easy multiplication section of the application. It can
    generate numbers from 1, 12 for the user to multiply. It will
    generate a neatly formatted question in the application.
    I will pass this parent class to the main application class.
    '''

    def __init__(self, **kwargs):
        '''
        #Docstring: in this init method, set the attributes
        that can be passed to children as the first number
        that we want to generate, the second number that
        needs to be generated, the users score, the number
        of questions they've been asked, the number of
        correct answers they give, the number of minutes
        they have to complete the problems and the number
        of seconds they have to complete the problems. We
        can increment these values later when we call instances
        of this class
        '''
        super(Easy_Multiplication_Level, self).__init__(**kwargs)
        self.easy_multiplication_first_num = random.randint(1, 12)
        self.easy_multiplication_second_num = random.randint(1, 12)
        self.easy_multiplication_score = 0
        self.easy_multiplication_questions = 0
        self.easy_multiplication_correct_answers = 0
        self.easy_multiplication_minutes = 1
        self.easy_multiplication_seconds = 0
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def easy_multiplication_generate_numbers(self, *args):
        '''
        #Docstring: This function will generate the random numbers using
        the random.randint() function. The numbers will be
        between 1, 20 since this is the easy level.

        param: *args: I pass *args as the parameter because we will call
        this function with the Clock.schedule_interval function. Since we
        will repeatedly call this function, this means that there will be
        an arbitrary number of arguments made to this function call, which
        is why I pass *args
        '''
        self.easy_multiplication_first_num = random.randint(1, 12)
        self.easy_multiplication_second_num = random.randint(1, 12)
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_multiplication(self):
        '''
        #Docstring: This method will enable us to call
        the generate_numbers() method in order to generate
        random numbers to add together for the easy multiplication
        questions. I use the Clock.schedule_interval function
        to make calls to the generate_number() function so that
        we can get new numbers each time the user clicks the Button
        to get a new question.
        '''
        Clock.schedule_interval(self.easy_multiplication_generate_numbers, 1)

        self.easy_multiplication_question = '{} x {}'.format(self.easy_multiplication_first_num, self.easy_multiplication_second_num)
        self.easy_multiplication_answer = self.easy_multiplication_first_num * self.easy_multiplication_second_num
        self.easy_multiplication_answer = str(self.easy_multiplication_answer)
######################################################################################################################################################################
class Easy_Division_Level(Screen):
    '''
    #Docstring: Class that will generate random questions
    in the easy division section of the application. It can
    generate numbers from 1, 20 for the user to subtract. It will
    generate a neatly formatted question in the application.
    I will pass this parent class to the main application class.
    '''

    def __init__(self, **kwargs):
        '''
        #Docstring: in this init method, set the attributes
        that can be passed to children as the first number
        that we want to generate, the second number that
        needs to be generated, the users score, the number
        of questions they've been asked, the number of
        correct answers they give, the number of minutes
        they have to complete the problems and the number
        of seconds they have to complete the problems. We
        can increment these values later when we call instances
        of this class
        '''
        super(Easy_Division_Level, self).__init__(**kwargs)
        self.easy_division_first_num = random.randint(1, 10)
        self.easy_division_second_num = random.randint(1, 10)
        self.easy_division_score = 0
        self.easy_division_questions = 0
        self.easy_division_correct_answers = 0
        self.easy_division_minutes = 1
        self.easy_division_seconds = 0
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def easy_division_generate_numbers(self, *args):
        '''
        #Docstring: This function will generate the random numbers using
        the random.randint() function. The numbers will be
        between 1, 20 since this is the easy level.

        param: *args: I pass *args as the parameter because we will call
        this function with the Clock.schedule_interval function. Since we
        will repeatedly call this function, this means that there will be
        an arbitrary number of arguments made to this function call, which
        is why I pass *args
        '''
        self.easy_division_first_num = random.randint(1, 10)
        self.easy_division_second_num = random.randint(1, 10)

        #If statement, specifies that if the first number is less than the second number,
        #I will call the function again. This will ensure that the user will never have to,
        #answer a negative value. This will keep the questions 'easy'...
        if self.easy_division_first_num < self.easy_division_second_num:
            self.easy_division_generate_numbers()

        elif self.easy_division_first_num % self.easy_division_second_num != 0:
            self.easy_division_generate_numbers()

        elif self.easy_division_second_num == 0 or self.easy_division_first_num == 0:
            self.easy_division_generate_numbers()
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------
    def easy_division(self):
        '''
        #Docstring: This method will enable us to call
        the generate_numbers() method in order to generate
        random numbers to add together for the easy division
        questions. I use the Clock.schedule_interval function
        to make calls to the generate_number() function so that
        we can get new numbers each time the user clicks the Button
        to get a new question.
        '''
        Clock.schedule_interval(self.easy_division_generate_numbers, 1)

        if self.easy_division_first_num < self.easy_division_second_num:
            self.easy_division_generate_numbers()

        elif self.easy_division_first_num % self.easy_division_second_num != 0:
            self.easy_division_generate_numbers()

        self.easy_division_question = '{} / {}'.format(self.easy_division_first_num, self.easy_division_second_num)
        self.easy_division_answer = self.easy_division_first_num / self.easy_division_second_num
        self.easy_division_answer = '{0:.0f}'.format(self.easy_division_answer)
        self.easy_division_answer = str(self.easy_division_answer)
######################################################################################################################################################################

class Intermediate_Addition_Level(Screen):
    '''
    #Docstring: Class that will generate random questions
    in the intermediate addition section of the application. It can
    generate numbers from 1, 20 for the user to add. It will
    generate a neatly formatted question in the application.
    I will pass this parent class to the main application class.
    '''

    def __init__(self, **kwargs):
        '''
        #Docstring: in this init method, set the attributes
        that can be passed to children as the first number
        that we want to generate, the second number that
        needs to be generated, the users score, the number
        of questions they've been asked, the number of
        correct answers they give, the number of minutes
        they have to complete the problems and the number
        of seconds they have to complete the problems. We
        can increment these values later when we call instances
        of this class
        '''
        super(Intermediate_Addition_Level, self).__init__(**kwargs)
        self.intermediate_addition_first_num = random.randint(1, 20)
        self.intermediate_addition_second_num = random.randint(1, 20)
        self.intermediate_addition_score = 0
        self.intermediate_addition_questions = 0
        self.intermediate_addition_correct_answers = 0
        self.intermediate_addition_minutes = 1
        self.intermediate_addition_seconds = 0
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def intermediate_addition_generate_numbers(self, *args):
        '''
        #Docstring: This function will generate the random numbers using
        the random.randint() function. The numbers will be
        between 1, 20 since this is the intermediate level.

        param: *args: I pass *args as the parameter because we will call
        this function with the Clock.schedule_interval function. Since we
        will repeatedly call this function, this means that there will be
        an arbitrary number of arguments made to this function call, which
        is why I pass *args
        '''
        self.intermediate_addition_first_num = random.randint(1, 150)
        self.intermediate_addition_second_num = random.randint(1, 150)
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_addition(self):
        '''
        #Docstring: This method will enable us to call
        the generate_numbers() method in order to generate
        random numbers to add together for the intermediate addition
        questions. I use the Clock.schedule_interval function
        to make calls to the generate_number() function so that
        we can get new numbers each time the user clicks the Button
        to get a new question.
        '''
        Clock.schedule_interval(self.intermediate_addition_generate_numbers, 1)
        self.intermediate_addition_question = '{} + {}'.format(self.intermediate_addition_first_num, self.intermediate_addition_second_num)
        self.intermediate_addition_answer = self.intermediate_addition_first_num + self.intermediate_addition_second_num
        self.intermediate_addition_answer = str(self.intermediate_addition_answer)
######################################################################################################################################################################

class Intermediate_Subtraction_Level(Screen):
    '''
    #Docstring: Class that will generate random questions
    in the intermediate subtraction section of the application. It can
    generate numbers from 1, 20 for the user to subtract. It will
    generate a neatly formatted question in the application.
    I will pass this parent class to the main application class.
    '''

    def __init__(self, **kwargs):
        '''
        #Docstring: in this init method, set the attributes
        that can be passed to children as the first number
        that we want to generate, the second number that
        needs to be generated, the users score, the number
        of questions they've been asked, the number of
        correct answers they give, the number of minutes
        they have to complete the problems and the number
        of seconds they have to complete the problems. We
        can increment these values later when we call instances
        of this class
        '''
        super(Intermediate_Subtraction_Level, self).__init__(**kwargs)
        self.intermediate_subtraction_first_num = random.randint(1, 150)
        self.intermediate_subtraction_second_num = random.randint(1, 150)
        self.intermediate_subtraction_score = 0
        self.intermediate_subtraction_questions = 0
        self.intermediate_subtraction_correct_answers = 0
        self.intermediate_subtraction_minutes = 1
        self.intermediate_subtraction_seconds = 0
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def intermediate_subtraction_generate_numbers(self, *args):
        '''
        #Docstring: This function will generate the random numbers using
        the random.randint() function. The numbers will be
        between 1, 20 since this is the intermediate level.

        param: *args: I pass *args as the parameter because we will call
        this function with the Clock.schedule_interval function. Since we
        will repeatedly call this function, this means that there will be
        an arbitrary number of arguments made to this function call, which
        is why I pass *args
        '''
        self.intermediate_subtraction_first_num = random.randint(1, 150)
        self.intermediate_subtraction_second_num = random.randint(1, 150)

        #If statement, specifies that if the first number is less than the second number,
        #I will call the function again. This will ensure that the user will never have to,
        #answer a negative value. This will keep the questions 'intermediate'...
        if self.intermediate_subtraction_first_num < self.intermediate_subtraction_second_num:
            self.intermediate_subtraction_generate_numbers()
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_subtraction(self):
        '''
        #Docstring: This method will enable us to call
        the generate_numbers() method in order to generate
        random numbers to add together for the intermediate subtraction
        questions. I use the Clock.schedule_interval function
        to make calls to the generate_number() function so that
        we can get new numbers each time the user clicks the Button
        to get a new question.
        '''
        Clock.schedule_interval(self.intermediate_subtraction_generate_numbers, 1)

        if self.intermediate_subtraction_first_num < self.intermediate_subtraction_second_num:
            self.intermediate_subtraction_generate_numbers()

        self.intermediate_subtraction_question = '{} - {}'.format(self.intermediate_subtraction_first_num, self.intermediate_subtraction_second_num)
        self.intermediate_subtraction_answer = self.intermediate_subtraction_first_num - self.intermediate_subtraction_second_num
        self.intermediate_subtraction_answer = str(self.intermediate_subtraction_answer)
#######################################################################################################################################################################

class Intermediate_Multiplication_Level(Screen):
    '''
    #Docstring: Class that will generate random questions
    in the intermediate multiplication section of the application. It can
    generate numbers from 1, 12 for the user to multiply. It will
    generate a neatly formatted question in the application.
    I will pass this parent class to the main application class.
    '''

    def __init__(self, **kwargs):
        '''
        #Docstring: in this init method, set the attributes
        that can be passed to children as the first number
        that we want to generate, the second number that
        needs to be generated, the users score, the number
        of questions they've been asked, the number of
        correct answers they give, the number of minutes
        they have to complete the problems and the number
        of seconds they have to complete the problems. We
        can increment these values later when we call instances
        of this class
        '''
        super(Intermediate_Multiplication_Level, self).__init__(**kwargs)
        self.intermediate_multiplication_first_num = random.randint(1, 30)
        self.intermediate_multiplication_second_num = random.randint(1, 30)
        self.intermediate_multiplication_score = 0
        self.intermediate_multiplication_questions = 0
        self.intermediate_multiplication_correct_answers = 0
        self.intermediate_multiplication_minutes = 1
        self.intermediate_multiplication_seconds = 0
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def intermediate_multiplication_generate_numbers(self, *args):
        '''
        #Docstring: This function will generate the random numbers using
        the random.randint() function. The numbers will be
        between 1, 20 since this is the intermediate level.

        param: *args: I pass *args as the parameter because we will call
        this function with the Clock.schedule_interval function. Since we
        will repeatedly call this function, this means that there will be
        an arbitrary number of arguments made to this function call, which
        is why I pass *args
        '''
        self.intermediate_multiplication_first_num = random.randint(1, 30)
        self.intermediate_multiplication_second_num = random.randint(1, 30)
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_multiplication(self):
        '''
        #Docstring: This method will enable us to call
        the generate_numbers() method in order to generate
        random numbers to add together for the intermediate multiplication
        questions. I use the Clock.schedule_interval function
        to make calls to the generate_number() function so that
        we can get new numbers each time the user clicks the Button
        to get a new question.
        '''
        Clock.schedule_interval(self.intermediate_multiplication_generate_numbers, 1)

        self.intermediate_multiplication_question = '{} x {}'.format(self.intermediate_multiplication_first_num, self.intermediate_multiplication_second_num)
        self.intermediate_multiplication_answer = self.intermediate_multiplication_first_num * self.intermediate_multiplication_second_num
        self.intermediate_multiplication_answer = str(self.intermediate_multiplication_answer)
######################################################################################################################################################################

class Intermediate_Division_Level(Screen):
    '''
    #Docstring: Class that will generate random questions
    in the intermediate division section of the application. It can
    generate numbers from 1, 20 for the user to subtract. It will
    generate a neatly formatted question in the application.
    I will pass this parent class to the main application class.
    '''

    def __init__(self, **kwargs):
        '''
        #Docstring: in this init method, set the attributes
        that can be passed to children as the first number
        that we want to generate, the second number that
        needs to be generated, the users score, the number
        of questions they've been asked, the number of
        correct answers they give, the number of minutes
        they have to complete the problems and the number
        of seconds they have to complete the problems. We
        can increment these values later when we call instances
        of this class
        '''
        super(Intermediate_Division_Level, self).__init__(**kwargs)
        self.intermediate_division_first_num = random.randint(1, 30)
        self.intermediate_division_second_num = random.randint(1, 30)
        self.intermediate_division_score = 0
        self.intermediate_division_questions = 0
        self.intermediate_division_correct_answers = 0
        self.intermediate_division_minutes = 1
        self.intermediate_division_seconds = 0
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def intermediate_division_generate_numbers(self, *args):
        '''
        #Docstring: This function will generate the random numbers using
        the random.randint() function. The numbers will be
        between 1, 20 since this is the intermediate level.

        param: *args: I pass *args as the parameter because we will call
        this function with the Clock.schedule_interval function. Since we
        will repeatedly call this function, this means that there will be
        an arbitrary number of arguments made to this function call, which
        is why I pass *args
        '''
        self.intermediate_division_first_num = random.randint(1, 30)
        self.intermediate_division_second_num = random.randint(1, 30)

        #If statement, specifies that if the first number is less than the second number,
        #I will call the function again. This will ensure that the user will never have to,
        #answer a negative value. This will keep the questions 'intermediate'...
        if self.intermediate_division_first_num < self.intermediate_division_second_num:
            self.intermediate_division_generate_numbers()

        elif self.intermediate_division_first_num % self.intermediate_division_second_num != 0:
            self.intermediate_division_generate_numbers()

        elif self.intermediate_division_second_num == 0 or self.intermediate_division_first_num == 0:
            self.intermediate_division_generate_numbers()
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------
    def intermediate_division(self):
        '''
        #Docstring: This method will enable us to call
        the generate_numbers() method in order to generate
        random numbers to add together for the intermediate division
        questions. I use the Clock.schedule_interval function
        to make calls to the generate_number() function so that
        we can get new numbers each time the user clicks the Button
        to get a new question.
        '''
        Clock.schedule_interval(self.intermediate_division_generate_numbers, 1)

        if self.intermediate_division_first_num < self.intermediate_division_second_num:
            self.intermediate_division_generate_numbers()

        elif self.intermediate_division_first_num % self.intermediate_division_second_num != 0:
            self.intermediate_division_generate_numbers()

        self.intermediate_division_question = '{} / {}'.format(self.intermediate_division_first_num, self.intermediate_division_second_num)
        self.intermediate_division_answer = self.intermediate_division_first_num / self.intermediate_division_second_num
        self.intermediate_division_answer = '{0:.0f}'.format(self.intermediate_division_answer)
        self.intermediate_division_answer = str(self.intermediate_division_answer)
#######################################################################################################################################################################

class Expert_Addition_Level(Screen):
    '''
    #Docstring: Class that will generate random questions
    in the expert addition section of the application. It can
    generate numbers from 1, 20 for the user to add. It will
    generate a neatly formatted question in the application.
    I will pass this parent class to the main application class.
    '''

    def __init__(self, **kwargs):
        '''
        #Docstring: in this init method, set the attributes
        that can be passed to children as the first number
        that we want to generate, the second number that
        needs to be generated, the users score, the number
        of questions they've been asked, the number of
        correct answers they give, the number of minutes
        they have to complete the problems and the number
        of seconds they have to complete the problems. We
        can increment these values later when we call instances
        of this class
        '''
        super(Expert_Addition_Level, self).__init__(**kwargs)
        self.expert_addition_first_num = random.randint(1, 150)
        self.expert_addition_second_num = random.randint(1, 150)
        self.expert_addition_score = 0
        self.expert_addition_questions = 0
        self.expert_addition_correct_answers = 0
        self.expert_addition_minutes = 1
        self.expert_addition_seconds = 0
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def expert_addition_generate_numbers(self, *args):
        '''
        #Docstring: This function will generate the random numbers using
        the random.randint() function. The numbers will be
        between 1, 20 since this is the expert level.

        param: *args: I pass *args as the parameter because we will call
        this function with the Clock.schedule_interval function. Since we
        will repeatedly call this function, this means that there will be
        an arbitrary number of arguments made to this function call, which
        is why I pass *args
        '''
        self.expert_addition_first_num = random.randint(1, 150)
        self.expert_addition_second_num = random.randint(1, 150)
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_addition(self):
        '''
        #Docstring: This method will enable us to call
        the generate_numbers() method in order to generate
        random numbers to add together for the expert addition
        questions. I use the Clock.schedule_interval function
        to make calls to the generate_number() function so that
        we can get new numbers each time the user clicks the Button
        to get a new question.
        '''
        Clock.schedule_interval(self.expert_addition_generate_numbers, 1)
        self.expert_addition_question = '{} + {}'.format(self.expert_addition_first_num, self.expert_addition_second_num)
        self.expert_addition_answer = self.expert_addition_first_num + self.expert_addition_second_num
        self.expert_addition_answer = str(self.expert_addition_answer)
######################################################################################################################################################################

class Expert_Subtraction_Level(Screen):
    '''
    #Docstring: Class that will generate random questions
    in the expert subtraction section of the application. It can
    generate numbers from 1, 20 for the user to subtract. It will
    generate a neatly formatted question in the application.
    I will pass this parent class to the main application class.
    '''

    def __init__(self, **kwargs):
        '''
        #Docstring: in this init method, set the attributes
        that can be passed to children as the first number
        that we want to generate, the second number that
        needs to be generated, the users score, the number
        of questions they've been asked, the number of
        correct answers they give, the number of minutes
        they have to complete the problems and the number
        of seconds they have to complete the problems. We
        can increment these values later when we call instances
        of this class
        '''
        super(Expert_Subtraction_Level, self).__init__(**kwargs)
        self.expert_subtraction_first_num = random.randint(1, 150)
        self.expert_subtraction_second_num = random.randint(1, 150)
        self.expert_subtraction_score = 0
        self.expert_subtraction_questions = 0
        self.expert_subtraction_correct_answers = 0
        self.expert_subtraction_minutes = 1
        self.expert_subtraction_seconds = 0
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def expert_subtraction_generate_numbers(self, *args):
        '''
        #Docstring: This function will generate the random numbers using
        the random.randint() function. The numbers will be
        between 1, 20 since this is the expert level.

        param: *args: I pass *args as the parameter because we will call
        this function with the Clock.schedule_interval function. Since we
        will repeatedly call this function, this means that there will be
        an arbitrary number of arguments made to this function call, which
        is why I pass *args
        '''
        self.expert_subtraction_first_num = random.randint(1, 150)
        self.expert_subtraction_second_num = random.randint(1, 150)

        #If statement, specifies that if the first number is less than the second number,
        #I will call the function again. This will ensure that the user will never have to,
        #answer a negative value. This will keep the questions 'expert'...
        if self.expert_subtraction_first_num < self.expert_subtraction_second_num:
            self.expert_subtraction_generate_numbers()
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_subtraction(self):
        '''
        #Docstring: This method will enable us to call
        the generate_numbers() method in order to generate
        random numbers to add together for the expert subtraction
        questions. I use the Clock.schedule_interval function
        to make calls to the generate_number() function so that
        we can get new numbers each time the user clicks the Button
        to get a new question.
        '''
        Clock.schedule_interval(self.expert_subtraction_generate_numbers, 1)

        if self.expert_subtraction_first_num < self.expert_subtraction_second_num:
            self.expert_subtraction_generate_numbers()

        self.expert_subtraction_question = '{} - {}'.format(self.expert_subtraction_first_num, self.expert_subtraction_second_num)
        self.expert_subtraction_answer = self.expert_subtraction_first_num - self.expert_subtraction_second_num
        self.expert_subtraction_answer = str(self.expert_subtraction_answer)
#######################################################################################################################################################################

class Expert_Multiplication_Level(Screen):
    '''
    #Docstring: Class that will generate random questions
    in the expert multiplication section of the application. It can
    generate numbers from 1, 12 for the user to multiply. It will
    generate a neatly formatted question in the application.
    I will pass this parent class to the main application class.
    '''

    def __init__(self, **kwargs):
        '''
        #Docstring: in this init method, set the attributes
        that can be passed to children as the first number
        that we want to generate, the second number that
        needs to be generated, the users score, the number
        of questions they've been asked, the number of
        correct answers they give, the number of minutes
        they have to complete the problems and the number
        of seconds they have to complete the problems. We
        can increment these values later when we call instances
        of this class
        '''
        super(Expert_Multiplication_Level, self).__init__(**kwargs)
        self.expert_multiplication_first_num = random.randint(1, 30)
        self.expert_multiplication_second_num = random.randint(1, 30)
        self.expert_multiplication_score = 0
        self.expert_multiplication_questions = 0
        self.expert_multiplication_correct_answers = 0
        self.expert_multiplication_minutes = 1
        self.expert_multiplication_seconds = 0
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def expert_multiplication_generate_numbers(self, *args):
        '''
        #Docstring: This function will generate the random numbers using
        the random.randint() function. The numbers will be
        between 1, 20 since this is the expert level.

        param: *args: I pass *args as the parameter because we will call
        this function with the Clock.schedule_interval function. Since we
        will repeatedly call this function, this means that there will be
        an arbitrary number of arguments made to this function call, which
        is why I pass *args
        '''
        self.expert_multiplication_first_num = random.randint(1, 30)
        self.expert_multiplication_second_num = random.randint(1, 30)
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_multiplication(self):
        '''
        #Docstring: This method will enable us to call
        the generate_numbers() method in order to generate
        random numbers to add together for the expert multiplication
        questions. I use the Clock.schedule_interval function
        to make calls to the generate_number() function so that
        we can get new numbers each time the user clicks the Button
        to get a new question.
        '''
        Clock.schedule_interval(self.expert_multiplication_generate_numbers, 1)

        self.expert_multiplication_question = '{} x {}'.format(self.expert_multiplication_first_num, self.expert_multiplication_second_num)
        self.expert_multiplication_answer = self.expert_multiplication_first_num * self.expert_multiplication_second_num
        self.expert_multiplication_answer = str(self.expert_multiplication_answer)
######################################################################################################################################################################

class Expert_Division_Level(Screen):
    '''
    #Docstring: Class that will generate random questions
    in the expert division section of the application. It can
    generate numbers from 1, 20 for the user to subtract. It will
    generate a neatly formatted question in the application.
    I will pass this parent class to the main application class.
    '''

    def __init__(self, **kwargs):
        '''
        #Docstring: in this init method, set the attributes
        that can be passed to children as the first number
        that we want to generate, the second number that
        needs to be generated, the users score, the number
        of questions they've been asked, the number of
        correct answers they give, the number of minutes
        they have to complete the problems and the number
        of seconds they have to complete the problems. We
        can increment these values later when we call instances
        of this class
        '''
        super(Expert_Division_Level, self).__init__(**kwargs)
        self.expert_division_first_num = random.randint(1, 30)
        self.expert_division_second_num = random.randint(1, 30)
        self.expert_division_score = 0
        self.expert_division_questions = 0
        self.expert_division_correct_answers = 0
        self.expert_division_minutes = 1
        self.expert_division_seconds = 0
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def expert_division_generate_numbers(self, *args):
        '''
        #Docstring: This function will generate the random numbers using
        the random.randint() function. The numbers will be
        between 1, 20 since this is the expert level.

        param: *args: I pass *args as the parameter because we will call
        this function with the Clock.schedule_interval function. Since we
        will repeatedly call this function, this means that there will be
        an arbitrary number of arguments made to this function call, which
        is why I pass *args
        '''
        self.expert_division_first_num = random.randint(1, 30)
        self.expert_division_second_num = random.randint(1, 30)

        #If statement, specifies that if the first number is less than the second number,
        #I will call the function again. This will ensure that the user will never have to,
        #answer a negative value. This will keep the questions 'expert'...
        if self.expert_division_first_num < self.expert_division_second_num:
            self.expert_division_generate_numbers()

        elif self.expert_division_first_num % self.expert_division_second_num != 0:
            self.expert_division_generate_numbers()

        elif self.expert_division_second_num == 0 or self.expert_division_first_num == 0:
            self.expert_division_generate_numbers()
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------
    def expert_division(self):
        '''
        #Docstring: This method will enable us to call
        the generate_numbers() method in order to generate
        random numbers to add together for the expert division
        questions. I use the Clock.schedule_interval function
        to make calls to the generate_number() function so that
        we can get new numbers each time the user clicks the Button
        to get a new question.
        '''
        Clock.schedule_interval(self.expert_division_generate_numbers, 1)

        if self.expert_division_first_num < self.expert_division_second_num:
            self.expert_division_generate_numbers()

        elif self.expert_division_first_num % self.expert_division_second_num != 0:
            self.expert_division_generate_numbers()

        self.expert_division_question = '{} / {}'.format(self.expert_division_first_num, self.expert_division_second_num)
        self.expert_division_answer = self.expert_division_first_num / self.expert_division_second_num
        self.expert_division_answer = '{0:.0f}'.format(self.expert_division_answer)
        self.expert_division_answer = str(self.expert_division_answer)
#######################################################################################################################################################################

class MinuteMathApp(App, Easy_Addition_Level, Easy_Subtraction_Level, Easy_Multiplication_Level, Easy_Division_Level, Intermediate_Addition_Level, Intermediate_Subtraction_Level, Intermediate_Multiplication_Level, Intermediate_Division_Level, Expert_Addition_Level, Expert_Subtraction_Level, Expert_Multiplication_Level, Expert_Division_Level):
    '''
    #Docstring: The main app class. I will make it a child of the
    Easy_Addition_Level class as well, so that it can gain all of the
    functionality of that class, in order to ask the user questions in
    the kivy app.
    '''

    def __init__(self, **kwargs):
        super(MinuteMathApp, self).__init__(**kwargs)
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def on_start(self):
        '''
        #Docstring: Method that will call the change_screen method so that I can
        dynamically change the screen from the opening screen when the
        user opens this application. The change_screen method will be called 5
        seconds after the user opens the application. 
        '''
        Clock.schedule_once(self.change_screen, 5)
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def change_screen(self, *args):
        '''
        #Docstring: Method that will dynamically change the screen.
        '''
        self.root.current = 'Options Screen'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    def easy_addition_timer(self, *args):
        '''
        #Docstring: Function that will subtract -1 seconds from
        self.easy_addition_seconds each time the function is
        called. Once seconds reaches a value of -1, minutes will
        decline by -1. Once we go below 0 minutes and 0 seconds,
        we will alert the user that their time is up.
        '''

        self.easy_addition_seconds -= 1

        if self.easy_addition_seconds == -1:
            self.easy_addition_seconds += 60
            self.easy_addition_minutes -= 1

        self.easy_addition_time = datetime.timedelta(minutes=self.easy_addition_minutes, seconds=self.easy_addition_seconds)
        self.root.ids.easy_addition_time.text = str(self.easy_addition_time)

        if '-1 day' in str(self.easy_addition_time):
            self.root.ids.easy_addition_time.text = 'Time Over!'
            self.event.cancel()
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_addition_start_timer(self):
        '''
        #Docstring: Method that will start the timer once a Button
        is pressed in the .kv file. I will bind the Button to this
        function. Once this is pressed, the time will be called and
        updated once per frame. This will give the visual effect of
        a countdown timer.
        '''
        self.event = Clock.schedule_interval(self.easy_addition_timer, 1)
        self.event()
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def easy_addition_time_over(self, *args):
        '''
        #Docstring: Method that will change the screen after the clock
        time has expired. This method will send the user back to the
        options screen so that they can choose to play again, or select
        another level to play on. I will also resent their score, their
        number of questions, their correct answers and % grade to 0
        '''

        #Set values back to 0, minutes back to 1
        self.easy_addition_questions = 0
        self.easy_addition_correct_answers = 0
        self.easy_addition_score = 0
        self.easy_addition_final_grade = 0
        self.easy_addition_minutes = 1
        self.easy_addition_seconds = 0

        #Set all of the labels to empty
        self.root.ids.easy_addition_question_number.text = ''
        self.root.ids.easy_addition_time.text = ''
        self.root.ids.easy_addition_user_answer.text = ''
        self.root.ids.easy_addition_result.text = ''
        self.root.ids.easy_addition_score.text = ''
        self.root.ids.easy_addition_final_grade.text = ''

        self.root.current = 'Easy Math Options'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_addition_addnums(self):
        '''
        #Docstring: This function will call the easy_addition() function that was
        created in the parent class 'Easy_Addition_Level'. It will allow us to
        generate numbers, add a question to the label, check to see if the users
        answer matches thecorrect answer,and then clear the screen when we want
        to generate a new question.
        '''
        self.easy_addition()
        self.root.ids.easy_addition_question.text = self.easy_addition_question
        self.root.ids.easy_addition_user_answer.text = ''
        self.root.ids.easy_addition_result.text = ''
        self.root.ids.easy_addition_score.text = self.root.ids.easy_addition_score.text.rstrip(':')
        self.root.ids.easy_addition_question_number.text = self.root.ids.easy_addition_question_number.text.rstrip(':')
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_addition_check_answer(self):
        '''
        #Docstring: A method that will allow me to check that the question the user entered
        is the correct answer or incorrect answer. The self.easy_addition_user_answer will
        be set equal to whatever the user entered in the label in the application. If the
        answer equals self.easy_addition_answer, I will increment their score by +=1, increment
        the number of correct answers by += 1, increment the number of total questions by += 1,
        update the label to let them know the answer IS correct, and display this on the screen. If
        their answer is not correct I will increment correct answers by += 0, I will increment the
        total number of questions, I will update the label to show them that the question is NOT
        correct, and I will display this information on the screen. If the clock indicates that the
        time is over, I will show them what their current score is, what their current %grade is,
        and what their current number of questions is. The screen will update the user that their
        time has expired, and the Clock.schedule_once() function will be used to move the user back
        to the options screen so that they can select a new level to play, or repeat the same level.
        I set the clock to 5 seconds so that they will have enough time to review their score.
        '''
        self.easy_addition_user_answer = self.root.ids.easy_addition_user_answer.text

        if self.easy_addition_answer == self.easy_addition_user_answer:
            self.root.ids.easy_addition_result.text = 'Correct!'
            self.easy_addition_score += 1
            self.easy_addition_correct_answers += 1
            self.easy_addition_questions += 1
            self.root.ids.easy_addition_score.text = 'Score: ' + str(self.easy_addition_score)
            self.root.ids.easy_addition_question_number.text = 'Question Number: ' + str(self.easy_addition_questions)
            

        else:
            self.root.ids.easy_addition_result.text = 'Incorrect!'
            self.easy_addition_score += 0
            self.easy_addition_questions += 1
            self.root.ids.easy_addition_score.text = 'Score: ' + str(self.easy_addition_score)
            self.root.ids.easy_addition_question_number.text = 'Question Number: ' + str(self.easy_addition_questions)

        if self.root.ids.easy_addition_time.text == 'Time Over!':
            self.root.ids.easy_addition_score.text = 'Score: ' + str(self.easy_addition_score)
            self.root.ids.easy_addition_question_number.text = 'Question Number: ' + str(self.easy_addition_questions)

            self.easy_addition_final_grade = (self.easy_addition_score / self.easy_addition_questions) * 100

            self.root.ids.easy_addition_final_grade.text = 'Final Grade: {0:.2f}%'.format(self.easy_addition_final_grade)

            Clock.schedule_once(self.easy_addition_time_over, 5)
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_addition_check_final_grade(self):
        self.easy_addition_final_grade = (self.easy_addition_score / self.easy_addition_questions) * 100

        self.root.ids.easy_addition_final_grade.text = 'Final Grade: {0:.2f}%'.format(self.easy_addition_final_grade)
            
    #------------------------------------------------------------------------------------------------------------------

    '''
    Now I create a series of Buttons for the easy additio level that will be used to help the user enter text to
    the label. If easy_addition_button1 is pressed, 1 will be added to the label. If easy_addition_button2 is
    pressed, 2 will be added to the label... and so on. This will help the user use the psuedo keypad to enter
    answers. There will be a clear Button that will delete whatever is in the label if the user decides to change
    their answer before entering a final answer.
    '''

    def easy_addition_button1(self):
        
        self.root.ids.easy_addition_user_answer.text += '1'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_addition_button2(self):
        self.root.ids.easy_addition_user_answer.text += '2'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_addition_button3(self):
        self.root.ids.easy_addition_user_answer.text += '3'
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_addition_button4(self):
        self.root.ids.easy_addition_user_answer.text += '4'
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_addition_button5(self):
        self.root.ids.easy_addition_user_answer.text += '5'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_addition_button6(self):
        self.root.ids.easy_addition_user_answer.text += '6'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_addition_button7(self):
        self.root.ids.easy_addition_user_answer.text += '7'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_addition_button8(self):
        self.root.ids.easy_addition_user_answer.text += '8'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_addition_button9(self):
        self.root.ids.easy_addition_user_answer.text += '9'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_addition_button0(self):
        self.root.ids.easy_addition_user_answer.text += '0'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_addition_clear_button(self):
        self.root.ids.easy_addition_user_answer.text = ''
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_subtraction_timer(self, *args):
        '''
        #Docstring: Function that will subtract -1 seconds from
        self.easy_subtraction_seconds each time the function is
        called. Once seconds reaches a value of -1, minutes will
        decline by -1. Once we go below 0 minutes and 0 seconds,
        we will alert the user that their time is up.
        '''

        self.easy_subtraction_seconds -= 1

        if self.easy_subtraction_seconds == -1:
            self.easy_subtraction_seconds += 60
            self.easy_subtraction_minutes -= 1

        self.easy_subtraction_time = datetime.timedelta(minutes=self.easy_subtraction_minutes, seconds=self.easy_subtraction_seconds)
        self.root.ids.easy_subtraction_time.text = str(self.easy_subtraction_time)

        if '-1 day' in str(self.easy_subtraction_time):
            self.root.ids.easy_subtraction_time.text = 'Time Over!'
            self.event.cancel()
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_subtraction_start_timer(self):
        '''
        #Docstring: Method that will start the timer once a Button
        is pressed in the .kv file. I will bind the Button to this
        function. Once this is pressed, the time will be called and
        updated once per frame. This will give the visual effect of
        a countdown timer.
        '''
        self.event = Clock.schedule_interval(self.easy_subtraction_timer, 1)
        self.event()
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def easy_subtraction_time_over(self, *args):
        '''
        #Docstring: Method that will change the screen after the clock
        time has expired. This method will send the user back to the
        options screen so that they can choose to play again, or select
        another level to play on. I will also resent their score, their
        number of questions, their correct answers and % grade to 0
        '''

        #Set values back to 0, minutes back to 1
        self.easy_subtraction_questions = 0
        self.easy_subtraction_correct_answers = 0
        self.easy_subtraction_score = 0
        self.easy_subtraction_final_grade = 0
        self.easy_subtraction_minutes = 1
        self.easy_subtraction_seconds = 0

        #Set all of the labels to empty
        self.root.ids.easy_subtraction_question_number.text = ''
        self.root.ids.easy_subtraction_time.text = ''
        self.root.ids.easy_subtraction_user_answer.text = ''
        self.root.ids.easy_subtraction_result.text = ''
        self.root.ids.easy_subtraction_score.text = ''
        self.root.ids.easy_subtraction_final_grade.text = ''

        self.root.current = 'Easy Math Options'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_subtraction_addnums(self):
        '''
        #Docstring: This function will call the easy_subtraction() function that was
        created in the parent class 'Easy_subtraction_Level'. It will allow us to
        generate numbers, add a question to the label, check to see if the users
        answer matches thecorrect answer,and then clear the screen when we want
        to generate a new question.
        '''
        self.easy_subtraction()
        self.root.ids.easy_subtraction_question.text = self.easy_subtraction_question
        self.root.ids.easy_subtraction_user_answer.text = ''
        self.root.ids.easy_subtraction_result.text = ''
        self.root.ids.easy_subtraction_score.text = self.root.ids.easy_subtraction_score.text.rstrip(':')
        self.root.ids.easy_subtraction_question_number.text = self.root.ids.easy_subtraction_question_number.text.rstrip(':')
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_subtraction_check_answer(self):
        '''
        #Docstring: A method that will allow me to check that the question the user entered
        is the correct answer or incorrect answer. The self.easy_subtraction_user_answer will
        be set equal to whatever the user entered in the label in the application. If the
        answer equals self.easy_subtraction_answer, I will increment their score by +=1, increment
        the number of correct answers by += 1, increment the number of total questions by += 1,
        update the label to let them know the answer IS correct, and display this on the screen. If
        their answer is not correct I will increment correct answers by += 0, I will increment the
        total number of questions, I will update the label to show them that the question is NOT
        correct, and I will display this information on the screen. If the clock indicates that the
        time is over, I will show them what their current score is, what their current %grade is,
        and what their current number of questions is. The screen will update the user that their
        time has expired, and the Clock.schedule_once() function will be used to move the user back
        to the options screen so that they can select a new level to play, or repeat the same level.
        I set the clock to 5 seconds so that they will have enough time to review their score.
        '''
        self.easy_subtraction_user_answer = self.root.ids.easy_subtraction_user_answer.text

        if self.easy_subtraction_answer == self.easy_subtraction_user_answer:
            self.root.ids.easy_subtraction_result.text = 'Correct!'
            self.easy_subtraction_score += 1
            self.easy_subtraction_correct_answers += 1
            self.easy_subtraction_questions += 1
            self.root.ids.easy_subtraction_score.text = 'Score: ' + str(self.easy_subtraction_score)
            self.root.ids.easy_subtraction_question_number.text = 'Question Number: ' + str(self.easy_subtraction_questions)
            

        else:
            self.root.ids.easy_subtraction_result.text = 'Incorrect!'
            self.easy_subtraction_score += 0
            self.easy_subtraction_questions += 1
            self.root.ids.easy_subtraction_score.text = 'Score: ' + str(self.easy_subtraction_score)
            self.root.ids.easy_subtraction_question_number.text = 'Question Number: ' + str(self.easy_subtraction_questions)

        if self.root.ids.easy_subtraction_time.text == 'Time Over!':
            self.root.ids.easy_subtraction_score.text = 'Score: ' + str(self.easy_subtraction_score)
            self.root.ids.easy_subtraction_question_number.text = 'Question Number: ' + str(self.easy_subtraction_questions)

            self.easy_subtraction_final_grade = (self.easy_subtraction_score / self.easy_subtraction_questions) * 100

            self.root.ids.easy_subtraction_final_grade.text = 'Final Grade: {0:.2f}%'.format(self.easy_subtraction_final_grade)

            Clock.schedule_once(self.easy_subtraction_time_over, 5)
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_subtraction_check_final_grade(self):
        self.easy_subtraction_final_grade = (self.easy_subtraction_score / self.easy_subtraction_questions) * 100

        self.root.ids.easy_subtraction_final_grade.text = 'Final Grade: {0:.2f}%'.format(self.easy_subtraction_final_grade)
            
    #------------------------------------------------------------------------------------------------------------------

    '''
    Now I create a series of Buttons for the easy additio level that will be used to help the user enter text to
    the label. If easy_subtraction_button1 is pressed, 1 will be added to the label. If easy_subtraction_button2 is
    pressed, 2 will be added to the label... and so on. This will help the user use the psuedo keypad to enter
    answers. There will be a clear Button that will delete whatever is in the label if the user decides to change
    their answer before entering a final answer.
    '''

    def easy_subtraction_button1(self):
        
        self.root.ids.easy_subtraction_user_answer.text += '1'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_subtraction_button2(self):
        self.root.ids.easy_subtraction_user_answer.text += '2'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_subtraction_button3(self):
        self.root.ids.easy_subtraction_user_answer.text += '3'
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_subtraction_button4(self):
        self.root.ids.easy_subtraction_user_answer.text += '4'
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_subtraction_button5(self):
        self.root.ids.easy_subtraction_user_answer.text += '5'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_subtraction_button6(self):
        self.root.ids.easy_subtraction_user_answer.text += '6'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_subtraction_button7(self):
        self.root.ids.easy_subtraction_user_answer.text += '7'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_subtraction_button8(self):
        self.root.ids.easy_subtraction_user_answer.text += '8'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_subtraction_button9(self):
        self.root.ids.easy_subtraction_user_answer.text += '9'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_subtraction_button0(self):
        self.root.ids.easy_subtraction_user_answer.text += '0'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_subtraction_clear_button(self):
        self.root.ids.easy_subtraction_user_answer.text = ''
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_multiplication_timer(self, *args):
            '''
            #Docstring: Function that will subtract -1 seconds from
            self.easy_multiplication_seconds each time the function is
            called. Once seconds reaches a value of -1, minutes will
            decline by -1. Once we go below 0 minutes and 0 seconds,
            we will alert the user that their time is up.
            '''

            self.easy_multiplication_seconds -= 1

            if self.easy_multiplication_seconds == -1:
                self.easy_multiplication_seconds += 60
                self.easy_multiplication_minutes -= 1

            self.easy_multiplication_time = datetime.timedelta(minutes=self.easy_multiplication_minutes, seconds=self.easy_multiplication_seconds)
            self.root.ids.easy_multiplication_time.text = str(self.easy_multiplication_time)

            if '-1 day' in str(self.easy_multiplication_time):
                self.root.ids.easy_multiplication_time.text = 'Time Over!'
                self.event.cancel()
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_multiplication_start_timer(self):
        '''
        #Docstring: Method that will start the timer once a Button
        is pressed in the .kv file. I will bind the Button to this
        function. Once this is pressed, the time will be called and
        updated once per frame. This will give the visual effect of
        a countdown timer.
        '''
        self.event = Clock.schedule_interval(self.easy_multiplication_timer, 1)
        self.event()
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def easy_multiplication_time_over(self, *args):
        '''
        #Docstring: Method that will change the screen after the clock
        time has expired. This method will send the user back to the
        options screen so that they can choose to play again, or select
        another level to play on. I will also resent their score, their
        number of questions, their correct answers and % grade to 0
        '''

        #Set values back to 0, minutes back to 1
        self.easy_multiplication_questions = 0
        self.easy_multiplication_correct_answers = 0
        self.easy_multiplication_score = 0
        self.easy_multiplication_final_grade = 0
        self.easy_multiplication_minutes = 1
        self.easy_multiplication_seconds = 0

        #Set all of the labels to empty
        self.root.ids.easy_multiplication_question_number.text = ''
        self.root.ids.easy_multiplication_time.text = ''
        self.root.ids.easy_multiplication_user_answer.text = ''
        self.root.ids.easy_multiplication_result.text = ''
        self.root.ids.easy_multiplication_score.text = ''
        self.root.ids.easy_multiplication_final_grade.text = ''

        self.root.current = 'Easy Math Options'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_multiplication_addnums(self):
        '''
        #Docstring: This function will call the easy_multiplication() function that was
        created in the parent class 'Easy_multiplication_Level'. It will allow us to
        generate numbers, add a question to the label, check to see if the users
        answer matches thecorrect answer,and then clear the screen when we want
        to generate a new question.
        '''
        self.easy_multiplication()
        self.root.ids.easy_multiplication_question.text = self.easy_multiplication_question
        self.root.ids.easy_multiplication_user_answer.text = ''
        self.root.ids.easy_multiplication_result.text = ''
        self.root.ids.easy_multiplication_score.text = self.root.ids.easy_multiplication_score.text.rstrip(':')
        self.root.ids.easy_multiplication_question_number.text = self.root.ids.easy_multiplication_question_number.text.rstrip(':')
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_multiplication_check_answer(self):
        '''
        #Docstring: A method that will allow me to check that the question the user entered
        is the correct answer or incorrect answer. The self.easy_multiplication_user_answer will
        be set equal to whatever the user entered in the label in the application. If the
        answer equals self.easy_multiplication_answer, I will increment their score by +=1, increment
        the number of correct answers by += 1, increment the number of total questions by += 1,
        update the label to let them know the answer IS correct, and display this on the screen. If
        their answer is not correct I will increment correct answers by += 0, I will increment the
        total number of questions, I will update the label to show them that the question is NOT
        correct, and I will display this information on the screen. If the clock indicates that the
        time is over, I will show them what their current score is, what their current %grade is,
        and what their current number of questions is. The screen will update the user that their
        time has expired, and the Clock.schedule_once() function will be used to move the user back
        to the options screen so that they can select a new level to play, or repeat the same level.
        I set the clock to 5 seconds so that they will have enough time to review their score.
        '''
        self.easy_multiplication_user_answer = self.root.ids.easy_multiplication_user_answer.text

        if self.easy_multiplication_answer == self.easy_multiplication_user_answer:
            self.root.ids.easy_multiplication_result.text = 'Correct!'
            self.easy_multiplication_score += 1
            self.easy_multiplication_correct_answers += 1
            self.easy_multiplication_questions += 1
            self.root.ids.easy_multiplication_score.text = 'Score: ' + str(self.easy_multiplication_score)
            self.root.ids.easy_multiplication_question_number.text = 'Question Number: ' + str(self.easy_multiplication_questions)
            

        else:
            self.root.ids.easy_multiplication_result.text = 'Incorrect!'
            self.easy_multiplication_score += 0
            self.easy_multiplication_questions += 1
            self.root.ids.easy_multiplication_score.text = 'Score: ' + str(self.easy_multiplication_score)
            self.root.ids.easy_multiplication_question_number.text = 'Question Number: ' + str(self.easy_multiplication_questions)

        if self.root.ids.easy_multiplication_time.text == 'Time Over!':
            self.root.ids.easy_multiplication_score.text = 'Score: ' + str(self.easy_multiplication_score)
            self.root.ids.easy_multiplication_question_number.text = 'Question Number: ' + str(self.easy_multiplication_questions)

            self.easy_multiplication_final_grade = (self.easy_multiplication_score / self.easy_multiplication_questions) * 100

            self.root.ids.easy_multiplication_final_grade.text = 'Final Grade: {0:.2f}%'.format(self.easy_multiplication_final_grade)

            Clock.schedule_once(self.easy_multiplication_time_over, 5)
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_multiplication_check_final_grade(self):
        self.easy_multiplication_final_grade = (self.easy_multiplication_score / self.easy_multiplication_questions) * 100

        self.root.ids.easy_multiplication_final_grade.text = 'Final Grade: {0:.2f}%'.format(self.easy_multiplication_final_grade)
            
    #------------------------------------------------------------------------------------------------------------------

    '''
    Now I create a series of Buttons for the easy additio level that will be used to help the user enter text to
    the label. If easy_multiplication_button1 is pressed, 1 will be added to the label. If easy_multiplication_button2 is
    pressed, 2 will be added to the label... and so on. This will help the user use the psuedo keypad to enter
    answers. There will be a clear Button that will delete whatever is in the label if the user decides to change
    their answer before entering a final answer.
    '''

    def easy_multiplication_button1(self):
        
        self.root.ids.easy_multiplication_user_answer.text += '1'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_multiplication_button2(self):
        self.root.ids.easy_multiplication_user_answer.text += '2'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_multiplication_button3(self):
        self.root.ids.easy_multiplication_user_answer.text += '3'
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_multiplication_button4(self):
        self.root.ids.easy_multiplication_user_answer.text += '4'
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_multiplication_button5(self):
        self.root.ids.easy_multiplication_user_answer.text += '5'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_multiplication_button6(self):
        self.root.ids.easy_multiplication_user_answer.text += '6'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_multiplication_button7(self):
        self.root.ids.easy_multiplication_user_answer.text += '7'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_multiplication_button8(self):
        self.root.ids.easy_multiplication_user_answer.text += '8'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_multiplication_button9(self):
        self.root.ids.easy_multiplication_user_answer.text += '9'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_multiplication_button0(self):
        self.root.ids.easy_multiplication_user_answer.text += '0'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_multiplication_clear_button(self):
        self.root.ids.easy_multiplication_user_answer.text = ''
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_division_timer(self, *args):
        '''
        #Docstring: Function that will subtract -1 seconds from
        self.easy_division_seconds each time the function is
        called. Once seconds reaches a value of -1, minutes will
        decline by -1. Once we go below 0 minutes and 0 seconds,
        we will alert the user that their time is up.
        '''

        self.easy_division_seconds -= 1

        if self.easy_division_seconds == -1:
            self.easy_division_seconds += 60
            self.easy_division_minutes -= 1

        self.easy_division_time = datetime.timedelta(minutes=self.easy_division_minutes, seconds=self.easy_division_seconds)
        self.root.ids.easy_division_time.text = str(self.easy_division_time)

        if '-1 day' in str(self.easy_division_time):
            self.root.ids.easy_division_time.text = 'Time Over!'
            self.event.cancel()
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_division_start_timer(self):
        '''
        #Docstring: Method that will start the timer once a Button
        is pressed in the .kv file. I will bind the Button to this
        function. Once this is pressed, the time will be called and
        updated once per frame. This will give the visual effect of
        a countdown timer.
        '''
        self.event = Clock.schedule_interval(self.easy_division_timer, 1)
        self.event()
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def easy_division_time_over(self, *args):
        '''
        #Docstring: Method that will change the screen after the clock
        time has expired. This method will send the user back to the
        options screen so that they can choose to play again, or select
        another level to play on. I will also resent their score, their
        number of questions, their correct answers and % grade to 0
        '''

        #Set values back to 0, minutes back to 1
        self.easy_division_questions = 0
        self.easy_division_correct_answers = 0
        self.easy_division_score = 0
        self.easy_division_final_grade = 0
        self.easy_division_minutes = 1
        self.easy_division_seconds = 0

        #Set all of the labels to empty
        self.root.ids.easy_division_question_number.text = ''
        self.root.ids.easy_division_time.text = ''
        self.root.ids.easy_division_user_answer.text = ''
        self.root.ids.easy_division_result.text = ''
        self.root.ids.easy_division_score.text = ''
        self.root.ids.easy_division_final_grade.text = ''

        self.root.current = 'Easy Math Options'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_division_addnums(self):
        '''
        #Docstring: This function will call the easy_division() function that was
        created in the parent class 'Easy_division_Level'. It will allow us to
        generate numbers, add a question to the label, check to see if the users
        answer matches thecorrect answer,and then clear the screen when we want
        to generate a new question.
        '''
        self.easy_division()
        self.root.ids.easy_division_question.text = self.easy_division_question
        self.root.ids.easy_division_user_answer.text = ''
        self.root.ids.easy_division_result.text = ''
        self.root.ids.easy_division_score.text = self.root.ids.easy_division_score.text.rstrip(':')
        self.root.ids.easy_division_question_number.text = self.root.ids.easy_division_question_number.text.rstrip(':')
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_division_check_answer(self):
        '''
        #Docstring: A method that will allow me to check that the question the user entered
        is the correct answer or incorrect answer. The self.easy_division_user_answer will
        be set equal to whatever the user entered in the label in the application. If the
        answer equals self.easy_division_answer, I will increment their score by +=1, increment
        the number of correct answers by += 1, increment the number of total questions by += 1,
        update the label to let them know the answer IS correct, and display this on the screen. If
        their answer is not correct I will increment correct answers by += 0, I will increment the
        total number of questions, I will update the label to show them that the question is NOT
        correct, and I will display this information on the screen. If the clock indicates that the
        time is over, I will show them what their current score is, what their current %grade is,
        and what their current number of questions is. The screen will update the user that their
        time has expired, and the Clock.schedule_once() function will be used to move the user back
        to the options screen so that they can select a new level to play, or repeat the same level.
        I set the clock to 5 seconds so that they will have enough time to review their score.
        '''
        self.easy_division_user_answer = self.root.ids.easy_division_user_answer.text

        if self.easy_division_answer == self.easy_division_user_answer:
            self.root.ids.easy_division_result.text = 'Correct!'
            self.easy_division_score += 1
            self.easy_division_correct_answers += 1
            self.easy_division_questions += 1
            self.root.ids.easy_division_score.text = 'Score: ' + str(self.easy_division_score)
            self.root.ids.easy_division_question_number.text = 'Question Number: ' + str(self.easy_division_questions)
            

        else:
            self.root.ids.easy_division_result.text = 'Incorrect!'
            self.easy_division_score += 0
            self.easy_division_questions += 1
            self.root.ids.easy_division_score.text = 'Score: ' + str(self.easy_division_score)
            self.root.ids.easy_division_question_number.text = 'Question Number: ' + str(self.easy_division_questions)

        if self.root.ids.easy_division_time.text == 'Time Over!':
            self.root.ids.easy_division_score.text = 'Score: ' + str(self.easy_division_score)
            self.root.ids.easy_division_question_number.text = 'Question Number: ' + str(self.easy_division_questions)

            self.easy_division_final_grade = (self.easy_division_score / self.easy_division_questions) * 100

            self.root.ids.easy_division_final_grade.text = 'Final Grade: {0:.2f}%'.format(self.easy_division_final_grade)

            Clock.schedule_once(self.easy_division_time_over, 5)
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_division_check_final_grade(self):
        

        self.easy_division_final_grade = (self.easy_division_score / self.easy_division_questions) * 100

        self.root.ids.easy_division_final_grade.text = 'Final Grade: {0:.2f}%'.format(self.easy_division_final_grade)
            
    #------------------------------------------------------------------------------------------------------------------

    '''
    Now I create a series of Buttons for the easy additio level that will be used to help the user enter text to
    the label. If easy_division_button1 is pressed, 1 will be added to the label. If easy_division_button2 is
    pressed, 2 will be added to the label... and so on. This will help the user use the psuedo keypad to enter
    answers. There will be a clear Button that will delete whatever is in the label if the user decides to change
    their answer before entering a final answer.
    '''

    def easy_division_button1(self):
        
        self.root.ids.easy_division_user_answer.text += '1'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_division_button2(self):
        self.root.ids.easy_division_user_answer.text += '2'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_division_button3(self):
        self.root.ids.easy_division_user_answer.text += '3'
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_division_button4(self):
        self.root.ids.easy_division_user_answer.text += '4'
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_division_button5(self):
        self.root.ids.easy_division_user_answer.text += '5'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_division_button6(self):
        self.root.ids.easy_division_user_answer.text += '6'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_division_button7(self):
        self.root.ids.easy_division_user_answer.text += '7'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_division_button8(self):
        self.root.ids.easy_division_user_answer.text += '8'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_division_button9(self):
        self.root.ids.easy_division_user_answer.text += '9'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_division_button0(self):
        self.root.ids.easy_division_user_answer.text += '0'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def easy_division_clear_button(self):
        self.root.ids.easy_division_user_answer.text = ''
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_addition_timer(self, *args):
            '''
            #Docstring: Function that will subtract -1 seconds from
            self.intermediate_addition_seconds each time the function is
            called. Once seconds reaches a value of -1, minutes will
            decline by -1. Once we go below 0 minutes and 0 seconds,
            we will alert the user that their time is up.
            '''

            self.intermediate_addition_seconds -= 1

            if self.intermediate_addition_seconds == -1:
                self.intermediate_addition_seconds += 60
                self.intermediate_addition_minutes -= 1

            self.intermediate_addition_time = datetime.timedelta(minutes=self.intermediate_addition_minutes, seconds=self.intermediate_addition_seconds)
            self.root.ids.intermediate_addition_time.text = str(self.intermediate_addition_time)

            if '-1 day' in str(self.intermediate_addition_time):
                self.root.ids.intermediate_addition_time.text = 'Time Over!'
                self.event.cancel()
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_addition_start_timer(self):
        '''
        #Docstring: Method that will start the timer once a Button
        is pressed in the .kv file. I will bind the Button to this
        function. Once this is pressed, the time will be called and
        updated once per frame. This will give the visual effect of
        a countdown timer.
        '''
        self.event = Clock.schedule_interval(self.intermediate_addition_timer, 1)
        self.event()
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def intermediate_addition_time_over(self, *args):
        '''
        #Docstring: Method that will change the screen after the clock
        time has expired. This method will send the user back to the
        options screen so that they can choose to play again, or select
        another level to play on. I will also resent their score, their
        number of questions, their correct answers and % grade to 0
        '''

        #Set values back to 0, minutes back to 1
        self.intermediate_addition_questions = 0
        self.intermediate_addition_correct_answers = 0
        self.intermediate_addition_score = 0
        self.intermediate_addition_final_grade = 0
        self.intermediate_addition_minutes = 1
        self.intermediate_addition_seconds = 0

        #Set all of the labels to empty
        self.root.ids.intermediate_addition_question_number.text = ''
        self.root.ids.intermediate_addition_time.text = ''
        self.root.ids.intermediate_addition_user_answer.text = ''
        self.root.ids.intermediate_addition_result.text = ''
        self.root.ids.intermediate_addition_score.text = ''
        self.root.ids.intermediate_addition_final_grade.text = ''

        self.root.current = 'Intermediate Math Options'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_addition_addnums(self):
        '''
        #Docstring: This function will call the intermediate_addition() function that was
        created in the parent class 'intermediate_Addition_Level'. It will allow us to
        generate numbers, add a question to the label, check to see if the users
        answer matches thecorrect answer,and then clear the screen when we want
        to generate a new question.
        '''
        self.intermediate_addition()
        self.root.ids.intermediate_addition_question.text = self.intermediate_addition_question
        self.root.ids.intermediate_addition_user_answer.text = ''
        self.root.ids.intermediate_addition_result.text = ''
        self.root.ids.intermediate_addition_score.text = self.root.ids.intermediate_addition_score.text.rstrip(':')
        self.root.ids.intermediate_addition_question_number.text = self.root.ids.intermediate_addition_question_number.text.rstrip(':')
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_addition_check_answer(self):
        '''
        #Docstring: A method that will allow me to check that the question the user entered
        is the correct answer or incorrect answer. The self.intermediate_addition_user_answer will
        be set equal to whatever the user entered in the label in the application. If the
        answer equals self.intermediate_addition_answer, I will increment their score by +=1, increment
        the number of correct answers by += 1, increment the number of total questions by += 1,
        update the label to let them know the answer IS correct, and display this on the screen. If
        their answer is not correct I will increment correct answers by += 0, I will increment the
        total number of questions, I will update the label to show them that the question is NOT
        correct, and I will display this information on the screen. If the clock indicates that the
        time is over, I will show them what their current score is, what their current %grade is,
        and what their current number of questions is. The screen will update the user that their
        time has expired, and the Clock.schedule_once() function will be used to move the user back
        to the options screen so that they can select a new level to play, or repeat the same level.
        I set the clock to 5 seconds so that they will have enough time to review their score.
        '''
        self.intermediate_addition_user_answer = self.root.ids.intermediate_addition_user_answer.text

        if self.intermediate_addition_answer == self.intermediate_addition_user_answer:
            self.root.ids.intermediate_addition_result.text = 'Correct!'
            self.intermediate_addition_score += 1
            self.intermediate_addition_correct_answers += 1
            self.intermediate_addition_questions += 1
            self.root.ids.intermediate_addition_score.text = 'Score: ' + str(self.intermediate_addition_score)
            self.root.ids.intermediate_addition_question_number.text = 'Question Number: ' + str(self.intermediate_addition_questions)
            

        else:
            self.root.ids.intermediate_addition_result.text = 'Incorrect!'
            self.intermediate_addition_score += 0
            self.intermediate_addition_questions += 1
            self.root.ids.intermediate_addition_score.text = 'Score: ' + str(self.intermediate_addition_score)
            self.root.ids.intermediate_addition_question_number.text = 'Question Number: ' + str(self.intermediate_addition_questions)

        if self.root.ids.intermediate_addition_time.text == 'Time Over!':
            self.root.ids.intermediate_addition_score.text = 'Score: ' + str(self.intermediate_addition_score)
            self.root.ids.intermediate_addition_question_number.text = 'Question Number: ' + str(self.intermediate_addition_questions)

            self.intermediate_addition_final_grade = (self.intermediate_addition_score / self.intermediate_addition_questions) * 100

            self.root.ids.intermediate_addition_final_grade.text = 'Final Grade: {0:.2f}%'.format(self.intermediate_addition_final_grade)

            Clock.schedule_once(self.intermediate_addition_time_over, 5)
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_addition_check_final_grade(self):
        self.intermediate_addition_final_grade = (self.intermediate_addition_score / self.intermediate_addition_questions) * 100

        self.root.ids.intermediate_addition_final_grade.text = 'Final Grade: {0:.2f}%'.format(self.intermediate_addition_final_grade)
            
    #------------------------------------------------------------------------------------------------------------------

    '''
    Now I create a series of Buttons for the intermediate additio level that will be used to help the user enter text to
    the label. If intermediate_addition_button1 is pressed, 1 will be added to the label. If intermediate_addition_button2 is
    pressed, 2 will be added to the label... and so on. This will help the user use the psuedo keypad to enter
    answers. There will be a clear Button that will delete whatever is in the label if the user decides to change
    their answer before entering a final answer.
    '''

    def intermediate_addition_button1(self):
        
        self.root.ids.intermediate_addition_user_answer.text += '1'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_addition_button2(self):
        self.root.ids.intermediate_addition_user_answer.text += '2'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_addition_button3(self):
        self.root.ids.intermediate_addition_user_answer.text += '3'
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_addition_button4(self):
        self.root.ids.intermediate_addition_user_answer.text += '4'
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_addition_button5(self):
        self.root.ids.intermediate_addition_user_answer.text += '5'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_addition_button6(self):
        self.root.ids.intermediate_addition_user_answer.text += '6'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_addition_button7(self):
        self.root.ids.intermediate_addition_user_answer.text += '7'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_addition_button8(self):
        self.root.ids.intermediate_addition_user_answer.text += '8'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_addition_button9(self):
        self.root.ids.intermediate_addition_user_answer.text += '9'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_addition_button0(self):
        self.root.ids.intermediate_addition_user_answer.text += '0'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_addition_clear_button(self):
        self.root.ids.intermediate_addition_user_answer.text = ''
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_subtraction_timer(self, *args):
        '''
        #Docstring: Function that will subtract -1 seconds from
        self.intermediate_subtraction_seconds each time the function is
        called. Once seconds reaches a value of -1, minutes will
        decline by -1. Once we go below 0 minutes and 0 seconds,
        we will alert the user that their time is up.
        '''

        self.intermediate_subtraction_seconds -= 1

        if self.intermediate_subtraction_seconds == -1:
            self.intermediate_subtraction_seconds += 60
            self.intermediate_subtraction_minutes -= 1

        self.intermediate_subtraction_time = datetime.timedelta(minutes=self.intermediate_subtraction_minutes, seconds=self.intermediate_subtraction_seconds)
        self.root.ids.intermediate_subtraction_time.text = str(self.intermediate_subtraction_time)

        if '-1 day' in str(self.intermediate_subtraction_time):
            self.root.ids.intermediate_subtraction_time.text = 'Time Over!'
            self.event.cancel()
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_subtraction_start_timer(self):
        '''
        #Docstring: Method that will start the timer once a Button
        is pressed in the .kv file. I will bind the Button to this
        function. Once this is pressed, the time will be called and
        updated once per frame. This will give the visual effect of
        a countdown timer.
        '''
        self.event = Clock.schedule_interval(self.intermediate_subtraction_timer, 1)
        self.event()
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def intermediate_subtraction_time_over(self, *args):
        '''
        #Docstring: Method that will change the screen after the clock
        time has expired. This method will send the user back to the
        options screen so that they can choose to play again, or select
        another level to play on. I will also resent their score, their
        number of questions, their correct answers and % grade to 0
        '''

        #Set values back to 0, minutes back to 1
        self.intermediate_subtraction_questions = 0
        self.intermediate_subtraction_correct_answers = 0
        self.intermediate_subtraction_score = 0
        self.intermediate_subtraction_final_grade = 0
        self.intermediate_subtraction_minutes = 1
        self.intermediate_subtraction_seconds = 0

        #Set all of the labels to empty
        self.root.ids.intermediate_subtraction_question_number.text = ''
        self.root.ids.intermediate_subtraction_time.text = ''
        self.root.ids.intermediate_subtraction_user_answer.text = ''
        self.root.ids.intermediate_subtraction_result.text = ''
        self.root.ids.intermediate_subtraction_score.text = ''
        self.root.ids.intermediate_subtraction_final_grade.text = ''

        self.root.current = 'Intermediate Math Options'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_subtraction_addnums(self):
        '''
        #Docstring: This function will call the intermediate_subtraction() function that was
        created in the parent class 'intermediate_subtraction_Level'. It will allow us to
        generate numbers, add a question to the label, check to see if the users
        answer matches thecorrect answer,and then clear the screen when we want
        to generate a new question.
        '''
        self.intermediate_subtraction()
        self.root.ids.intermediate_subtraction_question.text = self.intermediate_subtraction_question
        self.root.ids.intermediate_subtraction_user_answer.text = ''
        self.root.ids.intermediate_subtraction_result.text = ''
        self.root.ids.intermediate_subtraction_score.text = self.root.ids.intermediate_subtraction_score.text.rstrip(':')
        self.root.ids.intermediate_subtraction_question_number.text = self.root.ids.intermediate_subtraction_question_number.text.rstrip(':')
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_subtraction_check_answer(self):
        '''
        #Docstring: A method that will allow me to check that the question the user entered
        is the correct answer or incorrect answer. The self.intermediate_subtraction_user_answer will
        be set equal to whatever the user entered in the label in the application. If the
        answer equals self.intermediate_subtraction_answer, I will increment their score by +=1, increment
        the number of correct answers by += 1, increment the number of total questions by += 1,
        update the label to let them know the answer IS correct, and display this on the screen. If
        their answer is not correct I will increment correct answers by += 0, I will increment the
        total number of questions, I will update the label to show them that the question is NOT
        correct, and I will display this information on the screen. If the clock indicates that the
        time is over, I will show them what their current score is, what their current %grade is,
        and what their current number of questions is. The screen will update the user that their
        time has expired, and the Clock.schedule_once() function will be used to move the user back
        to the options screen so that they can select a new level to play, or repeat the same level.
        I set the clock to 5 seconds so that they will have enough time to review their score.
        '''
        self.intermediate_subtraction_user_answer = self.root.ids.intermediate_subtraction_user_answer.text

        if self.intermediate_subtraction_answer == self.intermediate_subtraction_user_answer:
            self.root.ids.intermediate_subtraction_result.text = 'Correct!'
            self.intermediate_subtraction_score += 1
            self.intermediate_subtraction_correct_answers += 1
            self.intermediate_subtraction_questions += 1
            self.root.ids.intermediate_subtraction_score.text = 'Score: ' + str(self.intermediate_subtraction_score)
            self.root.ids.intermediate_subtraction_question_number.text = 'Question Number: ' + str(self.intermediate_subtraction_questions)
            

        else:
            self.root.ids.intermediate_subtraction_result.text = 'Incorrect!'
            self.intermediate_subtraction_score += 0
            self.intermediate_subtraction_questions += 1
            self.root.ids.intermediate_subtraction_score.text = 'Score: ' + str(self.intermediate_subtraction_score)
            self.root.ids.intermediate_subtraction_question_number.text = 'Question Number: ' + str(self.intermediate_subtraction_questions)

        if self.root.ids.intermediate_subtraction_time.text == 'Time Over!':
            self.root.ids.intermediate_subtraction_score.text = 'Score: ' + str(self.intermediate_subtraction_score)
            self.root.ids.intermediate_subtraction_question_number.text = 'Question Number: ' + str(self.intermediate_subtraction_questions)

            self.intermediate_subtraction_final_grade = (self.intermediate_subtraction_score / self.intermediate_subtraction_questions) * 100

            self.root.ids.intermediate_subtraction_final_grade.text = 'Final Grade: {0:.2f}%'.format(self.intermediate_subtraction_final_grade)

            Clock.schedule_once(self.intermediate_subtraction_time_over, 5)
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_subtraction_check_final_grade(self):
        self.intermediate_subtraction_final_grade = (self.intermediate_subtraction_score / self.intermediate_subtraction_questions) * 100

        self.root.ids.intermediate_subtraction_final_grade.text = 'Final Grade: {0:.2f}%'.format(self.intermediate_subtraction_final_grade)
            
    #------------------------------------------------------------------------------------------------------------------

    '''
    Now I create a series of Buttons for the intermediate additio level that will be used to help the user enter text to
    the label. If intermediate_subtraction_button1 is pressed, 1 will be added to the label. If intermediate_subtraction_button2 is
    pressed, 2 will be added to the label... and so on. This will help the user use the psuedo keypad to enter
    answers. There will be a clear Button that will delete whatever is in the label if the user decides to change
    their answer before entering a final answer.
    '''

    def intermediate_subtraction_button1(self):
        
        self.root.ids.intermediate_subtraction_user_answer.text += '1'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_subtraction_button2(self):
        self.root.ids.intermediate_subtraction_user_answer.text += '2'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_subtraction_button3(self):
        self.root.ids.intermediate_subtraction_user_answer.text += '3'
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_subtraction_button4(self):
        self.root.ids.intermediate_subtraction_user_answer.text += '4'
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_subtraction_button5(self):
        self.root.ids.intermediate_subtraction_user_answer.text += '5'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_subtraction_button6(self):
        self.root.ids.intermediate_subtraction_user_answer.text += '6'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_subtraction_button7(self):
        self.root.ids.intermediate_subtraction_user_answer.text += '7'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_subtraction_button8(self):
        self.root.ids.intermediate_subtraction_user_answer.text += '8'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_subtraction_button9(self):
        self.root.ids.intermediate_subtraction_user_answer.text += '9'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_subtraction_button0(self):
        self.root.ids.intermediate_subtraction_user_answer.text += '0'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_subtraction_clear_button(self):
        self.root.ids.intermediate_subtraction_user_answer.text = ''
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_multiplication_timer(self, *args):
                '''
                #Docstring: Function that will subtract -1 seconds from
                self.intermediate_multiplication_seconds each time the function is
                called. Once seconds reaches a value of -1, minutes will
                decline by -1. Once we go below 0 minutes and 0 seconds,
                we will alert the user that their time is up.
                '''

                self.intermediate_multiplication_seconds -= 1

                if self.intermediate_multiplication_seconds == -1:
                    self.intermediate_multiplication_seconds += 60
                    self.intermediate_multiplication_minutes -= 1

                self.intermediate_multiplication_time = datetime.timedelta(minutes=self.intermediate_multiplication_minutes, seconds=self.intermediate_multiplication_seconds)
                self.root.ids.intermediate_multiplication_time.text = str(self.intermediate_multiplication_time)

                if '-1 day' in str(self.intermediate_multiplication_time):
                    self.root.ids.intermediate_multiplication_time.text = 'Time Over!'
                    self.event.cancel()
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_multiplication_start_timer(self):
        '''
        #Docstring: Method that will start the timer once a Button
        is pressed in the .kv file. I will bind the Button to this
        function. Once this is pressed, the time will be called and
        updated once per frame. This will give the visual effect of
        a countdown timer.
        '''
        self.event = Clock.schedule_interval(self.intermediate_multiplication_timer, 1)
        self.event()
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def intermediate_multiplication_time_over(self, *args):
        '''
        #Docstring: Method that will change the screen after the clock
        time has expired. This method will send the user back to the
        options screen so that they can choose to play again, or select
        another level to play on. I will also resent their score, their
        number of questions, their correct answers and % grade to 0
        '''

        #Set values back to 0, minutes back to 1
        self.intermediate_multiplication_questions = 0
        self.intermediate_multiplication_correct_answers = 0
        self.intermediate_multiplication_score = 0
        self.intermediate_multiplication_final_grade = 0
        self.intermediate_multiplication_minutes = 1
        self.intermediate_multiplication_seconds = 0

        #Set all of the labels to empty
        self.root.ids.intermediate_multiplication_question_number.text = ''
        self.root.ids.intermediate_multiplication_time.text = ''
        self.root.ids.intermediate_multiplication_user_answer.text = ''
        self.root.ids.intermediate_multiplication_result.text = ''
        self.root.ids.intermediate_multiplication_score.text = ''
        self.root.ids.intermediate_multiplication_final_grade.text = ''

        self.root.current = 'Intermediate Math Options'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_multiplication_addnums(self):
        '''
        #Docstring: This function will call the intermediate_multiplication() function that was
        created in the parent class 'intermediate_multiplication_Level'. It will allow us to
        generate numbers, add a question to the label, check to see if the users
        answer matches thecorrect answer,and then clear the screen when we want
        to generate a new question.
        '''
        self.intermediate_multiplication()
        self.root.ids.intermediate_multiplication_question.text = self.intermediate_multiplication_question
        self.root.ids.intermediate_multiplication_user_answer.text = ''
        self.root.ids.intermediate_multiplication_result.text = ''
        self.root.ids.intermediate_multiplication_score.text = self.root.ids.intermediate_multiplication_score.text.rstrip(':')
        self.root.ids.intermediate_multiplication_question_number.text = self.root.ids.intermediate_multiplication_question_number.text.rstrip(':')
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_multiplication_check_answer(self):
        '''
        #Docstring: A method that will allow me to check that the question the user entered
        is the correct answer or incorrect answer. The self.intermediate_multiplication_user_answer will
        be set equal to whatever the user entered in the label in the application. If the
        answer equals self.intermediate_multiplication_answer, I will increment their score by +=1, increment
        the number of correct answers by += 1, increment the number of total questions by += 1,
        update the label to let them know the answer IS correct, and display this on the screen. If
        their answer is not correct I will increment correct answers by += 0, I will increment the
        total number of questions, I will update the label to show them that the question is NOT
        correct, and I will display this information on the screen. If the clock indicates that the
        time is over, I will show them what their current score is, what their current %grade is,
        and what their current number of questions is. The screen will update the user that their
        time has expired, and the Clock.schedule_once() function will be used to move the user back
        to the options screen so that they can select a new level to play, or repeat the same level.
        I set the clock to 5 seconds so that they will have enough time to review their score.
        '''
        self.intermediate_multiplication_user_answer = self.root.ids.intermediate_multiplication_user_answer.text

        if self.intermediate_multiplication_answer == self.intermediate_multiplication_user_answer:
            self.root.ids.intermediate_multiplication_result.text = 'Correct!'
            self.intermediate_multiplication_score += 1
            self.intermediate_multiplication_correct_answers += 1
            self.intermediate_multiplication_questions += 1
            self.root.ids.intermediate_multiplication_score.text = 'Score: ' + str(self.intermediate_multiplication_score)
            self.root.ids.intermediate_multiplication_question_number.text = 'Question Number: ' + str(self.intermediate_multiplication_questions)
            

        else:
            self.root.ids.intermediate_multiplication_result.text = 'Incorrect!'
            self.intermediate_multiplication_score += 0
            self.intermediate_multiplication_questions += 1
            self.root.ids.intermediate_multiplication_score.text = 'Score: ' + str(self.intermediate_multiplication_score)
            self.root.ids.intermediate_multiplication_question_number.text = 'Question Number: ' + str(self.intermediate_multiplication_questions)

        if self.root.ids.intermediate_multiplication_time.text == 'Time Over!':
            self.root.ids.intermediate_multiplication_score.text = 'Score: ' + str(self.intermediate_multiplication_score)
            self.root.ids.intermediate_multiplication_question_number.text = 'Question Number: ' + str(self.intermediate_multiplication_questions)

            self.intermediate_multiplication_final_grade = (self.intermediate_multiplication_score / self.intermediate_multiplication_questions) * 100

            self.root.ids.intermediate_multiplication_final_grade.text = 'Final Grade: {0:.2f}%'.format(self.intermediate_multiplication_final_grade)

            Clock.schedule_once(self.intermediate_multiplication_time_over, 5)
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_multiplication_check_final_grade(self):
        self.intermediate_multiplication_final_grade = (self.intermediate_multiplication_score / self.intermediate_multiplication_questions) * 100

        self.root.ids.intermediate_multiplication_final_grade.text = 'Final Grade: {0:.2f}%'.format(self.intermediate_multiplication_final_grade)
            
    #------------------------------------------------------------------------------------------------------------------

    '''
    Now I create a series of Buttons for the intermediate additio level that will be used to help the user enter text to
    the label. If intermediate_multiplication_button1 is pressed, 1 will be added to the label. If intermediate_multiplication_button2 is
    pressed, 2 will be added to the label... and so on. This will help the user use the psuedo keypad to enter
    answers. There will be a clear Button that will delete whatever is in the label if the user decides to change
    their answer before entering a final answer.
    '''

    def intermediate_multiplication_button1(self):
        
        self.root.ids.intermediate_multiplication_user_answer.text += '1'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_multiplication_button2(self):
        self.root.ids.intermediate_multiplication_user_answer.text += '2'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_multiplication_button3(self):
        self.root.ids.intermediate_multiplication_user_answer.text += '3'
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_multiplication_button4(self):
        self.root.ids.intermediate_multiplication_user_answer.text += '4'
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_multiplication_button5(self):
        self.root.ids.intermediate_multiplication_user_answer.text += '5'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_multiplication_button6(self):
        self.root.ids.intermediate_multiplication_user_answer.text += '6'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_multiplication_button7(self):
        self.root.ids.intermediate_multiplication_user_answer.text += '7'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_multiplication_button8(self):
        self.root.ids.intermediate_multiplication_user_answer.text += '8'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_multiplication_button9(self):
        self.root.ids.intermediate_multiplication_user_answer.text += '9'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_multiplication_button0(self):
        self.root.ids.intermediate_multiplication_user_answer.text += '0'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_multiplication_clear_button(self):
        self.root.ids.intermediate_multiplication_user_answer.text = ''
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_division_timer(self, *args):
        '''
        #Docstring: Function that will subtract -1 seconds from
        self.intermediate_division_seconds each time the function is
        called. Once seconds reaches a value of -1, minutes will
        decline by -1. Once we go below 0 minutes and 0 seconds,
        we will alert the user that their time is up.
        '''

        self.intermediate_division_seconds -= 1

        if self.intermediate_division_seconds == -1:
            self.intermediate_division_seconds += 60
            self.intermediate_division_minutes -= 1

        self.intermediate_division_time = datetime.timedelta(minutes=self.intermediate_division_minutes, seconds=self.intermediate_division_seconds)
        self.root.ids.intermediate_division_time.text = str(self.intermediate_division_time)

        if '-1 day' in str(self.intermediate_division_time):
            self.root.ids.intermediate_division_time.text = 'Time Over!'
            self.event.cancel()
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_division_start_timer(self):
        '''
        #Docstring: Method that will start the timer once a Button
        is pressed in the .kv file. I will bind the Button to this
        function. Once this is pressed, the time will be called and
        updated once per frame. This will give the visual effect of
        a countdown timer.
        '''
        self.event = Clock.schedule_interval(self.intermediate_division_timer, 1)
        self.event()
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def intermediate_division_time_over(self, *args):
        '''
        #Docstring: Method that will change the screen after the clock
        time has expired. This method will send the user back to the
        options screen so that they can choose to play again, or select
        another level to play on. I will also resent their score, their
        number of questions, their correct answers and % grade to 0
        '''

        #Set values back to 0, minutes back to 1
        self.intermediate_division_questions = 0
        self.intermediate_division_correct_answers = 0
        self.intermediate_division_score = 0
        self.intermediate_division_final_grade = 0
        self.intermediate_division_minutes = 1
        self.intermediate_division_seconds = 0

        #Set all of the labels to empty
        self.root.ids.intermediate_division_question_number.text = ''
        self.root.ids.intermediate_division_time.text = ''
        self.root.ids.intermediate_division_user_answer.text = ''
        self.root.ids.intermediate_division_result.text = ''
        self.root.ids.intermediate_division_score.text = ''
        self.root.ids.intermediate_division_final_grade.text = ''

        self.root.current = 'Intermediate Math Options'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_division_addnums(self):
        '''
        #Docstring: This function will call the intermediate_division() function that was
        created in the parent class 'intermediate_division_Level'. It will allow us to
        generate numbers, add a question to the label, check to see if the users
        answer matches thecorrect answer,and then clear the screen when we want
        to generate a new question.
        '''
        self.intermediate_division()
        self.root.ids.intermediate_division_question.text = self.intermediate_division_question
        self.root.ids.intermediate_division_user_answer.text = ''
        self.root.ids.intermediate_division_result.text = ''
        self.root.ids.intermediate_division_score.text = self.root.ids.intermediate_division_score.text.rstrip(':')
        self.root.ids.intermediate_division_question_number.text = self.root.ids.intermediate_division_question_number.text.rstrip(':')
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_division_check_answer(self):
        '''
        #Docstring: A method that will allow me to check that the question the user entered
        is the correct answer or incorrect answer. The self.intermediate_division_user_answer will
        be set equal to whatever the user entered in the label in the application. If the
        answer equals self.intermediate_division_answer, I will increment their score by +=1, increment
        the number of correct answers by += 1, increment the number of total questions by += 1,
        update the label to let them know the answer IS correct, and display this on the screen. If
        their answer is not correct I will increment correct answers by += 0, I will increment the
        total number of questions, I will update the label to show them that the question is NOT
        correct, and I will display this information on the screen. If the clock indicates that the
        time is over, I will show them what their current score is, what their current %grade is,
        and what their current number of questions is. The screen will update the user that their
        time has expired, and the Clock.schedule_once() function will be used to move the user back
        to the options screen so that they can select a new level to play, or repeat the same level.
        I set the clock to 5 seconds so that they will have enough time to review their score.
        '''
        self.intermediate_division_user_answer = self.root.ids.intermediate_division_user_answer.text

        if self.intermediate_division_answer == self.intermediate_division_user_answer:
            self.root.ids.intermediate_division_result.text = 'Correct!'
            self.intermediate_division_score += 1
            self.intermediate_division_correct_answers += 1
            self.intermediate_division_questions += 1
            self.root.ids.intermediate_division_score.text = 'Score: ' + str(self.intermediate_division_score)
            self.root.ids.intermediate_division_question_number.text = 'Question Number: ' + str(self.intermediate_division_questions)
            

        else:
            self.root.ids.intermediate_division_result.text = 'Incorrect!'
            self.intermediate_division_score += 0
            self.intermediate_division_questions += 1
            self.root.ids.intermediate_division_score.text = 'Score: ' + str(self.intermediate_division_score)
            self.root.ids.intermediate_division_question_number.text = 'Question Number: ' + str(self.intermediate_division_questions)

        if self.root.ids.intermediate_division_time.text == 'Time Over!':
            self.root.ids.intermediate_division_score.text = 'Score: ' + str(self.intermediate_division_score)
            self.root.ids.intermediate_division_question_number.text = 'Question Number: ' + str(self.intermediate_division_questions)

            self.intermediate_division_final_grade = (self.intermediate_division_score / self.intermediate_division_questions) * 100

            self.root.ids.intermediate_division_final_grade.text = 'Final Grade: {0:.2f}%'.format(self.intermediate_division_final_grade)

            Clock.schedule_once(self.intermediate_division_time_over, 5)
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_division_check_final_grade(self):
        self.intermediate_division_final_grade = (self.intermediate_division_score / self.intermediate_division_questions) * 100

        self.root.ids.intermediate_division_final_grade.text = 'Final Grade: {0:.2f}%'.format(self.intermediate_division_final_grade)
            
    #------------------------------------------------------------------------------------------------------------------

    '''
    Now I create a series of Buttons for the intermediate additio level that will be used to help the user enter text to
    the label. If intermediate_division_button1 is pressed, 1 will be added to the label. If intermediate_division_button2 is
    pressed, 2 will be added to the label... and so on. This will help the user use the psuedo keypad to enter
    answers. There will be a clear Button that will delete whatever is in the label if the user decides to change
    their answer before entering a final answer.
    '''

    def intermediate_division_button1(self):
        
        self.root.ids.intermediate_division_user_answer.text += '1'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_division_button2(self):
        self.root.ids.intermediate_division_user_answer.text += '2'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_division_button3(self):
        self.root.ids.intermediate_division_user_answer.text += '3'
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_division_button4(self):
        self.root.ids.intermediate_division_user_answer.text += '4'
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_division_button5(self):
        self.root.ids.intermediate_division_user_answer.text += '5'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_division_button6(self):
        self.root.ids.intermediate_division_user_answer.text += '6'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_division_button7(self):
        self.root.ids.intermediate_division_user_answer.text += '7'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_division_button8(self):
        self.root.ids.intermediate_division_user_answer.text += '8'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_division_button9(self):
        self.root.ids.intermediate_division_user_answer.text += '9'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_division_button0(self):
        self.root.ids.intermediate_division_user_answer.text += '0'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def intermediate_division_clear_button(self):
        self.root.ids.intermediate_division_user_answer.text = ''
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_addition_timer(self, *args):
                '''
                #Docstring: Function that will subtract -1 seconds from
                self.expert_addition_seconds each time the function is
                called. Once seconds reaches a value of -1, minutes will
                decline by -1. Once we go below 0 minutes and 0 seconds,
                we will alert the user that their time is up.
                '''

                self.expert_addition_seconds -= 1

                if self.expert_addition_seconds == -1:
                    self.expert_addition_seconds += 60
                    self.expert_addition_minutes -= 1

                self.expert_addition_time = datetime.timedelta(minutes=self.expert_addition_minutes, seconds=self.expert_addition_seconds)
                self.root.ids.expert_addition_time.text = str(self.expert_addition_time)

                if '-1 day' in str(self.expert_addition_time):
                    self.root.ids.expert_addition_time.text = 'Time Over!'
                    self.event.cancel()
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_addition_start_timer(self):
        '''
        #Docstring: Method that will start the timer once a Button
        is pressed in the .kv file. I will bind the Button to this
        function. Once this is pressed, the time will be called and
        updated once per frame. This will give the visual effect of
        a countdown timer.
        '''
        self.event = Clock.schedule_interval(self.expert_addition_timer, 1)
        self.event()
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def expert_addition_time_over(self, *args):
        '''
        #Docstring: Method that will change the screen after the clock
        time has expired. This method will send the user back to the
        options screen so that they can choose to play again, or select
        another level to play on. I will also resent their score, their
        number of questions, their correct answers and % grade to 0
        '''

        #Set values back to 0, minutes back to 1
        self.expert_addition_questions = 0
        self.expert_addition_correct_answers = 0
        self.expert_addition_score = 0
        self.expert_addition_final_grade = 0
        self.expert_addition_minutes = 1
        self.expert_addition_seconds = 0

        #Set all of the labels to empty
        self.root.ids.expert_addition_question_number.text = ''
        self.root.ids.expert_addition_time.text = ''
        self.root.ids.expert_addition_user_answer.text = ''
        self.root.ids.expert_addition_result.text = ''
        self.root.ids.expert_addition_score.text = ''
        self.root.ids.expert_addition_final_grade.text = ''

        self.root.current = 'Expert Math Options'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_addition_addnums(self):
        '''
        #Docstring: This function will call the expert_addition() function that was
        created in the parent class 'expert_Addition_Level'. It will allow us to
        generate numbers, add a question to the label, check to see if the users
        answer matches thecorrect answer,and then clear the screen when we want
        to generate a new question.
        '''
        self.expert_addition()
        self.root.ids.expert_addition_question.text = self.expert_addition_question
        self.root.ids.expert_addition_user_answer.text = ''
        self.root.ids.expert_addition_result.text = ''
        self.root.ids.expert_addition_score.text = self.root.ids.expert_addition_score.text.rstrip(':')
        self.root.ids.expert_addition_question_number.text = self.root.ids.expert_addition_question_number.text.rstrip(':')
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_addition_check_answer(self):
        '''
        #Docstring: A method that will allow me to check that the question the user entered
        is the correct answer or incorrect answer. The self.expert_addition_user_answer will
        be set equal to whatever the user entered in the label in the application. If the
        answer equals self.expert_addition_answer, I will increment their score by +=1, increment
        the number of correct answers by += 1, increment the number of total questions by += 1,
        update the label to let them know the answer IS correct, and display this on the screen. If
        their answer is not correct I will increment correct answers by += 0, I will increment the
        total number of questions, I will update the label to show them that the question is NOT
        correct, and I will display this information on the screen. If the clock indicates that the
        time is over, I will show them what their current score is, what their current %grade is,
        and what their current number of questions is. The screen will update the user that their
        time has expired, and the Clock.schedule_once() function will be used to move the user back
        to the options screen so that they can select a new level to play, or repeat the same level.
        I set the clock to 5 seconds so that they will have enough time to review their score.
        '''
        self.expert_addition_user_answer = self.root.ids.expert_addition_user_answer.text

        if self.expert_addition_answer == self.expert_addition_user_answer:
            self.root.ids.expert_addition_result.text = 'Correct!'
            self.expert_addition_score += 1
            self.expert_addition_correct_answers += 1
            self.expert_addition_questions += 1
            self.root.ids.expert_addition_score.text = 'Score: ' + str(self.expert_addition_score)
            self.root.ids.expert_addition_question_number.text = 'Question Number: ' + str(self.expert_addition_questions)
            

        else:
            self.root.ids.expert_addition_result.text = 'Incorrect!'
            self.expert_addition_score += 0
            self.expert_addition_questions += 1
            self.root.ids.expert_addition_score.text = 'Score: ' + str(self.expert_addition_score)
            self.root.ids.expert_addition_question_number.text = 'Question Number: ' + str(self.expert_addition_questions)

        if self.root.ids.expert_addition_time.text == 'Time Over!':
            self.root.ids.expert_addition_score.text = 'Score: ' + str(self.expert_addition_score)
            self.root.ids.expert_addition_question_number.text = 'Question Number: ' + str(self.expert_addition_questions)

            self.expert_addition_final_grade = (self.expert_addition_score / self.expert_addition_questions) * 100

            self.root.ids.expert_addition_final_grade.text = 'Final Grade: {0:.2f}%'.format(self.expert_addition_final_grade)

            Clock.schedule_once(self.expert_addition_time_over, 5)
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_addition_check_final_grade(self):
        self.expert_addition_final_grade = (self.expert_addition_score / self.expert_addition_questions) * 100

        self.root.ids.expert_addition_final_grade.text = 'Final Grade: {0:.2f}%'.format(self.expert_addition_final_grade)
            
    #------------------------------------------------------------------------------------------------------------------

    '''
    Now I create a series of Buttons for the expert additio level that will be used to help the user enter text to
    the label. If expert_addition_button1 is pressed, 1 will be added to the label. If expert_addition_button2 is
    pressed, 2 will be added to the label... and so on. This will help the user use the psuedo keypad to enter
    answers. There will be a clear Button that will delete whatever is in the label if the user decides to change
    their answer before entering a final answer.
    '''

    def expert_addition_button1(self):
        
        self.root.ids.expert_addition_user_answer.text += '1'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_addition_button2(self):
        self.root.ids.expert_addition_user_answer.text += '2'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_addition_button3(self):
        self.root.ids.expert_addition_user_answer.text += '3'
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_addition_button4(self):
        self.root.ids.expert_addition_user_answer.text += '4'
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_addition_button5(self):
        self.root.ids.expert_addition_user_answer.text += '5'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_addition_button6(self):
        self.root.ids.expert_addition_user_answer.text += '6'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_addition_button7(self):
        self.root.ids.expert_addition_user_answer.text += '7'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_addition_button8(self):
        self.root.ids.expert_addition_user_answer.text += '8'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_addition_button9(self):
        self.root.ids.expert_addition_user_answer.text += '9'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_addition_button0(self):
        self.root.ids.expert_addition_user_answer.text += '0'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_addition_clear_button(self):
        self.root.ids.expert_addition_user_answer.text = ''
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_subtraction_timer(self, *args):
        '''
        #Docstring: Function that will subtract -1 seconds from
        self.expert_subtraction_seconds each time the function is
        called. Once seconds reaches a value of -1, minutes will
        decline by -1. Once we go below 0 minutes and 0 seconds,
        we will alert the user that their time is up.
        '''

        self.expert_subtraction_seconds -= 1

        if self.expert_subtraction_seconds == -1:
            self.expert_subtraction_seconds += 60
            self.expert_subtraction_minutes -= 1

        self.expert_subtraction_time = datetime.timedelta(minutes=self.expert_subtraction_minutes, seconds=self.expert_subtraction_seconds)
        self.root.ids.expert_subtraction_time.text = str(self.expert_subtraction_time)

        if '-1 day' in str(self.expert_subtraction_time):
            self.root.ids.expert_subtraction_time.text = 'Time Over!'
            self.event.cancel()
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_subtraction_start_timer(self):
        '''
        #Docstring: Method that will start the timer once a Button
        is pressed in the .kv file. I will bind the Button to this
        function. Once this is pressed, the time will be called and
        updated once per frame. This will give the visual effect of
        a countdown timer.
        '''
        self.event = Clock.schedule_interval(self.expert_subtraction_timer, 1)
        self.event()
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def expert_subtraction_time_over(self, *args):
        '''
        #Docstring: Method that will change the screen after the clock
        time has expired. This method will send the user back to the
        options screen so that they can choose to play again, or select
        another level to play on. I will also resent their score, their
        number of questions, their correct answers and % grade to 0
        '''

        #Set values back to 0, minutes back to 1
        self.expert_subtraction_questions = 0
        self.expert_subtraction_correct_answers = 0
        self.expert_subtraction_score = 0
        self.expert_subtraction_final_grade = 0
        self.expert_subtraction_minutes = 1
        self.expert_subtraction_seconds = 0

        #Set all of the labels to empty
        self.root.ids.expert_subtraction_question_number.text = ''
        self.root.ids.expert_subtraction_time.text = ''
        self.root.ids.expert_subtraction_user_answer.text = ''
        self.root.ids.expert_subtraction_result.text = ''
        self.root.ids.expert_subtraction_score.text = ''
        self.root.ids.expert_subtraction_final_grade.text = ''

        self.root.current = 'Expert Math Options'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_subtraction_addnums(self):
        '''
        #Docstring: This function will call the expert_subtraction() function that was
        created in the parent class 'expert_subtraction_Level'. It will allow us to
        generate numbers, add a question to the label, check to see if the users
        answer matches thecorrect answer,and then clear the screen when we want
        to generate a new question.
        '''
        self.expert_subtraction()
        self.root.ids.expert_subtraction_question.text = self.expert_subtraction_question
        self.root.ids.expert_subtraction_user_answer.text = ''
        self.root.ids.expert_subtraction_result.text = ''
        self.root.ids.expert_subtraction_score.text = self.root.ids.expert_subtraction_score.text.rstrip(':')
        self.root.ids.expert_subtraction_question_number.text = self.root.ids.expert_subtraction_question_number.text.rstrip(':')
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_subtraction_check_answer(self):
        '''
        #Docstring: A method that will allow me to check that the question the user entered
        is the correct answer or incorrect answer. The self.expert_subtraction_user_answer will
        be set equal to whatever the user entered in the label in the application. If the
        answer equals self.expert_subtraction_answer, I will increment their score by +=1, increment
        the number of correct answers by += 1, increment the number of total questions by += 1,
        update the label to let them know the answer IS correct, and display this on the screen. If
        their answer is not correct I will increment correct answers by += 0, I will increment the
        total number of questions, I will update the label to show them that the question is NOT
        correct, and I will display this information on the screen. If the clock indicates that the
        time is over, I will show them what their current score is, what their current %grade is,
        and what their current number of questions is. The screen will update the user that their
        time has expired, and the Clock.schedule_once() function will be used to move the user back
        to the options screen so that they can select a new level to play, or repeat the same level.
        I set the clock to 5 seconds so that they will have enough time to review their score.
        '''
        self.expert_subtraction_user_answer = self.root.ids.expert_subtraction_user_answer.text

        if self.expert_subtraction_answer == self.expert_subtraction_user_answer:
            self.root.ids.expert_subtraction_result.text = 'Correct!'
            self.expert_subtraction_score += 1
            self.expert_subtraction_correct_answers += 1
            self.expert_subtraction_questions += 1
            self.root.ids.expert_subtraction_score.text = 'Score: ' + str(self.expert_subtraction_score)
            self.root.ids.expert_subtraction_question_number.text = 'Question Number: ' + str(self.expert_subtraction_questions)
            

        else:
            self.root.ids.expert_subtraction_result.text = 'Incorrect!'
            self.expert_subtraction_score += 0
            self.expert_subtraction_questions += 1
            self.root.ids.expert_subtraction_score.text = 'Score: ' + str(self.expert_subtraction_score)
            self.root.ids.expert_subtraction_question_number.text = 'Question Number: ' + str(self.expert_subtraction_questions)

        if self.root.ids.expert_subtraction_time.text == 'Time Over!':
            self.root.ids.expert_subtraction_score.text = 'Score: ' + str(self.expert_subtraction_score)
            self.root.ids.expert_subtraction_question_number.text = 'Question Number: ' + str(self.expert_subtraction_questions)

            self.expert_subtraction_final_grade = (self.expert_subtraction_score / self.expert_subtraction_questions) * 100

            self.root.ids.expert_subtraction_final_grade.text = 'Final Grade: {0:.2f}%'.format(self.expert_subtraction_final_grade)

            Clock.schedule_once(self.expert_subtraction_time_over, 5)
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_subtraction_check_final_grade(self):
        self.expert_subtraction_final_grade = (self.expert_subtraction_score / self.expert_subtraction_questions) * 100

        self.root.ids.expert_subtraction_final_grade.text = 'Final Grade: {0:.2f}%'.format(self.expert_subtraction_final_grade)
            
    #------------------------------------------------------------------------------------------------------------------

    '''
    Now I create a series of Buttons for the expert additio level that will be used to help the user enter text to
    the label. If expert_subtraction_button1 is pressed, 1 will be added to the label. If expert_subtraction_button2 is
    pressed, 2 will be added to the label... and so on. This will help the user use the psuedo keypad to enter
    answers. There will be a clear Button that will delete whatever is in the label if the user decides to change
    their answer before entering a final answer.
    '''

    def expert_subtraction_button1(self):
        
        self.root.ids.expert_subtraction_user_answer.text += '1'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_subtraction_button2(self):
        self.root.ids.expert_subtraction_user_answer.text += '2'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_subtraction_button3(self):
        self.root.ids.expert_subtraction_user_answer.text += '3'
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_subtraction_button4(self):
        self.root.ids.expert_subtraction_user_answer.text += '4'
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_subtraction_button5(self):
        self.root.ids.expert_subtraction_user_answer.text += '5'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_subtraction_button6(self):
        self.root.ids.expert_subtraction_user_answer.text += '6'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_subtraction_button7(self):
        self.root.ids.expert_subtraction_user_answer.text += '7'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_subtraction_button8(self):
        self.root.ids.expert_subtraction_user_answer.text += '8'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_subtraction_button9(self):
        self.root.ids.expert_subtraction_user_answer.text += '9'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_subtraction_button0(self):
        self.root.ids.expert_subtraction_user_answer.text += '0'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_subtraction_clear_button(self):
        self.root.ids.expert_subtraction_user_answer.text = ''
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_multiplication_timer(self, *args):
                '''
                #Docstring: Function that will subtract -1 seconds from
                self.expert_multiplication_seconds each time the function is
                called. Once seconds reaches a value of -1, minutes will
                decline by -1. Once we go below 0 minutes and 0 seconds,
                we will alert the user that their time is up.
                '''

                self.expert_multiplication_seconds -= 1

                if self.expert_multiplication_seconds == -1:
                    self.expert_multiplication_seconds += 60
                    self.expert_multiplication_minutes -= 1

                self.expert_multiplication_time = datetime.timedelta(minutes=self.expert_multiplication_minutes, seconds=self.expert_multiplication_seconds)
                self.root.ids.expert_multiplication_time.text = str(self.expert_multiplication_time)

                if '-1 day' in str(self.expert_multiplication_time):
                    self.root.ids.expert_multiplication_time.text = 'Time Over!'
                    self.event.cancel()
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_multiplication_start_timer(self):
        '''
        #Docstring: Method that will start the timer once a Button
        is pressed in the .kv file. I will bind the Button to this
        function. Once this is pressed, the time will be called and
        updated once per frame. This will give the visual effect of
        a countdown timer.
        '''
        self.event = Clock.schedule_interval(self.expert_multiplication_timer, 1)
        self.event()
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def expert_multiplication_time_over(self, *args):
        '''
        #Docstring: Method that will change the screen after the clock
        time has expired. This method will send the user back to the
        options screen so that they can choose to play again, or select
        another level to play on. I will also resent their score, their
        number of questions, their correct answers and % grade to 0
        '''

        #Set values back to 0, minutes back to 1
        self.expert_multiplication_questions = 0
        self.expert_multiplication_correct_answers = 0
        self.expert_multiplication_score = 0
        self.expert_multiplication_final_grade = 0
        self.expert_multiplication_minutes = 1
        self.expert_multiplication_seconds = 0

        #Set all of the labels to empty
        self.root.ids.expert_multiplication_question_number.text = ''
        self.root.ids.expert_multiplication_time.text = ''
        self.root.ids.expert_multiplication_user_answer.text = ''
        self.root.ids.expert_multiplication_result.text = ''
        self.root.ids.expert_multiplication_score.text = ''
        self.root.ids.expert_multiplication_final_grade.text = ''

        self.root.current = 'Expert Math Options'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_multiplication_addnums(self):
        '''
        #Docstring: This function will call the expert_multiplication() function that was
        created in the parent class 'expert_multiplication_Level'. It will allow us to
        generate numbers, add a question to the label, check to see if the users
        answer matches thecorrect answer,and then clear the screen when we want
        to generate a new question.
        '''
        self.expert_multiplication()
        self.root.ids.expert_multiplication_question.text = self.expert_multiplication_question
        self.root.ids.expert_multiplication_user_answer.text = ''
        self.root.ids.expert_multiplication_result.text = ''
        self.root.ids.expert_multiplication_score.text = self.root.ids.expert_multiplication_score.text.rstrip(':')
        self.root.ids.expert_multiplication_question_number.text = self.root.ids.expert_multiplication_question_number.text.rstrip(':')
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_multiplication_check_answer(self):
        '''
        #Docstring: A method that will allow me to check that the question the user entered
        is the correct answer or incorrect answer. The self.expert_multiplication_user_answer will
        be set equal to whatever the user entered in the label in the application. If the
        answer equals self.expert_multiplication_answer, I will increment their score by +=1, increment
        the number of correct answers by += 1, increment the number of total questions by += 1,
        update the label to let them know the answer IS correct, and display this on the screen. If
        their answer is not correct I will increment correct answers by += 0, I will increment the
        total number of questions, I will update the label to show them that the question is NOT
        correct, and I will display this information on the screen. If the clock indicates that the
        time is over, I will show them what their current score is, what their current %grade is,
        and what their current number of questions is. The screen will update the user that their
        time has expired, and the Clock.schedule_once() function will be used to move the user back
        to the options screen so that they can select a new level to play, or repeat the same level.
        I set the clock to 5 seconds so that they will have enough time to review their score.
        '''
        self.expert_multiplication_user_answer = self.root.ids.expert_multiplication_user_answer.text

        if self.expert_multiplication_answer == self.expert_multiplication_user_answer:
            self.root.ids.expert_multiplication_result.text = 'Correct!'
            self.expert_multiplication_score += 1
            self.expert_multiplication_correct_answers += 1
            self.expert_multiplication_questions += 1
            self.root.ids.expert_multiplication_score.text = 'Score: ' + str(self.expert_multiplication_score)
            self.root.ids.expert_multiplication_question_number.text = 'Question Number: ' + str(self.expert_multiplication_questions)
            

        else:
            self.root.ids.expert_multiplication_result.text = 'Incorrect!'
            self.expert_multiplication_score += 0
            self.expert_multiplication_questions += 1
            self.root.ids.expert_multiplication_score.text = 'Score: ' + str(self.expert_multiplication_score)
            self.root.ids.expert_multiplication_question_number.text = 'Question Number: ' + str(self.expert_multiplication_questions)

        if self.root.ids.expert_multiplication_time.text == 'Time Over!':
            self.root.ids.expert_multiplication_score.text = 'Score: ' + str(self.expert_multiplication_score)
            self.root.ids.expert_multiplication_question_number.text = 'Question Number: ' + str(self.expert_multiplication_questions)

            self.expert_multiplication_final_grade = (self.expert_multiplication_score / self.expert_multiplication_questions) * 100

            self.root.ids.expert_multiplication_final_grade.text = 'Final Grade: {0:.2f}%'.format(self.expert_multiplication_final_grade)

            Clock.schedule_once(self.expert_multiplication_time_over, 5)
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_multiplication_check_final_grade(self):
        self.expert_multiplication_final_grade = (self.expert_multiplication_score / self.expert_multiplication_questions) * 100

        self.root.ids.expert_multiplication_final_grade.text = 'Final Grade: {0:.2f}%'.format(self.expert_multiplication_final_grade)
            
    #------------------------------------------------------------------------------------------------------------------

    '''
    Now I create a series of Buttons for the expert additio level that will be used to help the user enter text to
    the label. If expert_multiplication_button1 is pressed, 1 will be added to the label. If expert_multiplication_button2 is
    pressed, 2 will be added to the label... and so on. This will help the user use the psuedo keypad to enter
    answers. There will be a clear Button that will delete whatever is in the label if the user decides to change
    their answer before entering a final answer.
    '''

    def expert_multiplication_button1(self):
        
        self.root.ids.expert_multiplication_user_answer.text += '1'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_multiplication_button2(self):
        self.root.ids.expert_multiplication_user_answer.text += '2'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_multiplication_button3(self):
        self.root.ids.expert_multiplication_user_answer.text += '3'
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_multiplication_button4(self):
        self.root.ids.expert_multiplication_user_answer.text += '4'
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_multiplication_button5(self):
        self.root.ids.expert_multiplication_user_answer.text += '5'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_multiplication_button6(self):
        self.root.ids.expert_multiplication_user_answer.text += '6'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_multiplication_button7(self):
        self.root.ids.expert_multiplication_user_answer.text += '7'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_multiplication_button8(self):
        self.root.ids.expert_multiplication_user_answer.text += '8'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_multiplication_button9(self):
        self.root.ids.expert_multiplication_user_answer.text += '9'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_multiplication_button0(self):
        self.root.ids.expert_multiplication_user_answer.text += '0'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_multiplication_clear_button(self):
        self.root.ids.expert_multiplication_user_answer.text = ''
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_division_timer(self, *args):
        '''
        #Docstring: Function that will subtract -1 seconds from
        self.expert_division_seconds each time the function is
        called. Once seconds reaches a value of -1, minutes will
        decline by -1. Once we go below 0 minutes and 0 seconds,
        we will alert the user that their time is up.
        '''

        self.expert_division_seconds -= 1

        if self.expert_division_seconds == -1:
            self.expert_division_seconds += 60
            self.expert_division_minutes -= 1

        self.expert_division_time = datetime.timedelta(minutes=self.expert_division_minutes, seconds=self.expert_division_seconds)
        self.root.ids.expert_division_time.text = str(self.expert_division_time)

        if '-1 day' in str(self.expert_division_time):
            self.root.ids.expert_division_time.text = 'Time Over!'
            self.event.cancel()
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_division_start_timer(self):
        '''
        #Docstring: Method that will start the timer once a Button
        is pressed in the .kv file. I will bind the Button to this
        function. Once this is pressed, the time will be called and
        updated once per frame. This will give the visual effect of
        a countdown timer.
        '''
        self.event = Clock.schedule_interval(self.expert_division_timer, 1)
        self.event()
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def expert_division_time_over(self, *args):
        '''
        #Docstring: Method that will change the screen after the clock
        time has expired. This method will send the user back to the
        options screen so that they can choose to play again, or select
        another level to play on. I will also resent their score, their
        number of questions, their correct answers and % grade to 0
        '''

        #Set values back to 0, minutes back to 1
        self.expert_division_questions = 0
        self.expert_division_correct_answers = 0
        self.expert_division_score = 0
        self.expert_division_final_grade = 0
        self.expert_division_minutes = 1
        self.expert_division_seconds = 0

        #Set all of the labels to empty
        self.root.ids.expert_division_question_number.text = ''
        self.root.ids.expert_division_time.text = ''
        self.root.ids.expert_division_user_answer.text = ''
        self.root.ids.expert_division_result.text = ''
        self.root.ids.expert_division_score.text = ''
        self.root.ids.expert_division_final_grade.text = ''

        self.root.current = 'Expert Math Options'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_division_addnums(self):
        '''
        #Docstring: This function will call the expert_division() function that was
        created in the parent class 'expert_division_Level'. It will allow us to
        generate numbers, add a question to the label, check to see if the users
        answer matches thecorrect answer,and then clear the screen when we want
        to generate a new question.
        '''
        self.expert_division()
        self.root.ids.expert_division_question.text = self.expert_division_question
        self.root.ids.expert_division_user_answer.text = ''
        self.root.ids.expert_division_result.text = ''
        self.root.ids.expert_division_score.text = self.root.ids.expert_division_score.text.rstrip(':')
        self.root.ids.expert_division_question_number.text = self.root.ids.expert_division_question_number.text.rstrip(':')
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_division_check_answer(self):
        '''
        #Docstring: A method that will allow me to check that the question the user entered
        is the correct answer or incorrect answer. The self.expert_division_user_answer will
        be set equal to whatever the user entered in the label in the application. If the
        answer equals self.expert_division_answer, I will increment their score by +=1, increment
        the number of correct answers by += 1, increment the number of total questions by += 1,
        update the label to let them know the answer IS correct, and display this on the screen. If
        their answer is not correct I will increment correct answers by += 0, I will increment the
        total number of questions, I will update the label to show them that the question is NOT
        correct, and I will display this information on the screen. If the clock indicates that the
        time is over, I will show them what their current score is, what their current %grade is,
        and what their current number of questions is. The screen will update the user that their
        time has expired, and the Clock.schedule_once() function will be used to move the user back
        to the options screen so that they can select a new level to play, or repeat the same level.
        I set the clock to 5 seconds so that they will have enough time to review their score.
        '''
        self.expert_division_user_answer = self.root.ids.expert_division_user_answer.text

        if self.expert_division_answer == self.expert_division_user_answer:
            self.root.ids.expert_division_result.text = 'Correct!'
            self.expert_division_score += 1
            self.expert_division_correct_answers += 1
            self.expert_division_questions += 1
            self.root.ids.expert_division_score.text = 'Score: ' + str(self.expert_division_score)
            self.root.ids.expert_division_question_number.text = 'Question Number: ' + str(self.expert_division_questions)
            

        else:
            self.root.ids.expert_division_result.text = 'Incorrect!'
            self.expert_division_score += 0
            self.expert_division_questions += 1
            self.root.ids.expert_division_score.text = 'Score: ' + str(self.expert_division_score)
            self.root.ids.expert_division_question_number.text = 'Question Number: ' + str(self.expert_division_questions)

        if self.root.ids.expert_division_time.text == 'Time Over!':
            self.root.ids.expert_division_score.text = 'Score: ' + str(self.expert_division_score)
            self.root.ids.expert_division_question_number.text = 'Question Number: ' + str(self.expert_division_questions)

            self.expert_division_final_grade = (self.expert_division_score / self.expert_division_questions) * 100

            self.root.ids.expert_division_final_grade.text = 'Final Grade: {0:.2f}%'.format(self.expert_division_final_grade)

            Clock.schedule_once(self.expert_division_time_over, 5)
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_division_check_final_grade(self):
        self.expert_division_final_grade = (self.expert_division_score / self.expert_division_questions) * 100

        self.root.ids.expert_division_final_grade.text = 'Final Grade: {0:.2f}%'.format(self.expert_division_final_grade)
            
    #------------------------------------------------------------------------------------------------------------------

    '''
    Now I create a series of Buttons for the expert additio level that will be used to help the user enter text to
    the label. If expert_division_button1 is pressed, 1 will be added to the label. If expert_division_button2 is
    pressed, 2 will be added to the label... and so on. This will help the user use the psuedo keypad to enter
    answers. There will be a clear Button that will delete whatever is in the label if the user decides to change
    their answer before entering a final answer.
    '''

    def expert_division_button1(self):
        
        self.root.ids.expert_division_user_answer.text += '1'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_division_button2(self):
        self.root.ids.expert_division_user_answer.text += '2'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_division_button3(self):
        self.root.ids.expert_division_user_answer.text += '3'
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_division_button4(self):
        self.root.ids.expert_division_user_answer.text += '4'
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_division_button5(self):
        self.root.ids.expert_division_user_answer.text += '5'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_division_button6(self):
        self.root.ids.expert_division_user_answer.text += '6'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_division_button7(self):
        self.root.ids.expert_division_user_answer.text += '7'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_division_button8(self):
        self.root.ids.expert_division_user_answer.text += '8'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_division_button9(self):
        self.root.ids.expert_division_user_answer.text += '9'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_division_button0(self):
        self.root.ids.expert_division_user_answer.text += '0'
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def expert_division_clear_button(self):
        self.root.ids.expert_division_user_answer.text = ''
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

    
    

        

    

    

    
       
    
        
        



    











if __name__=='__main__':
    MinuteMathApp().run()
