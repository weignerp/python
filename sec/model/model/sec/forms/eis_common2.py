from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union

from xsdata.models.datatype import XmlDate

from model.sec.forms.eis_state_codes import StateCountryCode

__NAMESPACE__ = "http://www.sec.gov/edgar/common"


class AcceleratedStatusType(Enum):
    NON_ACCELERATED_FILER = "Non-Accelerated Filer"
    ACCELERATED_FILER = "Accelerated Filer"
    LARGE_ACCELERATED_FILER = "Large Accelerated Filer"
    NOT_APPLICABLE = "Not Applicable"


class ActType(Enum):
    """For certain filings by investment companies, the tag identifies Act or Acts
    when the form type may be filed under more than one Act.

    Valid values when required are 33, 34, 40, or 33 40.  Choose value
    from the list displayed when the arrow is selected.
    """

    VALUE_33 = "33"
    VALUE_40 = "40"
    VALUE_33_40 = "33 40"
    VALUE_34 = "34"


class BaseDocumentType(Enum):
    """Enter the type of this document.

    Select a value from the list displayed when the arrow is selected.
    Type any additional characters in the field to accurately specify a
    valid EDGAR document type.
    """

    CORRESP = "CORRESP"
    COVER = "COVER"
    EU_1 = "EU-1"
    EX_1 = "EX-1"
    EX_1_02 = "EX-1.02"
    EX_10 = "EX-10"
    EX_100_CAL = "EX-100.CAL"
    EX_100_DEF = "EX-100.DEF"
    EX_100_INS = "EX-100.INS"
    EX_100_LAB = "EX-100.LAB"
    EX_100_PRE = "EX-100.PRE"
    EX_100_REF = "EX-100.REF"
    EX_100_SCH = "EX-100.SCH"
    EX_101_CAL = "EX-101.CAL"
    EX_101_DEF = "EX-101.DEF"
    EX_101_INS = "EX-101.INS"
    EX_101_LAB = "EX-101.LAB"
    EX_101_PRE = "EX-101.PRE"
    EX_101_REF = "EX-101.REF"
    EX_101_SCH = "EX-101.SCH"
    EX_11 = "EX-11"
    EX_12 = "EX-12"
    EX_13 = "EX-13"
    EX_14 = "EX-14"
    EX_15 = "EX-15"
    EX_16 = "EX-16"
    EX_17 = "EX-17"
    EX_18 = "EX-18"
    EX_19 = "EX-19"
    EX_2 = "EX-2"
    EX_2_01_CAL = "EX-2.01.CAL"
    EX_2_01_DEF = "EX-2.01.DEF"
    EX_2_01_INS = "EX-2.01.INS"
    EX_2_01_LAB = "EX-2.01.LAB"
    EX_2_01_PRE = "EX-2.01.PRE"
    EX_2_01_REF = "EX-2.01.REF"
    EX_2_01_SCH = "EX-2.01.SCH"
    EX_20 = "EX-20"
    EX_21 = "EX-21"
    EX_22 = "EX-22"
    EX_23 = "EX-23"
    EX_24 = "EX-24"
    EX_25 = "EX-25"
    EX_25_A = "EX-25/A"
    EX_26 = "EX-26"
    EX_3 = "EX-3"
    EX_31 = "EX-31"
    EX_32 = "EX-32"
    EX_33 = "EX-33"
    EX_34 = "EX-34"
    EX_35 = "EX-35"
    EX_4 = "EX-4"
    EX_5 = "EX-5"
    EX_7 = "EX-7"
    EX_8 = "EX-8"
    EX_9 = "EX-9"
    EX_95 = "EX-95"
    EX_99 = "EX-99"
    EX_99_1_CHARTER = "EX-99.1 CHARTER"
    EX_99_10_12_B1_PLAN = "EX-99.10 12B1 PLAN"
    EX_99_11_OPIN_COUNSL = "EX-99.11 OPIN COUNSL"
    EX_99_12_REV_RULING = "EX-99.12 REV RULING"
    EX_99_12_TAX_OPINION = "EX-99.12 TAX OPINION"
    EX_99_13_OTH_CONTRCT = "EX-99.13 OTH CONTRCT"
    EX_99_14_OTH_CONSENT = "EX-99.14 OTH CONSENT"
    EX_99_15_OTH_FIN_ST = "EX-99.15 OTH FIN ST"
    EX_99_16_PWR_OF_ATTY = "EX-99.16 PWR OF ATTY"
    EX_99_17_AS_APPROP = "EX-99.17 (as approp)"
    EX_99_2_BYLAWS = "EX-99.2 BYLAWS"
    EX_99_2_OPIN_COUNSEL = "EX-99.2 OPIN COUNSEL"
    EX_99_2_A_CHARTER = "EX-99.2A CHARTER"
    EX_99_2_B_BYLAWS = "EX-99.2B BYLAWS"
    EX_99_2_C_VOTING_TRST = "EX-99.2C VOTING TRST"
    EX_99_2_D_HOLDERS_RTS = "EX-99.2D HOLDERS RTS"
    EX_99_2_E_DIV_REIN_PL = "EX-99.2E DIV REIN PL"
    EX_99_2_F_SUBSID_DEBT = "EX-99.2F SUBSID DEBT"
    EX_99_2_G_ADVSR_CONTR = "EX-99.2G ADVSR CONTR"
    EX_99_2_H_DISTR_CONTR = "EX-99.2H DISTR CONTR"
    EX_99_2_I_O_D_BENEFTS = "EX-99.2I O&D BENEFTS"
    EX_99_2_J_CUST_CONTR = "EX-99.2J CUST CONTR"
    EX_99_2_K_OTH_CONTRCT = "EX-99.2K OTH CONTRCT"
    EX_99_2_L_OPIN_COUNSL = "EX-99.2L OPIN COUNSL"
    EX_99_2_M_CNSNT_SRVCE = "EX-99.2M CNSNT SRVCE"
    EX_99_2_N_OTH_CONSENT = "EX-99.2N OTH CONSENT"
    EX_99_2_O_OTH_FIN_ST = "EX-99.2O OTH FIN ST"
    EX_99_2_P_STOCK_LTR = "EX-99.2P STOCK LTR"
    EX_99_2_Q_RETRMT_PLAN = "EX-99.2Q RETRMT PLAN"
    EX_99_2_R_CODE_ETH = "EX-99.2R CODE ETH"
    EX_99_20_OPIN_COUNSL = "EX-99.20 OPIN COUNSL"
    EX_99_21_7_R = "EX-99.21 7-R"
    EX_99_22_BD_REG = "EX-99.22 BD REG"
    EX_99_3_OTHER_FIN_ST = "EX-99.3 OTHER FIN ST"
    EX_99_3_VOTING_TRUST = "EX-99.3 VOTING TRUST"
    EX_99_31_MA_NR = "EX-99.31 MA-NR"
    EX_99_32_APP_CRT_DOC = "EX-99.32 APP CRT DOC"
    EX_99_33_APP_REG_DOC = "EX-99.33 APP REG DOC"
    EX_99_34_OPIN_COUNSL = "EX-99.34 OPIN COUNSL"
    EX_99_4_ACQ_AGREEMNT = "EX-99.4 ACQ AGREEMNT"
    EX_99_4_UNREG_ISSUER = "EX-99.4 UNREG ISSUER"
    EX_99_5_HOLDERS_RTS = "EX-99.5 HOLDERS RTS"
    EX_99_6_ADVSER_CONTR = "EX-99.6 ADVSER CONTR"
    EX_99_7_DISTR_CONTR = "EX-99.7 DISTR CONTR"
    EX_99_77_B_ACCT_LTTR = "EX-99.77B ACCT LTTR"
    EX_99_77_C_VOTES = "EX-99.77C VOTES"
    EX_99_77_D_POLICIES = "EX-99.77D POLICIES"
    EX_99_77_E_LEGAL = "EX-99.77E LEGAL"
    EX_99_77_F_CHNG_DEBT = "EX-99.77F CHNG DEBT"
    EX_99_77_G_DEFAULTS = "EX-99.77G DEFAULTS"
    EX_99_77_H_CHNG_CNTRL = "EX-99.77H CHNG CNTRL"
    EX_99_77_I_NEW_SECUR = "EX-99.77I NEW SECUR"
    EX_99_77_J_REVALUATN = "EX-99.77J REVALUATN"
    EX_99_77_K_CHNG_ACCNT = "EX-99.77K CHNG ACCNT"
    EX_99_77_L_NEW_ACCTNG = "EX-99.77L NEW ACCTNG"
    EX_99_77_M_MERGERS = "EX-99.77M MERGERS"
    EX_99_77_N_RULE_2_A_7 = "EX-99.77N RULE 2A-7"
    EX_99_77_O_RULE_10_F_3 = "EX-99.77O RULE 10F-3"
    EX_99_77_P_EXMPT_INFO = "EX-99.77P EXMPT INFO"
    EX_99_77_Q1_OTHR_EXHB = "EX-99.77Q1 OTHR EXHB"
    EX_99_77_Q2_ITEM_405 = "EX-99.77Q2 ITEM 405"
    EX_99_8_O_D_BENEFTS = "EX-99.8 O&D BENEFTS"
    EX_99_9_CUST_CONTRCT = "EX-99.9 CUST CONTRCT"
    EX_99_906_CERT = "EX-99.906 CERT"
    EX_99_A_BD_DIR_RESOL = "EX-99.a BD-DIR-RESOL"
    EX_99_A_CHARTER = "EX-99.a CHARTER"
    EX_99_A1_INDNTR_ORGN = "EX-99.A1 INDNTR ORGN"
    EX_99_A10_PERIODC_PP = "EX-99.A10 PERIODC PP"
    EX_99_A11_CODE_ETH = "EX-99.A11 CODE ETH"
    EX_99_A2_INDNTR_PMT = "EX-99.A2 INDNTR PMT"
    EX_99_A3_A_DIST_CONTR = "EX-99.A3A DIST CONTR"
    EX_99_A3_B_DEALER_AGR = "EX-99.A3B DEALER AGR"
    EX_99_A3_C_SCH_COMMIS = "EX-99.A3C SCH COMMIS"
    EX_99_A4_OTHER_AGRMT = "EX-99.A4 OTHER AGRMT"
    EX_99_A5_FORM_SECRTY = "EX-99.A5 FORM/SECRTY"
    EX_99_A6_CERT_BYLAWS = "EX-99.A6 CERT/BYLAWS"
    EX_99_A7_INSR_POLICY = "EX-99.A7 INSR POLICY"
    EX_99_A8_DEPOSIT_AGR = "EX-99.A8 DEPOSIT AGR"
    EX_99_A9_OTHER_CONTR = "EX-99.A9 OTHER CONTR"
    EX_99_B_BYLAWS = "EX-99.b BYLAWS"
    EX_99_B_CUST_AGRMETS = "EX-99.b CUST-AGRMETS"
    EX_99_B1_NOTIC_SHLDR = "EX-99.B1 NOTIC/SHLDR"
    EX_99_B2_ANRPT_SHLDR = "EX-99.B2 ANRPT/SHLDR"
    EX_99_C_HOLDERS_RTS = "EX-99.c HOLDERS RTS"
    EX_99_C_UNDER_CONTRT = "EX-99.c UNDER CONTRT"
    EX_99_C1_ACCT_CONSNT = "EX-99.C1 ACCT CONSNT"
    EX_99_C2_EVAL_CONSNT = "EX-99.C2 EVAL CONSNT"
    EX_99_C3_RTG_AGY_OPN = "EX-99.C3 RTG AGY OPN"
    EX_99_C4_TAX_OPINION = "EX-99.C4 TAX OPINION"
    EX_99_C5_REV_RULING = "EX-99.C5 REV RULING"
    EX_99_C6_OTHER_OPIN = "EX-99.C6 OTHER OPIN"
    EX_99_CERT = "EX-99.CERT"
    EX_99_CODE_ETH = "EX-99.CODE ETH"
    EX_99_D_ADVSR_CONTR = "EX-99.d ADVSR CONTR"
    EX_99_D_CONTRACTS = "EX-99.d CONTRACTS"
    EX_99_E_APPLICATIONS = "EX-99.e APPLICATIONS"
    EX_99_E_UNDR_CONTR = "EX-99.e UNDR CONTR"
    EX_99_F_BONUS_PROFIT = "EX-99.f BONUS PROFIT"
    EX_99_F_DEP_CERT_BYL = "EX-99.f DEP CERT/BYL"
    EX_99_G_CUST_AGREEMT = "EX-99.g CUST AGREEMT"
    EX_99_G_REINS_CONTRT = "EX-99.g REINS CONTRT"
    EX_99_H_OTH_MAT_CONT = "EX-99.h OTH MAT CONT"
    EX_99_H_PARTIC_AGREE = "EX-99.h PARTIC AGREE"
    EX_99_I_ADMIN_CONTRT = "EX-99.i ADMIN CONTRT"
    EX_99_I_LEGAL_OPININ = "EX-99.i LEGAL OPININ"
    EX_99_J_OTH_MAT_CONT = "EX-99.j OTH MAT CONT"
    EX_99_J_OTHER_OPININ = "EX-99.j OTHER OPININ"
    EX_99_K_LEGAL_OPININ = "EX-99.k LEGAL OPININ"
    EX_99_K_OMT_FIN_STAT = "EX-99.k OMT FIN STAT"
    EX_99_L_ACTUARIAL_OP = "EX-99.l ACTUARIAL OP"
    EX_99_L_INT_CAP_AGRE = "EX-99.l INT CAP AGRE"
    EX_99_M_12_B_1_PLAN = "EX-99.m 12B-1 PLAN"
    EX_99_M_CALCULATION = "EX-99.m CALCULATION"
    EX_99_N_18_F_3_PLAN = "EX-99.n 18F-3 PLAN"
    EX_99_N_OTH_OPINIONS = "EX-99.n OTH OPINIONS"
    EX_99_O_OMITD_FIN_ST = "EX-99.o OMITD FIN ST"
    EX_99_P_CODE_ETH = "EX-99.p CODE ETH"
    EX_99_P_INIT_CAP_AGR = "EX-99.p INIT CAP AGR"
    EX_99_Q_REDEEM_EXEMP = "EX-99.q REDEEM EXEMP"
    EX_99_RULE23_C1 = "EX-99.Rule23C1"
    EX_106 = "EX-106"
    GRAPHIC = "GRAPHIC"
    ORGCHART = "ORGCHART"


