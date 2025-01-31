from question_class import question
import random


def main():
    print("Welcome to the Lord of the Rings Knowledge Challenge!!!")
    print("")
    print("Based off of the books let's see how much you know.")
    print("")
    print("Mára Valto")
    print("")
    while True:
        mode = input(" Choose your difficulty Easy, Medium, or Hard (E, M, H): ").lower()
        if mode == "e":
            questions_and_answers = easy(questions)
            break
        elif mode == "m":
            questions_and_answers = medium(medium_questions)
            break
        elif mode == "h":
            questions_and_answers = hard(hard_questions)
            break
        else:
            print("Invalid input. Please choose E, M, or H.")


    while True:
        see_answers = input("Would you like to see the correct answers? (y/n): ").lower()
        if see_answers == "y":
            print_questions_and_answers(questions_and_answers)
            break
        elif see_answers == "n":
            break
        else:
            print("Invalid input. Please enter y or n.")


    while True:
        play_again = input("Would you like to play again? (y/n): ").lower()
        if play_again == "y":
            main()
        elif play_again == "n":
            print("Have a great day!")
            break
        else:
            print("Invalid input. Please enter y or n.")


# gets easy questions
def easy(questions):
    score = 0
    num_questions_to_ask = 10  # Set the number of questions to ask
    random.shuffle(questions)  # Shuffle the questions list randomly
    questions_and_answers = []  # List to store questions and correct answers
    for i, question in enumerate(questions[:num_questions_to_ask], 1):
        answer = input(f"Question {i}: {question.prompt}")
        if answer.lower() == question.answer.lower():  # Convert both answers to lowercase for case-insensitive comparison
            score += 1
        questions_and_answers.append((question.prompt, question.answer))  # Add question and correct answer to the list
    print(f"You got {score}/{num_questions_to_ask} Correct")
    return questions_and_answers

# gets medium questions
def medium(medium_questions):
    score = 0
    num_questions_to_ask = 10  # Set the number of questions to ask
    random.shuffle(medium_questions)  # Shuffle the questions list randomly
    questions_and_answers = []  # List to store questions and correct answers
    for i, question in enumerate(medium_questions[:num_questions_to_ask], 1):
        answer = input(f"Question {i}: {question.prompt}")
        if answer.lower() == question.answer.lower():  # Convert both answers to lowercase for case-insensitive comparison
            score += 1
        questions_and_answers.append((question.prompt, question.answer))  # Add question and correct answer to the list
    print(f"You got {score}/{num_questions_to_ask} Correct")
    return questions_and_answers

# gets hard questions
def hard(hard_questions):
    score = 0
    num_questions_to_ask = 10  # Set the number of questions to ask
    random.shuffle(hard_questions)  # Shuffle the questions list randomly
    questions_and_answers = []  # List to store questions and correct answers
    for i, question in enumerate(hard_questions[:num_questions_to_ask], 1):
        answer = input(f"Question {i}: {question.prompt}")
        if answer.lower() == question.answer.lower():  # Convert both answers to lowercase for case-insensitive comparison
            score += 1
        questions_and_answers.append((question.prompt, question.answer))  # Add question and correct answer to the list
    print(f"You got {score}/{num_questions_to_ask} Correct")
    return questions_and_answers


def print_questions_and_answers(questions_and_answers):
    # Print all questions and correct answers
    print("\nQuestions and Correct Answers:")
    for i, (prompt, answer) in enumerate(questions_and_answers, 1):
        print(f"Question {i}: {prompt}")
        print(f"Correct Answer: {answer}\n")


