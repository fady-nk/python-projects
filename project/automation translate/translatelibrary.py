from translate import Translator

translator= Translator(from_lang="english", to_lang="spanish")
translation = translator.translate("hello world")
print(translation)
