from servo import *

import RPIO

class InitioGpio:
	"""Helper that wraps up the GPIO pins"""

	"""Const for a servo"""
	RPIO_SERVO = "servo";

	"""Maintain a list of initialised ports, and how they have been initialised"""
	_initialisedPorts = {};

	def __init__(self):
		"""Sets up the GPIO"""
		self.servo = InitioServo();

	def __del__(self):
		"""Cleans up the RPIO once finished"""
		RPIO.cleanup();

	def initAsInput(self, port):
		"""Initialises a port as a input"""
		return self._initPort(port, RPIO.IN);

	def initAsOutput(self, port):
		"""Initialises a port as an output"""
		return self._initPort(port, RPIO.OUT);

	def initAsServoOutput(self, servoConfig):
		"""Initialises a port as a servo"""
		if servoConfig.port not in self._initialisedPorts:
			self.servo.registerServo(servoConfig);
			self._initialisedPorts[servoConfig.port] = self.RPIO_SERVO;
			return;
		self._checkPortIsType(servoConfig.port, self.RPIO_SERVO);

	def _initPort(self, port, type):
		"""Initialises a port as a given type, raises an error if already initialised as another type"""
		if port not in self._initialisedPorts:
			RPIO.setup(port, type);
			self._initialisedPorts[port] = type;
			return;
		self._checkPortIsType(port, type);

	def _checkPortIsType(self, port, type):
		"""Checks a port is a specific type, raising an exception if not"""
		if self._initialisedPorts[port] is not type:
			raise IncorrectPortMappingException();

	def setPin(self, pin, value):
		"""Sets a pin to be equal to a value"""
		self._checkPortIsType(pin, RPIO.OUT);
		RPIO.output(pin, value);	

