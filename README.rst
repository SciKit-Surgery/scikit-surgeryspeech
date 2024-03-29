scikit-surgeryspeech
===============================

.. image:: https://github.com/SciKit-Surgery/scikit-surgeryspeech/raw/master/weiss_logo.png
   :height: 128px
   :width: 128px
   :target: https://github.com/SciKit-Surgery/scikit-surgeryspeech
   :alt: Logo

|

.. image:: https://github.com/SciKit-Surgery/scikit-surgeryspeech/workflows/.github/workflows/ci.yml/badge.svg
   :target: https://github.com/SciKit-Surgery/scikit-surgeryspeech/actions
   :alt: GitHub Actions CI status

.. image:: https://coveralls.io/repos/github/SciKit-Surgery/scikit-surgeryspeech/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/SciKit-Surgery/scikit-surgeryspeech?branch=master
    :alt: Test coverage

.. image:: https://readthedocs.org/projects/scikit-surgeryspeech/badge/?version=latest
    :target: http://scikit-surgeryspeech.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg
   :target: CODE_OF_CONDUCT.md

.. image:: https://img.shields.io/twitter/follow/scikit_surgery?style=social
   :target: https://twitter.com/scikit_surgery?ref_src=twsrc%5Etfw
   :alt: Follow scikit_surgery on twitter


Author: Kim-Celine Kahl

scikit-surgeryspeech is part of the `SciKit-Surgery`_ software project, developed at the `Wellcome EPSRC Centre for Interventional and Surgical Sciences`_, part of `University College London (UCL)`_.

scikit-surgeryspeech supports Python 3.6.

scikit-surgeryspeech is a project which runs the `Python Speech Recognition API`_ in the background listening
for a specific command. After saying the keyword you can say different commands, which get
converted to QT Signals.

The speech recognition is done by the `Google Cloud API`_, you have to get the credentials to use it or change the recognition service.

Keyword detection is done by the `Porcupine API`_. This should be have been installed automatically via the pvporcupine dependency

Please explore the project structure, and implement your own functionality.

Example usage
-------------

To run an example, just start

::

    sksurgeryspeech.py -c example_config.json


The config file should define the paths for the porcupine library and the Google Cloud API if you are using it.

You can then say the keyword depending on the Porcupine keyword file you chose and afterwards a command. The command "quit" exits the application.

Note: each time you have already entered a command, you need to say the keyword again to trigger the listening to commands.

Developing
----------

Cloning
^^^^^^^

You can clone the repository using the following command:

::

    git clone https://github.com/SciKit-Surgery/scikit-surgeryspeech

If you have problems running the application, you might need to install portaudio

Mac
::

    brew install portaudio

Ubuntu
::

    sudo apt-get install libasound-dev portaudio19-dev

If you're going to try sphinx might need to install pulseaudo-dev

Ubuntu
::

    sudo apt-get install swig libpulse-dev


Set up the Porcupine keyword detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Then, you have to set the following variables in the configuration file

::
    
   "porcupine dynamic library path" : ".tox/py37/lib/python3.7/site-packages/pvporcupine/lib/linux/x86_64/libpv_porcupine.so",
	"porcupine model file path" : ".tox/py37/lib/python3.7/site-packages/pvporcupine/lib/common/porcupine_params.pv",
	"porcupine keyword file" : [".tox/py37/lib/python3.7/site-packages/pvporcupine/resources/keyword_files/linux/jarvis_linux.ppn"],
       

You can also `generate your own keyword files`_

If you are using the speech recognition service within your own application, you have to start a background thread which calls the method to listen to the keyword over and over again.

You can find an example how to create such a thread in the sksurgeryspech_demo.py

Use the Google Cloud speech recognition service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`Google Cloud API is set up correctly`:

To use the Google Cloud speech recognition service, you need to `get the credentials`_ first. After signing up, you
should get a json file with your credentials. Download this file and add add it to the configuration file

::

    "google credentials file" : "snappy-speech-6ff24bf3e262.json",

To the path of your json file. You should then be able to run the application.


Change speech recognition service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can try different speech recognition services by changing the recogniser entry in the config file. 
sphinx, google and google_cloud have all been tested, other options are possible but may not be implemented yet.

::

    "recogniser" : "sphinx"
    "recogniser" : "google" 
    "recogniser" : "google_cloud"
    "recogniser" : "wit"
    "recogniser" : "bing"
    "recogniser" : "azure"
    "recogniser" : "houndify"
    "recogniser" : "ibm"

Python development
^^^^^^^^^^^^^^^^^^

This project uses tox. Start with a clean python environment, then do:

::

    pip install tox
    tox

and the commands that are run can be found in tox.ini.


Installing
----------

You can pip install directly from the repository as follows:

::

    pip install git+https://github.com/SciKit-Surgery/scikit-surgeryspeech



Contributing
^^^^^^^^^^^^

Please see the `contributing guidelines`_.


Useful links
^^^^^^^^^^^^

* `Source code repository`_


Licensing and copyright
-----------------------

Copyright 2019 University College London.
scikit-surgeryspeech is released under the BSD-3 license. Please see the `license file`_ for details.


Acknowledgements
----------------

Supported by `Wellcome`_ and `EPSRC`_.


.. _`Wellcome EPSRC Centre for Interventional and Surgical Sciences`: http://www.ucl.ac.uk/weiss
.. _`source code repository`: https://github.com/SciKit-Surgery/scikit-surgeryspeech
.. _`SciKit-Surgery`: https://github.com/SciKit-Surgery/
.. _`University College London (UCL)`: http://www.ucl.ac.uk/
.. _`Wellcome`: https://wellcome.ac.uk/
.. _`EPSRC`: https://www.epsrc.ac.uk/
.. _`contributing guidelines`: https://github.com/SciKit-Surgery/scikit-surgeryspeechblob/master/CONTRIBUTING.rst
.. _`license file`: https://github.com/SciKit-Surgery/scikit-surgeryspeechblob/master/LICENSE
.. _`Python Speech Recognition API`: https://pypi.org/project/SpeechRecognition/
.. _`Google Cloud API`: https://cloud.google.com/speech-to-text/
.. _`Porcupine API`: https://github.com/Picovoice/Porcupine
.. _`generate your own keyword files`: https://github.com/Picovoice/Porcupine/tree/master/tools/optimizer
.. _`get the credentials`: https://console.cloud.google.com/freetrial/signup/tos?_ga=2.263649484.-1718611742.1562839990
