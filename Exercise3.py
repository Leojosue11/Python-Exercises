import random
import time

LIST_OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 2
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10


def generate_problems():
    left_number = random.randint(MIN_OPERAND,MAX_OPERAND)
    right_number = random.randint(MIN_OPERAND,MAX_OPERAND)
    operator = random.choice(LIST_OPERATORS)
    
    problem = str(left_number) + " " + operator + " "+str(right_number)
    answer = eval(problem)
    return problem, answer

wrong = 0
input("Press ENTER to start: ")
print("------------------------")
start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    problem, answer = generate_problems()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + problem + " = ")
        if int(guess) == answer :
            break
        wrong += 1
        
end_time = time.time() 
total_time = end_time - start_time     
print("------------------------------") 
print("Nice work! you end in", round(total_time,2), "seconds")  
print("You fail:", wrong, "times")    
    