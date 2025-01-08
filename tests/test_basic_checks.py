# SPDX-License-Identifier: MPL-2.0
# Copyright 2024, ASAM e.V.
# This Source Code Form is subject to the terms of the Mozilla
# Public License, v. 2.0. If a copy of the MPL was not distributed
# with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

import os
import pytest
import test_utils
from qc_baselib import Result, IssueSeverity, StatusType
from qc_openmaterial.checks import basic_checker


def test_valid_xml_document_positive(
    monkeypatch,
) -> None:
    base_path = "tests/data/valid_xml_document/"
    target_file_name = f"xml.valid_xml_document.positive.openmaterial"
    target_file_path = os.path.join(base_path, target_file_name)

    test_utils.create_test_config(target_file_path)

    test_utils.launch_main(monkeypatch)

    result = Result()
    result.load_from_file(test_utils.REPORT_FILE_PATH)

    assert (
        result.get_checker_status(basic_checker.valid_xml_document.CHECKER_ID)
        == StatusType.COMPLETED
    )
    assert (
        len(result.get_issues_by_rule_uid("asam.net:openmaterial:1.0.0:xml.valid_xml_document"))
        == 0
    )

    test_utils.cleanup_files()


def test_valid_xml_document_negative(
    monkeypatch,
) -> None:
    base_path = "tests/data/valid_xml_document/"
    target_file_name = f"xml.valid_xml_document.negative.openmaterial"
    target_file_path = os.path.join(base_path, target_file_name)

    test_utils.create_test_config(target_file_path)

    test_utils.launch_main(monkeypatch)

    result = Result()
    result.load_from_file(test_utils.REPORT_FILE_PATH)

    assert (
        result.get_checker_status(basic_checker.valid_xml_document.CHECKER_ID)
        == StatusType.COMPLETED
    )

    xml_doc_issues = result.get_issues_by_rule_uid(
        "asam.net:openmaterial:1.0.0:xml.valid_xml_document"
    )
    assert len(xml_doc_issues) == 1
    assert xml_doc_issues[0].level == IssueSeverity.ERROR
    test_utils.cleanup_files()


def test_parametric_input_xodr(
    monkeypatch,
) -> None:
    base_path = "tests/data/parametric_input_xodr/"
    target_file_name = f"CloseVehicleCrossing.openmaterial"
    target_file_path = os.path.join(base_path, target_file_name)

    test_utils.create_test_config(target_file_path)

    test_utils.launch_main(monkeypatch)

    result = Result()
    result.load_from_file(test_utils.REPORT_FILE_PATH)

    assert result.all_checkers_completed() == True
    assert result.get_issue_count() == 0
    test_utils.cleanup_files()


def test_parametric_entity_ref(
    monkeypatch,
) -> None:
    base_path = "tests/data/parametric_entity_ref/"
    target_file_name = f"CutIn.openmaterial"
    target_file_path = os.path.join(base_path, target_file_name)

    test_utils.create_test_config(target_file_path)

    test_utils.launch_main(monkeypatch)

    result = Result()
    result.load_from_file(test_utils.REPORT_FILE_PATH)

    assert result.all_checkers_completed() == True
    assert result.get_issue_count() == 0
    test_utils.cleanup_files()


def test_parameter_declaration_with_expression(
    monkeypatch,
) -> None:
    base_path = "tests/data/parameter_declaration_with_expression/"
    target_file_name = f"VehicleCatalog.openmaterial"
    target_file_path = os.path.join(base_path, target_file_name)

    test_utils.create_test_config(target_file_path)

    test_utils.launch_main(monkeypatch)

    result = Result()
    result.load_from_file(test_utils.REPORT_FILE_PATH)

    assert result.get_issue_count() == 0
    test_utils.cleanup_files()


def test_root_tag_is_openmaterial_positive(
    monkeypatch,
) -> None:
    base_path = "tests/data/root_tag_is_openmaterial/"
    target_file_name = f"positive.openmaterial"
    target_file_path = os.path.join(base_path, target_file_name)

    test_utils.create_test_config(target_file_path)

    test_utils.launch_main(monkeypatch)

    result = Result()
    result.load_from_file(test_utils.REPORT_FILE_PATH)

    assert (
        result.get_checker_status(basic_checker.root_tag_is_openmaterial.CHECKER_ID)
        == StatusType.COMPLETED
    )

    assert (
        len(
            result.get_issues_by_rule_uid(
                "asam.net:openmaterial:1.0.0:xml.root_tag_is_openmaterial"
            )
        )
        == 0
    )

    test_utils.cleanup_files()


