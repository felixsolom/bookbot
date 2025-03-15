from stats import get_num_words, get_num_chars, sorting_data
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    else:
        count = get_num_words(sys.argv[1])
        dict_to_sort = get_num_chars(sys.argv[1])
        sorted_data = sorting_data(dict_to_sort)
        
        print(f"""
        ============ BOOKBOT ============
        Analyzing book found at {sys.argv[1]}...
        ----------- Word Count ----------
        Found {count} total words
        --------- Character Count -------
        {sorted_data}
        ============= END ===============
        """)
    

if __name__=="__main__":
    main()