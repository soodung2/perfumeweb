from flask import Flask, render_template, request
 
 
app = Flask(__name__)
 
@app.route("/",  methods=['GET', 'POST'])
 
def index():
 
    if request.method == 'GET':
        name = request.args.get("name", "홍길동")
        print(request.form)
 
    return render_template('main.html', name = name)
 
if __name__ == "__main__":
    app.run()
#checkResult > span:nth-child(2)