mood = input("How are you feeling? ").lower().strip()

# Control flow: if/elif/else
if mood == "happy" :
    print("Great! Have an awesome rest of the day!")
elif mood == "sad" :
    print("I am sad to hear that, hope it gets better!")
else:
    print("Good to hear. Keep it up.")