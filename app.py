import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def fibonacci():
    termo_1 = 0
    termo_2 = 1
    numeros = "0, 1, "
    for i in range(48):
        termo_3 = termo_1 + termo_2
        numeros += str(termo_3) + ", "
        termo_1 = termo_2
        termo_2 = termo_3
    return numeros


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(host='0.0.0.0', port=port)
