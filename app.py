from flask import Flask, render_template
#import nxt.locator

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('nxt_rc.html')


@app.route('/check_connectivity', methods=['GET', 'POST'])
def check_connectivity():

    """
    # Codigo de ejemplo de NXT Python, por lo pronto por USB
    with nxt.locator.find() as b:
        print("Found brick:", b.get_device_info()[0])
        b.play_tone(440, 250)
    """

    return ("Se busco el brick.")

@app.route('/scan_color', methods=['GET', 'POST'])
def scan_color():

    """
    with nxt.locator.find() as b:
        color_scanner_sensor = b.get_sensor(nxt.sensor.Port.S4)
        color = color_scanner_sensor.get_sample()
        print(color) # El color detectado iria al BOX al centro del sitio web, o algun otro indicador que demos de alta
    """

    return ("Se detecto color.")

@app.route('/shoot', methods=['GET', 'POST'])
def shoot():

    # TODO: Agregar logica NXT

    return ("Abrazos no balazos")


if __name__ == '__main__':
    app.run(debug=True)