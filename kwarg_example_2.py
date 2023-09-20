
def create_greeting(**kwargs):
    #check if a name arguments is provided otherwise use a default value
    name = kwargs.get('name','Guest')
    #check if a greeting argument is provided otherwise use a default greeting
    greeting = kwargs.get('greeting', 'hello')
    #format the greeting message
    message = f"{greeting},{name}"

    return message

if __name__=="__main__":
    #create a greeting using kwargs
    greeting1 = create_greeting(name="Alice", greeting="Hi")
    #Display the meeting
    print(greeting1) #output Hi Alice
    #create another greeting with default values
    greeting2 = create_greeting()
    print(greeting2)


