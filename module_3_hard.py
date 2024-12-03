
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(*massive):
    summ = 0

    def calculate_element(element):
        nonlocal summ
        if isinstance(element, int):
            summ += element
        elif isinstance(element, str):
            summ += len(element)
        elif isinstance(element, list):
            for i in element:
                calculate_element(i)
        elif isinstance(element, tuple):
            for i in element:
                calculate_element(i)
        elif isinstance(element, set):
            for i in element:
                calculate_element(i)
        elif isinstance(element, dict):
            for key, value in element.items():
                if isinstance(key, int):
                    summ += key
                elif isinstance(key, str):
                    summ += len(key)
                calculate_element(value)


    for i in massive:
        calculate_element(i)

    return summ



result = calculate_structure_sum(*data_structure)
print(result)