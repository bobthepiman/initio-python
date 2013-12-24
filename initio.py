from config import *
from gpio import *
from drive import *
from head import *
from ultrasonic import *
from ir import *
from floor import *

class Initio:
	"""Wrapper for an Initio robot, powered by a PiRoCon board"""

	def __init__(self, config):
		"""Initialises the robot with a configuration"""
		self.configuration = config;
		self.gpio = InitioGpio();
		if self.configuration.drive is not None:
			self.drive = InitioDrive(self.configuration.drive, self.gpio);
		if self.configuration.head is not None:
			self.head = InitioHead(self.configuration.head, self.gpio);
		if self.configuration.ultrasonic is not None:
			self.ultrasonic = InitioUltrasonic(self.configuration.ultrasonic, self.gpio);
		if self.configuration.ir is not None:
			self.ir = InitioIr(self.configuration.ir, self.gpio);
		if self.configuration.floor is not None:
			self.floor = InitioFloor(self.configuration.floor, self.gpio);

