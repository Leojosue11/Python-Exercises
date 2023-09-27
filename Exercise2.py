with open("story.txt", "r") as f:
    story = f.read()

#Declare a set because we need unique values 
words = set()
start_of_word = -1

tarjet_start = "<"
tarjet_end = ">"

for i, char in enumerate(story):
    
    #Look for the character "<" and save his index and active flag
    if char == tarjet_start:
        start_of_word = i
    #Look for the character ">" and save his index return flag to initial value (-1)
    if char == tarjet_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

answers = {}

#Loop the set words and save the inputs in a list
for word in words :
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

#rewrite the story variable with the new string 
for word in words:
    story = story.replace(word,answers[word])
    
print(story)
