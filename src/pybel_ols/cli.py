# -*- coding: utf-8 -*-

"""Command line interface for PyBEL-OLS.

Building Resources via OLS
--------------------------
Namespaces, annotations, and hierarchies can be created by querying the ontologies stored in the EBI Ontology Lookup
Service.

Namespace
~~~~~~~~~
In order to convert UBERON to a namespace, the keyword inside the OLS, ``uberon`` is used as well as specifying the
encoding type and the applicability domain. The ``-o`` option can be used to specify which file to write the output
to.

.. code-block:: bash

    $ pybel-tools namespace from_ols uberon --domain Other --encoding A

Alternatively, the '-b' option can be used to specify an alternate OLS instance

.. code-block:: bash

    $ pybel-tools namespace from_ols uberon --domain Other --encoding A -b https://localhost/ols
"""

import sys

import click

from pybel.constants import BELNS_ENCODING_STR, NAMESPACE_DOMAIN_OTHER, NAMESPACE_DOMAIN_TYPES
from .ols_utils import BASE_URL, OlsAnnotationOntology, OlsNamespaceOntology


@click.group()
def main():
    """Run the PyBEL-OLS Command Line Interface."""


@main.command()
@click.argument('ontology')
@click.option('-e', '--encoding', default=BELNS_ENCODING_STR, help='The BEL Namespace encoding')
@click.option('-d', '--domain', type=click.Choice(NAMESPACE_DOMAIN_TYPES), default=NAMESPACE_DOMAIN_OTHER)
@click.option('-b', '--ols-base-url', default=BASE_URL, help='Default: {}'.format(BASE_URL))
@click.option('-o', '--output', type=click.File('w'), default=sys.stdout,
              help='The file to output to. Defaults to standard out.')
def namespace_from_ols(ontology, domain, encoding, ols_base_url, output):
    """Create a namespace from the ontology lookup service given the internal ontology keyword."""
    ont = OlsNamespaceOntology(ontology, domain, encoding=encoding, ols_base=ols_base_url)
    ont.write_namespace(output)


@main.command()
@click.argument('ontology')
@click.option('-b', '--ols-base-url', default=BASE_URL, help='Default: {}'.format(BASE_URL))
@click.option('-o', '--output', type=click.File('w'), default=sys.stdout,
              help='The file to output to. Defaults to standard out.')
def annotation_from_ols(ontology, ols_base_url, output):
    """Create an annotation from the ontology lookup service given the internal ontology keyword."""
    ont = OlsAnnotationOntology(ontology, ols_base=ols_base_url)
    ont.write_annotation(output)


@main.command()
@click.argument('ontology')
@click.argument('domain')
@click.option('--function')
@click.option('--encoding')
@click.option('-b', '--ols-base')
@click.option('-o', '--output', type=click.File('w'), default=sys.stdout)
def hierarchy_from_ols(ontology, domain, function, encoding, ols_base, output):
    """Create a hierarchy from the ontology lookup service."""
    ont = OlsNamespaceOntology(ontology, domain, bel_function=function, encoding=encoding, ols_base=ols_base)
    ont.write_namespace_hierarchy(output)


if __name__ == '__main__':
    main()
