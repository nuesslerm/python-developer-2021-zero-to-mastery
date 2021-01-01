from translate import Translator

translator = Translator(to_lang="ja")

try:
    with open("modules/translate.txt", mode="r") as file_to_translate:
        to_translate = file_to_translate.read()

        with open("modules/translated.txt", mode="w") as translated_file:
            translation = translator.translate(to_translate)
            translated_file.write(translation)
            print("translation finished successfully. 👏")
except FileNotFoundError as err:
    print("file does not exist in designated location")
    raise err
except IOError as err:
    print("IO error")
    raise err
