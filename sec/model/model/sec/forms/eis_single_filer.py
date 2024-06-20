from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from model.sec.forms.eis_common import ConfidentialDocumentsType1
from model.sec.forms.eis_common2 import (
    ContactType,
    EdgarDocumentsType,
    LiveTestType,
    ModulesSegmentType,
    NotificationType,
    SrosType,
)

__NAMESPACE__ = "http://www.sec.gov/edgar/singlefiler"


@dataclass
class FilerType:
    class Meta:
        name = "FILER_TYPE"

    filer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/singlefiler",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    filer_ccc: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerCcc",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/singlefiler",
            "required": True,
            "length": 8,
        },
    )
    file_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/singlefiler",
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
            "namespace": "http://www.sec.gov/edgar/singlefiler",
            "pattern": r"true|false",
        },
    )
    override_internet_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "overrideInternetFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/singlefiler",
            "pattern": r"true|false",
        },
    )
    return_copy_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "returnCopyFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/singlefiler",
            "pattern": r"true|false",
        },
    )


class SubmissionType(Enum):
    """Type of submission you are filing.

    Choose a value from the appropriate family of Submission Types.
    """

    N_54_A = "N-54A"
    N_54_A_A = "N-54A/A"
    N_54_C = "N-54C"
    N_54_C_A = "N-54C/A"
    N_6_F = "N-6F"
    N_6_F_A = "N-6F/A"
    N_8_A = "N-8A"
    N_8_A_A = "N-8A/A"
    DSTRBRPT = "DSTRBRPT"
    DSTRBRPT_A = "DSTRBRPT/A"
    SBS_DISPUTE_NOTICE = "SBS DISPUTE NOTICE"
    SBS_DISPUTE_NOTICE_A = "SBS DISPUTE NOTICE/A"
    ANNLRPT = "ANNLRPT"
    ANNLRPT_A = "ANNLRPT/A"
    QRTLYRPT = "QRTLYRPT"
    QRTLYRPT_A = "QRTLYRPT/A"
    SH_ER = "SH-ER"
    SH_ER_A = "SH-ER/A"
    SH_NT = "SH-NT"
    SH_NT_A = "SH-NT/A"
    N_PX_NT = "N-PX-NT"
    N_PX_NT_A = "N-PX-NT/A"
    N_PX_VR = "N-PX-VR"
    N_PX_VR_A = "N-PX-VR/A"
    N_PX_CR = "N-PX-CR"
    N_PX_CR_A = "N-PX-CR/A"
    N_PXCON = "N-PXCON"
    N_PXCON_A = "N-PXCON/A"
    N_PXCONP = "N-PXCONP"
    N_PXCONP_A = "N-PXCONP/A"
    DRS = "DRS"
    DRS_A = "DRS/A"
    IRANNOTICE = "IRANNOTICE"
    DOS = "DOS"
    DOS_A = "DOS/A"
    SDR_CCO = "SDR-CCO"
    SDR_CCO_A = "SDR-CCO/A"
    NRSRO_UPD = "NRSRO-UPD"
    NRSRO_CE = "NRSRO-CE"
    NRSRO_CE_A = "NRSRO-CE/A"
    NRSRO_WREG = "NRSRO-WREG"
    NRSRO_WCLS = "NRSRO-WCLS"
    NRSRO_FR = "NRSRO-FR"
    NRSRO_FR_A = "NRSRO-FR/A"


@dataclass
class EdgarSubmission:
    class Meta:
        name = "edgarSubmission"
        namespace = "http://www.sec.gov/edgar/singlefiler"

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
    start_period: Optional[str] = field(
        default=None,
        metadata={
            "name": "startPeriod",
            "type": "Element",
            "pattern": r"\d{1,2}-\d{1,2}-\d{4}",
        },
    )
    end_period: Optional[str] = field(
        default=None,
        metadata={
            "name": "endPeriod",
            "type": "Element",
            "pattern": r"\d{1,2}-\d{1,2}-\d{4}",
        },
    )
    brief_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "briefDescription",
            "type": "Element",
            "min_length": 1,
            "max_length": 1000,
            "pattern": r"[A-Za-z0-9!#-$%():;'@\*\+\-/=\?\^_`~{|},. \\\s<>&\"\[\]]{1,1000}",
        },
    )
    filer: Optional[FilerType] = field(
        default=None,
        metadata={
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
    sros: Optional[SrosType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    emerging_growth_company_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "emergingGrowthCompanyFlag",
            "type": "Element",
            "pattern": r"true|false",
        },
    )
    ex_transition_period_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "exTransitionPeriodFlag",
            "type": "Element",
            "pattern": r"true|false",
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
    calendar_year_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "calendarYearEnd",
            "type": "Element",
            "pattern": r"\d{4,4}",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 256,
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
        },
    )
    documents_confidential: Optional[ConfidentialDocumentsType1] = field(
        default=None,
        metadata={
            "name": "documentsConfidential",
            "type": "Element",
        },
    )
