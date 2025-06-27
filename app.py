from flask import Flask, render_template
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__,template_folder='templates', static_folder="./static", static_url_path="/static")

@app.route("/")
def home():
    return "Hello from Gunicorn + Flask on VPS at /webduino/"

@app.route("/matrix_control")
def index():
    return render_template("./matrix_control.html")

@app.route('/send_matrix', methods=['POST'])
def send_matrix():
    data = request.get_json()
    matrix = data.get('matrix', [])

    # 👉 你可以在這裡將資料轉發給 Webduino Smart 裝置
    # 例如透過 HTTP、MQTT 或 WebSocket 傳送
    print("接收到的點陣資料：", matrix)

    return jsonify({"message": "矩陣資料已接收！"})

app = DispatcherMiddleware(lambda environ, start_response: (
    start_response('404 Not Found', [('Content-Type', 'text/plain')]) or [b'Not Found']),
    {
        "/webduino": app
    }
)
