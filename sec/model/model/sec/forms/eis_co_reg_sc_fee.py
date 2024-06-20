from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from model.sec.forms.eis_common2 import (
    ContactType,
    EdgarDocumentsType,
    InvestmentCompanyType,
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
from model.sec.forms.eis_common_sc import (
    MgrSeriesClassType,
    RptClassType,
    RptSeriesType,
)

__NAMESPACE__ = "http://www.sec.gov/edgar/coregscfee"


@dataclass
class FilerType:
    class Meta:
        name = "FILER_TYPE"

    filer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregscfee",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    filer_ccc: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerCcc",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregscfee",
            "required": True,
            "length": 8,
        },
    )
    file_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregscfee",
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
            "namespace": "http://www.sec.gov/edgar/coregscfee",
            "pattern": r"true|false",
        },
    )
    return_copy_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "returnCopyFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregscfee",
            "pattern": r"true|false",
        },
    )
    override_internet_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "overrideInternetFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregscfee",
            "pattern": r"true|false",
        },
    )


class SubmissionType(Enum):
    """Type of submission you are filing.

    Choose a value from the appropriate family of Submission Types.
    """

    PREM14_A = "PREM14A"
    PREM14_C = "PREM14C"
    PRER14_A = "PRER14A"
    PRER14_C = "PRER14C"


@dataclass
class FilersType:
    class Meta:
        name = "FILERS_TYPE"

    filer: List[FilerType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregscfee",
            "min_occurs": 1,
        },
    )


@dataclass
class EdgarSubmission:
    """
    This is the root element for an EDGARLink Online submission.

    :ivar schema_version:
    :ivar live_test_flag:
    :ivar flags:
    :ivar submission_type:
    :ivar contact:
    :ivar filer:
    :ivar coregs:
    :ivar sros:
    :ivar fee_table_included_flag:
    :ivar inv_company:
    :ivar period_of_report:
    :ivar notifications:
    :ivar module_segments:
    :ivar documents:
    :ivar series_classes:
    :ivar edgar_fee: Comment describing your root element
    """

    class Meta:
        name = "edgarSubmission"
        namespace = "http://www.sec.gov/edgar/coregscfee"

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
    flags: Optional[FlagType] = field(
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
    inv_company: Optional[InvestmentCompanyType] = field(
        default=None,
        metadata={
            "name": "invCompany",
            "type": "Element",
        },
    )
    period_of_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "periodOfReport",
            "type": "Element",
            "pattern": r"\d{1,2}-\d{1,2}-\d{4}",
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
    series_classes: Optional["EdgarSubmission.SeriesClasses"] = field(
        default=None,
        metadata={
            "name": "seriesClasses",
            "type": "Element",
        },
    )
    edgar_fee: Optional["EdgarSubmission.EdgarFee"] = field(
        default=None,
        metadata={
            "name": "edgarFee",
            "type": "Element",
            "required": True,
        },
    )

    @dataclass
    class SeriesClasses:
        report_series_class: Optional[RptSeriesType] = field(
            default=None,
            metadata={
                "name": "reportSeriesClass",
                "type": "Element",
            },
        )
        report_class: Optional[RptClassType] = field(
            default=None,
            metadata={
                "name": "reportClass",
                "type": "Element",
            },
        )
        merge_series_class: Optional[MgrSeriesClassType] = field(
            default=None,
            metadata={
                "name": "mergeSeriesClass",
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
