def main(arg, arg2):

    
    print(arg+" "+arg2)
    

def fibonacci(n):

        
        if n == 0:
            return 0
        if n < 3:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)



def input_integer( ):

        while True:
             try:
                 n = abs(int(input("Please enter a number: ")))
                 return n
             except ValueError:
                 print("That was not integer number. Try again...")



if __name__ == "__main__":

    main("Hello","World!")
    print('This is Fibonacci number calculation program')
    n = input_integer()
    print('The result of Fibonacci secuence for ',n,'  ----->',fibonacci(n))
    
    
            
    
        

