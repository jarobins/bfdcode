# Bit Field Decode
# Functions that help decode bit fields. Used for instruction decoding for 
# processors and such

# Using the MIPS instructions to test the code

# The mask string for the parameters. Use unique letters for each param
# and place the letter in the corresponding field. 

r_type = "ppppppssssstttttdddddhhhhhffffff"
i_type = "ppppppssssstttttiiiiiiiiiiiiiiii"
j_type = "ppppppaaaaaaaaaaaaaaaaaaaaaaaaaa"

# ADD

inst_val = 0b00000001000001000110000000100000

def bin_string32(val, bs=1):
    '''Convert the value to a binary string of 32 length'''
    if bs:  # Byte Swap
        a = val & 0xFF
        b = (val >> 8) & 0xFF
        c = (val >> 16) & 0xFF
        d = (val >> 24) & 0xFF
        ret_val = "{:08b}{:08b}{:08b}{:08b}".format(a, b, c, d)
    else:
        ret_val = "{:032b}".format(val)
    return ret_val


def parse(v, m):
    s_val = bin_string32(v, bs=0)
    print(s_val)
    print(m)
    p = list(set(m))
    # Im making this short for no good reason other than 
    # list comps are cool.
    ret_d = {x : (s_val[m.index(x):m.count(x)+m.index(x)]) for x in p}

    # The function returns a dictionary of parameters and values from the
    # fields defines in the "m" variable. 
    return ret_d

if __name__ == "__main__":  
    data = parse(inst_val, r_type)
    for item in data:
        print("{} : {:X}".format(item, int(data[item], 2)))