@dataclass
class ContactEmailType:
    class Meta:
        name = "CONTACT_EMAIL_TYPE"

    contact_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "contactName",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "min_length": 1,
            "max_length": 30,
            "pattern": r"[A-Za-z0-9!#-$%():;'@\*\+\-/=\?\^_`~{|},. \\\s<>&\"\[\]]{1,30}",
        },
    )
    contact_phone_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "contactPhoneNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "min_length": 1,
            "max_length": 20,
            "pattern": r"[a-zA-Z0-9\s#(),.\-]{1,20}",
        },
    )
    contact_email_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "contactEmailAddress",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "min_length": 4,
            "max_length": 80,
            "pattern": r"([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,7}|[0-9]{1,3})(\]?)",
        },
    )


@dataclass
class ContactType:
    class Meta:
        name = "CONTACT_TYPE"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "min_length": 1,
            "max_length": 30,
            "pattern": r"[A-Za-z0-9!#-$%():;'@\*\+\-/=\?\^_`~{|},. \\\s<>&\"\[\]]{1,30}",
        },
    )
    phone_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "phoneNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "min_length": 1,
            "max_length": 20,
            "pattern": r"[a-zA-Z0-9\-]{1,20}",
        },
    )


@dataclass
class DepositorType:
    class Meta:
        name = "DEPOSITOR_TYPE"

    depositor_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "depositorId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    depositor_file_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "depositorFileNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "pattern": r"\d{1,3}-\d{1,8}-[a-zA-Z0-9]{1,4}|\d{1,3}-\d{1,8}",
        },
    )


@dataclass
class FilerCredentials:
    class Meta:
        name = "FILER_CREDENTIALS"

    cik: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    ccc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "length": 8,
        },
    )


@dataclass
class FilerType:
    class Meta:
        name = "FILER_TYPE"

    filer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    filer_ccc: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerCcc",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "length": 8,
        },
    )
    filer_file_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerFileNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "pattern": r"\d{1,3}-\d{1,8}-[a-zA-Z0-9]{1,4}|\d{1,3}-\d{1,8}",
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
            "namespace": "http://www.sec.gov/edgar/common",
            "min_occurs": 1,
            "pattern": r"\d{2,2}/\d{2,2}",
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
            "namespace": "http://www.sec.gov/edgar/common",
            "pattern": r"true|false",
        },
    )
    delaying_amendment_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "delayingAmendmentFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "pattern": r"true|false",
        },
    )
    override_internet_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "overrideInternetFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "pattern": r"true|false",
        },
    )
    return_copy_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "returnCopyFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "pattern": r"true|false",
        },
    )
    serial_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "serialFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "pattern": r"true|false",
        },
    )


class InvCompanyType(Enum):
    """Identifies the investment company type of the acquiring company.

    Choose a value from the list displayed when the arrow is selected.
    """

    N_1_A = "N-1A"
    N_1 = "N-1"
    N_2 = "N-2"
    N_3 = "N-3"
    N_4 = "N-4"
    N_5 = "N-5"
    N_6 = "N-6"
    S_1_OR_S_3 = "S-1 or S-3"
    S_6 = "S-6"


class LiveTestType(Enum):
    """Marks submission to be treated as a LIVE filing.

    Unless the "TEST" button is selected, the filing will be treated by
    EDGAR as a live filing and, if accepted, be disseminated. Submit
    live filings in LIVE mode if using EDGARLink Online. A filing with
    TEST selected cannot be changed into a live filing.
    """

    LIVE = "LIVE"
    TEST = "TEST"


class ModuleOrSegmentFlag(Enum):
    """M: is module.   S: is segment"""

    M = "M"
    S = "S"


@dataclass
class NameType2:
    class Meta:
        name = "NAME_TYPE_2"

    first_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "firstName",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "min_length": 1,
            "max_length": 150,
        },
    )
    middle_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "middleName",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "min_length": 1,
            "max_length": 150,
        },
    )
    last_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastName",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "min_length": 1,
            "max_length": 150,
        },
    )


class NewFileNumType(Enum):
    NEW = "NEW"


@dataclass
class NotificationType:
    class Meta:
        name = "NOTIFICATION_TYPE"

    internet_notification_address: List[str] = field(
        default_factory=list,
        metadata={
            "name": "internetNotificationAddress",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "min_occurs": 1,
            "min_length": 4,
            "max_length": 80,
            "pattern": r"([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,7}|[0-9]{1,3})(\]?)",
        },
    )


@dataclass
class OtherType:
    class Meta:
        name = "OTHER_TYPE"

    other: object = field(
        default="Other",
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
        },
    )
    other_specification: Optional[str] = field(
        default=None,
        metadata={
            "name": "otherSpecification",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "max_length": 255,
        },
    )


class RptOwnerRelationshipType(Enum):
    DIRECTOR = "DIRECTOR"
    OFFICER = "OFFICER"
    OWNER = "OWNER"
    OTHER = "OTHER"


