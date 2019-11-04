# Digital Land local plan collection

[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/digital-land/local-plan/blob/master/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://black.readthedocs.io/en/stable/)

A prototype of a national dataset of local plan documents published by Local Planning Authorities.

The list of documents collected is available in the dataset [dataset/local-plan.csv](dataset/local-plan.csv).

The source list of documents collected is kept and maintained using the [local plans prototype](https://local-plans-prototype.herokuapp.com/) -- [source](https://github.com/digital-land/local-plans-prototype).

The [collection](collection) directory contains:

* [collection/log](collection/log) -- log entries by date/URL (sha256)
* [collection/resource](collection/resource) -- collected files by contents (sha256)
* [index.json](collection/index.json) -- an index into the collection, used to build our [catalog](https://digital-land.github.io/catalog/) and other pages.

# Updating the collection

We recommend working in [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) before installing the python dependencies:

    $ make init
    $ make

# Licence

The software in this project is open source and covered by LICENSE file.

Individual datasets copied into this repository may have specific copyright and licensing, otherwise all content and data in this repository is
[© Crown copyright](http://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/copyright-and-re-use/crown-copyright/)
and available under the terms of the [Open Government 3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) licence.
