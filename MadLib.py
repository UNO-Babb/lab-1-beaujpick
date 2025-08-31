
#MadLib.py
#Name:
#Date:
#Assignment:

def main():
  print("Madlib")
  #Ask user for words
noun1 = input("Enter a food: ")
noun2 = input("Enter a place: ")
noun3 = input("Enter a noun: ")
noun4 = input("Enter a place: ")
noun5 = input("Enter a verb: ")
noun6= input("Enter an animal: ")
  #Print the story with the user supplied words.
print("I absolutely despise to eat", noun1,".")
print("I wanted to go to the", noun2,"so I took my favorite", noun3, "with me.")
print("I got tired and figured I'd head back to the", noun4, "and lie down.")
print("It was then I remembered I forgot to", noun5, "my", noun6, "!")
#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
