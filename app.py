import os
import cv2
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', "pipe_detection_secret_key")

# Get the base directory of the application
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create directories if they don't exist
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')
PROCESSED_FOLDER = os.path.join(BASE_DIR, 'static', 'processed')

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        flash('No image part')
        return redirect(request.url)
        
    file = request.files['image']
    
    if file.filename == '':
        flash('No selected image')
        return redirect(request.url)
        
    if file:
        # Save uploaded file
        filename = file.filename
        upload_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(upload_path)
        
        # Process the image to detect circles
        processed_filename, circle_count = detect_circles(upload_path, filename)
        
        return render_template('index.html', 
                            original_image=f"uploads/{filename}",
                            processed_image=f"processed/{processed_filename}",
                            circle_count=circle_count)
    
    return redirect('/')

def detect_circles(image_path, filename):
    # Read the image
    img = cv2.imread(image_path)
    if img is None:
        return filename, 0
    
    output_img = img.copy()
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (9, 9), 2)
    
    # Use Hough Circle Transform to detect circles
    circles = cv2.HoughCircles(
        blurred,
        cv2.HOUGH_GRADIENT,
        dp=1.2,            # Inverse ratio of accumulator resolution to image resolution
        minDist=30,        # Minimum distance between detected circles' centers
        param1=50,         # Upper threshold for Canny edge detector
        param2=30,         # Threshold for center detection
        minRadius=10,      # Minimum circle radius
        maxRadius=50       # Maximum circle radius
    )
    
    circle_count = 0
    
    # If circles are found, count and draw them
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")  # Convert to integer
        circle_count = len(circles)
        
        # Loop over the detected circles and draw them
        for i, (x, y, r) in enumerate(circles, 1):
            # Draw the circle outline
            cv2.circle(output_img, (x, y), r, (0, 255, 0), 2)
            
            # Draw a small circle at the center
            cv2.circle(output_img, (x, y), 5, (0, 0, 255), -1)
            
            # Add a label number near the circle
            cv2.putText(output_img, str(i), (x-15, y-15), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    
    # Save processed image
    processed_filename = f"processed_{filename}"
    processed_path = os.path.join(PROCESSED_FOLDER, processed_filename)
    cv2.imwrite(processed_path, output_img)
    
    return processed_filename, circle_count

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False) 