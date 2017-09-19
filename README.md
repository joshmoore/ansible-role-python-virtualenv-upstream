Python Virtualenv Upstream
==========================

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
        - role: openmicroscopy.python-virtualenv-upstream
          python_virtualenv_upstream_venv: /opt/test-venv
          python_virtualenv_upstream_packages:
            - omego
            - scc


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk
