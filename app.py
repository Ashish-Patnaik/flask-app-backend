from flask import Flask, request, jsonify
from rembg import remove  # Correct import
from PIL import Image
import io
import base64
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/remove_background', methods=['POST'])
def remove_background():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        img = Image.open(image_file)
        output = remove(img)  # Use the imported remove function

        img_bytes = io.BytesIO()
        output.save(img_bytes, format="PNG")
        img_bytes.seek(0)

        img_base64 = base64.b64encode(img_bytes.getvalue()).decode('utf-8')

        return jsonify({'image': img_base64}), 200

    except Exception as e:
        print(f"Error processing image: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)