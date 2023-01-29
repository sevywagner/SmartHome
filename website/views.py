from flask import Blueprint, render_template, request, redirect
from phue import Bridge

b = Bridge('192.168.1.68')

views = Blueprint('views', __name__)

@views.route('/')
def home():
	return render_template('index.html')

@views.route('/lights', methods=['GET', 'POST'])
def lights():
    if (request.method == 'POST'):
        b.connect()
        
        light = b.get_light_objects('name')['Hue lightstrip']
        
        if (request.form.get('mode') == 'on'):
            light.on = True
        else:
            light.on = False
        
    return redirect('/')