class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


question1 = Question("Onde surgiu o grupo Eco Road?", "Guareí Velho")

print(question1.text)
print(question1.answer)