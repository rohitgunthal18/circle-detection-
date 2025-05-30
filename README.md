# Pipe Detection App

A web application that detects and counts circular pipes in images using OpenCV and Flask.

## Features

- Upload images of trucks loaded with circular pipes
- Automatic detection and counting of circular pipes using computer vision
- Modern and responsive user interface
- Display of detected pipes with visual indicators
- Side-by-side comparison of original and processed images

## Technologies Used

- Python 3.9+
- Flask 2.0.1
- OpenCV (opencv-python-headless)
- HTML5/CSS3
- JavaScript

## Deployment Instructions

### Prerequisites

- A GitHub account
- A Render.com account (free tier available)

### Step-by-Step Deployment to Render

1. **Upload to GitHub**
   - Create a new repository on GitHub
   - Upload all project files to this repository

2. **Connect to Render**
   - Sign up for Render using your GitHub account
   - Create a new Web Service
   - Select your pipe detection repository from GitHub
   - Configure the service:
     - Name: pipe-detection-app (or your preferred name)
     - Environment: Python
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `gunicorn app:app`
     - Select the Free tier
   - Click "Create Web Service"

3. **Verify Deployment**
   - Once the build completes, Render will provide a URL for your application
   - Open the URL to access your pipe detection app

## Local Development

### Setup

1. Clone the repository:
```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Create a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Run the application:
```
python app.py
```

5. Open http://localhost:5000 in your browser

## Configuration

The application can be configured using environment variables:

- `SECRET_KEY`: Flask secret key (default: pipe_detection_secret_key)
- `PORT`: Port to run the application (default: 5000)

## Important Notes

- The free tier on Render has limited resources and may sleep after 15 minutes of inactivity
- Uploaded and processed images are stored temporarily and may be lost after redeploys
- For a production environment, consider using cloud storage for uploaded images

## Advanced Pipe Counter Application

An academic computer vision project that uses OpenCV to detect and count circular pipes in uploaded images. This application provides detailed analysis, visualization tools, and export options to facilitate industrial pipe counting.

## Features

### Detection and Analysis
- Upload images of trucks loaded with circular pipes
- Advanced image preprocessing for improved pipe detection accuracy
- Automatic detection of circular pipe ends with confidence scoring
- Count and visualize detected pipes with numbered outlines
- Detailed statistics about pipe count, sizes, and detection confidence

### Visualization Tools
- Multiple visualization modes: standard, heatmap, and information overlay
- Confidence-based color coding for pipe detections
- Interactive UI with tabbed views and toggles
- Histogram visualization of pipe size distribution

### Data Management
- Export detection results as CSV or JSON for further analysis
- Detailed history of all detection sessions
- Ability to review and compare past detections
- Parameter tracking for each detection

### Customization Options
- CLAHE enhancement for improved contrast
- Advanced edge detection options
- Adjustable detection sensitivity
- Adaptive parameter selection based on image characteristics

## Setup and Installation

1. Make sure you have Python (3.6 or higher) installed on your system.

2. Clone or download this repository to your local machine.

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```
   python app.py
   ```

5. Open your web browser and go to `http://127.0.0.1:5000/`

## How to Use

1. **Upload an Image**:
   - Click on the file browse button to select an image containing circular pipes
   - Optionally enable enhancement options:
     - CLAHE for better contrast in low-light conditions
     - Advanced edge detection for more precise pipe boundaries
     - Adjust sensitivity using the slider for fine-tuning detection

2. **Analyze Results**:
   - Review the pipe count, confidence score, and average pipe size
   - Switch between different visualization modes (standard, heatmap, info)
   - Examine the pipe size distribution histogram
   - View the detailed table of individual pipe data

3. **Export and Share Results**:
   - Export results as CSV for spreadsheet analysis
   - Export results as JSON for integration with other systems
   - Access detection history for all past sessions

## Technical Implementation

### Image Processing Pipeline

1. **Input Preprocessing**:
   - Grayscale conversion
   - Optional CLAHE enhancement
   - Adaptive blur for noise reduction
   - Optional edge enhancement

2. **Pipe Detection**:
   - Adaptive Hough Circle Transform with dynamic parameters
   - Size-based filtering to match pipe dimensions
   - Confidence calculation for each detection

3. **Results Analysis**:
   - Confidence scoring for each detected pipe
   - Statistical analysis of pipe sizes
   - Visualization generation (standard, heatmap, info overlay)

### Confidence Scoring System

The application estimates detection confidence based on:
- Edge strength around the circle perimeter
- Circle roundness and regularity
- Contrast with surrounding regions

### Parameter Optimization

The code dynamically adjusts detection parameters based on:
- Image dimensions and resolution
- User-selected sensitivity level
- Enhancement options enabled

## Academic Project Value

This project demonstrates several important computer vision concepts:
- Feature detection and object counting
- Image preprocessing and enhancement
- Confidence scoring and validation
- User interface design for technical applications
- Data visualization and export

## License

This project is open-source and available for educational and research purposes. 