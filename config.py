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

class UltrasonicConfiguration:
	"""Configuration for an ultrasonic distance sensor"""
	
	def __init__(self, p):
		"""Constructs the ultrasonic config"""
		self.port = p;

class ToggleSwitchConfiguration:
	"""Configuration for a toggle switch of some kind"""

	def __init__(self, p):
		"""Constructs the sensor config"""
		self.port = p;

class SidedToggleSwitchConfiguration(ToggleSwitchConfiguration):
	"""Configuration for a toggle switch which also has a side property"""

	def __init__(self, p, s):
		"""Constructs the sensor config"""
		ToggleSwitchConfiguration.__init__(self, p);
		self.side = s;

class SidedToggleSwitchPairConfiguration:
	"""A pair of toggle switches with side configurations"""

	def __init__(self, leftPort, rightPort):
		self.left = SidedToggleSwitchConfiguration(leftPort, Side.Left);
		self.right = SidedToggleSwitchConfiguration(rightPort, Side.Right);

class MotorConfiguration:
	"""Configuration for a motor that defines a port pair and a side"""

	def __init__(self, a, b, s):
		"""Construct a motor configuration"""
		self.portA = a;
		self.portB = b;
		self.side = s;

class DriveConfiguration:
	"""Configuration for a drive system (usually two motors)"""

	def __init__(self):
		"""This is the default configuration for the left motor"""
		self.leftMotor = MotorConfiguration(7, 9, Side.Left);

		"""This is the default configuration for the right motor"""
		self.rightMotor = MotorConfiguration(8, 10, Side.Right);
	

class ServoConfiguration:
	"""Configuration for a servo"""

	def __init__(self, p, min, max, mid):
		"""Construct a servo configuration"""
		self.port = p;
		self.minWidth = min;
		self.maxWidth = max;
		self.middleWidth = mid;

class HeadAssemblyConfiguration:
	"""Configuration for a head assembly"""

	def __init__(self):
		"""The default pan configuration"""
		self.panServo = ServoConfiguration(25, 54, 250, 147);

		"""The default tilt configuration"""
		self.tiltServo = ServoConfiguration(24, 65, 250, 160);

class InitioConfiguration:
	"""A configuration object to pass to an Initio"""
	
	def __init__(self):
		"""The default drive configuration"""
		self.drive = DriveConfiguration();

		"""The default configuration for the head assembly"""
		self.head = HeadAssemblyConfiguration();

		"""The default ultrasonic configuration"""
		self.ultrasonic = UltrasonicConfiguration(14);

		"""Default IR configuration"""
		self.ir = SidedToggleSwitchPairConfiguration(27, 18);

		"""Default floor sensor configuration"""
		self.floor = SidedToggleSwitchPairConfiguration(23, 22);