@dataclass
class SignatureType:
    class Meta:
        name = "SIGNATURE_TYPE"

    date_signed: Optional[str] = field(
        default=None,
        metadata={
            "name": "dateSigned",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "pattern": r"\d{1,2}-\d{1,2}-\d{4}",
        },
    )
    name_of_applicant: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfApplicant",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "min_length": 1,
            "max_length": 150,
            "pattern": r"([A-Za-z0-9\s!\\#$(),.:;=@'\-{}|/&]+)",
        },
    )
    signature: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "min_length": 1,
            "max_length": 150,
            "pattern": r"([A-Za-z0-9\s!\\#$(),.:;=@'\-{}|/&]+)",
        },
    )
    signer_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "signerName",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "min_length": 1,
            "max_length": 150,
            "pattern": r"([A-Za-z0-9\s!\\#$(),.:;=@'\-{}|/&]+)",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "min_length": 1,
            "max_length": 150,
        },
    )


@dataclass
class SignatureType2:
    class Meta:
        name = "SIGNATURE_TYPE_2"

    signature: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "min_length": 1,
            "max_length": 150,
        },
    )
    signer_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "signerName",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "min_length": 1,
            "max_length": 150,
            "pattern": r"([A-Za-z0-9\s!\\#$(),.:;=@'\-{}|/&]+)",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "min_length": 1,
            "max_length": 150,
        },
    )
    date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "pattern": r"\d{1,2}-\d{1,2}-\d{4}",
        },
    )


@dataclass
class SignatureType3:
    class Meta:
        name = "SIGNATURE_TYPE_3"

    signature: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "min_length": 1,
            "max_length": 150,
        },
    )
    signer_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "signerName",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "min_length": 1,
            "max_length": 150,
            "pattern": r"([A-Za-z0-9\s!\\#$(),.:;=@'\-{}|/&]+)",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "min_length": 1,
            "max_length": 150,
        },
    )
    date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "pattern": r"\d{1,2}-\d{1,2}-\d{4}",
        },
    )


@dataclass
class SignatureType4:
    class Meta:
        name = "SIGNATURE_TYPE_4"

    signature_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "signatureName",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "min_length": 1,
            "max_length": 30,
        },
    )
    signature_title: Optional[str] = field(
        default=None,
        metadata={
            "name": "signatureTitle",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "min_length": 1,
            "max_length": 150,
        },
    )
    signature_phone_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "signaturePhoneNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "pattern": r"[a-zA-Z0-9\s#(),.\-]{1,20}",
        },
    )
    signature_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "signatureDate",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
        },
    )


