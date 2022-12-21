import os

def getToday():
    year = input("What year: ")
    day = input("What day: ")
    token = input("What is the name of the file holding your session token: ")
    f = open(token,"r")
    cookie  = f.readline()
    dest = input("What is the destiniation file name: ")
    file = open(dest, "w")

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    print(url)
    input()
    os.system(f'curl -o input.txt "{url}" --cookie {cookie}')

getToday()
