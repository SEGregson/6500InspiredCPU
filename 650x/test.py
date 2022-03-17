#import CPU
import Register;


"""regFile = {};
for i in range(256):
    regFile[i] = bin(i);

print(regFile);"""

reg = Register.Register();
reg.setBytes(342);

print(reg);