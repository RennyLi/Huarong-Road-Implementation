import random
from random import shuffle  # import random and shuffle to randomize the puzzle

puzzle_list_nine=[1,2,3,4,5,6,7,8," "]
puzzle_list_sixteen=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15," "]  # first set a standard solvable puzzle

def puzzle_solvable_nine():  # define a function to show the solvable randomized puzzle
    inversion_number_nine=0  # use inversion number to know whether the puzzle is solvable
    while True:  
        random.shuffle(puzzle_list_nine)  # use random.shuffle to randomize the standard puzzle
        copy=puzzle_list_nine.copy()  # copy the puzzle and use the copy to test whether it's solvable
        copy.remove(" ")  # empty space doesn't involve in the test of solvability
        for t in copy:
            for s in copy[copy.index(t)+1:]:
                if t > s:
                    inversion_number_nine+=1 
        if inversion_number_nine%2 == 0:  # if the inversion number can be divided by 2, the puzzle is solvable
            break  
        else:
            inversion_number_nine=0  

    for i in puzzle_list_nine:
        print(i,end = '\t')  
        if (puzzle_list_nine.index(i)+1)%3 == 0:
            print()  

def puzzle_solvable_sixteen():  # define a function to show the solvable randomized puzzle
    inversion_number_sixteen=0  # use inversion number to know whether the puzzle is solvable
    while True:  
        random.shuffle(puzzle_list_sixteen)  # use random.shuffle to randomize the standard puzzle
        copy=puzzle_list_sixteen.copy()  # copy the puzzle and use the copy to test whether it's solvable
        copy.remove(" ")  # empty space doesn't involve in the test of solvability
        for t in copy:
            for s in copy[copy.index(t)+1:]:
                if t > s:
                    inversion_number_sixteen+=1 

        if inversion_number_sixteen%2 == 0 and puzzle_list_sixteen.index(" ") in [4,5,6,7,12,13,14,15]:
            break  # if inversion number is even & final space is even line away from initial space, then solvable
        elif inversion_number_sixteen%2 != 0 and puzzle_list_sixteen.index(" ") in [0,1,2,3,8,9,10,11]:
            break  # if inversion number is odd & final space is odd line away from initial space, then solvable
        else:
            inversion_number_sixteen=0  # otherwise, we should continue randomizing until solvable

    for i in puzzle_list_sixteen:
            print(i,end = '\t')  
            if (puzzle_list_sixteen.index(i)+1)%4 == 0:
                print()  

def check_choose_direction(p_direction):  # define a function to let user input 4 letters as directions
    if len(p_direction) != 7: 
        return False
    elif len(p_direction) == 7:
        left,right,up,down=p_direction.split(" ")  # assign the letters to corresponding variables
        for m in [left,right,up,down]: 
            if m.isalpha() is False:  # to ensure the input letters are ASCII letters
                return False
            elif m.isalpha() is True:
                direction_list=[str(left),str(right),str(up),str(down)]
                for i in direction_list:
                    for t in direction_list[0:direction_list.index(i)]:
                        if i == t:
                            return False
                        else:
                            return True

def choose_puzzle_nine_direction_and_move(p_direction):  # show the valid sliding moves together with the disignated letter
    left,right,up,down=p_direction.split(" ")  # this function is used for 8-tile puzzles
    if puzzle_list_nine.index(" ") == 0:
        p_nine_direction=input(f"Enter your move from (left-{left} up-{up}):")
    elif puzzle_list_nine.index(" ") == 1:
        p_nine_direction=input(f"Enter your move from (left-{left} right-{right} up-{up}):")
    elif puzzle_list_nine.index(" ") == 2:
        p_nine_direction=input(f"Enter your move from (right-{right} up-{up}):")
    elif puzzle_list_nine.index(" ") == 3:
        p_nine_direction=input(f"Enter your move from (left-{left} up-{up} down-{down}):")
    elif puzzle_list_nine.index(" ") == 4:
        p_nine_direction=input(f"Enter your move from (left-{left} right-{right} up-{up} down-{down}):")
    elif puzzle_list_nine.index(" ") == 5:
        p_nine_direction=input(f"Enter your move from (right-{right} up-{up} down-{down}):")
    elif puzzle_list_nine.index(" ") == 6:
        p_nine_direction=input(f"Enter your move from (left-{left} down-{down}):")
    elif puzzle_list_nine.index(" ") == 7:
        p_nine_direction=input(f"Enter your move from (left-{left} right-{right} down-{down}):")
    else:
        p_nine_direction=input(f"Enter your move from (right-{right} down-{down}):")

    if p_nine_direction == up:  # move the sliding blocks according to user's instructions
        i=puzzle_list_nine.index(" ")
        if i in [6,7,8]:
            print("Wrong move!")
        else:
            puzzle_list_nine[i],puzzle_list_nine[i+3]=puzzle_list_nine[i+3],puzzle_list_nine[i]
    elif p_nine_direction == down:
        i=puzzle_list_nine.index(" ")
        if i in [0,1,2]:
            print("Wrong move!")
        else:
            puzzle_list_nine[i],puzzle_list_nine[i-3]=puzzle_list_nine[i-3],puzzle_list_nine[i]
    elif p_nine_direction == left:
        i=puzzle_list_nine.index(" ")
        if i in [2,5,8]:
            print("Wrong move!")
        else:
            puzzle_list_nine[i],puzzle_list_nine[i+1]=puzzle_list_nine[i+1],puzzle_list_nine[i]
    elif p_nine_direction == right:
        i=puzzle_list_nine.index(" ")
        if i in [0,3,6]:
            print("Wrong move!")
        else:
            puzzle_list_nine[i],puzzle_list_nine[i-1]=puzzle_list_nine[i-1],puzzle_list_nine[i]

    for i in puzzle_list_nine:  # show the updated puzzle on the screen after each move
        print(i,end = '\t')
        if (puzzle_list_nine.index(i)+1)%3 == 0:
            print()
   
