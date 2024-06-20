from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from model.sec.forms.eis_common2 import (
    ContactType,
    EdgarDocumentsType,
    LiveTestType,
    ModulesSegmentType,
    NotificationType,
    RptOwnerRelationshipType,
    SrosType,
)

__NAMESPACE__ = "http://www.sec.gov/edgar/ownership"


@dataclass
class FlagType:
    class Meta:
        name = "FLAG_TYPE"

    override_internet_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "overrideInternetFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/ownership",
            "pattern": r"true|false",
        },
    )
    return_copy_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "returnCopyFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/ownership",
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
            "namespace": "http://www.sec.gov/edgar/ownership",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    irs_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "irsNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/ownership",
            "required": True,
            "pattern": r"\d{2}[\-]?\d{7}",
        },
    )
    filer_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerName",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/ownership",
            "required": True,
            "min_length": 1,
            "max_length": 150,
            "pattern": r"([A-Za-z0-9\s!\\#$(),.:;=@'\-{}|/&]+)",
        },
    )


class SubmissionType(Enum):
    """Type of submission you are filing.

    Choose a value from the appropriate family of Submission Types.
    """

    VALUE_144 = "144"
    VALUE_144_A = "144/A"


@dataclass
class ReportingOwnerType:
    class Meta:
        name = "REPORTING_OWNER_TYPE"

    filer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/ownership",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    filer_ccc: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerCcc",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/ownership",
            "required": True,
            "length": 8,
        },
    )
    filer_relationship: Optional[RptOwnerRelationshipType] = field(
        default=None,
        metadata={
            "name": "filerRelationship",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/ownership",
            "required": True,
        },
    )


@dataclass
class EdgarSubmission:
    """
    This is the root element for an EDGARLink Online submission.
    """

    class Meta:
        name = "edgarSubmission"
        namespace = "http://www.sec.gov/edgar/ownership"

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
    contact: Optional[ContactType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    filer: Optional[ReportingOwnerType] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
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
    sros: Optional[SrosType] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
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
