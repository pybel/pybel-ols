# -*- coding: utf-8 -*-

"""A PyBEL extension for building BEL resources with the EBI Ontology Lookup Service.

Citation
--------
If you use PyBEL in your work, please cite [1]_:

.. [1] Hoyt, C. T., *et al.* (2017). `PyBEL: a Computational Framework for Biological Expression Language <https://doi.org/10.1093/bioinformatics/btx660>`_. Bioinformatics, 34(December), 1–2.

Installation
------------
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
"""

from .ols_utils import (
    OlsAnnotationOntology, OlsConstrainedAnnotationOntology, OlsConstrainedNamespaceOntology,
    OlsConstrainedOntology, OlsNamespaceOntology, OlsOntology,
)

__all__ = [
    'OlsOntology',
    'OlsNamespaceOntology',
    'OlsAnnotationOntology',
    'OlsConstrainedOntology',
    'OlsConstrainedNamespaceOntology',
    'OlsConstrainedAnnotationOntology',
]

__version__ = '0.0.1-dev'

__title__ = 'pybel_ols'
__description__ = 'A PyBEL extension for building BEL resources with the EBI Ontology Lookup Service'
__url__ = 'https://github.com/pybel/pybel-ols'

__author__ = 'Charles Tapley Hoyt'
__email__ = 'charles.hoyt@scai.fraunhofer.de'

__license__ = 'MIT License'
__copyright__ = 'Copyright (c) 2018 Charles Tapley Hoyt'
