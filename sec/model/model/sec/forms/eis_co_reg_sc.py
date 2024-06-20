from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union

from model.sec.forms.eis_common2 import (
    ActType,
    ContactType,
    EdgarDocumentsType,
    InvestmentCompanyType,
    LiveTestType,
    ModulesSegmentType,
    NewFileNumType,
    NotificationType,
    SrosType,
)
from model.sec.forms.eis_common_sc import (
    MgrSeriesClassType,
    NewClassType,
    NewClassType2,
    NewSeriesClassType,
    RptClassType,
    RptSeriesType,
)

__NAMESPACE__ = "http://www.sec.gov/edgar/coregsc"


@dataclass
class FilerType:
    class Meta:
        name = "FILER_TYPE"

    filer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregsc",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    filer_ccc: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerCcc",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregsc",
            "required": True,
            "length": 8,
        },
    )
    file_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregsc",
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
            "namespace": "http://www.sec.gov/edgar/coregsc",
            "pattern": r"true|false",
        },
    )
    delaying_amendment_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "delayingAmendmentFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregsc",
            "pattern": r"true|false",
        },
    )
    return_copy_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "returnCopyFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregsc",
            "pattern": r"true|false",
        },
    )
    override_internet_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "overrideInternetFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregsc",
            "pattern": r"true|false",
        },
    )


class SubmissionType(Enum):
    """Type of submission you are filing.

    Choose a value from the appropriate family of Submission Types.
    """

    VALUE_485_APOS = "485APOS"
    VALUE_485_BPOS = "485BPOS"
    VALUE_485_BXT = "485BXT"
    VALUE_497 = "497"
    VALUE_497_AD = "497AD"
    VALUE_497_J = "497J"
    VALUE_497_K = "497K"
    VALUE_497_VPSUB = "497VPSUB"
    DEF_14_A = "DEF 14A"
    DEF_14_C = "DEF 14C"
    DEFA14_A = "DEFA14A"
    DEFA14_C = "DEFA14C"
    DEFR14_A = "DEFR14A"
    DEFR14_C = "DEFR14C"
    DEFM14_A = "DEFM14A"
    DEFM14_C = "DEFM14C"
    N_1_A = "N-1A"
    N_1_A_A = "N-1A/A"
    N_14 = "N-14"
    N_14_A = "N-14/A"
    N_3 = "N-3"
    N_3_A = "N-3/A"
    N_30_B_2 = "N-30B-2"
    N_30_D = "N-30D"
    N_30_D_A = "N-30D/A"
    N_4 = "N-4"
    N_4_A = "N-4/A"
    N_6 = "N-6"
    N_6_A = "N-6/A"
    N_CSR = "N-CSR"
    N_CSR_A = "N-CSR/A"
    N_CSRS = "N-CSRS"
    N_CSRS_A = "N-CSRS/A"
    N_Q = "N-Q"
    N_Q_A = "N-Q/A"
    NSAR_A = "NSAR-A"
    NSAR_A_A = "NSAR-A/A"
    NSAR_AT = "NSAR-AT"
    NSAR_AT_A = "NSAR-AT/A"
    NSAR_B = "NSAR-B"
    NSAR_B_A = "NSAR-B/A"
    NSAR_BT = "NSAR-BT"
    NSAR_BT_A = "NSAR-BT/A"
    NT_NCSR = "NT-NCSR"
    NT_NCSR_A = "NT-NCSR/A"
    NT_NSAR = "NT-NSAR"
    NT_NSAR_A = "NT-NSAR/A"
    N_VP = "N-VP"
    N_VP_A = "N-VP/A"
    POS_AMI = "POS AMI"
    PRE_14_A = "PRE 14A"
    PRE_14_C = "PRE 14C"
    N_VPFS = "N-VPFS"
    N_VPFS_A = "N-VPFS/A"


@dataclass
class FilerType2:
    class Meta:
        name = "FILER_TYPE_2"

    filer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregsc",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    filer_ccc: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerCcc",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregsc",
            "required": True,
            "length": 8,
        },
    )
    file_number: Optional[Union[str, NewFileNumType]] = field(
        default=None,
        metadata={
            "name": "fileNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregsc",
            "pattern": r"\d{1,3}-\d{1,8}-[a-zA-Z0-9]{1,4}|\d{1,3}-\d{1,8}",
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
            "namespace": "http://www.sec.gov/edgar/coregsc",
            "min_occurs": 1,
        },
    )


@dataclass
class EdgarSubmission:
    """
    This is the root element for an EDGARLink Online submission.
    """

    class Meta:
        name = "edgarSubmission"
        namespace = "http://www.sec.gov/edgar/coregsc"

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
    act: Optional[ActType] = field(
        default=None,
        metadata={
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
    effective_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "effectiveDate",
            "type": "Element",
            "pattern": r"\d{1,2}-\d{1,2}-\d{4}",
        },
    )
    inv_company: Optional[InvestmentCompanyType] = field(
        default=None,
        metadata={
            "name": "invCompany",
            "type": "Element",
        },
    )
    insurance_substitution_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "insuranceSubstitutionFlag",
            "type": "Element",
            "pattern": r"true|false",
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
        merge_series_class: Optional[MgrSeriesClassType] = field(
            default=None,
            metadata={
                "name": "mergeSeriesClass",
                "type": "Element",
            },
        )
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
        new_series_class: List[NewSeriesClassType] = field(
            default_factory=list,
            metadata={
                "name": "newSeriesClass",
                "type": "Element",
            },
        )
        new_class2: List[NewClassType2] = field(
            default_factory=list,
            metadata={
                "name": "newClass2",
                "type": "Element",
            },
        )
        new_class: Optional[NewClassType] = field(
            default=None,
            metadata={
                "name": "newClass",
                "type": "Element",
            },
        )
