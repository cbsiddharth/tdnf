#
# Copyright (C) 2019 VMware, Inc. All Rights Reserved.
#
# Licensed under the GNU General Public License v2 (the "License");
# you may not use this file except in compliance with the License. The terms
# of the License are located in the COPYING file of this distribution.
#
#   Author: Siddharth Chandrasekaran <csiddharth@vmware.com>

import re
import pytest

@pytest.fixture(scope='module', autouse=True)
def setup_test(utils):
    yield
    teardown_test(utils)

def teardown_test(utils):
    pass

def get_git_version(utils):
    ret = utils.run([ 'git', 'describe', '--tags', '--abbrev=0' ])
    assert(ret['retval'] == 0)
    assert(len(ret['stdout']) == 1)

    version = '0.0.0' # invalid_version
    capture = re.match(r'^(\d+\.\d+\.\d+)', ret['stdout'][0])
    if capture:
        version = capture.groups()[0]
    return version

def get_tdnf_version(utils):
    ret = utils.run([ 'tdnf', '--version' ])
    assert(ret['retval'] == 0)
    assert(len(ret['stdout']) == 1)
    return ret['stdout'][0].replace('tdnf: ', '')

def test_version_xyz_notation(utils):
    tdnf_version = get_tdnf_version(utils)
    assert(re.match(r'^\d+\.\d+\.\d+', tdnf_version) != None)

def test_version_from_git_tag(utils):
    git_version = get_git_version(utils)
    tdnf_version = get_tdnf_version(utils)
    assert(tdnf_version == git_version)
