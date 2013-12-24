from config import *
from gpio import *
from drive import *
from head import *
from ultrasonic import *

class Initio:
	"""Wrapper for an Initio robot, powered by a PiRoCon board"""

	def __init__(self, config):
		"""Initialises the robot with a configuration"""
		self.configuration = config;
		self.gpio = InitioGpio();
		self.drive = InitioDrive(self.configuration.drive, self.gpio);
		self.head = InitioHead(self.configuration.head, self.gpio);
		self.ultrasonic = InitioUltrasonic(self.configuration.ultrasonic, self.gpio);
