import sys

def count_word(filepath: str, target_word: str) -> int:
    count = 0
    with open(filepath, 'r') as file:
        for line in file:
            if target_word in line:
                count += 1
    return count

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python line_counter.py <file> <word>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    word = sys.argv[2]
    print(count_word(file_path, word))