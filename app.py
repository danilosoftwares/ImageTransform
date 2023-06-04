from flask import Flask, render_template
import upload

app = Flask(__name__)

app.add_url_rule('/image/upload',methods=['POST'], view_func=upload.upload_file)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)