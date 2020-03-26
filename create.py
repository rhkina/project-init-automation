import sys
import os
import gitlab
from dotenv import load_dotenv

load_dotenv()

PATH = os.getenv("FILEPATH")
TOKEN = os.getenv("TOKEN")

def create():
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))
    try:
        projectName = str(sys.argv[1])
    except:
        print ("Your project name is missing!")
        print ("Please enter the command: create <project_name>")
        return
#    os.makedirs(PATH + folderName)
#    gl = gitlab.Gitlab('https://gitlab.com/rhkina', private_token=TOKEN)
#    repo = g1.create_repo(projectName)
    print("Succesfully created repository {}".format(projectName))

if __name__ == "__main__":
    create()
