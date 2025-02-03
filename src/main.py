def guess_the_word(user_guess, secret_word="python"):
    return user_guess.strip().lower() == secret_word.lower()


# test
if __name__ == "__main__":
    print("Bienvenue dans le jeu Guess the Word!")
    user_guess = input("Devinez le mot secret : ")
    if guess_the_word(user_guess):
        print("Bravo ! Vous avez trouvé le mot secret.")
    else:
        print("Dommage, essayez encore !")
