"""
2. Закодируйте любую строку по алгоритму Хаффмана.
"""


def char_frequency(string):
    freq = {}

    for char in list(string):
        freq[char] = freq[char] + 1 if char in freq else 1

    freq = list(freq.items())
    freq.sort(key=lambda x: x[1])

    return freq


class MyNode:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def add_in_array(array, node, num):
    for i, v in enumerate(array):
        if v[1] >= num:
            array.insert(i, (node, num))
            break
    else:
        array.append((node, num))


def get_side(data):
    value, num = data.pop(0)
    return value if type(value) == MyNode else MyNode(value), num


def growing_tree(array):
    if len(array) > 1:

        left, num1 = get_side(array)
        right, num2 = get_side(array)

        if num1 > num2:
            left, right = right, left

        add_in_array(
            array=array,
            num=num1 + num2,
            node=MyNode(
                value=left.value + right.value,
                left=left, right=right
            )  # MyNode
        )  # add_in_array

        print('char_freq =', char_freq)
        growing_tree(array)


def search(tree, char, code=''):
    if tree.value == char:
        return code

    if char in tree.left.value:
        return search(tree.left, char, code + '0')

    if char in tree.right.value:
        return search(tree.right, char, code + '1')


text = 'beep boop beer!'
# text = 'My cat - Vasiliy!'

char_freq = char_frequency(text)
growing_tree(char_freq)

bin_tree = char_freq[0][0]

print()
print(text, end=' | ')
for i in text:
    print(search(bin_tree, i), end=' ')
