# Dictionary containing sample names and their corresponding keys
import sample_names_dictionary as sn
from flask import Flask, jsonify, request
app = Flask(__name__)

# To search whether the key is already assigned to a name
def isKeyPresent(key):
    for usr, curr_key in sn.name_Dict.items():
        if key == curr_key:
            return usr
    return None

@app.route("/", methods=["POST"])
# To find the name of the user based on the key
def findUsername() :
    request_data = request.get_json()
    new_public_key = request_data['publickey']
    username = isKeyPresent(str(new_public_key))
    # return 'hi'
    if username != None :
        return jsonify({"username": username})
    else :
        for usr, key in sn.name_Dict.items() :
            if key == None :
                sn.name_Dict[usr] = str(new_public_key)
                return jsonify({"username": usr})

@app.route("/<username>", methods=["GET"])
def get_key(username):
    try:
        key = sn.name_Dict[username]
        if key == None:
            return "not found", 404
        else:
            return jsonify({"publickey": key})
    except KeyError:
        return "not found", 404

if __name__ == "__main__":
    app.run()
