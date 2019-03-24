from flask import Flask,request,jsonify
import random
import requests

app = Flask(__name__)
url = "http://numbersapi.com/"
@app.route("/",methods=['GET'])
def respond():
    req = request.args
    print(req)  #ImmutableiDict([('name', 'Neel')])

    return "You have reached the root endpoint"


#curl -d '({"name":"advait","age":"21"})'
#curl -d '{"name":"advait","age":"21"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/

@app.route("/",methods=['POST'])
def verify():
    #data = request.data
    data = request.get_json()
    print(data.keys())
    return jsonify(data)


@app.route("/getfact",methods=['POST'])
def getFact():
    req = request.get_json()
    intent = req.get("queryResult").get("intent").get("displayName")
    number = req.get("queryResult").get("parameters").get("number")
    qtype = req.get("queryResult").get("parameters").get("type")
    if intent == "numbers":
        if qtype == "random":
            qtype = random.choice(["trivia","year","math"])
        qurl = url + str(int(number)) + "/" + qtype + "?json"
        res = requests.get(qurl).json()["text"]
        print(res)
        print(qurl)
        return jsonify({"fulfillmentText":res}) #prinnt on dialofflow
    print(intent,number,qtype)


    print(req)  #print on server side
    return jsonify({"fulfillmentText":"Flask server hit"}) #return on client side


if __name__ == "__main__":
    app.run()

