from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union

from model.sec.forms.eis_common import (
    AbsAssetClassTypes,
    AbsSubAssetClassTypes,
    SuccessorType,
)
from model.sec.forms.eis_common2 import (
    AcceleratedStatusType,
    ActType,
    ContactType,
    DepositorType,
    EdgarDocumentsType,
    FlagType,
    InvCompanyType,
    LiveTestType,
    ModulesSegmentType,
    NewFileNumType,
    NotificationType,
    SrosType,
    YesNoType,
)

__NAMESPACE__ = "http://www.sec.gov/edgar/coreg"


@dataclass
class FilerType:
    class Meta:
        name = "FILER_TYPE"

    filer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coreg",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    filer_ccc: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerCcc",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coreg",
            "required": True,
            "length": 8,
        },
    )
    file_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coreg",
            "pattern": r"\d{1,3}-\d{1,8}-[a-zA-Z0-9]{1,4}|\d{1,3}-\d{1,8}",
        },
    )
    ia_file_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "iaFileNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coreg",
            "pattern": r"\d{1,3}-\d{1,8}-[a-zA-Z0-9]{1,4}|\d{1,3}-\d{1,8}",
        },
    )
    duty_to_file_reports_remains: Optional[str] = field(
        default=None,
        metadata={
            "name": "dutyToFileReportsRemains",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coreg",
            "pattern": r"true|false",
        },
    )


@dataclass
class FiscalYearType:
    class Meta:
        name = "FISCAL_YEAR_TYPE"

    fiscal_year_end: List[str] = field(
        default_factory=list,
        metadata={
            "name": "fiscalYearEnd",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coreg",
            "min_occurs": 1,
            "pattern": r"\d{2,2}/\d{2,2}",
        },
    )


class ItemSubmissionType(Enum):
    VALUE_425 = "425"
    DEFA14_A = "DEFA14A"
    DFAN14_A = "DFAN14A"
    SC_TO_C = "SC TO-C"


class ItemType(Enum):
    VALUE_1_01 = "1.01"
    VALUE_1_02 = "1.02"
    VALUE_1_03 = "1.03"
    VALUE_1_04 = "1.04"
    VALUE_2_01 = "2.01"
    VALUE_2_02 = "2.02"
    VALUE_2_03 = "2.03"
    VALUE_2_04 = "2.04"
    VALUE_2_05 = "2.05"
    VALUE_2_06 = "2.06"
    VALUE_3_01 = "3.01"
    VALUE_3_02 = "3.02"
    VALUE_3_03 = "3.03"
    VALUE_4_01 = "4.01"
    VALUE_4_02 = "4.02"
    VALUE_5_01 = "5.01"
    VALUE_5_02 = "5.02"
    VALUE_5_03 = "5.03"
    VALUE_5_04 = "5.04"
    VALUE_5_05 = "5.05"
    VALUE_5_06 = "5.06"
    VALUE_5_07 = "5.07"
    VALUE_5_08 = "5.08"
    VALUE_6_01 = "6.01"
    VALUE_6_02 = "6.02"
    VALUE_6_03 = "6.03"
    VALUE_6_04 = "6.04"
    VALUE_6_05 = "6.05"
    VALUE_6_06 = "6.06"
    VALUE_7_01 = "7.01"
    VALUE_8_01 = "8.01"
    VALUE_9_01 = "9.01"


class ItemType2(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"
    VALUE_7 = "7"
    VALUE_8 = "8"
    VALUE_9_1 = "9.1"
    VALUE_9_2 = "9.2"


@dataclass
class SubjectCompanyType:
    class Meta:
        name = "SUBJECT_COMPANY_TYPE"

    filer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coreg",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    irs_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "irsNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coreg",
            "pattern": r"\d{2}[\-]?\d{7}",
        },
    )
    file_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coreg",
            "pattern": r"\d{1,3}-\d{1,8}-[a-zA-Z0-9]{1,4}|\d{1,3}-\d{1,8}",
        },
    )
    filer_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerName",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coreg",
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
            "namespace": "http://www.sec.gov/edgar/coreg",
            "min_length": 1,
            "max_length": 150,
            "pattern": r"([A-Za-z0-9\s!\\#$(),.:;=@'\-{}|/&]+)",
        },
    )


