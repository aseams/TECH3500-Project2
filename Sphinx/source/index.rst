.. Project 2 documentation master file, created by
   sphinx-quickstart on Tue Mar 30 17:04:44 2021.
   You can adapt this file completely to your liking, but it should at least contain the root `toctree` directive.

Welcome to Project 2's documentation!
=====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

enhance.py
==========
Create object to reference the neural network::

	sr = dnn_superres.DnnSuperResImpl_create()

Grab desired model, read it in, and set it to be used.::

	path = "LapSRN_x4.pb"
	sr.readModel(path)
	sr.setModel("lapsrn", 4)

Ask user for input file and read it in.::

	img = input("Input File: ")
	image = cv2.imread(img)

Do the work and print a success message::

	result = sr.upsample(image)
	path, filename = os.path.split(img)
	print("Successfully upscaled " + filename + "!")

Actually do the work and write it to a new file::

	cv2.imwrite("upscaled_" + str(filename), result)
	print("wrote upscaled_" + str(filename) + " to file")

vocabfetch.py
=============
.. automodule:: Project_2.vocabfetch
   :members: