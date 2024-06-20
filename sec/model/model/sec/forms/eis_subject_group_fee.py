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
    FeeOffsetType,
    FeeType,
)

__NAMESPACE__ = "http://www.sec.gov/edgar/subjectgroupfee"


class ComboSubmissionType(Enum):
    SC_13_E3 = "SC 13E3"
    SC_13_E3_A = "SC 13E3/A"
    SC_TO_I = "SC TO-I"
    SC_TO_I_A = "SC TO-I/A"
    SC_TO_T = "SC TO-T"
    SC_TO_T_A = "SC TO-T/A"
    SC_13_D_A = "SC 13D/A"


@dataclass
class FiledByType:
    class Meta:
        name = "FILED_BY_TYPE"

    filer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectgroupfee",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    filer_ccc: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerCcc",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectgroupfee",
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
            "namespace": "http://www.sec.gov/edgar/subjectgroupfee",
            "pattern": r"true|false",
        },
    )
    return_copy_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "returnCopyFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectgroupfee",
            "pattern": r"true|false",
        },
    )
    override_internet_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "overrideInternetFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectgroupfee",
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
            "namespace": "http://www.sec.gov/edgar/subjectgroupfee",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    irs_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "irsNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectgroupfee",
            "required": True,
            "pattern": r"\d{2}[\-]?\d{7}",
        },
    )
    file_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectgroupfee",
            "pattern": r"\d{1,3}-\d{1,8}-[a-zA-Z0-9]{1,4}|\d{1,3}-\d{1,8}",
        },
    )
    filer_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerName",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectgroupfee",
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
            "namespace": "http://www.sec.gov/edgar/subjectgroupfee",
            "min_length": 1,
            "max_length": 150,
            "pattern": r"([A-Za-z0-9\s!\\#$(),.:;=@'\-{}|/&]+)",
        },
    )


class SubmissionType(Enum):
    """Type of submission you are filing.

    Choose a value from the appropriate family of Submission Types.
    """

    SC13_E4_F = "SC13E4F"
    SC13_E4_F_A = "SC13E4F/A"
    SC14_D1_F = "SC14D1F"
    SC14_D1_F_A = "SC14D1F/A"
    SC_13_E3 = "SC 13E3"
    SC_13_E3_A = "SC 13E3/A"
    SC_TO_I = "SC TO-I"
    SC_TO_I_A = "SC TO-I/A"
    SC_TO_T = "SC TO-T"
    SC_TO_T_A = "SC TO-T/A"


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
            "namespace": "http://www.sec.gov/edgar/subjectgroupfee",
            "max_occurs": 2,
        },
    )


@dataclass
class EdgarSubmission:
    """
    This is the root element for an EDGARLink Online submission.

    :ivar schema_version:
    :ivar live_test_flag:
    :ivar flag:
    :ivar submission_type:
    :ivar filer:
    :ivar combo_form_types:
    :ivar sub_company_filer:
    :ivar contact:
    :ivar sros:
    :ivar fee_table_included_flag:
    :ivar notifications:
    :ivar module_segments:
    :ivar documents:
    :ivar edgar_fee: Comment describing your root element
    """

    class Meta:
        name = "edgarSubmission"
        namespace = "http://www.sec.gov/edgar/subjectgroupfee"

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
    fee_table_included_flag: Optional[YesNoType] = field(
        default=None,
        metadata={
            "name": "feeTableIncludedFlag",
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
    class EdgarFee:
        submission_fee: Optional[FeeType] = field(
            default=None,
            metadata={
                "name": "submissionFee",
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
