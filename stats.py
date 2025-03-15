def get_num_words(file_path):
    with open(file_path) as file:
        word_count = 0
        file_contents = file.read()
        words = file_contents.split()
        for i in range(len(words)):
            word_count += 1 
             
    return word_count
    
def get_num_chars(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        chars = []
        for char in file_contents:
            if char.isascii():
                char = char.lower()
                chars.append(char)
                       
        count = {}
        for i in chars:
            if i not in count:
                sum = 0
                for j in chars:
                    if i == j:
                        sum += 1
                    count.update({i: sum})
    return count
    
def sorting_data(dict):
    sorted_list = []
    for key, value in dict.items():
        if key.isalpha():
            sorted_list.append({key: value})
        
    sorted_list.sort(key=lambda x: list(x.values())[0], reverse=True)
    
    formated_string = ""
    for item in sorted_list:
        for key, value in item.items():
            formated_string += f"        {key}: {value}\n"
    return formated_string.strip()
        
    
            
         
    
                