from flask import Flask
import random
app = Flask(__name__)
random_number = random.randint(0, 9)


@app.route('/')
def home_page():
    return "<div style='text-align: center'>" \
           "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route('/<int:user_guess>')
def game_page(user_guess):
    if user_guess == random_number:
        return "<div style='text-align: center'>" \
               "<h1 style='color: green'>You got it right!</h1>" \
               "<img src='https://media.giphy.com/media/mGK1g88HZRa2FlKGbz/giphy.gif'>"
    elif user_guess < random_number:
        return "<div style='text-align: center'>" \
               "<h1 style='color: red'>That was low.</h1>" \
               "<img src='https://media.giphy.com/media/l1BgQSWd7WODurKvu/giphy.gif'>"

    elif user_guess > random_number:
        return "<div style='text-align: center'>" \
               "<h1 style='color: red'>Whew! That was high.</h1>" \
               "<img src='https://media.giphy.com/media/l3V0eXRJKmEcodX20/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
