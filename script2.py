import time
print('You are a secret agent who have just boarded the warship of your enemy.')
time.sleep(0.1)
print('There are 25 rooms on this warship, with one room containing the engine,')
time.sleep(0.1)
print('and another containing a fuel tank.')
time.sleep(0.1)
print('Your mission is to destroy the engine room and the fuel room with your 10 micebot.')
time.sleep(0.1)
print('A mousebot can be an explorer mouse or a bomb mouse. ')
time.sleep(0.1)
print('An explorer mouse can explore a room and search for clues,')
time.sleep(0.1)
print('while a bomb mouse can destroy a room.')
time.sleep(0.1)
print('Every mousebot destruct itself after exploring or destroying a room.')
time.sleep(0.1)
input('Press Enter to start your mission. Good Luck!')
import random
import os
fuel = [True,[0,0]]
engine = [True,[0,0]]
while fuel[1] == engine[1]:
    fuel[1] = [random.randint(1,5), random.randint(1,5)]
    engine[1] = [random.randint(1,5), random.randint(1,5)]
rooms_pos = []
for y in range(1,6):
    for x in range(1,6):
        rooms_pos.append([x,y])
rooms_names = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']
clues = []
clue = ''
command = ''
position = ''
pos_x = 0
pos_y = 0
command_list = []
something = []
num_mouse = 10
def read(command,command_list):
    command = str(command).lower()
    command_list = command.split()
    command = ''
    for x in command_list:
        command = command + x
    return command
def mastermind(pos_x):
    print('Mousebot Report: reached the target room.')
    command_list = [2 * x + pos_x for x in range(0,4)]
    print('Mousebot Reported: need a three-digit password to enter the room.')
    time.sleep(0.2)
    print('Mousebot trying to crack the password.')
    time.sleep(0.8)
    print('Mousebot Report: failed to crack the password,')
    time.sleep(0.1)
    if pos_x == 0:
        print('                   but found that the password consists of three non-repeating even numbers.')
    elif pos_x == 1:
        print('                   but found that the password consists of three non-repeating odd numbers.')
    time.sleep(0.2)
    print('Now you have 4 chances to test and find out the password.')
    time.sleep(0.5)
    Bomb_finished = False
    while not Bomb_finished:
        import random
        random.shuffle(command_list)
        B = command_list[:3]
        for turn in range(4):
            turn += 1
            pos_x = 0
            pos_y = ''
            while not (
                    pos_y.isdecimal()):
                pos_y = input('Please try a non-repeating three-digit number:')
            pos_y = int(pos_y)
            something = [int(x) for x in str(pos_y)]
            while len(something) < 3:
                something.insert(0,0)
            for x in range(0,3):
                for y in range(0,3):
                    if x == y and command_list[x] == something[y]:
                        pos_x += 10
                    elif command_list[x] == something[y]:
                        pos_x += 1
            print(f'{pos_x // 10} correct digit in the correct position,{(pos_x % 10)} correct digit in the wrong position.')
            time.sleep(0.2)
            print(f'You have {4 - turn} chances to test the password.')
            time.sleep(0.5)
        print('Now you have no more testing chances and have to decide a final password.')
        time.sleep(0.2)
        pos_y = int(input('What is your final password?'))
        if pos_y == B[0] * 100 + B[1] * 10 + B[2]:
            Bomb_finished = True
            print('Mousebot Report: password correct.')
        else:
            Bomb_finished = False
            print('Mousebot Report: password incorrect.')
        input('Press enter to start the next step.')
        return Bomb_finished
readable_commands = ['sendexplorer','sendbomb','readinformation']
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def put_map():
    for n in range(0,5):
        print(rooms_names[5 * n:5 * n + 5])
        time.sleep(0.05)
    print(f'You now have {num_mouse} micebot.')
