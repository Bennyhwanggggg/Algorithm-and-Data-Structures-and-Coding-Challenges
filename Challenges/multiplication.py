'''
Wrtten by Benny Hwang 08/09/2017
 Decodes all multiplications of the form

                        *  *  *
                   x       *  *
                     ----------
                     *  *  *  *
                     *  *  *
                     ----------
                     *  *  *  *

 such that the sum of all digits in all 4 columns is constant.
'''

# First number will go from 100 to 999
for n1 in range(100,1000):
    # Second number will go from 10 to 99
    for n2 in range(10,100):
        # The total product needs to be 4 digits
        product = n1*n2
        if product >= 1000 and product <= 9999:
            # Calculate the product with the 1st digit
            p1 = n1*int(str(n2)[-1])
            # The product needs to have 4 digit to satisfy requirement, but first digit cannot be 0
            if len(str(p1)) == 4 and int(str(p1)[0]) != 0:
                # Check the other part of the product
                p2 = n1*int(str(n2)[-2])
                # p2 needs to be 3 digits and first digit cannot be 0
                if len(str(p2)) == 3 and int(str(p2)[0]) != 0:
                    # Calculate the sum of columns
                    col1 = int(str(n1)[-1])+int(str(n2)[-1])+int(str(p1)[-1])+int(str(product)[-1])
                    col2 = int(str(n1)[-2])+int(str(n2)[-2])+int(str(p1)[-2])+int(str(p2)[-1])+int(str(product)[-2])
                    col3 = int(str(n1)[-3])+int(str(p1)[-3])+int(str(p2)[-2])+int(str(product)[-3])
                    col4 = int(str(p1)[-4])+int(str(p2)[-3])+int(str(product)[-4])
                    # If all sum equal
                    if col1 == col2 and col2==col3 and col3 == col4:
                        print(("{} * {} = {}, all columns adding up to {}.").format(n1,n2,product, col1))

                
                                                                                        
                                                                                                
            