class SroType(Enum):
    """Identifies one or more stock exchanges or other self-regulatory
    organizations on which the issuer's securities are listed or traded.

    Choose values from the list displayed. If none applies, select the
    value "NONE".
    """

    NONE = "NONE"
    AMEX = "AMEX"
    ARCA = "ARCA"
    BSE = "BSE"
    CBOE = "CBOE"
    CHX = "CHX"
    FINRA = "FINRA"
    ISE = "ISE"
    NASD = "NASD"
    NSX = "NSX"
    NYSE = "NYSE"
    PCX = "PCX"
    PHLX = "PHLX"


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
    VALUE_13_H = "13H"
    VALUE_13_H_A = "13H-A"
    VALUE_13_H_I = "13H-I"
    VALUE_13_H_R = "13H-R"
    VALUE_13_H_A_1 = "13H/A"
    VALUE_13_H_T = "13H-T"
    VALUE_144 = "144"
    VALUE_144_A = "144/A"
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
    VALUE_1_E_AD = "1-E AD"
    VALUE_1_E_AD_A = "1-E AD/A"
    VALUE_1_E = "1-E"
    VALUE_1_E_A = "1-E/A"
    VALUE_20_F = "20-F"
    VALUE_20_F_A = "20-F/A"
    VALUE_20_FR12_B = "20FR12B"
    VALUE_20_FR12_B_A = "20FR12B/A"
    VALUE_20_FR12_G = "20FR12G"
    VALUE_20_FR12_G_A = "20FR12G/A"
    VALUE_24_F_2_NT = "24F-2NT"
    VALUE_24_F_2_NT_A = "24F-2NT/A"
    VALUE_25 = "25"
    VALUE_25_A = "25/A"
    VALUE_2_E = "2-E"
    VALUE_2_E_A = "2-E/A"
    VALUE_305_B2 = "305B2"
    VALUE_305_B2_A = "305B2/A"
    VALUE_40_17_F1 = "40-17F1"
    VALUE_40_17_F1_A = "40-17F1/A"
    VALUE_40_17_F2 = "40-17F2"
    VALUE_40_17_F2_A = "40-17F2/A"
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
    VALUE_424_B1 = "424B1"
    VALUE_424_B2 = "424B2"
    VALUE_424_B3 = "424B3"
    VALUE_424_B4 = "424B4"
    VALUE_424_B5 = "424B5"
    VALUE_424_B7 = "424B7"
    VALUE_424_B8 = "424B8"
    VALUE_425 = "425"
    VALUE_485_APOS = "485APOS"
    VALUE_485_BPOS = "485BPOS"
    VALUE_485_BXT = "485BXT"
    VALUE_486_APOS = "486APOS"
    VALUE_486_BPOS = "486BPOS"
    VALUE_487 = "487"
    VALUE_497 = "497"
    VALUE_497_AD = "497AD"
    VALUE_497_H2 = "497H2"
    VALUE_497_J = "497J"
    VALUE_497_K1 = "497K1"
    VALUE_497_K2 = "497K2"
    VALUE_497_K3_A = "497K3A"
    VALUE_497_K3_B = "497K3B"
    VALUE_6_K = "6-K"
    VALUE_6_K_A = "6-K/A"
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
    ABS_15_G = "ABS-15G"
    ABS_15_G_A = "ABS-15G/A"
    ANNLRPT = "ANNLRPT"
    ANNLRPT_A = "ANNLRPT/A"
    ARS = "ARS"
    ARS_A = "ARS/A"
    AW = "AW"
    AW_WD = "AW WD"
    CB = "CB"
    CB_A = "CB/A"
    DEF_14_A = "DEF 14A"
    DEF_14_C = "DEF 14C"
    DEFA14_A = "DEFA14A"
    DEFA14_C = "DEFA14C"
    DEFC14_A = "DEFC14A"
    DEFC14_C = "DEFC14C"
    DEFM14_A = "DEFM14A"
    DEFM14_C = "DEFM14C"
    DEFN14_A = "DEFN14A"
    DEFR14_A = "DEFR14A"
    DEFR14_C = "DEFR14C"
    DEL_AM = "DEL AM"
    DFAN14_A = "DFAN14A"
    DFRN14_A = "DFRN14A"
    DSTRBRPT = "DSTRBRPT"
    DSTRBRPT_A = "DSTRBRPT/A"
    F_1 = "F-1"
    F_1_A = "F-1/A"
    F_10 = "F-10"
    F_10_A = "F-10/A"
    F_10_EF = "F-10EF"
    F_10_POS = "F-10POS"
    F_1_MEF = "F-1MEF"
    F_3 = "F-3"
    F_3_A = "F-3/A"
    F_3_ASR = "F-3ASR"
    F_3_D = "F-3D"
    F_3_DPOS = "F-3DPOS"
    F_3_MEF = "F-3MEF"
    F_4 = "F-4"
    F_4_A = "F-4/A"
    F_4_EF = "F-4EF"
    F_4_MEF = "F-4MEF"
    F_4_POS = "F-4 POS"
    F_6 = "F-6"
    F_6_A = "F-6/A"
    F_6_EF = "F-6EF"
    F_6_POS = "F-6 POS"
    F_7 = "F-7"
    F_7_A = "F-7/A"
    F_7_POS = "F-7 POS"
    F_8 = "F-8"
    F_8_A = "F-8/A"
    F_80 = "F-80"
    F_80_A = "F-80/A"
    F_8_POS = "F-8 POS"
    F_80_POS = "F-80POS"
    F_9 = "F-9"
    F_9_A = "F-9/A"
    F_9_EF = "F-9EF"
    F_9_POS = "F-9 POS"
    F_N = "F-N"
    F_N_A = "F-N/A"
    FWP = "FWP"
    F_X = "F-X"
    F_X_A = "F-X/A"
    N_1 = "N-1"
    N_1_A = "N-1/A"
    N_14 = "N-14"
    N_14_A = "N-14/A"
    N_14_8_C = "N-14 8C"
    N_14_8_C_A = "N-14 8C/A"
    N_14_MEF = "N-14MEF"
    N_18_F1 = "N-18F1"
    N_18_F1_A = "N-18F1/A"
    N_1_A_1 = "N-1 A"
    N_1_A_A = "N-1A/A"
    N_2 = "N-2"
    N_2_A = "N-2/A"
    N_23_C_2 = "N-23C-2"
    N_23_C_2_A = "N-23C-2/A"
    N_23_C3_A = "N-23C3A"
    N_23_C3_A_A = "N-23C3A/A"
    N_23_C3_B = "N-23C3B"
    N_23_C3_B_A = "N-23C3B/A"
    N_23_C3_C = "N-23C3C"
    N_23_C3_C_A = "N-23C3C/A"
    N_27_D_1 = "N-27D-1"
    N_27_D_1_A = "N-27D-1/A"
    N_2_MEF = "N-2MEF"
    N_3 = "N-3"
    N_3_A = "N-3/A"
    N_30_B_2 = "N-30B-2"
    N_30_D = "N-30D"
    N_30_D_A = "N-30D/A"
    N_4 = "N-4"
    N_4_A = "N-4/A"
    N_5 = "N-5"
    N_5_A = "N-5/A"
    N_54_A = "N-54A"
    N_54_A_A = "N-54A/A"
    N_54_C = "N-54C"
    N_54_C_A = "N-54C/A"
    N_6 = "N-6"
    N_6_A = "N-6/A"
    N_6_F = "N-6F"
    N_6_F_A = "N-6F/A"
    N_8_A = "N-8A"
    N_8_A_A = "N-8A/A"
    N_8_B_2 = "N-8B-2"
    N_8_B_2_A = "N-8B-2/A"
    N_8_B_3 = "N-8B-3"
    N_8_B_3_A = "N-8B-3/A"
    N_8_B_4 = "N-8B-4"
    N_8_B_4_A = "N-8B-4/A"
    N_8_F = "N-8F"
    N_8_F_A = "N-8F/A"
    N_CSR = "N-CSR"
    N_CSR_A = "N-CSR/A"
    N_CSRS = "N-CSRS"
    N_CSRS_A = "N-CSRS/A"
    N_PX = "N-PX"
    N_PX_A = "N-PX/A"
    N_PX_FM = "N-PX-FM"
    N_PX_FM_A = "N-PX-FM/A"
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
    NT_NCSR = "NT-NCSR"
    NT_NCSR_A = "NT-NCSR/A"
    NT_NSAR = "NT-NSAR"
    NT_NSAR_A = "NT-NSAR/A"
    POS_8_C = "POS 8C"
    POS_AM = "POS AM"
    POS_AMI = "POS AMI"
    POS_EX = "POS EX"
    POS462_B = "POS462B"
    POS462_C = "POS462C"
    POSASR = "POSASR"
    PRE_14_A = "PRE 14A"
    PRE_14_C = "PRE 14C"
    PREC14_A = "PREC14A"
    PREC14_C = "PREC14C"
    PREM14_A = "PREM14A"
    PREM14_C = "PREM14C"
    PREN14_A = "PREN14A"
    PRER14_A = "PRER14A"
    PRER14_C = "PRER14C"
    PRRN14_A = "PRRN14A"
    PX14_A6_G = "PX14A6G"
    PX14_A6_N = "PX14A6N"
    QRTLYRPT = "QRTLYRPT"
    QRTLYRPT_A = "QRTLYRPT/A"
    RW = "RW"
    RW_WD = "RW WD"
    S_1 = "S-1"
    S_1_A = "S-1/A"
    S_11 = "S-11"
    S_11_A = "S-11/A"
    S_11_MEF = "S-11MEF"
    S_1_MEF = "S-1MEF"
    S_20 = "S-20"
    S_20_A = "S-20/A"
    S_3 = "S-3"
    S_3_A = "S-3/A"
    S_3_ASR = "S-3ASR"
    S_3_D = "S-3D"
    S_3_DPOS = "S-3DPOS"
    S_3_MEF = "S-3MEF"
    S_4 = "S-4"
    S_4_A = "S-4/A"
    S_4_POS = "S-4 POS"
    S_4_EF = "S-4EF"
    S_4_MEF = "S-4MEF"
    S_6 = "S-6"
    S_6_A = "S-6/A"
    S_8_POS = "S-8 POS"
    S_8 = "S-8"
    S_B = "S-B"
    S_B_A = "S-B/A"
    S_BMEF = "S-BMEF"
    SC_13_D = "SC 13D"
    SC_13_D_A = "SC 13D/A"
    SC_13_E1 = "SC 13E1"
    SC_13_E1_A = "SC 13E1/A"
    SC_13_E3 = "SC 13E3"
    SC_13_E3_A = "SC 13E3/A"
    SC_13_G = "SC 13G"
    SC_13_G_A = "SC 13G/A"
    SC_14_D9 = "SC 14D9"
    SC_14_D9_A = "SC 14D9/A"
    SC_14_F1 = "SC 14F1"
    SC_14_F1_A = "SC 14F1/A"
    SC_TO_C = "SC TO-C"
    SC_TO_I = "SC TO-I"
    SC_TO_I_A = "SC TO-I/A"
    SC_TO_T = "SC TO-T"
    SC_TO_T_A = "SC TO-T/A"
    SC13_E4_F = "SC13E4F"
    SC13_E4_F_A = "SC13E4F/A"
    SC14_D1_F = "SC14D1F"
    SC14_D1_F_A = "SC14D1F/A"
    SC14_D9_C = "SC14D9C"
    SC14_D9_F = "SC14D9F"
    SC14_D9_F_A = "SC14D9F/A"
    SH_ER = "SH-ER"
    SH_ER_A = "SH-ER/A"
    SH_NT = "SH-NT"
    SH_NT_A = "SH-NT/A"
    SP_15_D2 = "SP 15D2"
    SP_15_D2_A = "SP 15D2/A"
    SUPPL = "SUPPL"
    T_3 = "T-3"
    T_3_A = "T-3/A"
    T_6 = "T-6"
    T_6_A = "T-6/A"
    UNDER = "UNDER"
    UNDER_A = "UNDER/A"
    ETR = "ETR"
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
    DRSLTR = "DRSLTR"
    SD = "SD"
    SD_A = "SD/A"


