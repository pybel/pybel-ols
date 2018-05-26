PyBEL-OLS |build| |coverage| |documentation|
============================================
A PyBEL [1]_ extension for building BEL resources with the EBI [2]_ Ontology
Lookup Service.

Installation |pypi_version| |python_versions| |pypi_license|
------------------------------------------------------------
Get the Latest
~~~~~~~~~~~~~~~
Download the most recent code from `GitHub <https://github.com/pybel/pybel-ols>`_ with:

.. code-block:: sh

   $ python3 -m pip install git+https://github.com/pybel/pybel-ols.git

For Developers
~~~~~~~~~~~~~~
Clone the repository from `GitHub <https://github.com/pybel/pybel-ols>`_ and install in editable mode with:

.. code-block:: sh

   $ git clone https://github.com/pybel/pybel-ols.git
   $ cd bio2bel
   $ python3 -m pip install -e .

References
----------
.. [1] Hoyt, C. T., *et al.* (2017). `PyBEL: a Computational Framework for Biological Expression Language
       <https://doi.org/10.1093/bioinformatics/btx660>`_. Bioinformatics, 34(December), 1–2.

.. [2] Cote, R., *et al.* (2006). `The Ontology Lookup Service, a lightweight cross-platform tool for controlled
       vocabulary queries <https://doi.org/10.1186/1471-2105-7-97>`_. BMC Bioinformatics, 7, 1–7.

.. |build| image:: https://travis-ci.org/pybel/pybel-ols.svg?branch=master
    :target: https://travis-ci.org/pybel/pybel-ols
    :alt: Build Status

.. |coverage| image:: https://codecov.io/gh/pybel/pybel-ols/coverage.svg?branch=master
    :target: https://codecov.io/gh/pybel/pybel-ols?branch=master
    :alt: Coverage Status

.. |documentation| image:: https://readthedocs.org/projects/pybel-ols/badge/?version=latest
    :target: https://pybel.readthedocs.io/projects/ols/en/latest/?badge=latest
    :alt: Documentation Status

.. |climate| image:: https://codeclimate.com/github/pybel/pybel-ols/badges/gpa.svg
    :target: https://codeclimate.com/github/pybel/pybel-ols
    :alt: Code Climate

.. |python_versions| image:: https://img.shields.io/pypi/pyversions/pybel-ols.svg
    :alt: Stable Supported Python Versions

.. |pypi_version| image:: https://img.shields.io/pypi/v/pybel-ols.svg
    :alt: Current version on PyPI

.. |pypi_license| image:: https://img.shields.io/pypi/l/pybel-ols.svg
    :alt: MIT License
