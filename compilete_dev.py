import os

os.system("git add -A")
name = input("Name: ")
os.system(f'git commit -m "{name}"')
os.system("git push")