.. pydomjudge documentation master file, created by
   sphinx-quickstart on Fri Sep 12 10:52:16 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

pydomjudge documentation
========================


A Python wrapper for the DOMJudge API. Easily interact with DOMJudge contest management systems from your Python code.

Features
--------

- Full API coverage for DOMJudge v4 endpoints
- Pydantic models for all major entities (Contest, Team, Submission, etc.)
- Simple, unified client interface (``DOMJudge``)
- Supports authentication, file uploads, and more
- Designed for scripting, automation, and integration

Planned / To Do
---------------

- Add more automatic tests and CI integration
- Expand documentation and usage examples
- Add more API endpoint coverage as DOMJudge evolves
- Improve error handling and type hints

Installation
------------

.. code-block:: bash

   pip install pydomjudge

Or clone this repository and install locally:

.. code-block:: bash

   git clone https://github.com/xivqn/pydomjudge.git
   cd pydomjudge
   pip install .

Requirements
------------

- Python 3.8+
- `DOMJudge <https://www.domjudge.org/>`_ instance (for API access)
- See ``requirements.txt`` for dependencies

Usage Example
-------------

.. code-block:: python

   from pydomjudge import DOMJudge

   dj = DOMJudge("http://localhost/domjudge", "admin", "adminpass")
   contests = dj.get_all_contests()
   for contest in contests:
       print(contest.name, contest.start_time)


.. toctree::
   :maxdepth: 3
   :caption: API Reference

   pydomjudge