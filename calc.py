from server import *
import math

def read(inpu):
    lis = []
    for x in inpu:
        if x == "C":
            if len(lis) != 0:
                del lis[len(lis)-1]
        elif x == "CE":
            del lis[:]
        else:
            lis.append(x)
    return lis

def show(inpu):
    string = ""
    for x in inpu:
        string += str(x)
    return string
    
def intep(inpu):
    string = ""
    for x in inpu:
        if x == "sin(":
            string += "math.sin("
        elif x == "cos(":
            string += "math.cos("
        elif x == "tan(":
            string += "math.tan("
        elif x == "sqrt(":
            string += "math.sqrt("
        elif x == "log(":
            string += "math.log("
        else:
            string += str(x)
    return string
        
def displa(x):
    display = ""
    global n
    global user_input
    global ans
    if (x == "+" or x == "-" or x == "*" or x == "/") and history[0] == []:
        n = 0
        user_input.append(ans)
        user_input.append(x)
        history[n] = user_input
        do = read(user_input)
        display = show(do)
    elif x == "=" and user_input != []:
        for i in range(len(history)-1, 0, -1):
            history[i] = history[i-1][:]
        del history[0][:]
        do = read(history[1])
        display = intep(do)
        try:
            ans = eval(display)
            display = str(ans)
        except SyntaxError:
            display += ")"
            try:
                ans = eval(display)
                display = str(ans)
            except SyntaxError:
                display = "syntax error"
            except ValueError:
                display = "math error"
            except:
                display = "something wrong"
        except ValueError:
                display = "math error"
        except:
            display = "something wrong"

        del user_input[:]
    elif x == "=":
        display = ans
    elif x == "<":
        if n != 4 and history[n+1] != []:
            n += 1
        do = read(history[n])
        display = show(do)
    elif x == ">":
        if n != 0:
            n -= 1
        do = read(history[n])
        display = show(do)
    else:
        n = 0
        user_input.append(x)
        history[n] = user_input
        do = read(user_input)
        display = show(do)
    return display