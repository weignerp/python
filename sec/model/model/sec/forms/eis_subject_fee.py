from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from model.sec.forms.eis_common2 import (
    ContactType,
    EdgarDocumentsType,
    LiveTestType,
    ModulesSegmentType,
    NotificationType,
    SrosType,
    YesNoType,
)
from model.sec.forms.eis_common_fee import (
    FeeOfferingType,
    FeeOffsetType,
    FeeType,
)

__NAMESPACE__ = "http://www.sec.gov/edgar/subjectfee"


@dataclass
class FiledByType:
    class Meta:
        name = "FILED_BY_TYPE"

    filer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectfee",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    filer_ccc: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerCcc",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectfee",
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
            "namespace": "http://www.sec.gov/edgar/subjectfee",
            "pattern": r"true|false",
        },
    )
    delaying_amendment_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "delayingAmendmentFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectfee",
            "pattern": r"true|false",
        },
    )
    return_copy_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "returnCopyFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectfee",
            "pattern": r"true|false",
        },
    )
    override_internet_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "overrideInternetFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectfee",
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
            "namespace": "http://www.sec.gov/edgar/subjectfee",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    irs_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "irsNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectfee",
            "pattern": r"\d{2}[\-]?\d{7}",
        },
    )
    file_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectfee",
            "pattern": r"\d{1,3}-\d{1,8}-[a-zA-Z0-9]{1,4}|\d{1,3}-\d{1,8}",
        },
    )
    filer_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerName",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectfee",
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

    SC_13_E1 = "SC 13E1"
    SC_13_E1_A = "SC 13E1/A"
    F_6 = "F-6"
    F_6_A = "F-6/A"
    F_6_EF = "F-6EF"


@dataclass
class EdgarSubmission:
    """
    This is the root element for an EDGARLink Online submission.

    :ivar schema_version:
    :ivar live_test_flag:
    :ivar flag:
    :ivar submission_type:
    :ivar contact:
    :ivar filer:
    :ivar sub_company_filer:
    :ivar sros:
    :ivar fee_table_included_flag:
    :ivar effective_date:
    :ivar depository:
    :ivar references:
    :ivar notifications:
    :ivar module_segments:
    :ivar documents:
    :ivar edgar_fee: Comment describing your root element
    """

    class Meta:
        name = "edgarSubmission"
        namespace = "http://www.sec.gov/edgar/subjectfee"

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
    filer: Optional[FiledByType] = field(
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
    fee_table_included_flag: Optional[YesNoType] = field(
        default=None,
        metadata={
            "name": "feeTableIncludedFlag",
            "type": "Element",
        },
    )
    effective_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "effectiveDate",
            "type": "Element",
            "pattern": r"\d{1,2}-\d{1,2}-\d{4}",
        },
    )
    depository: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 1,
            "max_length": 50,
            "pattern": r"[A-Za-z0-9!#-$%():;'@\*\+\-/=\?\^_`~{|},. \\\s<>&\"\[\]]{1,50}",
        },
    )
    references: Optional["EdgarSubmission.References"] = field(
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
    edgar_fee: Optional["EdgarSubmission.EdgarFee"] = field(
        default=None,
        metadata={
            "name": "edgarFee",
            "type": "Element",
        },
    )

    @dataclass
    class References:
        references_429: List[str] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
                "pattern": r"\d{1,3}-\d{1,8}-[a-zA-Z0-9]{1,4}|\d{1,3}-\d{1,8}",
            },
        )

    @dataclass
    class EdgarFee:
        submission_fee: Optional[FeeType] = field(
            default=None,
            metadata={
                "name": "submissionFee",
                "type": "Element",
            },
        )
        submission_offering: List[FeeOfferingType] = field(
            default_factory=list,
            metadata={
                "name": "submissionOffering",
                "type": "Element",
            },
        )
        submission_offset: List[FeeOffsetType] = field(
            default_factory=list,
            metadata={
                "name": "submissionOffset",
                "type": "Element",
            },
        )