class SubmissionType(Enum):
    """Type of submission you are filing.

    Choose a value from the appropriate family of Submission Types.
    """

    VALUE_10_12_B = "10-12B"
    VALUE_10_12_B_A = "10-12B/A"
    VALUE_10_12_G = "10-12G"
    VALUE_10_12_G_A = "10-12G/A"
    VALUE_10_D = "10-D"
    VALUE_10_D_A = "10-D/A"
    VALUE_10_K = "10-K"
    VALUE_10_K_A = "10-K/A"
    VALUE_10_KSB = "10KSB"
    VALUE_10_KSB_A = "10KSB/A"
    VALUE_10_KT = "10-KT"
    VALUE_10_KT_A = "10-KT/A"
    VALUE_10_Q = "10-Q"
    VALUE_10_Q_A = "10-Q/A"
    VALUE_10_QT = "10-QT"
    VALUE_10_QT_A = "10-QT/A"
    VALUE_11_K = "11-K"
    VALUE_11_K_A = "11-K/A"
    VALUE_11_KT = "11-KT"
    VALUE_11_KT_A = "11-KT/A"
    VALUE_15_12_B = "15-12B"
    VALUE_15_12_B_A = "15-12B/A"
    VALUE_15_12_G = "15-12G"
    VALUE_15_12_G_A = "15-12G/A"
    VALUE_15_15_D = "15-15D"
    VALUE_15_15_D_A = "15-15D/A"
    VALUE_15_F_12_B = "15F-12B"
    VALUE_15_F_12_B_A = "15F-12B/A"
    VALUE_15_F_12_G = "15F-12G"
    VALUE_15_F_12_G_A = "15F-12G/A"
    VALUE_15_F_15_D = "15F-15D"
    VALUE_15_F_15_D_A = "15F-15D/A"
    VALUE_18_12_B = "18-12B"
    VALUE_18_12_B_A = "18-12B/A"
    VALUE_18_12_G = "18-12G"
    VALUE_18_12_G_A = "18-12G/A"
    VALUE_18_K = "18-K"
    VALUE_18_K_A = "18-K/A"
    VALUE_1_A_W = "1-A-W"
    VALUE_1_A_W_A = "1-A-W/A"
    VALUE_1_E_AD = "1-E AD"
    VALUE_1_E_AD_A = "1-E AD/A"
    VALUE_1_E = "1-E"
    VALUE_1_E_A = "1-E/A"
    VALUE_1_SA = "1-SA"
    VALUE_1_SA_A = "1-SA/A"
    VALUE_1_U = "1-U"
    VALUE_1_U_A = "1-U/A"
    VALUE_1_Z_W = "1-Z-W"
    VALUE_1_Z_W_A = "1-Z-W/A"
    VALUE_20_F = "20-F"
    VALUE_20_F_A = "20-F/A"
    VALUE_20_FR12_B = "20FR12B"
    VALUE_20_FR12_B_A = "20FR12B/A"
    VALUE_20_FR12_G = "20FR12G"
    VALUE_20_FR12_G_A = "20FR12G/A"
    VALUE_25 = "25"
    VALUE_25_A = "25/A"
    VALUE_253_G1 = "253G1"
    VALUE_253_G2 = "253G2"
    VALUE_253_G3 = "253G3"
    VALUE_253_G4 = "253G4"
    VALUE_2_E = "2-E"
    VALUE_2_E_A = "2-E/A"
    VALUE_305_B2 = "305B2"
    VALUE_305_B2_A = "305B2/A"
    VALUE_40_17_G = "40-17G"
    VALUE_40_17_G_A = "40-17G/A"
    VALUE_40_17_GCS = "40-17GCS"
    VALUE_40_17_GCS_A = "40-17GCS/A"
    VALUE_40_24_B2 = "40-24B2"
    VALUE_40_24_B2_A = "40-24B2/A"
    VALUE_40_33 = "40-33"
    VALUE_40_33_A = "40-33/A"
    VALUE_40_6_B = "40-6B"
    VALUE_40_6_B_A = "40-6B/A"
    VALUE_40_8_B25 = "40-8B25"
    VALUE_40_8_F_2 = "40-8F-2"
    VALUE_40_8_F_2_A = "40-8F-2/A"
    VALUE_40_APP = "40-APP"
    VALUE_40_APP_A = "40-APP/A"
    VALUE_40_F = "40-F"
    VALUE_40_F_A = "40-F/A"
    VALUE_40_FR12_B = "40FR12B"
    VALUE_40_FR12_B_A = "40FR12B/A"
    VALUE_40_FR12_G = "40FR12G"
    VALUE_40_FR12_G_A = "40FR12G/A"
    VALUE_40_OIP = "40-OIP"
    VALUE_40_OIP_A = "40-OIP/A"
    VALUE_424_A = "424A"
    VALUE_486_APOS = "486APOS"
    VALUE_486_BPOS = "486BPOS"
    VALUE_486_BXT = "486BXT"
    VALUE_487 = "487"
    VALUE_497_H2 = "497H2"
    VALUE_6_K = "6-K"
    VALUE_6_K_A = "6-K/A"
    F_SR = "F-SR"
    F_SR_A = "F-SR/A"
    VALUE_8_A12_B = "8-A12B"
    VALUE_8_A12_B_A = "8-A12B/A"
    VALUE_8_A12_G = "8-A12G"
    VALUE_8_A12_G_A = "8-A12G/A"
    VALUE_8_K = "8-K"
    VALUE_8_K_A = "8-K/A"
    VALUE_8_K12_B = "8-K12B"
    VALUE_8_K12_B_A = "8-K12B/A"
    VALUE_8_K12_G3 = "8-K12G3"
    VALUE_8_K12_G3_A = "8-K12G3/A"
    VALUE_8_K15_D5 = "8-K15D5"
    VALUE_8_K15_D5_A = "8-K15D5/A"
    APP_WD = "APP WD"
    APP_WD_A = "APP WD/A"
    ARS = "ARS"
    ARS_A = "ARS/A"
    AW = "AW"
    AW_WD = "AW WD"
    DEL_AM = "DEL AM"
    DOSLTR = "DOSLTR"
    F_10_POS = "F-10POS"
    F_3_DPOS = "F-3DPOS"
    F_4_POS = "F-4 POS"
    F_7_POS = "F-7 POS"
    F_8_POS = "F-8 POS"
    F_80_POS = "F-80POS"
    F_9_POS = "F-9 POS"
    N_18_F1 = "N-18F1"
    N_18_F1_A = "N-18F1/A"
    N_23_C_2 = "N-23C-2"
    N_23_C_2_A = "N-23C-2/A"
    N_23_C3_A = "N-23C3A"
    N_23_C3_A_A = "N-23C3A/A"
    N_23_C3_B = "N-23C3B"
    N_23_C3_B_A = "N-23C3B/A"
    N_23_C3_C = "N-23C3C"
    N_23_C3_C_A = "N-23C3C/A"
    N_8_B_2 = "N-8B-2"
    N_8_B_2_A = "N-8B-2/A"
    N_8_B_3 = "N-8B-3"
    N_8_B_3_A = "N-8B-3/A"
    N_8_B_4 = "N-8B-4"
    N_8_B_4_A = "N-8B-4/A"
    N_8_F = "N-8F"
    N_8_F_A = "N-8F/A"
    NSAR_U = "NSAR-U"
    NSAR_U_A = "NSAR-U/A"
    NT_10_D = "NT 10-D"
    NT_10_D_A = "NT 10-D/A"
    NT_10_K = "NT 10-K"
    NT_10_K_A = "NT 10-K/A"
    NT_10_Q = "NT 10-Q"
    NT_10_Q_A = "NT 10-Q/A"
    NT_11_K = "NT 11-K"
    NT_11_K_A = "NT 11-K/A"
    NT_15_D2 = "NT 15D2"
    NT_15_D2_A = "NT 15D2/A"
    NT_20_F = "NT 20-F"
    NT_20_F_A = "NT 20-F/A"
    POS_8_C = "POS 8C"
    POS_AM = "POS AM"
    POS_EX = "POS EX"
    POS462_B = "POS462B"
    POS462_C = "POS462C"
    RW_WD = "RW WD"
    RW = "RW"
    S_3_DPOS = "S-3DPOS"
    S_4_POS = "S-4 POS"
    S_6 = "S-6"
    S_6_A = "S-6/A"
    S_8_POS = "S-8 POS"
    SP_15_D2 = "SP 15D2"
    SP_15_D2_A = "SP 15D2/A"
    SPDSCL = "SPDSCL"
    SUPPL = "SUPPL"
    T_3 = "T-3"
    T_3_A = "T-3/A"
    T_6 = "T-6"
    T_6_A = "T-6/A"
    UNDER = "UNDER"
    UNDER_A = "UNDER/A"


