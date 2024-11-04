from main.tools import colors
import random
def main():
    print(selected_banner)
    
    print("\t\t\033[38;5;226mA Complete Resource Hub For Cyber Security Community")
    print("\u001b[37m--------------------------------------------------------------------------------")
def attack(name):
    print(f"\u001b[32m\t\t\t\t{name}")
    print("\u001b[37m--------------------------------------------------------------------------------")
def wrap_text(text, width=80):
    wrapped_text = []
    lines = text.split(" ")
    line = ""
    for word in lines:
        if len(line) + len(word) <= width:
            line += word + " "
        else:
            wrapped_text.append(line)
            line = word + " "
    wrapped_text.append(line)
    return "\n".join(wrapped_text)
def description(Description):
    print(f"\033[1m\u001b[37mDescription:{colors.reset}\033[38;5;226m")
    print(wrap_text(Description))
    print("\u001b[37m--------------------------------------------------------------------------------")

# For the cybronix devs improvise the code accordingly
def pick_banner():
    colors = ['\033[91m','\033[92m','\033[93m','\033[94m','\033[95m','\033[96m' ]
    RESET = '\033[0m'
    banner = [
        
        """
         
          
                _    _           _             __  __               _   
    | |  | |         | |           |  \/  |             | |  
    | |__| | __ _ ___| |_ ___  _ __| \  / | __ _ _ __ __| |  
    |  __  |/ _` / __| __/ _ \| '__| |\/| |/ _` | '__/ _` |  
    | |  | | (_| \__ \ || (_) | |  | |  | | (_| | | | (_| |  
    |_|  |_|\__,_|___/\__\___/|_|  |_|  |_|\__,_|_|  \__,_|  
                                                            

                                                       
                                                                    """,



       
    ]

    def color_style_text(color, text):
        return (color + text + RESET)

    banner_s = color_style_text(random.choice(colors),random.choice(banner))
    return banner_s

selected_banner = pick_banner()
