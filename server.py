from flask import Flask, redirect, url_for, render_template, request
from time import sleep
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home(): 
    if request.method == 'POST':
      
      di=request.form["dicta"]
      return redirect(url_for("rikrol",dict=di))
    return render_template('index.html')

@app.route('/<dict>')
def rikrol(dict):
    sleep(2)
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ?t=1")

if __name__ == '__main__':
    app.run()