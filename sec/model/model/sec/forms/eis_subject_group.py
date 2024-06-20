from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from model.sec.forms.eis_common2 import (
    ContactType,
    DepositorType,
    EdgarDocumentsType,
    LiveTestType,
    ModulesSegmentType,
    NotificationType,
    SrosType,
)

__NAMESPACE__ = "http://www.sec.gov/edgar/subjectgroup"


class ComboSubmissionType(Enum):
    SC_13_D_A = "SC 13D/A"
    SC_TO_I = "SC TO-I"
    SC_TO_I_A = "SC TO-I/A"
    SC_TO_T = "SC TO-T"
    SC_TO_T_A = "SC TO-T/A"


@dataclass
class FiledByType:
    class Meta:
        name = "FILED_BY_TYPE"

    filer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectgroup",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    filer_ccc: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerCcc",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectgroup",
            "required": True,
            "length": 8,
        },
    )


@dataclass
class FlagType:
    class Meta:
        name = "FLAG_TYPE"

    confirming_copy_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "confirmingCopyFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectgroup",
            "pattern": r"true|false",
        },
    )
    return_copy_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "returnCopyFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectgroup",
            "pattern": r"true|false",
        },
    )
    override_internet_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "overrideInternetFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectgroup",
            "pattern": r"true|false",
        },
    )


@dataclass
class SubjectCompanyType:
    class Meta:
        name = "SUBJECT_COMPANY_TYPE"

    filer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectgroup",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    irs_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "irsNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectgroup",
            "pattern": r"\d{2}[\-]?\d{7}",
        },
    )
    file_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectgroup",
            "pattern": r"\d{1,3}-\d{1,8}-[a-zA-Z0-9]{1,4}|\d{1,3}-\d{1,8}",
        },
    )
    filer_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerName",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectgroup",
            "required": True,
            "min_length": 1,
            "max_length": 150,
            "pattern": r"([A-Za-z0-9\s!\\#$(),.:;=@'\-{}|/&]+)",
        },
    )
    group_name: List[str] = field(
        default_factory=list,
        metadata={
            "name": "groupName",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectgroup",
            "min_length": 1,
            "max_length": 150,
            "pattern": r"([A-Za-z0-9\s!\\#$(),.:;=@'\-{}|/&]+)",
        },
    )


class SubmissionType(Enum):
    """Type of submission you are filing.

    Choose a value from the appropriate family of Submission Types.
    """

    FWP = "FWP"
    SC_13_D = "SC 13D"
    SC_13_D_A = "SC 13D/A"
    SC_13_G = "SC 13G"
    SC_13_G_A = "SC 13G/A"
    SC_14_D9 = "SC 14D9"
    SC_14_D9_A = "SC 14D9/A"
    SC_TO_C = "SC TO-C"
    SC14_D9_C = "SC14D9C"
    SC14_D9_F = "SC14D9F"
    SC14_D9_F_A = "SC14D9F/A"


@dataclass
class ComboFormType:
    """Used to specify a different form type for a co-registrant filing.

    Choose the value from the list displayed when the arrow is selected.
    """

    class Meta:
        name = "COMBO_FORM_TYPE"

    combo_form_type: List[ComboSubmissionType] = field(
        default_factory=list,
        metadata={
            "name": "comboFormType",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectgroup",
            "max_occurs": 2,
        },
    )


@dataclass
class EdgarSubmission:
    """
    This is the root element for an EDGARLink Online submission.
    """

    class Meta:
        name = "edgarSubmission"
        namespace = "http://www.sec.gov/edgar/subjectgroup"

    schema_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemaVersion",
            "type": "Element",
            "length": 5,
        },
    )
    live_test_flag: Optional[LiveTestType] = field(
        default=None,
        metadata={
            "name": "liveTestFlag",
            "type": "Element",
            "required": True,
        },
    )
    flag: Optional[FlagType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    submission_type: Optional[SubmissionType] = field(
        default=None,
        metadata={
            "name": "submissionType",
            "type": "Element",
            "required": True,
        },
    )
    filer: Optional[FiledByType] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    combo_form_types: Optional[ComboFormType] = field(
        default=None,
        metadata={
            "name": "comboFormTypes",
            "type": "Element",
        },
    )
    sub_company_filer: Optional[SubjectCompanyType] = field(
        default=None,
        metadata={
            "name": "subCompanyFiler",
            "type": "Element",
            "required": True,
        },
    )
    contact: Optional[ContactType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    sros: Optional[SrosType] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    rule163_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "rule163Flag",
            "type": "Element",
            "pattern": r"true|false",
        },
    )
    rule433_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "rule433Flag",
            "type": "Element",
            "pattern": r"true|false",
        },
    )
    first_filing_issuing_entity_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "firstFilingIssuingEntityFlag",
            "type": "Element",
            "pattern": r"true|false",
        },
    )
    depositor: Optional[DepositorType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    notifications: Optional[NotificationType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    module_segments: Optional[ModulesSegmentType] = field(
        default=None,
        metadata={
            "name": "moduleSegments",
            "type": "Element",
        },
    )
    documents: Optional[EdgarDocumentsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
