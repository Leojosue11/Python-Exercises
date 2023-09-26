with open("story.txt", "r") as f:
    story = f.read()
    print(enumerate(story))
    
words = []
start_of_word = -1

tarjet_start = "<"
tarjet_end = ">"

for i, char in enumerate(story):
    if char == tarjet_start:
        start_of_word = i
    
    if char == tarjet_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.append(word)
        start_of_word = -1

print(words)
