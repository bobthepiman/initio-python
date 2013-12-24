from config import *
from gpio import *
from drive import *

class Initio:
	"""Wrapper for an Initio robot, powered by a PiRoCon board"""

	def __init__(self, config):
		"""Initialises the robot with a configuration"""
		self.configuration = config;
		self.gpio = InitioGpio();
		self.drive = InitioDrive(self.configuration.drive, self.gpio);
		self._consumeConfiguration();

	def _consumeConfiguration(self):
		"""Processes the current configuration"""
		if self.configuration is None:
			raise ConfigException();
		self.gpio.initAsOutput(self.configuration.head.panServo.port);
		self.gpio.initAsOutput(self.configuration.head.tiltServo.port);

