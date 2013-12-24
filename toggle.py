class ToggleSensor:
	"""Class that wraps up the behaviour of a toggle switch"""

	def __init__(self, config, gpio):
		"""Sets up the sensor"""
		self.gpio = gpio;
		self.configuration = config;
		self.callbacks = [];
		self.value = None;
		self._consumeConfiguration();

	def _consumeConfiguration(self):
		"""Handles the configuration"""
		self.gpio.initAsInput(self.configuration.port);
		self.gpio.addInterrupt(self.configuration.port, self._onChange);

	def _onChange(self, pin, value):
		"""Internal handler for when the value changes"""
		if self.value is not value:
			self.value = value;
			for fn in self.callbacks:
				fn(value);

	def addCallback(self, fn):
		self.callbacks.append(fn);

class ToggleSensorPair:
	"""Class that wraps up the behaviour of two toggle switches working in sided pair"""

	def __init__(self, config, gpio):
		"""Sets up a sensor pair"""
		self.gpio = gpio;
		self.configuration = config;
		self.leftValue = None;
		self.rightValue = None;
		self.callbacks = [];
		self._consumeConfiguration();

	def _consumeConfiguration(self):
		"""Handles the configuration"""
		self.left = ToggleSensor(self.configuration.left, self.gpio);
		self.right = ToggleSensor(self.configuration.right, self.gpio);
		self.left.addCallback(self._onLeftChange);
		self.right.addCallback(self._onRightChange);

	def _onLeftChange(self, value):
		"""When the left value changes"""
		self.leftValue = value;
		self._callCallbacks();	

	def _onRightChange(self, value):
		"""When the right value changes"""
		self.rightValue = value;
		self._callCallbacks();

	def _callCallbacks(self):
		for fn in self.callbacks:
			fn(self.leftValue, self.rightValue);

	def addCallback(self, fn):
		self.callbacks.append(fn);