def test_root_tag_is_openmaterial_negative(
    monkeypatch,
) -> None:
    base_path = "tests/data/root_tag_is_openmaterial/"
    target_file_name = f"negative.openmaterial"
    target_file_path = os.path.join(base_path, target_file_name)

    test_utils.create_test_config(target_file_path)

    test_utils.launch_main(monkeypatch)

    result = Result()
    result.load_from_file(test_utils.REPORT_FILE_PATH)

    assert (
        result.get_checker_status(basic_checker.valid_xml_document.CHECKER_ID)
        == StatusType.COMPLETED
    )

    xml_doc_issues = result.get_issues_by_rule_uid(
        "asam.net:openmaterial:1.0.0:xml.root_tag_is_openmaterial"
    )
    assert len(xml_doc_issues) == 1
    assert xml_doc_issues[0].level == IssueSeverity.ERROR
    test_utils.cleanup_files()


def test_fileheader_is_present_positive(
    monkeypatch,
) -> None:
    base_path = "tests/data/fileheader_is_present/"
    target_file_name = f"positive.openmaterial"
    target_file_path = os.path.join(base_path, target_file_name)

    test_utils.create_test_config(target_file_path)

    test_utils.launch_main(monkeypatch)

    result = Result()
    result.load_from_file(test_utils.REPORT_FILE_PATH)

    assert (
        result.get_checker_status(basic_checker.fileheader_is_present.CHECKER_ID)
        == StatusType.COMPLETED
    )

    assert (
        len(
            result.get_issues_by_rule_uid(
                "asam.net:openmaterial:1.0.0:xml.fileheader_is_present"
            )
        )
        == 0
    )

    test_utils.cleanup_files()


def test_fileheader_is_present_negative(
    monkeypatch,
) -> None:
    base_path = "tests/data/fileheader_is_present/"
    target_file_name = f"negative.openmaterial"
    target_file_path = os.path.join(base_path, target_file_name)

    test_utils.create_test_config(target_file_path)

    test_utils.launch_main(monkeypatch)

    result = Result()
    result.load_from_file(test_utils.REPORT_FILE_PATH)

    assert (
        result.get_checker_status(basic_checker.fileheader_is_present.CHECKER_ID)
        == StatusType.COMPLETED
    )

    xml_doc_issues = result.get_issues_by_rule_uid(
        "asam.net:openmaterial:1.0.0:xml.fileheader_is_present"
    )
    assert len(xml_doc_issues) == 1
    assert xml_doc_issues[0].level == IssueSeverity.ERROR
    test_utils.cleanup_files()


def test_version_is_defined_positive(
    monkeypatch,
) -> None:
    base_path = "tests/data/version_is_defined/"
    target_file_name = f"positive.openmaterial"
    target_file_path = os.path.join(base_path, target_file_name)

    test_utils.create_test_config(target_file_path)

    test_utils.launch_main(monkeypatch)

    result = Result()
    result.load_from_file(test_utils.REPORT_FILE_PATH)

    assert (
        result.get_checker_status(basic_checker.version_is_defined.CHECKER_ID)
        == StatusType.COMPLETED
    )

    assert (
        len(result.get_issues_by_rule_uid("asam.net:openmaterial:1.0.0:xml.version_is_defined"))
        == 0
    )

    test_utils.cleanup_files()


def test_version_is_defined_negative_attr(
    monkeypatch,
) -> None:
    base_path = "tests/data/version_is_defined/"
    target_file_name = f"negative_no_attr.openmaterial"
    target_file_path = os.path.join(base_path, target_file_name)

    test_utils.create_test_config(target_file_path)

    test_utils.launch_main(monkeypatch)

    result = Result()
    result.load_from_file(test_utils.REPORT_FILE_PATH)

    assert (
        result.get_checker_status(basic_checker.version_is_defined.CHECKER_ID)
        == StatusType.COMPLETED
    )

    xml_doc_issues = result.get_issues_by_rule_uid(
        "asam.net:openmaterial:1.0.0:xml.version_is_defined"
    )
    assert len(xml_doc_issues) == 1
    assert xml_doc_issues[0].level == IssueSeverity.ERROR
    test_utils.cleanup_files()


def test_version_is_defined_negative_type(
    monkeypatch,
) -> None:
    base_path = "tests/data/version_is_defined/"
    target_file_name = f"negative_no_type.openmaterial"
    target_file_path = os.path.join(base_path, target_file_name)

    test_utils.create_test_config(target_file_path)

    test_utils.launch_main(monkeypatch)

    result = Result()
    result.load_from_file(test_utils.REPORT_FILE_PATH)

    assert (
        result.get_checker_status(basic_checker.version_is_defined.CHECKER_ID)
        == StatusType.COMPLETED
    )

    xml_doc_issues = result.get_issues_by_rule_uid(
        "asam.net:openmaterial:1.0.0:xml.version_is_defined"
    )
    assert len(xml_doc_issues) == 1
    assert xml_doc_issues[0].level == IssueSeverity.ERROR
    test_utils.cleanup_files()
