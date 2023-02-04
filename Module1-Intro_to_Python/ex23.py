import sys
script, input_encoding, error =sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()
    
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
    
    
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    
    print(raw_bytes, "<===>", cooked_string)
    
    
languages = open("data/languages.txt", encoding="UTF-8")

main(languages, input_encoding, error)
'''python
playing with utf codes
raw_bytes = b'\xe6\x96\x87\xe8\xa8\x80'
print(raw_bytes.decode())
utf_string = "文言"
print("Is b'\xe6\x96\x87\xe8\xa8\x80' the same as 文言?")
raw_bytes == utf_string.encode()
'''