from faker import Faker
from flask import Flask, flash,session,jsonify

app = Flask(__name__)

@app.route('/datos',methods=['GET'])
def datos():
    fake = Faker()
    lista = list()
    for _ in range(13):
        data = dict()
        data["name"] = fake.name()
        data["city"] = fake.city()
        data["address"] = fake.address()
        data["phone_number"] = fake.phone_number()
        lista.append(data)
    return jsonify({"datos":lista})

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80, debug=True)