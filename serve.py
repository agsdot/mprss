# to run webserver, issue command in terminal
# python serve.py and goto your browser and point it to http://localhost:3000

import SimpleHTTPServer
import SocketServer
httpd = SocketServer.TCPServer(("", 3000), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.serve_forever()
