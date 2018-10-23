from flask import Flask

app = Flask(__name__)


# @app.route('/greet')
# @app.route('/greet/<name>')
# def greet(name=""):
#     return "Hello {}".format(name)

@app.route('/f/<temperature>')
def fahrenheit(temperature=""):
    new_temperature = float(temperature)
    result = str(new_temperature * 9.0 / 5 + 32)
    return "You inputted {} degrees celsius. In fahrenheit that is {} degrees".format(new_temperature, result)


@app.route('/c/<temperature>')
def celius(temperature=""):
    new_temperature = float(temperature)
    result = str(new_temperature * 5 / 9 - 32)
    return "You inputted {} degrees fahrenheit. In celsius that is {} degrees".format(new_temperature, result)


if __name__ == '__main__':
    app.run()
