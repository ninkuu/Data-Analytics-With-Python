import sys
script, input_encoding =sys.argv


def main(language_file, encoding):
    line = language_file.readline()
    
    if line:
        print_line(line, encoding)
        return main(language_file, encoding)
    
    
def print_line(line, encoding):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding)
    cooked_string = raw_bytes.decode(encoding)
    
    print(raw_bytes, "<===>", cooked_string)
    
    
languages = open("data/languages.txt", encoding="UTF-8")

main(languages, input_encoding)
