
class ConfigException(Exception):
	"""Exception raised when there is a problem with the configuration"""
	pass

class Orientation:
	"""An enum which provides direction information"""
	Left, Right = range(0, 2);

class MotorConfiguration:
	"""Configuration for a motor that defines a port pair and a side"""

	"""Port A is the port that will be +ve when going forwards"""
	portA = 0;

	"""Port B is the port that is -ve when the robot is going forwards"""
	portB = 0;

	"""Which side of the robot this is for"""
	side = None;

	def __init__(self, a, b, s):
		"""Construct a motor configuration"""
		self.portA = a;
		self.portB = b;
		self.side = s;

class InitioConfiguration:
	"""A configuration object to pass to an Initio"""
	
	"""This is the default configuration for the left motor"""
	leftMotor = MotorConfiguration(7, 9, Orientation.Left);

	"""This is the default configuration for the right motor"""
	rightMotor = MotorConfiguration(8, 10, Orientation.Right);
