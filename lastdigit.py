num = int(input("Enter number: "))

lastdigit_num = int(repr(num)[-1])

exp = int(input("Enter exponent: "))

if exp == 0:
    print(1)

else:
    lastdigit_exp = int(repr(exp)[-1])
    last2digit_exp = 10*int(repr(exp)[-2])+int(repr(exp)[-1])

    mod_exp_2_3_7_8 = last2digit_exp % 4

    if lastdigit_exp % 2 == 1:
        mod_exp_4_9 = 1
    else:
        mod_exp_4_9 = 0

    arr_2 = [2,4,8,6]
    arr_3 = [3,9,7,1]
    arr_4 = [4,6]
    arr_7 = [7,9,3,1]
    arr_8 = [8,4,2,6]
    arr_9 = [9,1]

    if lastdigit_num == 0:
        print(f"Last digit of {num}^{exp} is 0.")

    elif lastdigit_num == 1:
        print(f"Last digit of {num}^{exp} is 1.")

    elif lastdigit_num == 2:
        print(f"Last digit of {num}^{exp} is {arr_2[mod_exp_2_3_7_8 - 1]}.")
        
    elif lastdigit_num == 3:
        print(f"Last digit of {num}^{exp} is {arr_3[mod_exp_2_3_7_8 - 1]}.")

    elif lastdigit_num == 4:
        print(f"Last digit of {num}^{exp} is {arr_4[mod_exp_4_9 - 1]}.")

    elif lastdigit_num == 5:
        print(f"Last digit of {num}^{exp} is 5.")

    elif lastdigit_num == 6:
        print(f"Last digit of {num}^{exp} is 6.")

    elif lastdigit_num == 7:
        print(f"Last digit of {num}^{exp} is {arr_7[mod_exp_2_3_7_8 - 1]}.")

    elif lastdigit_num == 8:
        print(f"Last digit of {num}^{exp} is {arr_8[mod_exp_2_3_7_8 - 1]}.")

    elif lastdigit_num == 9:
        print(f"Last digit of {num}^{exp} is {arr_9[mod_exp_4_9 - 1]}.")

        
'''

Currently error handling not supported, exp < 10 not supported

'''
