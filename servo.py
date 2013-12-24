from subprocess import call

class RunningServo:
	"""A class for a running servo to manage its state"""

	def __init__(self, config):
		"""Initialises the servo"""
		self.config = config;
		self.output = None;

class UnitialisedPinException(Exception):
	"""Exception for when you try and use an unintialised pin"""
	pass

class InitioServo:
	"""Class for managing servos"""

	def __init__(self):
		self.currentServos = {};

		self._mappings = {
			25: 22,
			24: 18
		}

	def __del__(self):
		"""Destructor cleans up its started processes"""
		self._stop();

	def registerServo(self, config):
		"""Registers a servo"""
		self.currentServos[config.port] = RunningServo(config);
		self._reset();

	def deregisterServo(self, pin):
		"""Deregisters a servo"""
		self.currentServos.pop(pin, None);
		self._reset();

	def setOutput(self, pin, value):
		"""Sets the value of a servo, where the value is a percentage of its range"""
		if pin not in self.currentServos:
			raise UninitialisedPinException();
		servo = self.currentServos[pin];
		if value > 100:
			value = 100;
		if value < -100:
			value = -100;

		if value is 0:
			target = servo.config.middleWidth;
		elif value < 0:
			max = servo.config.middleWidth;
			min = servo.config.minWidth;
			target = int(round((((max - min)/100.0)*(value+100)) + min));
		else:
			max = servo.config.maxWidth;
			min = servo.config.middleWidth;
			target = int(round((((max - min)/100.0)*value) + min));

		i = 0;
		for pinNumber in self.currentServos:
			if pinNumber is pin:
				break;
			i = i + 1;
		call("echo " + str(i) + "=" + str(target) + " > /dev/servoblaster", shell=True);

	def _stop(self):
		"""Stops the running service, if any"""
		call(["killall", "servod"]);

	def _start(self):
		"""Starts the service with correct configuration"""
		max = 0;
		min = 2000;
		pins = [];
		for pin, servo in self.currentServos.iteritems():
			pins.append(str(self._mappings[pin]));
			if servo.config.minWidth < min:
				min = servo.config.minWidth;
			if servo.config.maxWidth > max:
				max = servo.config.maxWidth;
		call(["../pibits/ServoBlaster/user/servod", "--pcm", "--p1pins=" + ",".join(pins), "--min=" + str(min), "--max=" + str(max)]);

	def _reset(self):
		"""Resets the service so it is configured correctly"""
		self._stop();
		self._start();

