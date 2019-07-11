Python Virtualenv Upstream
==========================

[![Build Status](https://travis-ci.org/ome/ansible-role-python-virtualenv-upstream.svg)](https://travis-ci.org/ome/ansible-role-python-virtualenv-upstream)
[![Ansible Role](https://img.shields.io/ansible/role/42000.svg)](https://galaxy.ansible.com/ome/python_virtualenv_upstream/)

Create a Python virtualenv using the upstream package.

This can be used when the distribution python-virtualenv package is too old.


Role Variables
--------------

All variables are optional.
- `python_virtualenv_upstream_venv`: Create/update a virtualenv in this location
- `python_virtualenv_upstream_packages`: List of packages to be installed in the virtualenv, ignored if `python_virtualenv_upstream_venv` is not set

You can leave these variables unset and create your virtualenv using the Ansible `pip` module instead, by defining the module parameter `virtualenv_command: /opt/virtualenv-setup/virtualenv/virtualenv.py`
Use this if you require more control over the virtualenv, such as versions of packages


Example Playbook
----------------

    - hosts: all
      roles:
        - role: ome.python_virtualenv_upstream
          python_virtualenv_upstream_venv: /opt/test-venv
          python_virtualenv_upstream_packages:
            - omego
            - scc


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk
