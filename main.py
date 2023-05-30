class FlatIterator:

    def __init__(self, list_of_list):

        # Задание №3 код для списка списков любого уровня вложенности
        #
        # while True:
        #     self.list = []
        #     has_list = False
        #     for element in list_of_list:
        #         if type(element) is list:
        #             self.list.extend(element)
        #             has_list = True
        #         else:
        #             self.list.append(element)
        #     list_of_list = self.list
        #     if not has_list:
        #         break

        # Задание 1 код для списка

        self.list = list_of_list
        self.len = len(self.list)

    def __iter__(self):
        self.count1 = 0
        self.count2 = 0
        return self

    def __next__(self):
        # реализация для задания 1
        self.count2 += 1
        if self.count2 > len(self.list[self.count1]):
            self.count1 += 1
            self.count2 = 1
        if self.count1 == self.len:
            raise StopIteration

        item = self.list[self.count1][self.count2-1]
        print(item)
        return item

        # Реализация для задания 3
        # self.count += 1
        # if self.count > self.len:
        #     raise StopIteration
        # item = self.list[self.count-1]
        # return item

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
        [3, 4, 6]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, 3, 4, 6]
    ):

        assert flat_iterator_item == check_item

    # assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, 3, 4, 6]


if __name__ == '__main__':
    test_1()
