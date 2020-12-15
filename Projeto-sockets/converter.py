class converter:

    def __init__(self, o, v):
        self.o = o
        self.v = v

    def coin(self):
        if self.o == 1:
            dolar = (float(self.v) / 5.12)
            self.resultconv1 = dolar
            return self.resultconv1

        elif self.o == 2:
            iene = (float(self.v) / 0.049)
            self.resultconv2 = iene
            return self.resultconv2

        elif self.o == 3:
            peso = (float(self.v) / 0.049)
            self.resultconv3 = peso
            return self.resultconv3

    def speed(self):
        if self.o == 1:
            km = (float(self.v)* 3.60)
            self.resultconv4 = km
            return self.resultconv4

        elif self.o == 2:
            ms = (float(self.v)/ 3.60)
            self.resultconv5 = ms
            return self.resultconv5

        elif self.o == 3:
            mph = ((self.v) / 1.60934)
            self.resultconv6 = mph
            return self.resultconv6


    def time(self):
        if self.o == 1:
            #Hora -> Minuto
            minute = self.v / 0.01666666666
            self.resultconv7 = minute
            return self.resultconv7

        elif self.o == 2:
            #Minuto -> Hora
            hour = (self.v *0.01666666666)
            self.resultconv8 = hour
            return self.resultconv8

        elif self.o == 3:
            #Segundo -> Minuto
            minute = (self.v *0.01666666666)
            self.resultconv9 = minute
            return self.resultconv9