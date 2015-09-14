import sae
from astpy import wsgi

application = sae.create_wsgi_app(wsgi.application)