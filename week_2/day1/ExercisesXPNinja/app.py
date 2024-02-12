# Exc. 1
"""PATH - one of the environmental variables available in *nix systems.
It stores pathways to important *nix executables, allowing us to NOT specify 
the full path of a certain command / script when we want to run it in the terminal.
Eg, we can type pwd <cmd> instead of looking first where this executable is stored (which pwd) and running it with the full path (eg as /bin/pwd).
To add a command / executable to the PATH: export PATH="/path-to-executable/executable:$PATH". 
This will live for the entire shell lifecycle (when we close the shell, the PATH reverts to its previous state).
To save changes permanently use configuration files on *nix systems (such as .bashrc in Linux).
"""

# Exc. 2
"""Alias creation in *nix system:
alias custom_name='cmd(s) we want to shortcut'.
Eg, alias py='python3'.
To make alias persist - add it to 1 of the *nix config files (/.bashrc VS /.zshrc)
vim ~/.bashrc
alias py='python3'
"""

# Exc. 3
3 <= 3 < 9  # True
3 == 3 == 3  # True
bool(0)  # False
bool(5 == "5")  # False
bool(4 == 4) == bool("4" == "4")  # True
bool(bool(None))  # False

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)  # True
print("y is", y)  # False
print("a:", a)  # 5
print("b:", b)  # 10


# Exc. 4
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print(len(my_text)) # 445

# if we used the multiline string, the length of the string would include hidden characters such as \n, spaces etc.

my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
           Ut enim ad minim veniam, quis nostrud exercitation ullamco 
           laboris nisi ut aliquip ex ea commodo consequat. 
           Duis aute irure dolor in reprehenderit in voluptate velit 
           esse cillum dolore eu fugiat nulla pariatur. 
           Excepteur sint occaecat cupidatat non proident, 
           sunt in culpa qui officia deserunt mollit anim id est laborum."""
print(len(my_text)) # 529


# Exc. 5
longest_msg = 0

while True: 
    msg = input("Enter the longest sentence you can w/o using the character A: ")

    if 'A' in msg:
        print("Sorry, ou lost.")
        break

    if len(msg) > longest_msg:
        longest_msg = len(msg)
        print(f"Amazing! Your longest sentence w/o A is {longest_msg} cahracters long!")
