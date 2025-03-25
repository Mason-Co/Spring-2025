# Programmer: Mason Colacicco
# Date: March
# Program: Word Frequency

def main():
    num_words = {}

    file = open('text.txt', 'r')
    infile = file.readlines()
    words = [word.lower().strip(".").strip(",").strip("!").strip("?") for line in infile for word in line.strip().split()]

    for word in words:
        if word in num_words:
            num_words[word] += 1
        else:
            num_words[word] = 1

    for word in num_words:
        print(f"{word} : {num_words[word]}")

if __name__ == '__main__':
    main()