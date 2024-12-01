# pylint: disable=C0114
from flask import Flask, request # pylint: disable=E0401
from calculator import Calculator

app = Flask(__name__)

@app.route('/calculator')
def calculator():
    """
    Main function for app
    """
    req_args = request.args.to_dict()
    c = Calculator(req_args['arg1'], req_args['arg2'])
    res = f"{req_args['arg1']} + {req_args['arg2']} = {c.add()}"
    return res

if __name__ == '__main__':
    app.run(debug=True)
