from config import *

class InitioHead:
	"""Wrapper for Initio robot pan/tilt head system"""

	def __init__(self, config, gpio):
		"""Initialises the head system with a configuration"""
		self.configuration = config;
		self.gpio = gpio;
		self._consumeConfiguration();

	def _consumeConfiguration(self):
		"""Processes the current configuration"""
		if self.configuration is None:
			raise ConfigException();
		self.gpio.initAsServoOutput(self.configuration.panServo);
                self.gpio.initAsServoOutput(self.configuration.tiltServo);

	def pan(self, percent):
		"""Sets the pan to a percent of its range"""
		self.gpio.servo.setOutput(self.configuration.panServo.port, percent);

	def tilt(self, percent):
		"""Sets the tilt to a percent of its range"""
		self.gpio.servo.setOutput(self.configuration.tiltServo.port, percent);

