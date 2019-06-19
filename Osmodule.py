import os
import stat
# print(os.access("main.py", os.R_OK))

# print(os.getcwd())

# print(os.chdir("../../Desktop"))
# print(os.getcwd())

os.chmod("lambda.py",stat.S_IRWXO)
