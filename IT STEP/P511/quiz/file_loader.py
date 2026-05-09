import os
class Loader():
    def __init__(self, path : str):
        folder = os.path.dirname(os.path.abspath(__file__)) #__file__ дает нам путь к текущему файлу который был взят из команды запуска. abspath делает его полным от корня диска
        self.path = folder + "/" + path
        if not os.path.exists(self.path):
            os.mkdir(self.path)
            print("a")
        with open(self.path + "/" + "history.txt", 'a', encoding="utf-8"):
            pass

    def get_history(self) -> list:
        history_path = self.path + "/" + "history.txt"
        if os.path.exists(history_path):
            with open(history_path, 'r', encoding="utf-8") as history:
                return history.readlines()
        return list()

    def save_to_history(self, name : str, correct_count : int, all_count : int):
        history_path = self.path + "/" + "history.txt"
        if os.path.exists(history_path):
            with open(history_path, 'a', encoding="utf-8") as history:
                history.write("-<>-"*5+"Name: "+name+"-<>-"*5 + "\n")
                history.write(f"Answered {correct_count} correctly out of {all_count}\n")
                history.write(f"Score: {100*correct_count/all_count}%\n\n")
    
    def create_quiz(self, name : str, line_list : list):
        if os.path.exists(self.path):
            with open(self.path + "/" + name + ".txt", "w", encoding="utf-8") as quiz:
                for line in line_list:
                    answers = "|".join(line["answers"])
                    quiz.write(f"{line["question"]}|{answers}|{line["correct"]}\n")
                    
    
    def get_quizes_list(self) -> list:
        if os.path.exists(self.path):
            file_list = os.listdir(self.path)
            name_list = list()
            for file in file_list:
                name, ext = os.path.splitext(file)
                if ext == ".txt" and name != "history": 
                    name_list.append(name)
            return name_list
        return list()
    
    def get_quiz(self, name : str) -> list:
        quiz_path = self.path + "/" + name + ".txt"
        if os.path.exists(quiz_path):
            with open(quiz_path, "r", encoding="utf-8") as quiz:
                question_list = list()
                for line in quiz:
                    output = line.strip().split("|")
                    if(len(output) != 6): continue
                    question = output[0]
                    answers = output[1:5]
                    try: correct = int(output[5])
                    except: continue
                    question_list.append(
                        {
                            "question":question,
                            "answers":answers,
                            "correct":correct
                        }
                    )
                return question_list
        return list()

            
        