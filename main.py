import re

file_paths = {
            "boot.dev": ["messages/boot.dev/october.txt", "messages/boot.dev/september.txt"],
            "donthedeveloper": ["messages/donthedeveloper/october.txt", "messages/donthedeveloper/september.txt"]
            }

def open_file(file_path):
    try:
        with open(file_path) as text_string:
            return text_string.read()
    except FileNotFoundError:
        print(f"\n\033[38;5;{172}m{file_path} \033[31mFile Not Found\n\033[39m...")
    
def count_which_popular_emojis_I_use(file_paths):
    # List of top 10 emojis of 2023 from: https://www.meltwater.com/en/blog/top-emojis-2023
    top_ten_emojis = {'😊': 0, '✨': 0, '🥰': 0, '😍': 0, '🙏': 0, '🔥': 0, '❤️': 0, '🤣': 0, '😭': 0, '😂': 0}

    # iterates through all the files in file_paths
    for discord in file_paths:
        for path in file_paths[discord]:
            current_file = open_file(path)

            # increments an emoji counter in the top_ten_emojis, dict each time it finds a matching emoji in the files
            for char in current_file:
                if char in top_ten_emojis:
                    top_ten_emojis[char] += 1

    return top_ten_emojis






def main():
    #boot.dev_emoji_count = 
    
    popular_emojis = count_which_popular_emojis_I_use(file_paths)
    print(popular_emojis) # test




        


    
        
        





main()