from config import *

class InitioDrive:
	"""Wrapper for Initio robot drive system"""

	def __init__(self, config, gpio):
		"""Initialises the drive system with a configuration"""
		self.configuration = config;
		self.gpio = gpio;
		self._consumeConfiguration();

	def _consumeConfiguration(self):
		"""Processes the current configuration"""
		if self.configuration is None:
			raise ConfigException();
		self.gpio.initAsOutput(self.configuration.leftMotor.portA);
		self.gpio.initAsOutput(self.configuration.leftMotor.portB);
		self.gpio.initAsOutput(self.configuration.rightMotor.portA);
		self.gpio.initAsOutput(self.configuration.rightMotor.portB);

	def _getMotorForSide(self, side):
		"""Returns the motor currently connected to the specified side"""
		return self.configuration.leftMotor if side is Side.Left else self.configuration.rightMotor;

	def _wheelDir(self, side, dir):
		motor = self._getMotorForSide(side);
		motorAval = dir is Direction.Forward;
		motorBval = dir is Direction.Backward;
		self.gpio.setPin(motor.portA, motorAval);
		self.gpio.setPin(motor.portB, motorBval);

	def _stopMotor(self, side):
		motor = self._getMotorForSide(side);
		self.gpio.setPin(motor.portA, False);
		self.gpio.setPin(motor.portB, False);

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

