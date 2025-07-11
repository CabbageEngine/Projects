# Storing functions for welcome screen and primary menu


def welcomeIntro():
    prompt = "Welcome to Sals Grocers.\n"
    prompt += "Fresh produce, premium goods, and low prices everyday!\n"
    print(prompt)

def displayMenu():
    menu_items = ['(V)iew Products', '(A)dd Item', '(R)emove Item', \
        '(D)isplay Cart', '(Q)uit']
    print(" | ".join(menu_items))


