import sys

def ask_user_for_idea(ideas,filename):
    while True:
        try:
            idea = input("What is your new idea?:")
        except KeyboardInterrupt:
            break

        ideas.append(idea)
        display_ideas(ideas)
        save_ideas_to_file(filename, ideas)

def display_ideas(ideas):
    for index,idea in enumerate(ideas):
        print("{}. {}".format(index+1,idea))

def load_ideas_from_file(filename):
    ideas = []
    with open(filename, "r") as file:
        for line in file:
            ideas.append(line.strip())
    return ideas

def save_ideas_to_file(filename, ideas):
    with open(filename, "w") as file:
        for idea in ideas:
            file.write(f"{idea}\n")


def main():

    filename = "ideabank.txt"
    ideas = load_ideas_from_file(filename)

    if(len(sys.argv)) > 1 and sys.argv[1] == "--list":
        display_ideas(ideas)
    elif(len(sys.argv) > 2 and sys.argv[1] == "--delete"):

        index_to_delete = int(sys.argv[2])
        try:
            if index_to_delete < 1:
                raise IndexError
            print(ideas[index_to_delete - 1])
            ideas.remove(ideas[index_to_delete - 1])
            save_ideas_to_file(filename, ideas)
        except IndexError:
            print("Wrong index!")

    else:
        ask_user_for_idea(ideas,filename)

if __name__ == "__main__":
    main()