class YesNoType(Enum):
    Y = "Y"
    N = "N"


@dataclass
class AddressType:
    class Meta:
        name = "ADDRESS_TYPE"

    street1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "min_length": 1,
            "max_length": 40,
        },
    )
    street2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "min_length": 1,
            "max_length": 40,
        },
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "min_length": 1,
            "max_length": 30,
        },
    )
    state_or_country: Optional[StateCountryCode] = field(
        default=None,
        metadata={
            "name": "stateOrCountry",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
        },
    )
    zip_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "zipCode",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "min_length": 1,
            "max_length": 10,
            "pattern": r"[0-9A-Za-z #\-]*",
        },
    )


@dataclass
class EdgarliteAddressType:
    class Meta:
        name = "EDGARLITE_ADDRESS_TYPE"

    street1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "min_length": 1,
            "max_length": 40,
        },
    )
    street2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "min_length": 1,
            "max_length": 40,
        },
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "min_length": 1,
            "max_length": 30,
        },
    )
    state_or_country_code: Optional[StateCountryCode] = field(
        default=None,
        metadata={
            "name": "stateOrCountryCode",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
        },
    )
    state_or_country: Optional[str] = field(
        default=None,
        metadata={
            "name": "stateOrCountry",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "min_length": 1,
            "max_length": 50,
        },
    )
    zip_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "zipCode",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "min_length": 1,
            "max_length": 10,
            "pattern": r"[0-9A-Za-z #\-]*",
        },
    )


