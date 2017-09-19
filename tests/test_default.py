import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_virtualenv_created(File):
    assert File('/opt/test-venv/bin/python').exists


def test_virtualenv_packages(Command):
    out = Command.check_output('/opt/test-venv/bin/pip list')
    packages = [s.split()[0] for s in out.split('\n')]
    assert 'scc' in packages
    assert 'omego' in packages


@pytest.mark.parametrize("cmd", ["omego", "scc"])
def test_virtualenv_installed_packages(Command, cmd):
    Command.check_output("/opt/test-venv/bin/%s version" % cmd)


@pytest.mark.parametrize("cmd", ["pip", "virtualenv"])
def test_no_global_virtualenv(Command, cmd):
    assert not Command.exists(cmd)
