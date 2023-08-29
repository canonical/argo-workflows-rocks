# Copyright 2023 Canonical Ltd.
# See LICENSE file for licensing details.
#
# Tests for required artifacts to be present in the ROCK image.
#

from charmed_kubeflow_chisme.rock import CheckRock
from pathlib import Path

import os
import logging
import random
import pytest
import string
import subprocess
import yaml
from pytest_operator.plugin import OpsTest

@pytest.fixture()
def rock_test_env():
    """Yelds random docker container name, then cleans it up after."""
    container_name = "".join([str(i) for i in random.choices(string.ascii_lowercase, k=8)])
    yield container_name

    try:
        subprocess.run(["docker", "rm", container_name], check=True, capture_output=True)
    except Exception as error:
        print(f"Failed to remove Docker container {container_name} error: {str(error)}")


@pytest.mark.abort_on_fail
def test_rock_artefacts(ops_test: OpsTest, rock_test_env):
    """Test that all artefacts are present in the ROCK: binaries."""
    check_rock = CheckRock("rockcraft.yaml")
    container_name = rock_test_env
    LOCAL_ROCK_IMAGE = f"{check_rock.get_image_name()}:{check_rock.get_version()}"

    # verify that all artifacts are in correct locations
    try:
        subprocess.run(
            ["docker", "run", "--name", container_name, LOCAL_ROCK_IMAGE, "exec", "pebble", "ls", "/bin/argoexec"],
            check=True
        )
    except subprocess.CalledProcessError as error:
        print(f"Failed to execute docker run for container {container_name} error: {str(error)}")
        assert 0
