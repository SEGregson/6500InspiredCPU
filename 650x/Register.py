class Register:
    # this is an 8 or 16 bit little endian register

    def __init__(self, num=1):
        assert num <= 2, "Can't be more that a 16bit register";
        self.bytes = [];
        self.num = num;
        for i in range(num):
            self.bytes.append(0);

    def __str__(self):
        return str(self.bytes);

    def setBytes(self, cont: int) -> None:
        # modify for any amount of bytes

        assert cont < 2**self.num+1, f"register too small for {cont}";

        if cont < 256:
            self.bytes[0] = bin(cont);
        else:
            temp = str(bin(cont));

            temp = temp[::-1];

            b0 = temp[:7];
            b1 = temp[8:];

            self.bytes[0] = int("0b" + b0[::-1], 2);
            self.bytes[1] = int(b1[::-1], 2);
    
    def getBytes(self):
        return self.bytes;