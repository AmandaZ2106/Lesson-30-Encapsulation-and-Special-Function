class Word:
    def words(self,enteredword):
        self.enteredword=enteredword 
        revword=("")
        for a in enteredword:
            revword=a+revword
        print(revword)
w=Word()
w.words("Amanda")

