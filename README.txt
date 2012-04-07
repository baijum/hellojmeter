Hello JMeter
============

Note: This instruction only works in a GNU/Linux system where Java is
installed

This package download and install JMeter with a sample application written in
Flask.

1. Clone the repository locally

   ::

     git clone git://github.com/baijum/hellojmeter.git

2. Install Python

   ::

   cd hellojmeter
   ./installpy27.sh

3. Bootstrap buildout

   ::

     ./usr/bin/python bootstrap.py -d

4. Run buildout

   ::

     ./bin/buildout

Running sample application
--------------------------

To run sample application::

   ./bin/hellojmeterctl

Running JMeter
--------------

To run JMeter::

  ./apache-jmeter-2.6/bin/jmeter


Links
-----

http://www.youtube.com/watch?v=7rO6TtO-QrI
