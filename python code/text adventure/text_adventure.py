import os
import time

def picture_show(pic_raw):
    pic = pic_raw+".jpg"
    os.startfile("C:\\Users\\manji\\Downloads\\python code\\text adventure\\pictures\\"+pic)

def logo_print_fuction():
    for line in lines:
        time.sleep(0.1)
        print(line)



logo = """
                                       AAA                  GGGGGGGGGGGGG     OOOOOOOOO     NNNNNNNN        NNNNNNNN
                                      A:::A              GGG::::::::::::G   OO:::::::::OO   N:::::::N       N::::::N
                                     A:::::A           GG:::::::::::::::G OO:::::::::::::OO N::::::::N      N::::::N
                                    A:::::::A         G:::::GGGGGGGG::::GO:::::::OOO:::::::ON:::::::::N     N::::::N
                                   A:::::::::A       G:::::G       GGGGGGO::::::O   O::::::ON::::::::::N    N::::::N
                                  A:::::A:::::A     G:::::G              O:::::O     O:::::ON:::::::::::N   N::::::N
                                 A:::::A A:::::A    G:::::G              O:::::O     O:::::ON:::::::N::::N  N::::::N
                                A:::::A   A:::::A   G:::::G    GGGGGGGGGGO:::::O     O:::::ON::::::N N::::N N::::::N
                               A:::::A     A:::::A  G:::::G    G::::::::GO:::::O     O:::::ON::::::N  N::::N:::::::N
                              A:::::AAAAAAAAA:::::A G:::::G    GGGGG::::GO:::::O     O:::::ON::::::N   N:::::::::::N
                             A:::::::::::::::::::::AG:::::G        G::::GO:::::O     O:::::ON::::::N    N::::::::::N
                            A:::::AAAAAAAAAAAAA:::::AG:::::G       G::::GO::::::O   O::::::ON::::::N     N:::::::::N
                           A:::::A             A:::::AG:::::GGGGGGGG::::GO:::::::OOO:::::::ON::::::N      N::::::::N
                          A:::::A               A:::::AGG:::::::::::::::G OO:::::::::::::OO N::::::N       N:::::::N
                         A:::::A                 A:::::A GGG::::::GGG:::G   OO:::::::::OO   N::::::N        N::::::N
                        AAAAAAA                   AAAAAAA   GGGGGG   GGGG     OOOOOOOOO     NNNNNNNN         NNNNNNN
                        

███████  ██████ ██ ███████ ███    ██ ████████ ██ ███████ ██  ██████     ██████  ██████  ███████  █████  ██   ██ ████████ ██   ██ ██████   ██████  ██    ██  ██████  ██   ██ 
██      ██      ██ ██      ████   ██    ██    ██ ██      ██ ██          ██   ██ ██   ██ ██      ██   ██ ██  ██     ██    ██   ██ ██   ██ ██    ██ ██    ██ ██       ██   ██ 
███████ ██      ██ █████   ██ ██  ██    ██    ██ █████   ██ ██          ██████  ██████  █████   ███████ █████      ██    ███████ ██████  ██    ██ ██    ██ ██   ███ ███████ 
     ██ ██      ██ ██      ██  ██ ██    ██    ██ ██      ██ ██          ██   ██ ██   ██ ██      ██   ██ ██  ██     ██    ██   ██ ██   ██ ██    ██ ██    ██ ██    ██ ██   ██ 
███████  ██████ ██ ███████ ██   ████    ██    ██ ██      ██  ██████     ██████  ██   ██ ███████ ██   ██ ██   ██    ██    ██   ██ ██   ██  ██████   ██████   ██████  ██   ██ 
                                                                                                                                                                            
                                                                                                                                                                            
"""
lines = logo.split('\n')

time.sleep(2)
logo_print_fuction()

def choice_1():
    print("You chose option 1.")

def choice_2():
    print("You chose option 2.")

def choice_3():
    print("You chose option 3.")

# Main game loop
while True:
    user_input = input("Enter your choice (1, 2, 3): ")

    choices = {
        '1': choice_1,
        '2': choice_2,
        '3': choice_3,
    }

    if user_input in choices:
        choices[user_input]()
    else:
        print("Invalid choice. Try again.")
