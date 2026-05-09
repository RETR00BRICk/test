import my_console
import file_loader
import string
console = my_console.Console(100)
loader = file_loader.Loader("quizes")
modes = ["menu","player","admin"]
mode_num = 0
if __name__ == "__main__":

    while True:
        console.clear()
        console.frametext(f"MODE: {modes[mode_num].upper()}",".")
       
        match mode_num:
            case 0:
                actions = ["quit","play","history"]
                action, action_num = console.handle_choices("Choose action:", actions)
                match action_num:
                    case 0:
                        console.clear()
                        confirm = console.handle_confirm()
                        if confirm: exit()
                    case 1:
                        console.clear()
                        console.frametext("MODE SELECT", ".")
                        mod_choice = ["player","admin"]
                        mode, _ = console.handle_choices("Choose quiz mode:", mod_choice)
                        mode_num = modes.index(mode)
                    case 2:
                        history = loader.get_history()
                        if len(history) > 0:
                            console.clear()
                            console.frametext("HISTORY OF YOUR QUIZES", "_")
                            console.textlist(history)
                        else:
                            console.error("History is empty!")
                        console.handle_enter()
            case 1:
                actions = ["choose quiz", "back to menu"]
                _, action_num = console.handle_choices("Choose action:", actions)
                match action_num:
                    case 0:
                        console.clear()
                        console.frametext("QUIZ LIST", "_")
                        quizes = loader.get_quizes_list()
                        if len(quizes) > 0:
                            choice, _ = console.handle_choices("Choose quiz: ", quizes)
                            quiz = loader.get_quiz(choice)
                            correct_answers = 0
                            questions_count = len(quiz)
                            if questions_count <= 0:
                                console.error("Quiz is empty!")
                                console.handle_enter()
                                continue
                            for num, line in enumerate(quiz):
                                console.clear()
                                console.frametext(f"QUIZ: {choice} | QUESTION {num + 1}/{questions_count}", ".")
                                console.text(f"QUESTION: {line["question"]}")

                                _, answer_num = console.handle_choices("Pick an answer", line["answers"])
                                if answer_num == line["correct"]:
                                    correct_answers += 1
                            
                            console.clear()
                            console.frametext("CONGRATS! YOU FINISHED THE QUIZ!", "=")
                            console.text(f"Quiz name: {choice}")
                            console.text(f"Correct answers: {correct_answers} out of {questions_count}")
                            console.text(f"Score: {100*correct_answers/questions_count}%")
                            loader.save_to_history(choice, correct_answers, questions_count)
                            console.handle_enter()
                        else:
                            console.error("No available quizes in 'quizes/' folder!")
                            console.handle_enter()
                    case 1:
                        mode_num = 0
            case 2:
                actions = ["create new quiz", "back to menu"]
                _, action_num = console.handle_choices("Choose action:", actions)
                match action_num:
                    case 0:
                        console.clear()
                        console.frametext("CREATING NEW QUIZ", ".")
                        forbidden = string.punctuation
                        name = console.handle_input("Enter quiz name (don't use special symbols or punctuation) >>> ", forbidden)
                        questions_count = console.handle_range_input("How many questions do you want to make? (5 to 10)", range(5,11))
                        quiz = list()

                        for question_num in range(questions_count):
                            console.clear()
                            console.frametext(f"CREATING QUESTION {question_num + 1}/{questions_count}", ".")
                            question = console.handle_input(f"Enter the question text >>> ", "|")
                            answers = list()
                            for answer_num in range(4):
                                answer = console.handle_input(f"Enter answer variant number {answer_num+1} >>> ", "|")
                                answers.append(answer.strip())
                            _, correct_num = console.handle_choices("Mark correct answer:",answers)
                            quiz.append(
                                {
                                    "question":question,
                                    "answers":answers,
                                    "correct":correct_num
                                }
                            )

                        console.clear()
                        console.text(f"Finished making {name} quiz, questions: {questions_count}")
                        loader.create_quiz(name, quiz)
                        console.text(f"Saved as {name}.txt in 'quizes/' folder")
                        console.handle_enter()
                    case 1:
                        mode_num = 0