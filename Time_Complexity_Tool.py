
#import modules
 
import os
import random
import string
import tkinter as tk
import numpy as np
from tkinter import *
from tkinter import ttk
from random import randint
from timeit import repeat
from tkinter.scrolledtext import ScrolledText

# Designing window for registration
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", ).pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, command = register_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
    
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("250x200")
    Label(user_not_found_screen, text="User Not Found, please register").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
    

    
# Implementing event on Analysis_screen button
    
def Analysis_screen():
    global Analysis_screen
    Analysis_screen = Tk()
    Analysis_screen.title("Analysis_screen")
    Analysis_screen.geometry("1000x720")
    Label(Analysis_screen, text="Please enter code in the entry section").pack()
    
    ScrolledText(Analysis_screen).pack()
   
    Button(Analysis_screen,text="Analyse", height="5", width="50", command = Analyse).pack()
    Label(text="").pack()
    Button(Analysis_screen, text="Recommendation", height="5", width="50", command=recommendation).pack()
    Label(text="").pack()
    Button(Analysis_screen, text="Select_Language", height="5", width="50", command=Select_Language).pack()
    Label(text="").pack()
    Button(Analysis_screen, text="Exit", height="5", width="50", command=exit).pack()
    Label(text="").pack()
    Label(Analysis_screen, text="").pack()
    Analysis_screen.mainloop()
    
 
# Time_complexity():

class NotFittedError(Exception):
    pass


class ComplexityClass(object):
   

    def __init__(self):
        # list of parameters of the fitted function class as returned by the
        # last square method np.linalg.lstsq
        self.coeff = None

    def fit(self, n, t):
        """ Fit complexity class parameters to timing data.

        Input:
        ------

        n -- Array of values of N for which execution time has been measured.

        t -- Array of execution times for each N in seconds.

        Output:
        -------

        residuals -- Sum of square errors of fit
        """
        x = self._transform_n(n)
        y = self._transform_time(t)
        coeff, residuals, rank, s = np.linalg.lstsq(x, y, rcond=-1)
        self.coeff = coeff
        return residuals[0]

    def compute(self, n):
        """ Compute the value of the fitted function at `n`. """
        if self.coeff is None:
            raise NotFittedError()

        # Result is linear combination of the terms with the fitted
        # coefficients
        x = self._transform_n(n)
        tot = 0
        for i in range(len(self.coeff)):
            tot += self.coeff[i] * x[:, i]
        return tot

    def __str__(self):
        prefix = '{}: '.format(self.__class__.__name__)

        if self.coeff is None:
            return prefix + ': not yet fitted'
        return prefix + self.format_str().format(*tuple(self.coeff)) + ' (sec)'

# --- abstract methods

    @classmethod
    def format_str(cls):
        """ Return a string describing the fitted function.

        The string must contain one formatting argument for each coefficient.
        """
        return 'FORMAT STRING NOT DEFINED'

    def _transform_n(self, n):
        """ Terms of the linear combination defining the complexity class.

        Output format: number of Ns x number of coefficients .
        """
        raise NotImplementedError()

    def _transform_time(self, t):
        """ Transform time as needed for fitting.
        (e.g., t->log(t)) for exponential class.
        """
        return t

    def __gt__(self, other):
        return self.order > other.order

    def __lt__(self, other):
        return self.order < other.order

    def __le__(self, other):
        return (self < other) or self == other

    def __ge__(self, other):
        return (self > other) or self == other

    def __eq__(self, other):
        return self.order == other.order

    def __hash__(self):
        return id(self)


# datagen

def n_(n):
    """ Return N. """
    return n


def range_n(n, start=0):
    """ Return the sequence [start, start+1, ..., start+N-1]. """
    return list(range(start, start+n))


def integers(n, min_, max_):
    """ Return sequence of N random integers between min_ and max_ (included).
    """
    return [random.randint(min_, max_) for _ in range(n)]


def large_integers(n):
    """ Return sequence of N large random integers. """
    return [random.randint(-50, 50) * 1000000 + random.randint(0, 10000)
            for _ in range(n)]