question_prompts = [
    "Where does Frodo live?: \n(a) Rohan\n(b) Shire\n(c) Pelinor Fields\n\n",
    "How many people are there in the fellowship?: \n(a) 7\n(b) 10\n(c) 9\n\n",
    "What is the name of the mine that the Fellowship travels through?\n(a) Moria\n(b) Argonath\n(c) Mount Doom\n\n",
    "Who is the wizard who visits the Shire?\n(a) Morgoth\n(b) Gandalf\n(c) Saurmon\n\n",
    "What is the name of the horse that accompanies the Fellwoship?\n(a) Garth\n(b) Brego\n(c) Bill\n\n",
    "Where does Elrond live?\n(a) Argonath\n(b) Rivindell \n(c) Rohan\n\n",
    "Who is Frodo's Gardener?\n(a) Samwise Gamgee\n(b) Fatty Lumpkin\n(c) Lotho Baggins\n\n",
    "How many rings of power were given to the Elves?\n(a) 5\n(b) 3\n(c) 7\n\n",
    "How many rings of power were given to the Dwarves?\n(a) 9\n(b) 7\n(c) 11\n\n",
    "How many rings of power were given to Men?\n(a) 9\n(b) 3\n(c) 10\n\n",
    "Where was Sauron's ring forged?\n(a) Khazad-Dum\n(b) Mordor\n(c) Dale\n\n",
    "What is the name of the mountain pass that the Fellowship attempts to travel through?\n(a) Caradhras\n(b) Arnor\n(c) Numenor\n\n",
    "Who is Théodred?\n(a) a Hobbit who works at the Green Dragon\n(b) First Steward of Gondor\n(c) Son of Théoden \n\n",
    "Who goes by the nickname 'Strider?\n(a) Elendil\n(b) Bormir\n(c) Aragorn\n\n",
    "Who did Frodo used to steal mushrooms from?\n(a) Farmer Eowyn\n(b) Farmer Maggot\n(c) Farmer Gaffer\n\n",
    "How many hobbits were part of the Fellowhship?\n(a) 3\n(b) 7\n(c) 4\n\n",
    "What is the name of the city Gandalf was supposed to meet Frodo?\n(a) Bree\n(b) Osgiliath\n(c) Khad\n\n",
    "Who is the king of Rohan?\n(a) Gloin\n(b) Glorfindel\n(c) Théoden\n\n",
    "Where was the Council of Elrond located?\n(a) Weathertop\n(b) Rivendell\n(c) Minis Tirith\n\n",
    "What alias did Frodo use when traveling to Bree?\n(a) Slim Shady\n(b) Mr. Proudfeet\n(c) Mr. Underhill\n\n"
]
# easy questions answer key
questions = [
    question(question_prompts[0], "b"),
    question(question_prompts[1], "c"),
    question(question_prompts[2], "a"),
    question(question_prompts[3], "b"),
    question(question_prompts[4], "c"),
    question(question_prompts[5], "b"),
    question(question_prompts[6], "a"),
    question(question_prompts[7], "b"),
    question(question_prompts[8], "b"),
    question(question_prompts[9], "a"),
    question(question_prompts[10], "b"),
    question(question_prompts[11], "a"),
    question(question_prompts[12], "c"),
    question(question_prompts[13], "c"),
    question(question_prompts[14], "b"),
    question(question_prompts[15], "c"),
    question(question_prompts[16], "a"),
    question(question_prompts[17], "c"),
    question(question_prompts[18], "b"),
    question(question_prompts[19], "c"),
]

# medium questions
medium_question_prompts = [
    "Where does Barliman Butterbur work at?\n(a) The Prancing Pony\n(b) The Green Dragon\n(c) Worm Tongue Inn\n\n",
    "Who is Théodred\n(a) Son of Eomer\n(b) Son of Théoden\n(c) Son of Theothor\n\n",
    "What is the name of the horse Gandalf rode?\n(a) Bill\n(b) Haste\n(c) Shadowfax\n\n",
    "How old was Bilbo when he left the Shire to live in Rivendell?\n(a) 45\n(b) 69\n(c) 111\n\n",
    "Which of the following is a language the Elves speak?\n(a) Quenya\n(b) Farsi\n(c) Dwarvish\n\n",
    "What's the name of the first elf that Samwise meets?\n(a) Haldir\n(b) Arwen\n(c) Gildor\n\n",
    "Which is the advisor to Théodon?\n(a) Faramir\n(b) Sarumon the Wise\n(c) Grima Wormtongue\n\n",
    "What was Minus Morgul called before being conqured?\n(a) Minas Ecthelion\n(b) Minas Cirith\n(c) Minus Ithil\n\n",
    "Who is the Lord and Lady of Lorien\n(a) Celeborn & Galadriel\n(b) Glorfindel & Iemna\n(c) Celebrimbor & Sythia\n\n",
    "What is the name of the spider that tries to kill Frodo and Sam?\n(a) Garnith\n(b) Groppy\n(c) Shelob\n\n",
    "Which is NOT a son of Elrond?\n(a) Elladan\n(b) Gil-Galad\n(c) Elrohir\n\n",
    "What is the name of the Ent that helps Merry and Pippin?\n(a) Treeman\n(b) Treebeard\n(c) Treefriend\n\n",
    "Which office did Frodo hold in Hobbiton after the demise of Mordor?\n(a) Sheriff\n(b) Mayor\n(c) King\n\n",
    "Who does Eowyn marry?\n(a) Pippin\n(b) Gimli\n(c) Faramir\n\n",
    "Who rides Oliphants?\n(a) The Orcs\n(b) The Gondorians\n(c) The Haradrim\n\n",
    "What is the name of the massive gate crasher used againts Minis Tirith\n(a) Grond\n(b) Shagrat\n(c) Pelinor\n\n",
    "How many eagles did Gandalf request pick up Frodo and Sam?\n(a) 2\n(b) 1\n(c) 3\n\n",
    "Who had the ring one ring the longest?\n(a) Gollum\n(b) Anduin\n(c) Frodo\n\n",
    "Who cut off Sauron's finger?\n(a) Elendil\n(b) Isildir\n(c) Elrond\n\n",
    "Who of the following killed a Balrog?\n(a) Glamring\n(b) Thor\n(c) Glorfindel\n\n"
]

