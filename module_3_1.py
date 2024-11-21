calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    tuple_ = (len(string), string.upper(), string.lower())
    count_calls()
    print(tuple_)

def is_contains(string, list):
    result = False
    for item in list:
        item = item.casefold()
        if string.casefold() in item:
            result = True
    count_calls()
    print(result)

string_info('TaBlE')
string_info('rEfrIgErAtOr')
string_info('flOWer')
is_contains('Four', ['One', 'Two', 'Three'])
is_contains('bEAr', ['Lion', 'Bear', 'Wolf'])
print(calls)