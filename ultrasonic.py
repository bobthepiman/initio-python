import time

class InitioUltrasonic:
	"""Class that manages ultrasonic sensor"""

	MAX_DISTANCE = 999;

	def __init__(self, config, gpio):
		"""Initialises the ultrasonic sensor"""
		self.configuration = config;
		self.gpio = gpio;

	def query(self):
	        measurements = [0.0, 0.0, 0.0, 0.0, 0.0];

	        for k in range(5):
			# Set port as output
			self.gpio.setAsOutput(self.configuration.port);

			# Send a pulse
			self.gpio.setPin(self.configuration.port, True);
	                time.sleep(0.00001);
			self.gpio.setPin(self.configuration.port, False);
	                timeSent = time.time();

			# set port as input
			self.gpio.setAsInput(self.configuration.port);

			# Wait for transition to 1
	                firstTransition = timeSent;
	                while ((self.gpio.getPin(self.configuration.port) == 0) and ((firstTransition - timeSent) < 0.02)):
	                        firstTransition = time.time();
	                firstTransition = time.time();
	                
			# Wait for transition to 0
			secondTransition = firstTransition;
	                while ((self.gpio.getPin(self.configuration.port) == 1) and ((secondTransition - firstTransition) < 0.02)):
	                        secondTransition = time.time();
	                secondTransition = time.time();
	
			# Compute distance
	                pulseDuration = secondTransition - firstTransition;
        	        distance = pulseDuration*343/2*100;
	                measurements[k] = distance;
        
		# The final distance is the mean of the middle 3
		sortedMeasurements = sorted(measurements);        
		averageDistance = (sortedMeasurements[1] + sortedMeasurements[2] + sortedMeasurements[3])/3;                

	        if (averageDistance > 280):
			return self.MAX_DISTANCE;
	        if (averageDistance < 2): 
			return 1;
                        
	        return averageDistance;
