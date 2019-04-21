from flask import Flask, request, jsonify, make_response
import re

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # JSONでの日本語文字化け対策


#半角英数字判定
alnumReg = re.compile(r'^[a-zA-Z0-9]+$')
def isalnum(s):
    return alnumReg.match(s) is not None

# ASCII判定
asciiReg = re.compile(r'^[!-~]+$')
def isascii(s):
    return asciiReg.match(s) is not None

# sign_up判定
def signup_judge(user_id, password):
    cause = ""
    judge = True
    if (len(user_id) == 0) or (len(password)):
        cause = "user_id or password is required"
        judge = False
    if not (isalnum(user_id) or isalnum(password)):
        cause = "user_id and password should be half-width alphanumeric"
        judge = False
    if not ((len(user_id) > 6) and (len(user_id) < 20)):
        cause = "the number of user_id should be 6 to 20"
        judge = False
    if not ((len(password) > 6) and (len(user_id) < 20)):
        cause = "the number of user_id should be 6 to 20"
        judge = False
    return judge, cause

# POST process
@app.route('/signup', methods=['POST'])
def post_json():
    json = request.get_json()  # POSTされたJSONを取得
    # judge, cause = signup_judge(json["user_id"], json["password"])
    return make_response(jsonify(json))  # JSONをレスポンス

# GET process
@app.route('/users', methods=['GET'])
def get_json_from_dictionary():
    dic = {
        'foo': 'bar',
        'ほげ': 'ふが'
    }
    return make_response(jsonify(dic))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3008)