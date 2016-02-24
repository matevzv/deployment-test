import socket

class DeploymentSample:

	def __init__(self, message):
		self.message = message

	def getHelloFromHost(self):
		return self.message + socket.gethostname()
