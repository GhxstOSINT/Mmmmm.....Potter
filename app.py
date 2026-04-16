from flask import Flask, request, render_template_string

app = Flask(__name__)

def get_flag():
    return "CTF{x0r_5cr1pt_m4st3r}"

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Azkaban Black Box</title>
    <style>
        body { background: #050505; color: #00ff41; font-family: 'Courier New', monospace; display: flex; flex-direction: column; align-items: center; padding-top: 100px; }
        .terminal { border: 1px solid #00ff41; padding: 40px; box-shadow: 0 0 20px #00ff41; background: #000; text-align: center; }
        input { background: transparent; border: none; border-bottom: 1px solid #00ff41; color: #00ff41; outline: none; width: 350px; font-size: 1.2em; text-align: center; margin-bottom: 20px; }
        .status { font-weight: bold; margin-bottom: 10px; }
    </style>
</head>
<body>
    <div class="terminal">
        <h2>[ AZKABAN_SECURE_VAULT ]</h2>
        <p>PROVIDE MAGICAL SIGNATURE:</p>
        <form method="POST">
            <input type="text" name="sig" autofocus autocomplete="off" placeholder="...">
            <br>
            <button type="submit" style="background:#00ff41; color:#000; border:none; padding:5px 15px; cursor:pointer; font-family: monospace;">VERIFY</button>
        </form>
        <div class="status">{{ msg }}</div>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def vault():
    msg = ""
    if request.method == 'POST':
        sig = request.form.get('sig', '').strip()
        target = [121, 26, 75, 98, 92, 32, 100, 90, 125, 28, 29]
        
        if not sig:
            msg = "ERROR: SIGNATURE CANNOT BE EMPTY."
        elif len(sig) != len(target):
            msg = f"ACCESS DENIED. LENGTH MISMATCH."
        else:
            res = [(ord(sig[i]) ^ 42) + i for i in range(len(sig))]
            if res == target:
                msg = f"ACCESS GRANTED. FLAG: {get_flag()}"
            else:
                msg = "ACCESS DENIED. SIGNATURE MISMATCH."
            
    return render_template_string(HTML, msg=msg)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)