from flask import Flask, request, jsonify
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import io

# Initialize Flask app
app = Flask(__name__)

# Load BLIP Model and Processor
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")

@app.route("/describe", methods=["POST"])
def describe_image():
    try:
        # Get the image file from the request
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided"}), 400
        image_file = request.files['image']

        # Open the image using PIL
        image = Image.open(image_file.stream)

        # Process the image and generate a caption
        inputs = processor(image, return_tensors="pt")
        output = model.generate(**inputs)
        caption = processor.decode(output[0], skip_special_tokens=True)

        # Return the caption
        return jsonify({"description": caption})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
