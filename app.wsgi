import sys
sys.path.insert(0, '/var/www/html')

activate_this = '/home/pi/.local/share/virtualenvs/html-NW9Setf-/bin/activate_this'

with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from website import create_app
app = create_app()