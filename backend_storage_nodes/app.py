from flask import Flask, request, jsonify
import os   

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():     
      file = request.files['file']
      file.save(os.path.join('uploads', file.filename))
      return jsonify({'message': 'File uploaded successfully'})

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Distributed File Storage System!"


if __name__ == '__main__':
      os.makedirs('storage', exist_ok=True)
      app.run(host='0.0.0.0' ,port=5000)

