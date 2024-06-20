from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from model.sec.forms.eis_common2 import (
    ContactType,
    EdgarDocumentsType,
    FlagType,
    InvCompanyType,
    LiveTestType,
    ModulesSegmentType,
    NotificationType,
    SrosType,
)
from model.sec.forms.eis_common_fee import FeeSalesShareType
from model.sec.forms.eis_common_sc import (
    RptClassType,
    RptSeriesType,
)

__NAMESPACE__ = "http://www.sec.gov/edgar/singlefilerscfee"


@dataclass
class FilerType:
    class Meta:
        name = "FILER_TYPE"

    filer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/singlefilerscfee",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    filer_ccc: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerCcc",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/singlefilerscfee",
            "required": True,
            "length": 8,
        },
    )
    file_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/singlefilerscfee",
            "pattern": r"\d{1,3}-\d{1,8}-[a-zA-Z0-9]{1,4}|\d{1,3}-\d{1,8}",
        },
    )


class SubmissionType(Enum):
    """Type of submission you are filing.

    Choose a value from the appropriate family of Submission Types.
    """

    VALUE_24_F_2_NT = "24F-2NT"
    VALUE_24_F_2_NT_A = "24F-2NT/A"


@dataclass
class EdgarSubmission:
    """
    :ivar schema_version:
    :ivar live_test_flag:
    :ivar flags:
    :ivar submission_type:
    :ivar contact:
    :ivar filer:
    :ivar sros:
    :ivar period_of_report:
    :ivar inv_company:
    :ivar notifications:
    :ivar module_segments:
    :ivar documents:
    :ivar series_classes:
    :ivar edgar_fee: Comment describing your root element
    """

    class Meta:
        name = "edgarSubmission"
        namespace = "http://www.sec.gov/edgar/singlefilerscfee"

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
    sros: Optional[SrosType] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    period_of_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "periodOfReport",
            "type": "Element",
            "required": True,
            "pattern": r"\d{1,2}-\d{1,2}-\d{4}",
        },
    )
    inv_company: Optional[InvCompanyType] = field(
        default=None,
        metadata={
            "name": "invCompany",
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
    series_classes: Optional["EdgarSubmission.SeriesClasses"] = field(
        default=None,
        metadata={
            "name": "seriesClasses",
            "type": "Element",
        },
    )
    edgar_fee: Optional[FeeSalesShareType] = field(
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