@dataclass
class FilerType2:
    class Meta:
        name = "FILER_TYPE_2"

    filer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coreg",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    filer_ccc: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerCcc",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coreg",
            "required": True,
            "length": 8,
        },
    )
    file_number: Optional[Union[str, NewFileNumType]] = field(
        default=None,
        metadata={
            "name": "fileNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coreg",
            "pattern": r"\d{1,3}-\d{1,8}-[a-zA-Z0-9]{1,4}|\d{1,3}-\d{1,8}",
        },
    )
    ia_file_number: Optional[Union[str, NewFileNumType]] = field(
        default=None,
        metadata={
            "name": "iaFileNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coreg",
            "pattern": r"\d{1,3}-\d{1,8}-[a-zA-Z0-9]{1,4}|\d{1,3}-\d{1,8}",
        },
    )
    duty_to_file_reports_remains: Optional[str] = field(
        default=None,
        metadata={
            "name": "dutyToFileReportsRemains",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coreg",
            "pattern": r"true|false",
        },
    )
    emerging_growth_company_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "emergingGrowthCompanyFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coreg",
            "pattern": r"true|false",
        },
    )
    ex_transition_period_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "exTransitionPeriodFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coreg",
            "pattern": r"true|false",
        },
    )


@dataclass
class ItemsType:
    class Meta:
        name = "ITEMS_TYPE"

    item: List[ItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coreg",
            "min_occurs": 1,
        },
    )


