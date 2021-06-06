from translate import Translator

while True:
        a = Translator(from_lang = input("enter the language form which you want to  translate: "), to_lang = input("Enter the language to translate: "))

        transltion = a.translate(input("Enter the text: "))

        print(transltion)
