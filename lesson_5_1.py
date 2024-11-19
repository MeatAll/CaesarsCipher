
def find_sentences(str_text: str):
    list_sentences = []
    while str_text.__contains__('.'):
        sentence = str_text[0:str_text.index('.') + 1]
        list_sentences.append(sentence)
        str_text = str_text[str_text.index('.') + 1: len(str_text)]
        #print(len(list_sentences))
        #print(sentence)
    if len(str_text) != 0:
        list_sentences.append(str_text)
        #print(str_text)
    return list_sentences

def find_words():
    vat_text = str(input('Введите текст:\n'))
    var_target_word = str(input('Введите искомое слово:\n'))
    sentences_list = find_sentences(vat_text)
    int_num = 1
    for sentence in sentences_list:
        if sentence.lower().__contains__(var_target_word.lower()):
            print('Номер предложения: ' + int_num.__str__())
            print(sentence)
        int_num = int_num + 1

find_words()


