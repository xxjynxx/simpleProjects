print("\n--- Morse Code Translator ---")

print("\n1.Encode Text\n2.Decode Text\n")

choice = input("Enter: ")
try:
	choice = int(choice)
except ValueError:
	print("\nError: Invalid Number")
	quit()

def morse_values(x):
    x = x.lower()
    values = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.",
    "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
    "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
    "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
    "y": "-.--", "z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.", "!": "-.-.--", "/": "-..-.",
    "(": "-.--.", ")": "-.--.-", "&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-...-",
    "+": ".-.-.", "-": "-....-", "_": "..--.-", "\"": ".-..-.", "$": "...-..-", "@": ".--.-.",
    "¿": "..-.-", "¡": "--...-"," ":" "
}

    return values[x]
def get_key(x):
  values = {
      "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.",
      "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
      "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
      "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
      "y": "-.--", "z": "--..",
      "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
      "6": "-....", "7": "--...", "8": "---..", "9": "----.",
      ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.", "!": "-.-.--", "/": "-..-.",
      "(": "-.--.", ")": "-.--.-", "&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-...-",
      "+": ".-.-.", "-": "-....-", "_": "..--.-", "\"": ".-..-.", "$": "...-..-", "@": ".--.-.",
      "¿": "..-.-", "¡": "--...-"," ":" "
  }
  for key, value in values.items():
    if x==value:
      return key

if choice==1:
	print("Enter text to encode...")
	text = input("Enter: ")
	print("\n")
	list_text = list(text)
	coded_list = map(morse_values, list_text)
	coded_final = list(coded_list)
	final_code = ' '.join(coded_final)
	print('\nCode: ', final_code)
elif choice==2:
	print("Enter code to decode...")
	code = input("Enter: ")
	print("\n")
	list_code = code.split(" ")
	text_list = map(get_key, list_code)
	text = ''.join(text_list)
	print('\nDecoded: ', text)
else:
	print("\nError: Invalid value")