def choose_puzzle_sixteen_direction_and_move(p_direction):  # show the valid sliding moves together with the disignated letter
    left,right,up,down=p_direction.split(" ") # this function is used for 15-tile puzzles
    if puzzle_list_sixteen.index(" ") == 0:
        p_sixteen_direction=input(f"Enter your move from (left-{left} up-{up}):")
    elif puzzle_list_sixteen.index(" ") in [1,2]:
        p_sixteen_direction=input(f"Enter your move from (left-{left} right-{right} up-{up}):")
    elif puzzle_list_sixteen.index(" ") == 3:
        p_sixteen_direction=input(f"Enter your move from (right-{right} up{up}):")
    elif puzzle_list_sixteen.index(" ") in [4,8]:
        p_sixteen_direction=input(f"Enter your move from (left-{left} up-{up} down-{down}):")
    elif puzzle_list_sixteen.index(" ") in [5,6,9,10]:
        p_sixteen_direction=input(f"Enter your move from (left-{left} right-{right} up-{up} down-{down}):")
    elif puzzle_list_sixteen.index(" ") in [7,11]:
        p_sixteen_direction=input(f"Enter your move from (right-{right} up-{up} down-{down}):")
    elif puzzle_list_sixteen.index(" ") == 12:
        p_sixteen_direction=input(f"Enter your move from (left-{left} down-{down}):")
    elif puzzle_list_sixteen.index(" ") in [13,14]:
        p_sixteen_direction=input(f"Enter your move from (left-{left} right-{right} down-{down}):")
    else:
        p_sixteen_direction=input(f"Enter your move from (right-{right} down-{down}):")

    if p_sixteen_direction == up:  # move the sliding blocks according to user's instructions
        i=puzzle_list_sixteen.index(" ")
        if i in [12,13,14,15]:
            print("Wrong move!")
        else:
            puzzle_list_sixteen[i],puzzle_list_sixteen[i+4]=puzzle_list_sixteen[i+4],puzzle_list_sixteen[i]
    elif p_sixteen_direction == down:
        i=puzzle_list_sixteen.index(" ")
        if i in [0,1,2,3]:
            print("Wrong move!")
        else:
            puzzle_list_sixteen[i],puzzle_list_sixteen[i-4]=puzzle_list_sixteen[i-4],puzzle_list_sixteen[i]
    elif p_sixteen_direction == left:
        i=puzzle_list_sixteen.index(" ")
        if i in [3,7,11,15]:
            print("Wrong move!")
        else:
            puzzle_list_sixteen[i],puzzle_list_sixteen[i+1]=puzzle_list_sixteen[i+1],puzzle_list_sixteen[i]
    elif p_sixteen_direction == right:
        i=puzzle_list_sixteen.index(" ")
        if i in [0,4,8,12]:
            print("Wrong move!")
        else:
            puzzle_list_sixteen[i],puzzle_list_sixteen[i-1]=puzzle_list_sixteen[i-1],puzzle_list_sixteen[i]
    
    for i in puzzle_list_sixteen:  # show the updated puzzle on the screen after each move
            print(i,end = '\t')
            if (puzzle_list_sixteen.index(i)+1)%4 == 0:
                print()

def check_result_nine():  # check whether the 8-tile puzzle is solved
    if puzzle_list_nine == [1,2,3,4,5,6,7,8," "]:
        return True
    else:
        return False

def check_result_sixteen():  # check whether the 15-tile puzzle is solved
    if puzzle_list_sixteen == [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15," "]:
        return True
    else:
        return False

def main(): 
    while True:  
        print("Welcome to Renny's sliding puzzle program!")  # display a brief intriduction about the game at the start of the game
        print("You will move the tiles with the keyboard with any four letters")
        print("of your own choice for left, right, up and down movements respectively.")  # prompt the user to enter four letters for four direction moves

        while True:
            p_direction=input("Please enter the corresponding four different letters separated by a space:") 
            if check_choose_direction(p_direction):
                break
            else:
                continue

        print("You will choose either the 8 or 15-puzzle to play with.")  # prompt user for selection of either 8 or 15 puzzle
        your_instruction=input("Enter 1 for 8-puzzle, 2 for 15-puzzle or q to end the game:")
        count=0  # track total number of moves

        if your_instruction == "1":  
            puzzle_solvable_nine()  # generate a randomized, solvable 8-tile puzzle accordingly
            while True: 
                choose_puzzle_nine_direction_and_move(p_direction)  # move the sliding blocks
                count+=1  
                if check_result_nine():  # inform the user when the puzzle is solved
                    print("Congratulations!")
                    print("Your move:",count)  #display the total number of moves
                    break  
        elif your_instruction == "2": 
            puzzle_solvable_sixteen()  # generate a randomized, solvable 15-tile puzzle accordingly
            while True: 
                choose_puzzle_sixteen_direction_and_move(p_direction)  # move the sliding puzzle
                count+=1 
                if check_result_sixteen():  # inform the user when the puzzle is solved
                    print("Congratulations!")
                    print("Your move:",count)  # display the total number of moves
                    break  
        elif your_instruction == "q": 
            print("Thanks for playing the game!")
            print("Your move:",count) 
            break
        
        end_instruction=input("Enter 3 to continue another game, 4 to end the game:")  
        if end_instruction == 3:  
            continue  
        elif end_instruction == 4: 
            print("Thanks for playing the game!")
            break  
        break
main()  