@dataclass
class ItemsType2:
    class Meta:
        name = "ITEMS_TYPE_2"

    item_type2: List[ItemType2] = field(
        default_factory=list,
        metadata={
            "name": "itemType2",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coreg",
            "min_occurs": 1,
            "max_occurs": 10,
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
            "namespace": "http://www.sec.gov/edgar/coreg",
            "min_occurs": 1,
        },
    )


@dataclass
class AbsEeEelments:
    class Meta:
        name = "ABS_EE_EELMENTS"

    absee_start_period: Optional[str] = field(
        default=None,
        metadata={
            "name": "abseeStartPeriod",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coreg",
            "required": True,
            "pattern": r"\d{1,2}-\d{1,2}-\d{4}",
        },
    )
    absee_end_period: Optional[str] = field(
        default=None,
        metadata={
            "name": "abseeEndPeriod",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coreg",
            "required": True,
            "pattern": r"\d{1,2}-\d{1,2}-\d{4}",
        },
    )
    absee_file_number: Optional[Union[str, NewFileNumType]] = field(
        default=None,
        metadata={
            "name": "abseeFileNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coreg",
            "required": True,
            "pattern": r"\d{1,3}-\d{1,8}-[a-zA-Z0-9]{1,4}|\d{1,3}-\d{1,8}",
        },
    )
    absee_coregs: Optional[FilersType] = field(
        default=None,
        metadata={
            "name": "abseeCoregs",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coreg",
        },
    )
    absee_accession_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "abseeAccessionNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coreg",
            "pattern": r"[*]{0}|[0-9]{1,10}\-[0-9]{1,2}\-[0-9]{1,6}",
        },
    )