def strings(n, chars=string.ascii_letters):
    """ Return random string of N characters, sampled at random from `chars`.
    """
    return ''.join([random.choice(chars) for i in xrange(n)])


# --- Concrete implementations of the most popular complexity classes


class Constant(ComplexityClass):
    order = 10

    def _transform_n(self, n):
        return np.ones((len(n), 1))

    @classmethod
    def format_str(cls):
        return 'time = {:.2G}'


class Linear(ComplexityClass):
    order = 30

    def _transform_n(self, n):
        return np.vstack([np.ones(len(n)), n]).T

    @classmethod
    def format_str(cls):
        return 'time = {:.2G} + {:.2G}*n'


class Quadratic(ComplexityClass):
    order = 50

    def _transform_n(self, n):
        return np.vstack([np.ones(len(n)), n * n]).T

    @classmethod
    def format_str(cls):
        return 'time = {:.2G} + {:.2G}*n^2'


class Cubic(ComplexityClass):
    order = 60

    def _transform_n(self, n):
        return np.vstack([np.ones(len(n)), n ** 3]).T

    @classmethod
    def format_str(cls):
        return 'time = {:.2G} + {:.2G}*n^3'


class Logarithmic(ComplexityClass):
    order = 20

    def _transform_n(self, n):
        return np.vstack([np.ones(len(n)), np.log(n)]).T

    @classmethod
    def format_str(cls):
        return 'time = {:.2G} + {:.2G}*log(n)'


class Linearithmic(ComplexityClass):
    order = 40

    def _transform_n(self, n):
        return np.vstack([np.ones(len(n)), n * np.log(n)]).T

    @classmethod
    def format_str(cls):
        return 'time = {:.2G} + {:.2G}*n*log(n)'


class Polynomial(ComplexityClass):
    order = 70

    def _transform_n(self, n):
        return np.vstack([np.ones(len(n)), np.log(n)]).T

    def _transform_time(self, t):
        return np.log(t)

    @classmethod
    def format_str(cls):
        return 'time = {:.2G} * x^{:.2G}'


class Exponential(ComplexityClass):
    order = 80

    def _transform_n(self, n):
        return np.vstack([np.ones(len(n)), n]).T

    def _transform_time(self, t):
        return np.log(t)

    @classmethod
    def format_str(cls):
        return 'time = {:.2G} * {:.2G}^n'


ALL_CLASSES = [Constant, Linear, Quadratic, Cubic, Polynomial,
               Logarithmic, Linearithmic, Exponential]

time_complex= "linear"
    
def measure_execution_time(func, data_generator,
    min_n=100, max_n=100000, n_measures=10,
    n_repeats=1, n_timings=1):
    
    class func_wrapper(object):

        def __init__(self, n):
            self.data = data_generator(n)

        def __call__(self):
            return func(self.data)

    # TODO: check that max_n is not larger than max int64
    ns = np.linspace(min_n, max_n, n_measures).astype('int64')
    execution_time = np.empty(n_measures)
    for i, n in enumerate(ns):
        timer = Timer(func_wrapper(n))
        measurements = timer.repeat(n_timings, n_repeats)
        execution_time[i] = np.min(measurements)
    return ns, execution_time

def infer_big_o_class(ns, time, classes=ALL_CLASSES, verbose=False):

    best_class = None
    best_residuals = np.inf
    fitted = {}
    for class_ in classes:
        inst = class_()
        residuals = inst.fit(ns, time)
        fitted[inst] = residuals

            # NOTE: subtract 1e-6 for tiny preference for simpler methods
            # TODO: improve simplicity bias (AIC/BIC)?
        if residuals < best_residuals - 1e-6:
            best_residuals = residuals
            best_class = inst
        if verbose:
            print(inst, '(r={:f})'.format(residuals))
    return best_class, fitted


def big_o(func, data_generator,
              min_n=100, max_n=100000, n_measures=10,
              n_repeats=1, n_timings=1, classes=ALL_CLASSES, verbose=False, return_raw_data=False):
    ns, time = measure_execution_time(func, data_generator,
                                      min_n, max_n, n_measures, n_repeats,
                                      n_timings)
    best, fitted = infer_big_o_class(ns, time, classes, verbose=verbose)

    if return_raw_data:
        fitted['measures'] = ns
        fitted['times'] = time

    return best, fitted
    
    

# Implementing event on analyse button
     
def Analyse():
    global Analysis
    Analysis = Tk()
    Analysis.title("Analysis")
    Analysis.geometry("350x250")
    Label(Analysis, text="Time complexity").pack()
    if time_complex == "constant":
        Label(Analysis, text="The Time complexity your program is O(1)").pack()
    elif time_complex== "linear":
        Label(Analysis, text="The Time complexity your program is O(n)").pack()
    elif time_complex=="quadratic":
        Label(Analysis, text="The Time complexity your program is O(n^2)").pack()
    elif time_complex=="cubic":
        Label(Analysis, text="The Time complexity your program is O(n^3)").pack()
    elif time_complex=="exponential":
        Label(Analysis, text="The Time complexity your program is O(2^n)").pack()
    elif time_complex=="logarithmic":
        Label(Analysis, text="The Time complexity your program is O(log_n)").pack()
    else :
        Label(Analysis, text="Sorry, cannot find the complexity of this program").pack()
        
        
# Implementing event on select language button
     
def Select_Language():
    win =Tk()
    win.geometry('400x300')
    course=['C','C++','Java',
    'Python','swift','ruby',
    'PHP','ASP','JS']
    l1=Label(win,text="Choose Your Favourite Language")
    l1.grid(column=0, row=0)
    cb=ttk.Combobox(win,values=course,width=10)
    cb.grid(column=0, row=1)
    cb.current(0)
    b=Button(win,text="ok",command=language_selected)
    b.grid(column=0, row=2)
    l2=Label(win,text="")
    l2.grid(column=0, row=3)
    win.mainloop()

def language_selected():
    global language_selected_screen
    language_selected_screen = Toplevel(Analysis_screen)
    language_selected_screen.title("Language selected")
    language_selected_screen.geometry("250x100")
    Label(language_selected_screen, text="Language Selected Successfully").pack()
    

def delete_language_selected_screen():
    language_selected_screen.destroy()
    
    
# Implementing event on recommendation button
     
def recommendation():
    if time_complex=="linear":
        Label(Analysis_screen, text="your code has best time complexity", fg="green", font=("calibri", 11)).pack()
    elif time_complex=="logarithmic":
        Label(Analysis_screen, text="your code has best time complexity", fg="green", font=("calibri", 11)).pack()
    elif time_complex=="constant":
            Label(Analysis_screen, text="your code has average time complexity", fg="green", font=("calibri", 11)).pack()
    elif time_complex=="quadratic":
        Label(Analysis_screen, text="your code has worst time complexity", fg="red", font=("calibri", 11)).pack()
    elif time_complex=="exponential":
        Label(Analysis_screen, text="your code has worst time complexity", fg="red", font=("calibri", 11)).pack()
    elif time_complex=="cubic":
        Label(Analysis_screen, text="your code has worst time complexity", fg="red", font=("calibri", 11)).pack()
    else :
         Label(Analysis_screen, text="Sorry can't say anything about your program time complexity", fg="red", font=("calibri", 11)).pack()
    


 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("1000x720")
    main_screen.title("Time Complexity Analyser Tool")
    Label(text="Select Your Choice", width="300", height="2", font=("Calibri", 25)).pack()
    Label(text="").pack()
    Button(text="Login", height="5", width="50", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="5", width="50", command=register).pack()
    Label(text="").pack()
    Button(text="Analysis_Screen", height="5", width="50", command=Analysis_screen).pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text=" Tool To Support Time Complexity By Kishan Kumar Sharma(19BCE2569) and Aditya Narayan (19BCE2172) ").pack()
    main_screen.mainloop()
 
 
main_account_screen()