@dataclass
class EdgarDocumentType:
    """Document names must be lower case and no longer than thirty-two (32)
    characters in length.

    The names must start with a letter (a-z) and may contain numbers
    (0-9) with no spaces.  Document names may contain one period (.),
    one hyphen (-), and one underscore (_) character and must end with
    *.htm, *.txt, *.pdf, *.fil, *.jpg, *.gif, *.xml or *.xsd extensions.
    """

    class Meta:
        name = "EDGAR_DOCUMENT_TYPE"

    conformed_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "conformedName",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "min_length": 1,
            "max_length": 32,
            "pattern": r"([a-zA-Z0-9]+[\w\._\-]*)([\.](([hH][tT][mM])|([tT][xX][tT])|([pP][dD][fF])|([xX][mM][lL])|([jJ][pP][gG])|([gG][iI][fF])|([fF][iI][lL])|([xX][sS][dD])))",
        },
    )
    conformed_document_type: Optional[
        Union[SubmissionType, BaseDocumentType, str]
    ] = field(
        default=None,
        metadata={
            "name": "conformedDocumentType",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "min_length": 4,
            "max_length": 128,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "min_length": 1,
            "max_length": 255,
            "pattern": r"[A-Za-z0-9!#-$%():;'@\*\+\-/=\?\^_`~{|},. \\\s<>&\"\[\]]{1,255}",
        },
    )
    contents: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "min_length": 1,
        },
    )


@dataclass
class InvestmentCompanyType:
    """Identifies the investment company type of the filer.

    Choose a value from the list displayed when the arrow is selected.
    """

    class Meta:
        name = "INVESTMENT_COMPANY_TYPE"

    is_im_company: Optional[str] = field(
        default=None,
        metadata={
            "name": "isImCompany",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "pattern": r"true|false",
        },
    )
    inv_company_type: Optional[InvCompanyType] = field(
        default=None,
        metadata={
            "name": "invCompanyType",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
        },
    )


@dataclass
class ModuleSegmentType:
    """
    Single module segment type.
    """

    class Meta:
        name = "MODULE_SEGMENT_TYPE"

    mod_or_seg_flag: Optional[ModuleOrSegmentFlag] = field(
        default=None,
        metadata={
            "name": "modOrSegFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
        },
    )
    nick_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "nickName",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "min_length": 1,
            "max_length": 15,
            "pattern": r"[a-zA-Z][-_a-zA-Z0-9]*",
        },
    )
    cik: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "pattern": r"\d{1,10}",
        },
    )
    ccc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "length": 8,
        },
    )
    document_type: Optional[Union[SubmissionType, BaseDocumentType, str]] = (
        field(
            default=None,
            metadata={
                "name": "documentType",
                "type": "Element",
                "namespace": "http://www.sec.gov/edgar/common",
                "required": True,
                "min_length": 4,
                "max_length": 128,
            },
        )
    )


@dataclass
class SrosType:
    """Identifies one or more stock exchanges or other self-regulatory
    organizations on which the issuer's securities are listed or traded.

    Choose values from the list displayed. If none applies, select the
    value "None".
    """

    class Meta:
        name = "SROS_TYPE"

    sro_id: List[SroType] = field(
        default_factory=list,
        metadata={
            "name": "sroId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "min_occurs": 1,
            "max_occurs": 13,
        },
    )


@dataclass
class StateCountryType:
    class Meta:
        name = "STATE_COUNTRY_TYPE"

    state_or_country: Optional[StateCountryCode] = field(
        default=None,
        metadata={
            "name": "stateOrCountry",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
        },
    )


@dataclass
class EdgarDocumentsType:
    class Meta:
        name = "EDGAR_DOCUMENTS_TYPE"

    document: List[EdgarDocumentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "min_occurs": 1,
        },
    )


@dataclass
class ModulesSegmentType:
    """
    Group of module segment type elements.
    """

    class Meta:
        name = "MODULES_SEGMENT_TYPE"

    module_segment: List[ModuleSegmentType] = field(
        default_factory=list,
        metadata={
            "name": "moduleSegment",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "min_occurs": 1,
        },
    )
