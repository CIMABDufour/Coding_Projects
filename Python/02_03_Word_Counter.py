# Medium Difficulty Project
# Word Counter
# Count instances of words within a text file


def count_dict(words) :
    new_word_list = []
    char_list = ['!', ',', '.', ':', ';', '?']
    for word in words :
        if word not in char_list :
            lower_word = word.lower()
            new_word_list.append(lower_word)
    word_dict = {i : new_word_list.count(i) for i in new_word_list}
    return word_dict


path = 'C:\\Users\\BenBi\\OneDrive\\Desktop\\'
file_name = 'words.txt'
full_path = path + file_name

read_file = open(full_path, 'r')

word_list = []

for line in read_file.readlines() :
    if line.strip() :
        for n in line.split(' '):
            word_list.append(n)
count_words = count_dict(word_list)

print(count_words)
