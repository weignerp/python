from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from model.sec.forms.eis_common2 import (
    ContactType,
    EdgarDocumentsType,
    InvestmentCompanyType,
    LiveTestType,
    ModulesSegmentType,
    NotificationType,
    SrosType,
)
from model.sec.forms.eis_common_sc import (
    RptClassType,
    RptSeriesType,
)

__NAMESPACE__ = "http://www.sec.gov/edgar/subjectsc"


@dataclass
class FiledByType:
    class Meta:
        name = "FILED_BY_TYPE"

    filer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectsc",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    filer_ccc: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerCcc",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectsc",
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
            "namespace": "http://www.sec.gov/edgar/subjectsc",
            "pattern": r"true|false",
        },
    )
    return_copy_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "returnCopyFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectsc",
            "pattern": r"true|false",
        },
    )
    override_internet_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "overrideInternetFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectsc",
            "pattern": r"true|false",
        },
    )


class SubmissionType(Enum):
    """Type of submission you are filing.

    Choose a value from the appropriate family of Submission Types.
    """

    DEFC14_A = "DEFC14A"
    DEFC14_C = "DEFC14C"
    DEFN14_A = "DEFN14A"
    DFAN14_A = "DFAN14A"
    DFRN14_A = "DFRN14A"
    PREC14_A = "PREC14A"
    PREC14_C = "PREC14C"
    PREN14_A = "PREN14A"
    PRRN14_A = "PRRN14A"
    PX14_A6_G = "PX14A6G"
    PX14_A6_N = "PX14A6N"


@dataclass
class SubjectCompanyType:
    class Meta:
        name = "SUBJECT_COMPANY_TYPE"

    filer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectsc",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    irs_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "irsNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectsc",
            "required": True,
            "pattern": r"\d{2}[\-]?\d{7}",
        },
    )
    file_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectsc",
            "pattern": r"\d{1,3}-\d{1,8}-[a-zA-Z0-9]{1,4}|\d{1,3}-\d{1,8}",
        },
    )
    filer_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerName",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectsc",
            "required": True,
            "min_length": 1,
            "max_length": 150,
            "pattern": r"([A-Za-z0-9\s!\\#$(),.:;=@'\-{}|/&]+)",
        },
    )
    filer_inv_company: Optional[InvestmentCompanyType] = field(
        default=None,
        metadata={
            "name": "filerInvCompany",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/subjectsc",
        },
    )


@dataclass
class EdgarSubmission:
    """
    This is the root element for an EDGARLink Online submission.
    """

    class Meta:
        name = "edgarSubmission"
        namespace = "http://www.sec.gov/edgar/subjectsc"

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
