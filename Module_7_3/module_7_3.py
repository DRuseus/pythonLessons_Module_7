class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def __remove_punctuation(self, text):
        punctuation_list = [',', '.', '=', '!', '?', ';', ':', ' - ']
        text = text.replace('\n', ' ')
        text = text.lower()
        for p in punctuation_list:
            text = text.replace(p, '')
            text = text.rstrip(' ')
            text = text.strip(' ')
        return text

    def get_all_words(self, file_name=None):
        _re_dict = {}
        if file_name == None:
            for f in self.file_names:
                with open(f, 'r', encoding='utf-8') as file:
                    file.seek(0)
                    _re_dict[f] = self.__remove_punctuation(file.read()).split()
        else:
            with open(file_name, 'r', encoding='utf-8') as file:
                file.seek(0)
                _re_dict[file_name] = self.__remove_punctuation(file.read()).split()
        return _re_dict
        pass

    def find(self, word):
        word = word.lower()
        _re_dict = {}
        for i in self.file_names:
            _list = self.get_all_words(i)[i]
            if _list.count(word) != 0:
                _re_dict[i] = _list.index(word) + 1
            else:
                _re_dict[i] = 0
        return _re_dict

    def count(self, word):
        word = word.lower()
        _re_dict = {}
        for i in self.file_names:
            _list = self.get_all_words(i)[i]
            _re_dict[i] = _list.count(word)
        return _re_dict


finder0 = WordsFinder('test_file.txt')
print(finder0.get_all_words()) # Все слова
print(finder0.find('TEXT')) # 3 слово по счёту
print(finder0.count('teXT')) # 4 слова teXT в тексте всего
print()
finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))
print()
finder2 = WordsFinder('Rudyard Kipling - If.txt')
print(finder2.get_all_words())
print(finder2.find('if'))
print(finder2.count('if'))
print()
finder3 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder3.get_all_words())
print(finder3.find('captain'))
print(finder3.count('captain'))
print()
finder4 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt', 'Rudyard Kipling - If.txt')
print(finder4.get_all_words())
print(finder4.find('my'))
print(finder4.count('my'))
