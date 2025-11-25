from flask import Flask, jsonify, request

application = Flask(__name__)

@application.route('/api/data', methods=['GET'])
def get_data():
    sample_data = {"message": "Hello from Flask!"}
    return jsonify(sample_data)

@application.route('/api/data', methods=['POST'])
def post_data():
    data = request.json
    return jsonify({"received_data": data}), 201

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000)  # Adjusted host for Elastic Beanstalk