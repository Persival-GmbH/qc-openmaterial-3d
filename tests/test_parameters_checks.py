# SPDX-License-Identifier: MPL-2.0
# Copyright 2024, ASAM e.V.
# This Source Code Form is subject to the terms of the Mozilla
# Public License, v. 2.0. If a copy of the MPL was not distributed
# with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

import os
import pytest
import test_utils
from qc_baselib import Result, IssueSeverity, StatusType
from qc_openmaterial.checks import parameters_checker


def test_valid_parameter_declaration_in_catalogs_positive(
    monkeypatch,
) -> None:
    base_path = "tests/data/valid_parameter_declaration_in_catalogs/"
    target_file_name = (
        f"parameters.valid_parameter_declaration_in_catalogs.positive.openmaterial"
    )
    target_file_path = os.path.join(base_path, target_file_name)

    test_utils.create_test_config(target_file_path)

    test_utils.launch_main(monkeypatch)

    result = Result()
    result.load_from_file(test_utils.REPORT_FILE_PATH)

    assert (
        result.get_checker_status(
            parameters_checker.valid_parameter_declaration_in_catalogs.CHECKER_ID
        )
        == StatusType.COMPLETED
    )

    assert (
        len(
            result.get_issues_by_rule_uid(
                "asam.net:openmaterial:1.2.0:parameters.valid_parameter_declaration_in_catalogs"
            )
        )
        == 0
    )

    test_utils.cleanup_files()


def test_valid_parameter_declaration_in_catalogs_negative(
    monkeypatch,
) -> None:
    base_path = "tests/data/valid_parameter_declaration_in_catalogs/"
    target_file_name = (
        f"parameters.valid_parameter_declaration_in_catalogs.negative.openmaterial"
    )
    target_file_path = os.path.join(base_path, target_file_name)

    test_utils.create_test_config(target_file_path)

    test_utils.launch_main(monkeypatch)

    result = Result()
    result.load_from_file(test_utils.REPORT_FILE_PATH)

    assert (
        result.get_checker_status(
            parameters_checker.valid_parameter_declaration_in_catalogs.CHECKER_ID
        )
        == StatusType.COMPLETED
    )

    parameters_issues = result.get_issues_by_rule_uid(
        "asam.net:openmaterial:1.2.0:parameters.valid_parameter_declaration_in_catalogs"
    )
    assert len(parameters_issues) == 1
    assert parameters_issues[0].level == IssueSeverity.ERROR
    test_utils.cleanup_files()


def test_valid_parameter_declaration_in_catalogs_negative_no_default(
    monkeypatch,
) -> None:
    base_path = "tests/data/valid_parameter_declaration_in_catalogs/"
    target_file_name = (
        f"parameters.valid_parameter_declaration_in_catalogs.negative_no_default.openmaterial"
    )
    target_file_path = os.path.join(base_path, target_file_name)

    test_utils.create_test_config(target_file_path)

    test_utils.launch_main(monkeypatch)

    result = Result()
    result.load_from_file(test_utils.REPORT_FILE_PATH)

    assert (
        result.get_checker_status(
            parameters_checker.valid_parameter_declaration_in_catalogs.CHECKER_ID
        )
        == StatusType.COMPLETED
    )

    parameters_issues = result.get_issues_by_rule_uid(
        "asam.net:openmaterial:1.2.0:parameters.valid_parameter_declaration_in_catalogs"
    )
    assert len(parameters_issues) == 1
    assert parameters_issues[0].level == IssueSeverity.ERROR
    test_utils.cleanup_files()


def test_valid_parameter_declaration_in_catalogs_negative_multiple(
    monkeypatch,
) -> None:
    base_path = "tests/data/valid_parameter_declaration_in_catalogs/"
    target_file_name = (
        f"parameters.valid_parameter_declaration_in_catalogs.negative.multiple.openmaterial"
    )
    target_file_path = os.path.join(base_path, target_file_name)

    test_utils.create_test_config(target_file_path)

    test_utils.launch_main(monkeypatch)

    result = Result()
    result.load_from_file(test_utils.REPORT_FILE_PATH)

    assert (
        result.get_checker_status(
            parameters_checker.valid_parameter_declaration_in_catalogs.CHECKER_ID
        )
        == StatusType.COMPLETED
    )

    parameters_issues = result.get_issues_by_rule_uid(
        "asam.net:openmaterial:1.2.0:parameters.valid_parameter_declaration_in_catalogs"
    )
    assert len(parameters_issues) == 2
    assert parameters_issues[0].level == IssueSeverity.ERROR
    assert parameters_issues[1].level == IssueSeverity.ERROR
    assert "maxSteering" in parameters_issues[0].locations[0].description
    assert "trackWidth" in parameters_issues[1].locations[0].description
    test_utils.cleanup_files()
