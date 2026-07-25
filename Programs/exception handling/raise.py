try:
    num=int(input("guess the number: "))
    if num!=4:
        raise Exception(" you guessed wrong and number was 4 ") 
except Exception as e:
    print(f"error {e}")
else:
    print("you guessed it correctly ")