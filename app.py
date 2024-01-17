from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def hello_world():
    if request.method == 'POST':
        domain = request.form['domain']
        print(domain)
        return render_template('index.html',domain=domain)
    else:
        return render_template('index.html', domain=None)


if __name__ == '__main__':
    app.run(debug=True)
