from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'F:\\Python\\spy\\video'
app.config['ALLOWED_EXTENSIONS'] = {'mp4', 'avi', 'mkv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def save_video_file(video_file):
    filename = secure_filename(video_file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # Создание каталога, если он не существует
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    video_file.save(filepath)
    return filepath

class Svideo(Resource):
    def post(self):
        if 'video' not in request.files:
            return {'error': 'No file part'}, 400
        video_file = request.files['video']
        if video_file.filename == '' or not allowed_file(video_file.filename):
            return {'error': 'Invalid file'}, 400

        filepath = save_video_file(video_file)
        return {'message': f'File saved to {filepath}'}, 200

api = Api(app)
api.add_resource(Svideo, "/api/upload_video")

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="192.168.1.104")
