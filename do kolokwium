import math
import numpy as np
import matplotlib.pyplot as plt

# TAYLOR SERIES FUNCTIONS
MIN_ERROR = 0.005
MAX_TERMS = 85

def taylor_approx(x, function, a):
    ''' this function approximates the number of terms required to build a Taylor polynomial by calculating the number of terms required to approximate a value of e that is less than MIN_ERROR '''
    for i in range(1, MAX_TERMS + 1):

        if(function == 'exp'):
            approx = func_exp(x, i)
            actual = math.exp(x)

        elif(function == 'cos'):
            approx = func_cos(x, i)
            actual = np.cos(x)

        elif(function == 'binom'):
            approx = func_binom(x, a, i)
            actual = (1 + x) ** a

        elif(function == 'ln'):
            approx = func_ln(x, a, i)
            actual = np.log(x)

        error = abs(approx - actual)
        if error < MIN_ERROR or i == MAX_TERMS:
            terms = i
            break

    return terms, approx, actual, error

# APPROXIMATION FUNCTIONS

def func_exp(x, n):
    ''' approximates exponential functions in the form e ** x '''
    exp_approx = 0;
    for i in range(n):
        num = x**i / math.factorial(i)
        exp_approx += num

    return exp_approx

def func_cos(x, n):
    ''' approximates cos() function '''
    cos_approx = 0
    for i in range(n):
        coef = (-1)**i
        num = x**(2*i)
        denom = math.factorial(2*i)
        cos_approx += ( coef ) * ( (num)/(denom) )
    
    return cos_approx

def func_binom(x, a, n):
    ''' approximates binomial functions of form (1 + x) ** a '''
    binom_approx = 0
    for i in range(n):
        coef = math.comb(a, i)
        num = x**i
        binom_approx += coef * num

    return binom_approx

def func_ln(x, a, n):
    ''' approximates ln(x) for 0 < x < 2a '''
    ln_approx = np.log(x)
    for i in range(1, n):
        num = ((x - a)**n) / (n*(a**n))
        ln_approx += num

    return ln_approx

def main():
    function = 'ln'
    step = 0.5
    x_bounds = {
        'low': -10,
        'high': 100
    }
    y_bounds = {
        'low': -10,
        'high': 100
    }
    a = 10

    # define default input / output params
    x = np.arange(x_bounds['low'], x_bounds['high'], step, dtype=np.float64)
    y = np.copy(x)
    y_hat = np.copy(x)

    i = 0
    for index in x:
        terms, approx, actual, error = taylor_approx(index, function, a)
        y[i] = actual
        y_hat[i] = approx
        i += 1
        print(f'{terms} terms: Taylor Series approx= {approx}, exp calc= {actual}, error = {error}')

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.plot(x, y_hat)
    ax.legend([str(function) + '() function','Taylor Series - ' + str(terms) + ' terms'])
    plt.xlim([x_bounds['low'], x_bounds['high']])
    plt.ylim([y_bounds['low'], y_bounds['high']])

    plt.show()

if __name__ == "__main__":
    main()



import sympy as sp

def taylor_series(f, x0, n):
    """
    Oblicza rozwinięcie Taylora funkcji f wokół punktu x0 do rzędu n.
    
    f  – funkcja symboliczna (sympy)
    x0 – punkt rozwinięcia
    n  – liczba wyrazów
    """
    x = sp.symbols('x')
    series = 0
    for k in range(n + 1):
        term = (sp.diff(f, x, k).subs(x, x0) / sp.factorial(k)) * (x - x0)**k
        series += term
    return sp.simplify(series)


x = sp.symbols('x')
f = sp.sin(x)

ts = taylor_series(f, 0, 6)
print(ts)




def chi_squared(observed, expected):
    """
    Liczy statystykę chi-squared (χ²) dla dwóch list:
    observed – wartości obserwowane
    expected – wartości oczekiwane (muszą być > 0)
    """
    if len(observed) != len(expected):
        raise ValueError("Listy 'observed' i 'expected' muszą mieć tę samą długość")

    chi2 = 0
    for o, e in zip(observed, expected):
        if e == 0:
            raise ValueError("Wartość oczekiwana nie może być równa zero")
        chi2 += (o - e)**2 / e
    return chi2





def chi_squared_from_file(filename):
    observed = []
    expected = []

    with open(filename, 'r') as f:
        for line in f:
            if line.strip():  # pomijanie pustych linii
                o, e = map(float, line.split())
                observed.append(o)
                expected.append(e)

    # liczenie chi-squared
    chi2 = 0
    for o, e in zip(observed, expected):
        if e == 0:
            raise ValueError("Wartość oczekiwana nie może być równa zero")
        chi2 += (o - e)**2 / e
    
    return chi2
chi2_value = chi_squared_from_file("dane.txt")
print("Chi-squared:", chi2_value)





