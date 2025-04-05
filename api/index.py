from vercel_wsgi import handle
from taskmanager.wsgi import application

app = handle(application)
