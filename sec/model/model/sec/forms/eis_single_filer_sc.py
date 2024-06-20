from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from model.sec.forms.eis_common2 import (
    ContactType,
    EdgarDocumentsType,
    InvCompanyType,
    LiveTestType,
    ModulesSegmentType,
    NotificationType,
    SrosType,
)
from model.sec.forms.eis_common_sc import (
    MultiAccessionNumbersType,
    RptClassType,
    RptSeriesType,
)

__NAMESPACE__ = "http://www.sec.gov/edgar/singlefilersc"


@dataclass
class FilerType:
    class Meta:
        name = "FILER_TYPE"

    filer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/singlefilersc",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    filer_ccc: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerCcc",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/singlefilersc",
            "required": True,
            "length": 8,
        },
    )
    file_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/singlefilersc",
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
            "namespace": "http://www.sec.gov/edgar/singlefilersc",
            "pattern": r"true|false",
        },
    )
    return_copy_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "returnCopyFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/singlefilersc",
            "pattern": r"true|false",
        },
    )
    override_internet_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "overrideInternetFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/singlefilersc",
            "pattern": r"true|false",
        },
    )


class SubmissionType(Enum):
    """Type of submission you are filing.

    Choose a value from the appropriate family of Submission Types.
    """

    VALUE_497_K = "497K"
    VALUE_497_VPU = "497VPU"
    VALUE_497_VPI = "497VPI"
    N_PX = "N-PX"
    N_PX_A = "N-PX/A"
    N_PX_FM = "N-PX-FM"
    N_PX_FM_A = "N-PX-FM/A"
    N_CR = "N-CR"
    N_CR_A = "N-CR/A"
    NT_NCEN = "NT-NCEN"
    NT_NCEN_A = "NT-NCEN/A"
    NPORT_EX = "NPORT-EX"
    NPORT_EX_A = "NPORT-EX/A"
    N_LIQUID = "N-LIQUID"
    N_LIQUID_A = "N-LIQUID/A"
    N_RN = "N-RN"
    N_RN_A = "N-RN/A"


@dataclass
class EdgarSubmission:
    class Meta:
        name = "edgarSubmission"
        namespace = "http://www.sec.gov/edgar/singlefilersc"

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
    contact_email: Optional[str] = field(
        default=None,
        metadata={
            "name": "contactEmail",
            "type": "Element",
            "min_length": 4,
            "max_length": 80,
            "pattern": r"([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,7}|[0-9]{1,3})(\]?)",
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
            "pattern": r"\d{1,2}-\d{1,2}-\d{4}",
        },
    )
    inv_company: Optional[InvCompanyType] = field(
        default=None,
        metadata={
            "name": "invCompany",
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
    series_classes: Optional["EdgarSubmission.SeriesClasses"] = field(
        default=None,
        metadata={
            "name": "seriesClasses",
            "type": "Element",
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
    multi_accession_numbers: Optional[MultiAccessionNumbersType] = field(
        default=None,
        metadata={
            "name": "multiAccessionNumbers",
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
