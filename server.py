from flask import Flask, request

app = Flask(__name__)



@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!'

@app.route("/calculator/add", methods=['POST'])
def add():
    req_data=request.get_json()
    x=req_data['first']
    y=req_data['second']
    

    return f'{x+y}'

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    req_data=request.get_json()
    x=req_data['first']
    y=req_data['second']
    return f'{x-y}'

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
