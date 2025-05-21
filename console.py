class Console:
    def WriteLine(self,message):
        return print(message)

    def ReadLine(self, message):
        # print(message)
        return input(message+"\n")