

def reverser(smth):
    reversed = ""
    for char in smth:
        reversed = char + reversed
    return reversed


print(reverser('hello'))


def sumOdigits(num):
    sum = 0
    for char in str(num):
        sum = int(char) + sum
    return sum


print(sumOdigits(1234))


def fib(N):
    last = 0
    cur = 1
    fibby = [0,1]
    index = 3

    if N <= 0:
        return []
    elif N == 1:
        return [0]
    elif N == 2:
        return fibby

    while index != N + 1:
        cur = cur + last
        last = cur - last
        fibby.append(cur)
        index += 1    
    return fibby

print(fib(5))


def vowelCnt(string):
    vowels = {"a", "e", "i", "o", "u", "y"}
    count = 0
    for char in string.lower():
        if char in vowels:
            count += 1
    return count

print(vowelCnt("Breyon's Crayons."))


def paliChecker(smth: str):
    reversed = reverser(smth).lower()
    return reversed == smth.lower()

print(paliChecker("Mom"))


def uniqueness(smth):
    count = set()
    for element in smth:
        count.add(element)
    return list(count)

print(uniqueness([1,1,1,2,5,4,78,65,65]))

def brackets(text):
    round = 0
    for char in text:
        if char == "(":
            round += 1
        if char == ")":
            if round % 2 == 0:
                print("Not balanced")
            else:
                round += 1
    if round % 2 == 0:
        print("Balanced, as all things should be. - Thanos")
    else:
        print("Not balanced")

print(brackets("(()()())"))


def brackets_v2(text):
    current_open = 0
    b_open = 0
    b_close = 0

    for c in text:
        if c == '(':
            b_open += 1
        elif c == ')':
            b_close += 1

        if b_close > b_open:
            return False

    return b_open == b_close

print('Brackets v2')
print(brackets_v2(')(()))()())'))
print(brackets_v2('(())()()(())()'))