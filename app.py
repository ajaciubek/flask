from flask import Flask, request

app = Flask(__name__)

@app.route('/calculator')
def calculator():
    req_args = request.args.to_dict()
    res = f"{req_args['arg1']} + {req_args['arg2']} = {int(req_args['arg1']) + int(req_args['arg2'])}"
    return res

if __name__ == '__main__':
    app.run(debug=True)
