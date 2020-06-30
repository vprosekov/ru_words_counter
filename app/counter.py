import matplotlib.pyplot as plt
def count_letters_RU(text):
    letter_counts = {}
    alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'Ё', 'ё']
    for letter in alphabet:
        letter_count = text.count(letter)
        if letter_count != 0:
            letter_counts[letter] = letter_count
    return letter_counts

def make_letters_hist(letter_counts, path):
    plot_x = list(letter_counts.keys())
    plt.figure(figsize=(13, 3))
    plt.bar(plot_x, letter_counts.values(), align='edge', width=0.3)
    plt.grid()
    plt.savefig(path)