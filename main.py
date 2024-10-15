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

def count_my_popular_emojis(discord):
    count_emojis = {}

    for path in file_paths[discord]:
        current_file = open_file(path)
        for char in current_file:
            # uses a regex that checks for anything that isn't a letter, number and specified punctuation chars
            if re.match(r'[^\w\s\',-./#—:\[\]"<!>?()=&@%]', char):
                if char in count_emojis:
                    count_emojis[char] += 1
                else:
                    count_emojis[char] = 1

    return count_emojis




def main():
    #boot.dev_emoji_count = 
    
    popular_emojis = count_which_popular_emojis_I_use(file_paths)
    print("popular emojis:", popular_emojis) # test

    my_emoji_count = {}
    boot_dev_emojis = count_my_popular_emojis("boot.dev")
    donthedeveloper_emojis = count_my_popular_emojis("donthedeveloper")

    print("my emojis:", my_emoji_count) # test
    print("boot.dev:", boot_dev_emojis) # test
    print("donthedeveloper:", donthedeveloper_emojis) # test



 #   for path in file_paths["boot.dev"]:
  #      current_file = open_file(path)
  #      for char in current_file:
  #          if re.match(r'[^\w\s\',-./#—:\[\]"<!>?()=&]', char):
  #              print(char)


    
        
        





main()