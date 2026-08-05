# FPGA Lab Manager
# FPGALab Class

"""
FPGALab class.
Manages a collection of FPGA objects.
"""

from fpga import FPGA

class FPGALab:

	def __init__(self,name):

		self.name = name
		self.fpgas = []

	def add_fpga(self,fpga):

		if isinstance(fpga, FPGA):
			self.fpgas.append(fpga)
			print("New FPGA Added!")
		else:
			print("Only FPGA object are allowed")

	def remove_fpga(self,fpga):

		if fpga in self.fpgas:
			self.fpgas.remove(fpga)
			print("Selected FPGA Removed")
		else:
			print("Selected FPGA Not Found")

	def find_fpga(self,name):

		for fpga in self.fpgas:

			if fpga.name == name:
				return fpga

		return None

	def show_all(self):

		for fpga in self.fpgas:
			print(fpga)

	def total_luts(self):

		total = 0

		for fpga in self.fpgas:
			
			total += len(fpga)
		
		return total

	def power_report(self):

		total = 0

		for fpga in self.fpgas:

			print (f"{fpga.name} , {fpga.power} W")

			total += fpga.power

		print (f"Total Power: {total} W")
		return total