###############################################################################
# File: hashCalc.py      Monday 7 Oct 2013  ac
#
# Usage:  y = express(x)
#
# Action: In string x the hash character '#' is used to represent a dice roll.
#         eg #6  represents random number 1 thru 6
#            #20 represents random number 1 thru 20
#            3#6 represents three #6s added together   and so on
#        express() should comply with usual expression syntax
#
# Addition: modify so that multiple assignment statements can be used
#           of the form:  a = expression ; b = expression ;
#                           ^            ^
#                           literals
#
###############################################################################

import random

# Utility functions for rolling dice
# underscore so that they are not used inadvertently


def d(n):
    '''generate and return a random number 1 thru n'''
    return random.randint(1, n)


def r(m, n):
    '''generate m d(n)s and sum them'''
    t = 0
    for i in range(m):
        t += d(n)
    return t


def rollStat(kind=0):
    if kind == 0:
        stats = [0, 0, 0]
        stats = [d(6) for x in stats]
    elif kind == 1:
        stats = [0, 0, 0, 0]
        stats = [d(6) for x in stats]
        stats.remove(min(stats))
    elif kind == 2:
        stats = [0, 0, 0]
        stats = [d(6) for x in stats]
        stats = [d(6) if x < 5 else x for x in stats]
        stats = [d(6) if x < 4 else x for x in stats]
    else:
        stats = [0, 0, 0]
    return sum(stats)


def rollStats(kind=0):
    stats = [0, 0, 0, 0, 0, 0]
    stats = [rollStat(kind) for x in stats]
    if stats[0] == 18:
        stats[0] = stats[0] + d(100) / 1000.0
    return stats


#To add arrays. b could be strings but only integer
def add(a, b):
    return [a + int(x) for a, x in zip(a, b)]


# Description of algorithm
#
# find a #
# look after the hash for completion of an expression
# enclose the expression in parentheses - leaving the hash
# look for expression before the hash
# if no such expression found - substitute # with d
# else
# find beginning of expression and insert r(
# now substitute #( with a comma
# completed
# If any more hashes?  Then do again

def express(s):
    '''process an expression with # as the die roll symbol'''
    # stick in delimiters so we don't walk off the end'
    s = '|' + s + '|'    # Use bar '|' as not present in expressions
    p = s.find('#')
    while p >= 0:
        # process forward of the # and insert parentheses where appropriate
        aft = p + 1
        c = s[aft]
        while c == ' ': # Skip space routine
            aft += 1
            c = s[aft]
        while c == '#':
            aft += 1
            c = s[aft]
        if c in '01234567890.':  # Is it a number?
            while c in '0123456789.':
                aft += 1
                c = s[aft]
        elif c.lower() in '(abcdefghijklmnopqrstuvwxyz_':  # Ident or ()
            while c.lower() in 'abcdefghijklmnopqrstuvwxyz_.0123456789':
                aft += 1
                c = s[aft]
            if c == '(':  # () term or function
                ccount = 1
                while c != ')' or ccount != 0:
                    aft += 1
                    c = s[aft]
                    if c == '(':
                        ccount += 1
                    if c == ')':
                        ccount -= 1
                aft += 1
                c = s[aft]
            while c == '[':  # could be list (array)
                ccount = 1
                while c != ']' or ccount != 0:
                    aft += 1
                    c = s[aft]
                    if c == '[':
                        ccount += 1
                    if c == ']':
                        ccount -= 1
                aft += 1
                c = s[aft]
        else:
            pass
        s = s[:aft] + ')' + s[aft:]
        s = s[:p] + '#(' + s[p + 1:]
        # Now search before the # and substitute for multiple dice
        aft = p - 1
        c = s[aft]
        while c == ']':
            ccount = 1
            while c != '[' or ccount != 0:
                aft -= 1
                c = s[aft]
                if c == ']':
                    ccount += 1
                if c == '[':
                    ccount -= 1
            aft -= 1
            c = s[aft]
        if c == ')':
            ccount = 1
            while c != '(' or ccount != 0:
                aft -= 1
                c = s[aft]
                if c == ')':
                    ccount += 1
                if c == '(':
                    ccount -= 1
            aft -= 1
            c = s[aft]
        while c.lower() in 'abcdefghijklmnopqrstuvwxyz_.0123456789':
            aft -= 1
            c = s[aft]

        # Now make the substitutions necessary
        aft += 1    # point to first character of inclusion, if any.
        if p == aft:
            s = s[:p] + 'd' + s[p + 1:]
        else:
            # Modify later in string first else it will change addresses
            s = s[:p] + ',' + s[p + 2:]
            s = s[:aft] + 'r(' + s[aft:]

        #end of loop process for this # is there another?
        p = s.find('#')

    # Now rip out the delimiters introduced at beginning of function
    s = s[1:len(s) - 1]
    return s


# Description of assignment algorithm

def statements(s):
    s = s.replace(' ', '')
    ss = s.split(';')
    assigns = []
    for sment in ss:
        assigns.append(statement(sment))
    for assign in assigns:
        print( 'to:', assign[0], 'from:', assign[1])
    # process the returned values
#    for assign in assigns:
#        if assign[0] =='output':
#            print('output =', eval(assign[1]))
#        else:
#            globals()[assign[0]] = eval(assign[1])
    return assigns


# +++++++++






def statement(s):
    # check to see if we have an assign
    start = 0
    finish = len(s)
    p = s.find('=', start, finish)
    if p >= 1:
        assign = True
        if s[p + 1] == '=':
            assign = False
            p += 1
        elif s[p - 1] == '!':
            assign = False
        elif s[p - 1] == '<' and s[p - 2] != '<':
            assign = False
        elif s[p - 1] == '>' and s[p - 2] != '>':
            assign = False
        else:
            assign = True
    else:
        assign = False

    if assign:          # we have an assignment
        lvalue = s[start:p]
        start = p + 1
    else:
        lvalue = 'output'
    rvalue = s[start: finish]

    return lvalue, express(rvalue)




if __name__ == '__main__':
    carryon = True
    print('Hello,')
    while( carryon ):
        z = input('Statement: ')
        if z == 'exit':
            carryon = False
            print('bye.')
        else:
            z1 = statements(z)
            print()



#if __name__ == '__main__':
    #carryon = True
    #print('Hello,')
    #while( carryon ):
        #z = input('Expression: ')
        #if z == 'exit':
            #carryon = False
            #print('bye.')
        #else:
            #z = z.strip()
            #if z != '':
                #z1 = express(z)
                #print('   Reduced: ' + z1)
                #z2 = eval(z1)
                #print('    Result: ', end='')
                #print(z2)
                #print()



