"""
Web server Flask xử lý phân tích cảm xúc văn bản sử dụng Watson NLP.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emot_detector():
    """
    Nhận chuỗi văn bản từ giao diện, gọi hàm phân tích và trả về chuỗi kết quả.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is <strong>{response['dominant_emotion']}</strong>."
    )

@app.route("/")
def render_index_page():
    """
    Render giao diện trang chủ chính (index.html) của ứng dụng.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000
    )
