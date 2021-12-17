import numpy

IMM = 8188      # Example of a 13-bit signed value of -4

# this is how to convert this number back to its negative form
IMM = IMM | (0b111<<13)  # Negative sign extend by adding 3 bits to make this a 16 bit number
print ("Signed value = ", numpy.int16(IMM)) # convert it to a signed 16 bit number



