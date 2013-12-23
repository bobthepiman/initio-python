from config import *
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

	def _getMotorForSide(self, side):
		"""Returns the motor currently connected to the specified side"""
		return self.configuration.leftMotor if side is Side.Left else self.configuration.rightMotor;

	def _wheelDir(self, side, dir):
		motor = self._getMotorForSide(side);
		motorAval = dir is Direction.Forward;
		motorBval = dir is Direction.Backward;
		self._setPin(motor.portA, motorAval);
		self._setPin(motor.portB, motorBval);

	def _stopMotor(self, side):
		motor = self._getMotorForSide(side);
		self._setPin(motor.portA, False);
		self._setPin(motor.portB, False);

	def forwards(self):
		"""Commands the robot to drive forwards"""
		self._wheelDir(Side.Left, Direction.Forward);
		self._wheelDir(Side.Right, Direction.Forward);

	def stop(self):
		"""Commands the robot to drive forwards"""
		self._stopMotor(Side.Left);
		self._stopMotor(Side.Right);

	def clockwise(self):
		"""Commands the robot to rotate clockwise"""
		self._wheelDir(Side.Left, Direction.Forward);
		self._wheelDir(Side.Right, Direction.Backward);

	def anticlockwise(self):
		"""Commands the robot to rotate anticlockwise"""
		self._wheelDir(Side.Left, Direction.Backward);
		self._wheelDir(Side.Right, Direction.Forward);

	def reverse(self):
		"""Commands the robot to drive backwards"""
		self._wheelDir(Side.Left, Direction.Backward);
		self._wheelDir(Side.Right, Direction.Backward);

