""" 
    useful websites:
    https://cx16.dk/6502/index.html - general information
"""

from Register import *;
class CPU:
    def __init__(self):
        ## begin in the base states
        # init Registers

        self.pc = Register(0);      # program counter
        self.sp = Register(0);      # stack pointer
        self.acc = Register(0);     # accumulator
        self.irx = Register(0);     # index register x
        self.iry = Register(0);     # index register y

        # now time for the flags (all for last operation result)
        self.cF = False;     # carry flag - checks for overflow or underflow bits
        self.zF = False;     # zero flag - checks if last result was 0
        self.idF = False;    # interrupt disable - does what it says on the tin (disables interrupts)
        self.dmF = False;    # decimal mode - causes the cpu to follow the Binary Coded Decimal
        self.bcF = False;    # break command - detects interrupts being thrown
        self.ofF = False;    # overflow flag - checks if the overflow causes the bit to invert (e.g. 64+64=-128)
        self.nF = False;     # negitive flaf - checks if the result was negitive

        # storage registers
        # create 256 registers each with a hex value
        regFile = {};
        for i in range(256):
            regFile[hex(i)] = Register(1).setBytes(0);

        stack = list[256];



    ## now is time for the instruction set:

    # load/store
    def LDA(self, ad):
        self.acc.setBytes();


    # transfer

    # stack operations

    # logic

    # arithmetic

    # increment/decrement

    # shifts

    # jumps and calls

    # branches

    # flag status change

    # system funcitons


