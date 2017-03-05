#!/usr/bin/python3

## TASK
# Write a program that implements message flow from the top layer to the bottom layer of the 7-layer protocol model. Your program should include a separate protocol function for each layer. Protocol headers are sequence up to 64 characters. Each protocol function has two parameters: a message passed from the higher layer protocol (a char buffer) and the size of the message. This function attaches its header in front of the message, prints the new message on the standard output, and then invokes the protocol function of the lower-layer protocol. Program input is an application message (a sequence of 80 characters or less).

## Implementation

# layer is object with methods
class Layer:
	def __init__(self):
		self.level = 997
		self.message = None
		self.size_of_message = None

	def protocol(self):
		return [self.level, self.message, self.size_of_message]

	def packet(self, message):
		self.message = str(len(message)) + message
		self.size_of_message = len(message)
		while self.level > 1:
			self.level-=1
			self.packet(self.message)
			packet = self.protocol()
			print(packet)

	# def message_flow(message, )



if __name__ == '__main__':
	l = Layer()
	l.protocol()
	l.packet('message')
	l.protocol()
	l.packet('2message2')
	