while (fuel[0] or engine[0]) and num_mouse > 0:
    clear_screen()
    put_map()
    while position == '':
        while not command in readable_commands:
            command = ''
            command_list = []
            command = str(input('What are you going to do?(send explorer/send bomb/read information)'))
            command = read(command,command_list)
        command_list = []
        if command == 'readinformation':
            command = ''
            if len(clues) == 0:
                print('You have not got any information yet.')
                time.sleep(0.5)
            else:
                for clue in clues:
                    print(clue)
                    time.sleep(0.5)
            input('Press enter to close the information page.')
            clear_screen()
            put_map()
        elif command == 'sendbomb':
            print('Choose a target.')
            while pos_y <= 0 or pos_y >= 6:
                time.sleep(0.2)
                pos_y = int(input('Mousebot Report: target row required.(1~5)'))
                time.sleep(0.2)
                if pos_y <= 0 or pos_y >= 6:
                    print('Mousebot Report: invalid row.')
            while pos_x <= 0 or pos_x >= 6:
                time.sleep(0.2)
                pos_x = int(input('Mousebot Report: target column required.(1~5)'))
                time.sleep(0.2)
                if pos_x <= 0 or pos_x >= 6:
                    print('Mousebot Report: invalid column.')
            position = str(pos_y * 5 + pos_x - 5)
            time.sleep(0.2)
            if rooms_pos[int(position)-1] == fuel[1]:
                print('Mousebot Report: fuel tank destroyed successfully.')
                fuel[0] = False
                clue = f'Fuel tank found in row {pos_y}, column {pos_x}. Already destroyed.'
            elif rooms_pos[int(position)-1] == engine[1]:
                print('Mousebot Report: engine destroyed successfully.')
                engine[0] = False
                clue = f'Engine found in row {pos_y}, column {pos_x}. Already destroyed.'
            else:
                print('Mousebot Report: an empty room destoryed successfully.')
                clue = f'Nothing found in row {pos_y}, column {pos_x}.'
            rooms_names[int(position) - 1] = 'HH'
            command = ''
        elif command == 'sendexplorer':
            while not position in rooms_names:
                position = str(input('Choose a room to explore:'))
                if position == '  ':
                    time.sleep(0.2)
                    print('This room has already been explored.')
                    position = ''
                elif position == 'HH':
                    time.sleep(0.2)
                    print('It is too dangerous to explore a destroyed room.')
                    position = ''
            pos_x = random.randint(0,1)
            clear_screen()
            time.sleep(0.2)
            Bomb_finished = mastermind(pos_x)
            clear_screen()
            if Bomb_finished:
                print('Mousebot Report: now available to scan the row or column of the room.')
                time.sleep(0.5)
                while command != 'row' and command != 'column':
                    command = str(input('Which to scan, the row or the column?(row/column)'))
                    command = read(command,command_list)
                clue = ''
                if command == 'column':
                    if rooms_pos[int(position) - 1][0] == fuel[1][0]:
                        clue += f'Fuel Tank in column {rooms_pos[int(position) - 1][0]}.       '
                        print('Scan complete(1/2):Fuel Tank in this column.')
                    else:
                        clue += f'Fuel Tank not in column {rooms_pos[int(position) - 1][0]}.   '
                        print('Scan complete(1/2):Fuel Tank not in this column.')
                    time.sleep(0.5)
                    if rooms_pos[int(position) - 1][0] == engine[1][0]:
                        clue += f'Engine in column {rooms_pos[int(position) - 1][0]}.'
                        print('Scan complete(2/2):Engine in this column.')
                    else:
                        clue += f'Engine not in column {rooms_pos[int(position) - 1][0]}.'
                        print('Scan complete(2/2):Engine not in this column.')
                else:
                    if rooms_pos[int(position) - 1][1] == fuel[1][1]:
                        clue += f'Fuel Tank in row {rooms_pos[int(position) - 1][1]}.          '
                        print('Scan complete(1/2):Fuel Tank in this row.')
                    else:
                        clue += f'Fuel Tank not in row {rooms_pos[int(position) - 1][1]}.      '
                        print('Scan complete(1/2):Fuel Tank not in this row.')
                    time.sleep(0.5)
                    if rooms_pos[int(position) - 1][1] == engine[1][1]:
                        clue += f'Engine in row {rooms_pos[int(position) - 1][1]}.'
                        print('Scan complete(2/2):Engine in this row.')
                    else:
                        clue += f'Engine not in row {rooms_pos[int(position) - 1][1]}.'
                        print('Scan complete(2/2):Engine not in this row.')
            else:
                time.sleep(0.2)
                print('Mousebot Report: failed to enter the room. Scanning function unavailable.')
                time.sleep(0.2)
                print('Mousebot now trying to analyze the odors here before self-destruction.')
                command = random.choice(['row','column'])
                if command == 'column':
                    time.sleep(0.5)
                    if rooms_pos[int(position) - 1][0] == fuel[1][0] or rooms_pos[int(position) - 1][0] == engine[1][0]:
                        print('Mousebot Report: mousebot smelled a special odor in this column.')
                        clue = f'Something special found in column {rooms_pos[int(position) - 1][0]}.'
                    else:
                        print('Mousebot Report: mousebot find nothing special in this column.')
                        clue = f'Nothing special found in column {rooms_pos[int(position) - 1][0]}.'
                elif command == 'row':
                    if rooms_pos[int(position) - 1][1] == fuel[1][1] or rooms_pos[int(position) - 1][1] == engine[1][1]:
                        print('Mousebot Report: mousebot smelled a special odor in this row.')
                        clue = f'Something special found in row {rooms_pos[int(position) - 1][1]}.'
                    else:
                        print('Mousebot Report: mousebot find nothing special in this row.')
                        clue = f'Nothing special found in row {rooms_pos[int(position) - 1][1]}.'
            rooms_names[int(position) - 1] = '  '
    time.sleep(0.2)
    print('Mousebot Reported: Self-destruction complete.')
    time.sleep(0.5)
    input('Press Enter to end this turn.')
    clues.append(clue)
    clue = ''
    position = ''
    num_mouse -= 1
    pos_y = 0
    pos_x = 0
clear_screen()
if fuel[0] or engine[0]:
    print('You now have no more mousebot but your target has not been reached.')
    time.sleep(0.2)
    print('You failed to complete your mission.')
else:
    print('You successfully destroyed both the fuel tank and the engine!')
    time.sleep(0.2)
    print('The warship has now started to sink.')
    time.sleep(0.2)
    print('You can now get on the lifeboat and leave your enemy behind.')
    time.sleep(0.2)
    print('A helicopter will soon come and pick you up.')
    time.sleep(0.2)
    print('        * * [ MISSION COMPLETE ] * *')