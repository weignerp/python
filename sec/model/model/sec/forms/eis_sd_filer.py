from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union

from model.sec.forms.eis_common2 import (
    ContactType,
    EdgarDocumentsType,
    LiveTestType,
    ModulesSegmentType,
    NewFileNumType,
    NotificationType,
    YesNoType,
)

__NAMESPACE__ = "http://www.sec.gov/edgar/sdfiler"


@dataclass
class FilerType:
    class Meta:
        name = "FILER_TYPE"

    filer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sdfiler",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    filer_ccc: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerCcc",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sdfiler",
            "required": True,
            "length": 8,
        },
    )
    file_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sdfiler",
            "pattern": r"\d{1,3}-\d{1,8}-[a-zA-Z0-9]{1,4}|\d{1,3}-\d{1,8}",
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
            "namespace": "http://www.sec.gov/edgar/sdfiler",
            "pattern": r"true|false",
        },
    )
    override_internet_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "overrideInternetFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sdfiler",
            "pattern": r"true|false",
        },
    )
    return_copy_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "returnCopyFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sdfiler",
            "pattern": r"true|false",
        },
    )


class Rule13P1ItemType(Enum):
    VALUE_1_01 = "1.01"
    VALUE_1_02 = "1.02"


class Rule13Q1ItemType(Enum):
    VALUE_2_01 = "2.01"


class SubmissionType(Enum):
    """Type of submission you are filing.

    Choose a value from the appropriate family of Submission Types.
    """

    SD = "SD"
    SD_A = "SD/A"


@dataclass
class FilerType2:
    class Meta:
        name = "FILER_TYPE_2"

    filer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sdfiler",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    filer_ccc: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerCcc",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sdfiler",
            "required": True,
            "length": 8,
        },
    )
    file_number: Optional[Union[str, NewFileNumType]] = field(
        default=None,
        metadata={
            "name": "fileNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sdfiler",
            "pattern": r"\d{1,3}-\d{1,8}-[a-zA-Z0-9]{1,4}|\d{1,3}-\d{1,8}",
        },
    )


@dataclass
class Rule13P1ItemPeriodType:
    class Meta:
        name = "RULE13P1_ITEM_PERIOD_TYPE"

    rule13_p1_item: Optional[Rule13P1ItemType] = field(
        default=None,
        metadata={
            "name": "rule13P1Item",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sdfiler",
            "required": True,
        },
    )
    period: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sdfiler",
            "required": True,
            "pattern": r"\d{1,2}-\d{1,2}-\d{4}",
        },
    )


@dataclass
class Rule13Q1Type:
    class Meta:
        name = "RULE13Q1_TYPE"

    rule13_q1_item: Optional[Rule13Q1ItemType] = field(
        default=None,
        metadata={
            "name": "rule13Q1Item",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sdfiler",
            "required": True,
        },
    )
    period: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sdfiler",
            "required": True,
            "pattern": r"\d{1,2}-\d{1,2}-\d{4}",
        },
    )
    resource_ext_issuer: Optional[YesNoType] = field(
        default=None,
        metadata={
            "name": "resourceExtIssuer",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sdfiler",
            "required": True,
        },
    )


@dataclass
class FilersType:
    class Meta:
        name = "FILERS_TYPE"

    filer: List[FilerType2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sdfiler",
            "min_occurs": 1,
        },
    )


@dataclass
class Rule13P1Type:
    class Meta:
        name = "RULE13P1_TYPE"

    rule13_p1_item_period: List[Rule13P1ItemPeriodType] = field(
        default_factory=list,
        metadata={
            "name": "rule13P1ItemPeriod",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sdfiler",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )


@dataclass
class Rule13Type:
    class Meta:
        name = "RULE13_TYPE"

    rule13_p1: Optional[Rule13P1Type] = field(
        default=None,
        metadata={
            "name": "rule13P1",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sdfiler",
        },
    )
    rule13_q1: Optional[Rule13Q1Type] = field(
        default=None,
        metadata={
            "name": "rule13Q1",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sdfiler",
        },
    )


@dataclass
class EdgarSubmission:
    class Meta:
        name = "edgarSubmission"
        namespace = "http://www.sec.gov/edgar/sdfiler"

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
    contact: Optional[ContactType] = field(
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
    accession_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "accessionNumber",
            "type": "Element",
            "pattern": r"[*]{0}|[0-9]{1,10}\-[0-9]{1,2}\-[0-9]{1,6}",
        },
    )
    filer: Optional[FilerType] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    coregs: Optional[FilersType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    rule13: Optional[Rule13Type] = field(
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
