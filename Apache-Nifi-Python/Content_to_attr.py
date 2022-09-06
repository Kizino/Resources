from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import InputStreamCallback

# Define a subclass of InputStreamCallback for use in session.read()
class PyInputStreamCallback(InputStreamCallback):
	def __init__(self):
		self.content = None
	def process(self, inputStream):
		self.content = IOUtils.toString(inputStream, StandardCharsets.UTF_8)

flowFile = session.get()
if(flowFile != None):
	ff_callback = PyInputStreamCallback()
	session.read(flowFile, ff_callback)

	flowFile = session.putAttribute(flowFile, "attr_name", ff_callback.content)
	session.transfer(flowFile, REL_SUCCESS)
