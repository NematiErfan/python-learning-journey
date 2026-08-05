# FPFA Lab Manager

"""
FPGA class definition.
Represents FPGA hardware devices and their behaviors.
"""

class FPGA:

	def __init__(self,name,vendor,frequency,power,luts):

		self.name= name
		self.vendor = vendor
		self.frequency = frequency
		self.power = power
		self.luts = luts
		self.configured = False

	def configure(self):

		self.configured = True

	def reset(self):

		self.configured = False

	def increase_frequency(self,step):

		self.frequency += step

	def low_power_mode(self):

		self.power = self.power / 2

	def __len__(self):

		return self.luts

	def __str__(self):

		if self.configured:
			return f"FPGA {self.name} produced by {self.vendor} present with {self.frequency} Mhz Frequency and {self.power} W of Power, it has {self.luts} number of LUTs, Done! FPGA Configured"
		else:
			return f"FPGA {self.name} produced by {self.vendor} present with {self.frequency} Mhz Frequency and {self.power} W of Power, it has {self.luts} number of LUTs, FPGA Not Configured!"