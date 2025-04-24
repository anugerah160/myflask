"""
Flask app for emotion detection using Watson NLP API.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def emotion_detector_route():
    """
    Render the index HTML page where users can input text.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def detect_emotion():
    """
    Receive user text input and return the emotion analysis response.
    Handles both GET and POST requests.
    """
    text = (
        request.form.get('text')
        if request.method == 'POST'
        else request.args.get('textToAnalyze')
    )
    result = emotion_detector(text)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    response = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


    return response

if __name__ == '__main__':
    app.run(debug=True)
