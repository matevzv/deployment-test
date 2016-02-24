import unittest
import socket
from deploymentsample import DeploymentSample

class TestDeployment(unittest.TestCase):

	def test_code_deployment(self):
		message = "Hello deployed code from: "
		hello = DeploymentSample(message)
		hi = hello.getHelloFromHost()
		print(hi)
		self.assertEqual(message + socket.gethostname(), hi)

if __name__ == '__main__':
	unittest.main()
