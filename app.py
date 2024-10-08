from flask import Flask, render_template, request, jsonify
import nxt.locator

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('nxt_rc.html')

@app.route('/check_connectivity', methods=['GET'])
def check_connectivity():

    # TODO: Logica con NXT-Python para conectar con controller brick y emitir sonido de confirmacion
    connection_status = True # Placeholder para el valor de estado de comunicacion
    rsp = {"connection_status":connection_status}

    return (jsonify(rsp), 200)

@app.route('/move', methods=['POST'])
def move():

    direction = request.json['direction']

    try:
        b = nxt.locator.find()

        motor1 = b.get_motor(nxt.motor.Port.A)
        motor2 = b.get_motor(nxt.motor.Port.B)
        syncmot = nxt.motor.SynchronizedMotors(motor1, motor2, 0)
        if direction == "forward":
            syncmot.turn(64, 180, timeout=3)
        else:
            syncmot.turn(64, -180, timeout=3)
    except:
        print("NO BRICK WAS FOUND!")

    return (f"{direction} movement request sent to controller brick", 200)

@app.route('/scan_color', methods=['GET'])
def scan_color():

    # TODO: Logica con NXT-Python para detectar color con el sensor y enviar el valor rgb/hexa de regreso
    detected_color = "#4842f5" # Placeholder para el valor que obtendremos del sensor y se mostrara en la GUI
    rsp = {"detected_color":detected_color}

    return (jsonify(rsp), 200)

@app.route('/shoot', methods=['GET'])
def shoot():

    # TODO: Logica con NXT-Python para activar el motor que activa el mecanismo de disparo

    return (jsonify({"abrazos":True, "balazos":False}), 200)

if __name__ == '__main__':
    app.run(debug=True)