# medium questions answer key
medium_questions = [
    question(medium_question_prompts[0], "a"),
    question(medium_question_prompts[1], "b"),
    question(medium_question_prompts[2], "c"),
    question(medium_question_prompts[3], "c"),
    question(medium_question_prompts[4], "a"), 
    question(medium_question_prompts[5], "c"),
    question(medium_question_prompts[6], "c"),
    question(medium_question_prompts[7], "c"),
    question(medium_question_prompts[8], "a"),
    question(medium_question_prompts[9], "c"),
    question(medium_question_prompts[10], "b"),
    question(medium_question_prompts[11], "b"),
    question(medium_question_prompts[12], "b"),
    question(medium_question_prompts[13], "c"),
    question(medium_question_prompts[14], "c"),
    question(medium_question_prompts[15], "a"),
    question(medium_question_prompts[16], "c"),
    question(medium_question_prompts[17], "b"),
    question(medium_question_prompts[18], "b"),
    question(medium_question_prompts[19], "c"),
]

# hard questions 
hard_question_prompts = [
    "What is Aragorn's Father's name?\n(a) Arathorn II\n(b) Aragon I\n(c) Aroniel\n\n",
    "What is the name of the Eagle King?\n(a) Thror\n(b) Thorondor\n(c) Your mom\n\n",
    "When did the Third Age begin?\n(a) 3000\n(b) 1972\n(c) 1308\n\n",
    "What is the name of the wise woman of Gondor in the houses of healing?\n(a) Freda\n(b) Ioreth\n(c) Rosemary\n\n",
    "What is the title of last chapter in Return of the King?\n(a) Home at last\n(b) The Grey Havens\n(c) The Road goes on\n\n",
    "Who plants a seedling of the White Tree in Minas Arnor?\n(a) Isildur\n(b) Aragon\n(c) Elendil\n\n",
    "What year was Frodo born?\n(a) 2968\n(b) 3021\n(c) 2554\n\n",
    "What is the name of the King of the Dead?\n(a) Argeb\n(b) Ohtar \n(c) Rioc\n\n",
    "What is a meeting of Ents called?\n(a) Entmoot\n(b) Entday\n(c) Ent-meet\n\n",
    "What is the name of the Ent that entertains Merry and Pippin during Entmoot?\n(a) High Willow\n(b) Mossytrunk\n(c) Quickbeam\n\n",
    "Who is lord of the Balrogs?\n(a) Sauron\n(b) Gothmog\n(c) Gilbatorix\n\n",
    "Who does Gorbad start a fight with in Cirith-Ungol\n(a) Lurtz\n(b) Gothmog\n(c) Shagrat\n\n",
    "What was the last remaining Balrog called?\n(a) Durin's Bane\n(b) Haradroth\n(c) Morgon\n\n",
    "What year did the Istari arrive in middle-earth?\n(a) 1972\n(b) 1000\n(c) 956\n\n",
    "Which is NOT a name of the 5 Istari?\n(a) Alatar\n(b) Radagast\n(c) Palandrone\n\n",
    "Which of the following is NOT a name that Aragon at one point goes by?\n(a) Elessar\n(b) Strider\n(c) Chosen One\n\n",
    "Who goes by the name 'Chief' in the Shire?\n(a) Old Took\n(b) Sarumon\n(c) Lotho\n\n",
    "What gift does Galadriel give Samwise when he leaves Lorien?\n(a) A dagger\n(b) A cooking pot\n(c) A pot of dirt\n\n",
    "Who was the first person that Smeagol killed?\n(a) Heagol\n(b) Fatty\n(c) Deagol\n\n",
    "Which of the following does Legolas take to the Grey Havens?\n(a) Gimli\n(b) Gandalf\n(c) Frodo\n\n"
]

# hard questions answer key
hard_questions = [
    question(hard_question_prompts[0], "a"),
    question(hard_question_prompts[1], "b"),
    question(hard_question_prompts[2], "c"),
    question(hard_question_prompts[3], "b"),
    question(hard_question_prompts[4], "b"),
    question(hard_question_prompts[5], "a"),
    question(hard_question_prompts[6], "a"),
    question(hard_question_prompts[7], "c"),
    question(hard_question_prompts[8], "a"),
    question(hard_question_prompts[9], "c"),
    question(hard_question_prompts[10], "b"),
    question(hard_question_prompts[11], "c"),
    question(hard_question_prompts[12], "a"),
    question(hard_question_prompts[13], "b"),
    question(hard_question_prompts[14], "a"),
    question(hard_question_prompts[15], "c"),
    question(hard_question_prompts[16], "b"),
    question(hard_question_prompts[17], "c"),
    question(hard_question_prompts[18], "c"),
    question(hard_question_prompts[19], "a")
]

main()
