import codecs
encoded_text = open("mod26-question.txt").readline()
decoded_text = codecs.decode(obj=encoded_text, encoding="rot_13")
print(decoded_text)