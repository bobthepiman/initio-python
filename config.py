class ConfigException(Exception):
	"""Exception raised when there is a problem with the configuration"""
	pass

class Side:
	"""An enum which provides side information"""
	Left, Right = range(0, 2);

class Direction:
	"""An enum which provides direction information"""
	Forward, Backward = range(2, 4);

class Rotation:
	"""An enum which provides rotation information"""
	Clockwise, Anticlockwise = range(4, 6);

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

class DriveConfiguration:
	"""Configuration for a drive system (usually two motors)"""

	"""This is the default configuration for the left motor"""
	leftMotor = MotorConfiguration(7, 9, Side.Left);

	"""This is the default configuration for the right motor"""
	rightMotor = MotorConfiguration(8, 10, Side.Right);
	

class ServoConfiguration:
	"""Configuration for a servo"""

	"""The port that this servo listens on"""
	port = 0;

	"""The minimum PWM width this servo supports"""
	minWidth = 50;

	"""The maximum PWM width this servo supports"""
	maxWidth = 250;

	def __init__(self, p, min, max):
		"""Construct a servo configuration"""
		self.port = p;
		self.minWidth = min;
		self.maxWidth = max;

class HeadAssemblyConfiguration:
	"""Configuration for a head assembly"""

	"""The default pan configuration"""
	panServo = ServoConfiguration(22, 55, 250);

	"""The default tilt configuration"""
	tiltServo = ServoConfiguration(18, 65, 250);

class InitioConfiguration:
	"""A configuration object to pass to an Initio"""
	
	"""The default drive configuration"""
	drive = DriveConfiguration();

	"""The default configuration for the head assembly"""
	head = HeadAssemblyConfiguration();
