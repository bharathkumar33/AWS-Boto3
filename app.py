import psutil
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    CPU_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    Message = None
    if CPU_percent > 80 or mem_percent > 0:
        Message = "High CPU or Memory Utilisation detected. Please scale up"
    #return f"CPU Utilisation: {CPU_percent} and Memory Utilisation: {mem_percent}"
    return render_template("index.html", cpu_metric=CPU_percent, mem_metric=mem_percent, message=Message)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')