@dataclass
class EdgarSubmission:
    """
    This is the root element for an EDGARLink Online submission.
    """

    class Meta:
        name = "edgarSubmission"
        namespace = "http://www.sec.gov/edgar/coreg"

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
    sponsor_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "sponsorId",
            "type": "Element",
            "pattern": r"\d{1,10}",
        },
    )
    abs_asset_classes: Optional[AbsAssetClassTypes] = field(
        default=None,
        metadata={
            "name": "absAssetClasses",
            "type": "Element",
        },
    )
    abs_sub_asset_classes: Optional[AbsSubAssetClassTypes] = field(
        default=None,
        metadata={
            "name": "absSubAssetClasses",
            "type": "Element",
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
    accession_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "accessionNumber",
            "type": "Element",
            "pattern": r"[*]{0}|[0-9]{1,10}\-[0-9]{1,2}\-[0-9]{1,6}",
        },
    )
    inv_company: Optional[InvCompanyType] = field(
        default=None,
        metadata={
            "name": "invCompany",
            "type": "Element",
        },
    )
    items: Optional[ItemsType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    items_type2: Optional[ItemsType2] = field(
        default=None,
        metadata={
            "name": "itemsType2",
            "type": "Element",
        },
    )
    item_submission_type: Optional[ItemSubmissionType] = field(
        default=None,
        metadata={
            "name": "itemSubmissionType",
            "type": "Element",
        },
    )
    fiscal_year: Optional[FiscalYearType] = field(
        default=None,
        metadata={
            "name": "fiscalYear",
            "type": "Element",
        },
    )
    depositor: Optional[DepositorType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    successor_company: Optional[SuccessorType] = field(
        default=None,
        metadata={
            "name": "successorCompany",
            "type": "Element",
        },
    )
    sub_company_filer: Optional[SubjectCompanyType] = field(
        default=None,
        metadata={
            "name": "subCompanyFiler",
            "type": "Element",
        },
    )
    shell_company_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "shellCompanyFlag",
            "type": "Element",
            "pattern": r"true|false",
        },
    )
    voluntary_filer_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "voluntaryFilerFlag",
            "type": "Element",
            "pattern": r"true|false",
        },
    )
    well_known_seasoned_issuer_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "wellKnownSeasonedIssuerFlag",
            "type": "Element",
            "pattern": r"true|false",
        },
    )
    filer_new_registrant_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerNewRegistrantFlag",
            "type": "Element",
            "pattern": r"true|false",
        },
    )
    pursuant_general_instruction_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "pursuantGeneralInstructionFlag",
            "type": "Element",
            "pattern": r"true|false",
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
    accelerated_filer_status: Optional[AcceleratedStatusType] = field(
        default=None,
        metadata={
            "name": "acceleratedFilerStatus",
            "type": "Element",
        },
    )
    small_business_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "smallBusinessFlag",
            "type": "Element",
            "pattern": r"true|false",
        },
    )
    is_combo_submission: Optional[str] = field(
        default=None,
        metadata={
            "name": "isComboSubmission",
            "type": "Element",
            "pattern": r"true|false",
        },
    )
    absee_elements: Optional[AbsEeEelments] = field(
        default=None,
        metadata={
            "name": "abseeElements",
            "type": "Element",
        },
    )
    selected_category: Optional[str] = field(
        default=None,
        metadata={
            "name": "selectedCategory",
            "type": "Element",
            "min_length": 1,
            "max_length": 50,
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
