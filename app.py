from flask import Flask, request # pylint: disable=E0401

# pylint: disable=EC0114

app = Flask(__name__)

@app.route('/calculator')
def calculator():
    """
    Main function for app
    """
    req_args = request.args.to_dict()
    result = int(req_args['arg1']) + int(req_args['arg2'])
    res = f"{req_args['arg1']} + {req_args['arg2']} = {result}"
    return res

if __name__ == '__main__':
    app.run(debug=True)
