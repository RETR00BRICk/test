import os
class Console:
    def __init__(self, width: int):
        self.width = width
        
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def border(self):
        print("|",end="")
    
    def error(self, text : str):
        self.border()
        print("-<(!)>- ERROR: " + text)

    def separate(self):
        print('='*self.width)

    def text(self, text : str):
        self.border()
        print(text)

    def textlist(self, lines : list):
        for line in lines:
            if type(line) == str:
                self.text(line.strip())

    def frametext(self, text : str, symbol : str):
        frame_width_before = (self.width - len(text))//2
        frame_width_after = (self.width - frame_width_before - len(text))
        self.border()
        print(symbol[0]*frame_width_before + text + symbol[0]*frame_width_after)

    def bigtext(self, text: str, symbol: str):
        self.border()
        text_len = len(text)
        if text_len >= self.width:
            print(text)
            return
        string = [symbol[0]]*self.width
        for letter_num in range(text_len):
            letter_string_num = (letter_num) * (self.width-1) // (text_len-1)
            string[letter_string_num] = text[letter_num]
        print("".join(string))
 
    def handle_choices(self, text : str, choices: list) -> tuple:
        self.border()
        print(f">>> {text} <<<")
        for num in range(len(choices)):
            choice = choices[num]
            if type(choice) != str: return
            self.border()
            print(f"[{num+1}]> {choice} <")

        while True:
            self.border()
            choice = input("Enter your choice >>> ")
            try:
                choice_int = int(choice)-1
                if choice_int in range(len(choices)):
                    return choices[choice_int], choice_int
                else:
                    self.error("Choice does not exist. Pick a valid one!")
            except:
                self.error("Invalid input. Enter a number!")
    
    def handle_input(self, text: str, forbidden : str) -> str:
        while True:
            self.border()
            string = input(">"+text).strip()
            valid = len(string) > 0
            for char in string:
                if char in forbidden:
                    valid = False
                    break
            if valid:
                return string
            else:
                self.error("Input is invalid. Enter correct one!")
    
    def handle_range_input(self, text : str, int_range : range) -> int:
        self.border()
        print(f">>> {text} <<<") 
        while True:
            self.border()
            string = input(f"Enter number in range from {int_range.start} to {int_range.stop-1} >>> ").strip()
            try:
                int_input = int(string)
                if int_input in int_range:
                    return int_input         
                else:
                    self.error("Input is outside the given range! Enter a valid one")
            except:
                self.error("Input is not a number! Pick a valid one")

    def handle_enter(self):
        self.border()
        _ = input("(i) Press enter to continue...")

    def handle_confirm(self) -> bool:
        self.border()
        confirm = input("(i) Confirm? Press enter or write anything to confirm, write 'c' to cancel >>> ")
        return confirm.lower() != 'c'
    
    
        