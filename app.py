from flask import Flask, render_template,request
import subprocess
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def hello_world():
    if request.method == 'POST':
        domain = request.form['domain']
        options=request.form.getlist('options')
        scripts=request.form.getlist('scripts')
        print(scripts)
        if scripts[0]=="hydrarecon":
            result=['python3','crawlers/HydraRecon/hydrarecon.py']
            result.extend(options)
            result.extend(["-d",domain])
            ans=subprocess.Popen(result,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            ans.wait()
            output=ans.stdout.read().decode()
            return render_template('result.html',result=output)
        if scripts[0]=="finalrecon":
            result=['python3','crawlers/FinalRecon/finalrecon.py']
            result.extend(options)
            result.extend([domain])
            print(result)
            ans=subprocess.Popen(result,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            ans.wait()
            output=ans.stdout.read().decode()
            return render_template('result.html',result=output)
    else:
        return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
