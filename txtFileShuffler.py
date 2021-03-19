import random

def shuffle():
    lines = open('links.txt').readlines()
    random.shuffle(lines)
    open('links.txt','w').writelines(lines)


