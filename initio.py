import config
import RPIO

class Initio:
	"""Wrapper for an Initio robot, powered by a PiRoCon board"""

	"""Maintain a list of initialised ports, and how they have been initialised"""
	_initialisedPorts = {};

	def __init__(self, config):
		"""Initialises the robot with a configuration"""
		self.configuration = config;
		self._consumeConfiguration();

	def __del__(self):
		RPIO.cleanup();

	def _consumeConfiguration(self):
		"""Processes the current configuration"""
		if self.configuration is None:
			raise ConfigException();
		self._initAsOutput(self.configuration.leftMotor.portA);
		self._initAsOutput(self.configuration.leftMotor.portB);
		self._initAsOutput(self.configuration.rightMotor.portA);
		self._initAsOutput(self.configuration.rightMotor.portB);

	def _initAsInput(self, port):
		"""Initialises a port as a input"""
		return self._initPort(port, RPIO.IN);

	def _initAsOutput(self, port):
		"""Initialises a port as an output"""
		return self._initPort(port, RPIO.OUT);

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

	def _setPin(self, pin, value):
		"""Sets a pin to be equal to a value"""
		self._checkPortIsType(pin, RPIO.OUT);
		RPIO.output(pin, value);	

	def forwards(self):
		"""Commands the robot to drive forwards"""
		self._setPin(self.configuration.leftMotor.portA, True);
		self._setPin(self.configuration.leftMotor.portB, False);
		self._setPin(self.configuration.rightMotor.portA, True);
		self._setPin(self.configuration.rightMotor.portB, False);

	def stop(self):
		"""Commands the robot to drive forwards"""
		self._setPin(self.configuration.leftMotor.portA, False);
		self._setPin(self.configuration.leftMotor.portB, False);
		self._setPin(self.configuration.rightMotor.portA, False);
		self._setPin(self.configuration.rightMotor.portB, False);

