from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional

from xsdata.models.datatype import XmlDate


@dataclass
class AcqDispNoFoot:
    """
    This element cannot have a footnote.
    """

    class Meta:
        name = "ACQ_DISP_NO_FOOT"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"A|D",
        },
    )


@dataclass
class Footnote:
    class Meta:
        name = "FOOTNOTE"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"F[1-9][0-9]?",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class FootnoteId:
    class Meta:
        name = "FOOTNOTE_ID"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"F[1-9][0-9]?",
        },
    )


@dataclass
class Issuer:
    class Meta:
        name = "ISSUER"

    issuer_cik: Optional[str] = field(
        default=None,
        metadata={
            "name": "issuerCik",
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 10,
            "pattern": r"[0-9]+",
        },
    )
    issuer_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "issuerName",
            "type": "Element",
            "max_length": 150,
        },
    )
    issuer_trading_symbol: Optional[str] = field(
        default=None,
        metadata={
            "name": "issuerTradingSymbol",
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 10,
        },
    )


class ReportingAddressRptOwnerState(Enum):
    VALUE = ""
    SPACE = " "
    SPACE_SPACE = "  "
    AL = "AL"
    AK = "AK"
    AZ = "AZ"
    AR = "AR"
    CA = "CA"
    CO = "CO"
    CT = "CT"
    DE = "DE"
    DC = "DC"
    FL = "FL"
    GA = "GA"
    HI = "HI"
    ID = "ID"
    IL = "IL"
    IN = "IN"
    IA = "IA"
    KS = "KS"
    KY = "KY"
    LA = "LA"
    ME = "ME"
    MD = "MD"
    MA = "MA"
    MI = "MI"
    MN = "MN"
    MS = "MS"
    MO = "MO"
    MT = "MT"
    NE = "NE"
    NV = "NV"
    NH = "NH"
    NJ = "NJ"
    NM = "NM"
    NY = "NY"
    NC = "NC"
    ND = "ND"
    OH = "OH"
    OK = "OK"
    OR = "OR"
    PA = "PA"
    RI = "RI"
    SC = "SC"
    SD = "SD"
    TN = "TN"
    TX = "TX"
    X1 = "X1"
    UT = "UT"
    VT = "VT"
    VA = "VA"
    WA = "WA"
    WV = "WV"
    WI = "WI"
    WY = "WY"
    A0 = "A0"
    A1 = "A1"
    Z4 = "Z4"
    A2 = "A2"
    A3 = "A3"
    A4 = "A4"
    A5 = "A5"
    A6 = "A6"
    A7 = "A7"
    A8 = "A8"
    A9 = "A9"
    B0 = "B0"
    B2 = "B2"
    Y6 = "Y6"
    B3 = "B3"
    B4 = "B4"
    B5 = "B5"
    B6 = "B6"
    B7 = "B7"
    VALUE_1_A = "1A"
    B8 = "B8"
    B9 = "B9"
    C1 = "C1"
    VALUE_1_B = "1B"
    VALUE_1_C = "1C"
    C3 = "C3"
    C4 = "C4"
    VALUE_1_D = "1D"
    C5 = "C5"
    C6 = "C6"
    C7 = "C7"
    C8 = "C8"
    VALUE_1_F = "1F"
    C9 = "C9"
    D1 = "D1"
    G6 = "G6"
    D0 = "D0"
    D2 = "D2"
    D3 = "D3"
    VALUE_1_E = "1E"
    B1 = "B1"
    D4 = "D4"
    D5 = "D5"
    D6 = "D6"
    D9 = "D9"
    E0 = "E0"
    X2 = "X2"
    E2 = "E2"
    E3 = "E3"
    E4 = "E4"
    E8 = "E8"
    E9 = "E9"
    F0 = "F0"
    F2 = "F2"
    F3 = "F3"
    F4 = "F4"
    F6 = "F6"
    F7 = "F7"
    F8 = "F8"
    F9 = "F9"
    G0 = "G0"
    Y3 = "Y3"
    G1 = "G1"
    G2 = "G2"
    L7 = "L7"
    VALUE_1_M = "1M"
    G3 = "G3"
    G4 = "G4"
    VALUE_2_N = "2N"
    G7 = "G7"
    VALUE_1_G = "1G"
    G9 = "G9"
    G8 = "G8"
    H1 = "H1"
    H2 = "H2"
    H3 = "H3"
    H4 = "H4"
    VALUE_1_J = "1J"
    VALUE_1_H = "1H"
    H5 = "H5"
    H7 = "H7"
    H6 = "H6"
    H8 = "H8"
    H9 = "H9"
    I0 = "I0"
    I3 = "I3"
    I4 = "I4"
    VALUE_2_C = "2C"
    I5 = "I5"
    I6 = "I6"
    VALUE_2_Q = "2Q"
    VALUE_2_M = "2M"
    J0 = "J0"
    J1 = "J1"
    J3 = "J3"
    J4 = "J4"
    J5 = "J5"
    J6 = "J6"
    GU = "GU"
    J8 = "J8"
    Y7 = "Y7"
    J9 = "J9"
    S0 = "S0"
    K0 = "K0"
    K1 = "K1"
    K4 = "K4"
    X4 = "X4"
    K2 = "K2"
    K3 = "K3"
    K5 = "K5"
    K6 = "K6"
    Y8 = "Y8"
    K7 = "K7"
    K8 = "K8"
    K9 = "K9"
    L0 = "L0"
    L2 = "L2"
    L3 = "L3"
    L6 = "L6"
    L8 = "L8"
    M0 = "M0"
    Y9 = "Y9"
    M2 = "M2"
    VALUE_1_P = "1P"
    M3 = "M3"
    J2 = "J2"
    M4 = "M4"
    M5 = "M5"
    M6 = "M6"
    VALUE_1_N = "1N"
    M7 = "M7"
    VALUE_1_R = "1R"
    M8 = "M8"
    M9 = "M9"
    N0 = "N0"
    N1 = "N1"
    N2 = "N2"
    VALUE_1_Q = "1Q"
    N4 = "N4"
    N5 = "N5"
    VALUE_1_U = "1U"
    N6 = "N6"
    N7 = "N7"
    N8 = "N8"
    N9 = "N9"
    O0 = "O0"
    O1 = "O1"
    VALUE_1_T = "1T"
    O2 = "O2"
    O3 = "O3"
    O4 = "O4"
    VALUE_2_P = "2P"
    O5 = "O5"
    VALUE_1_K = "1K"
    VALUE_1_S = "1S"
    O9 = "O9"
    P0 = "P0"
    Z5 = "Z5"
    P1 = "P1"
    P2 = "P2"
    P3 = "P3"
    E1 = "E1"
    T6 = "T6"
    P5 = "P5"
    P6 = "P6"
    P7 = "P7"
    P8 = "P8"
    VALUE_1_W = "1W"
    Q2 = "Q2"
    Q3 = "Q3"
    Q4 = "Q4"
    Q5 = "Q5"
    Q6 = "Q6"
    Q7 = "Q7"
    VALUE_1_V = "1V"
    Q8 = "Q8"
    P4 = "P4"
    R0 = "R0"
    VALUE_1_Y = "1Y"
    VALUE_1_X = "1X"
    R1 = "R1"
    R2 = "R2"
    R4 = "R4"
    R5 = "R5"
    R6 = "R6"
    R8 = "R8"
    R9 = "R9"
    S1 = "S1"
    PR = "PR"
    S3 = "S3"
    S4 = "S4"
    S5 = "S5"
    VALUE_1_Z = "1Z"
    S6 = "S6"
    U8 = "U8"
    U7 = "U7"
    U9 = "U9"
    Z0 = "Z0"
    Z1 = "Z1"
    V0 = "V0"
    V1 = "V1"
    Y0 = "Y0"
    S8 = "S8"
    S9 = "S9"
    T0 = "T0"
    T1 = "T1"
    Z2 = "Z2"
    T2 = "T2"
    T8 = "T8"
    U0 = "U0"
    VALUE_2_B = "2B"
    VALUE_2_A = "2A"
    D7 = "D7"
    U1 = "U1"
    T3 = "T3"
    VALUE_1_L = "1L"
    U3 = "U3"
    F1 = "F1"
    V2 = "V2"
    V3 = "V3"
    L9 = "L9"
    V6 = "V6"
    V7 = "V7"
    V8 = "V8"
    V9 = "V9"
    F5 = "F5"
    VALUE_2_D = "2D"
    W0 = "W0"
    W1 = "W1"
    Z3 = "Z3"
    W2 = "W2"
    W3 = "W3"
    W4 = "W4"
    W5 = "W5"
    W6 = "W6"
    W8 = "W8"
    VALUE_2_E = "2E"
    W7 = "W7"
    VALUE_2_G = "2G"
    W9 = "W9"
    VALUE_2_H = "2H"
    C0 = "C0"
    X0 = "X0"
    VALUE_2_J = "2J"
    X3 = "X3"
    VALUE_2_K = "2K"
    VALUE_2_L = "2L"
    X5 = "X5"
    Q1 = "Q1"
    D8 = "D8"
    VI = "VI"
    X8 = "X8"
    U5 = "U5"
    T7 = "T7"
    Y4 = "Y4"
    Y5 = "Y5"
    XX = "XX"
    C2 = "C2"
    E5 = "E5"
    E7 = "E7"
    G5 = "G5"
    I7 = "I7"
    X9 = "X9"
    I8 = "I8"
    I9 = "I9"
    VALUE_2_F = "2F"
    L1 = "L1"
    L4 = "L4"
    L5 = "L5"
    M1 = "M1"
    O6 = "O6"
    Q9 = "Q9"
    R3 = "R3"
    T4 = "T4"
    U2 = "U2"
    U4 = "U4"
    U6 = "U6"
    X7 = "X7"
    Y2 = "Y2"


@dataclass
class ReportingId:
    class Meta:
        name = "REPORTING_ID"

    rpt_owner_cik: Optional[str] = field(
        default=None,
        metadata={
            "name": "rptOwnerCik",
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 10,
            "pattern": r"[0-9]+",
        },
    )
    rpt_owner_ccc: Optional[str] = field(
        default=None,
        metadata={
            "name": "rptOwnerCcc",
            "type": "Element",
            "length": 8,
        },
    )
    rpt_owner_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "rptOwnerName",
            "type": "Element",
            "max_length": 150,
        },
    )


@dataclass
class ReportingRelationship:
    """Each Reporting Owner must have at least one of the four relationship
    booleans set to true.

    This is not enforced by this schema but will be enforced during
    EDGAR processing.
    """

    class Meta:
        name = "REPORTING_RELATIONSHIP"

    is_director: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isDirector",
            "type": "Element",
        },
    )
    is_officer: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isOfficer",
            "type": "Element",
        },
    )
    is_ten_percent_owner: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isTenPercentOwner",
            "type": "Element",
        },
    )
    is_other: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isOther",
            "type": "Element",
        },
    )
    officer_title: Optional[str] = field(
        default=None,
        metadata={
            "name": "officerTitle",
            "type": "Element",
            "max_length": 30,
        },
    )
    other_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "otherText",
            "type": "Element",
            "max_length": 30,
        },
    )


@dataclass
class Signature:
    class Meta:
        name = "SIGNATURE"

    signature_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "signatureName",
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 255,
        },
    )
    signature_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "signatureDate",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class TransactionTimelinessNofoot:
    class Meta:
        name = "TRANSACTION_TIMELINESS_NOFOOT"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "white_space": "collapse",
            "pattern": r"[E|L]{0,1}",
        },
    )


@dataclass
class AcqDispCode:
    class Meta:
        name = "ACQ_DISP_CODE"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"A|D",
        },
    )
    footnote_id: List[FootnoteId] = field(
        default_factory=list,
        metadata={
            "name": "footnoteId",
            "type": "Element",
            "max_occurs": 99,
        },
    )


@dataclass
class BooleanWithFootnote:
    class Meta:
        name = "BOOLEAN_WITH_FOOTNOTE"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    footnote_id: List[FootnoteId] = field(
        default_factory=list,
        metadata={
            "name": "footnoteId",
            "type": "Element",
            "max_occurs": 99,
        },
    )


@dataclass
class DateAndOrFootnote:
    """For a truly optional date field, such as Deemed Execution Date, allow a date
    value and/or footnotes.

    Can have a footnote without a date value. Do not need a value or a
    footnoteId.
    """

    class Meta:
        name = "DATE_AND_OR_FOOTNOTE"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    footnote_id: List[FootnoteId] = field(
        default_factory=list,
        metadata={
            "name": "footnoteId",
            "type": "Element",
            "max_occurs": 99,
        },
    )


@dataclass
class DateWithFootnote:
    class Meta:
        name = "DATE_WITH_FOOTNOTE"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    footnote_id: List[FootnoteId] = field(
        default_factory=list,
        metadata={
            "name": "footnoteId",
            "type": "Element",
            "max_occurs": 99,
        },
    )


@dataclass
class FootnoteGroup:
    class Meta:
        name = "FOOTNOTE_GROUP"

    footnote: List[Footnote] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 99,
        },
    )


@dataclass
class IndirectNature:
    class Meta:
        name = "INDIRECT_NATURE"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 100,
        },
    )
    footnote_id: List[FootnoteId] = field(
        default_factory=list,
        metadata={
            "name": "footnoteId",
            "type": "Element",
            "max_occurs": 99,
        },
    )


@dataclass
class NumberWithFootnote:
    class Meta:
        name = "NUMBER_WITH_FOOTNOTE"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_inclusive": Decimal("0.0"),
            "max_inclusive": Decimal("999999999999.9999"),
            "total_digits": 16,
            "fraction_digits": 4,
        },
    )
    footnote_id: List[FootnoteId] = field(
        default_factory=list,
        metadata={
            "name": "footnoteId",
            "type": "Element",
            "max_occurs": 99,
        },
    )


@dataclass
class OptDateWithFootnote:
    """Some date fields may have just footnotes.

    Either a date value or a footnoteId is required. Additional
    footnoteIds may also be provided.
    """

    class Meta:
        name = "OPT_DATE_WITH_FOOTNOTE"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    footnote_id: List[FootnoteId] = field(
        default_factory=list,
        metadata={
            "name": "footnoteId",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 99,
            "sequence": 1,
        },
    )


@dataclass
class OptNumberWithFootnote:
    """Some numeric fields may have just footnotes.

    Either a numeric value or a footnoteId is required. Additional
    footnoteIds may also be provided.
    """

    class Meta:
        name = "OPT_NUMBER_WITH_FOOTNOTE"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_inclusive": Decimal("0.0"),
            "max_inclusive": Decimal("999999999999.9999"),
            "total_digits": 16,
            "fraction_digits": 4,
        },
    )
    footnote_id: List[FootnoteId] = field(
        default_factory=list,
        metadata={
            "name": "footnoteId",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 99,
            "sequence": 1,
        },
    )


@dataclass
class OwnershipType:
    class Meta:
        name = "OWNERSHIP_TYPE"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"D|I",
        },
    )
    footnote_id: List[FootnoteId] = field(
        default_factory=list,
        metadata={
            "name": "footnoteId",
            "type": "Element",
            "max_occurs": 99,
        },
    )


@dataclass
class ReportingAddress:
    """A document submitted as part of a Reduced Content submission can include an
    address for a Reporting Owner.

    All address elements are optional. If you do not include any address
    element, EDGAR will retrieve the Reporting Owner's address based
    upon the provided CIK. This address will be included in the version
    of the document that is disseminated.

    :ivar rpt_owner_street1:
    :ivar rpt_owner_street2:
    :ivar rpt_owner_city:
    :ivar rpt_owner_state:
    :ivar rpt_owner_zip_code:
    :ivar rpt_owner_state_description: This is not for the use of the
        filers. This field is passed to the stylesheets and the EDGAR
        PDF generator to improve the display of non-U.S. addresses.
    :ivar rpt_owner_good_address: This is not for the use of the filers.
        This field is just for internal EDGAR processing.
    """

    class Meta:
        name = "REPORTING_ADDRESS"

    rpt_owner_street1: Optional[str] = field(
        default=None,
        metadata={
            "name": "rptOwnerStreet1",
            "type": "Element",
            "min_length": 0,
            "max_length": 40,
        },
    )
    rpt_owner_street2: Optional[str] = field(
        default=None,
        metadata={
            "name": "rptOwnerStreet2",
            "type": "Element",
            "min_length": 0,
            "max_length": 40,
        },
    )
    rpt_owner_city: Optional[str] = field(
        default=None,
        metadata={
            "name": "rptOwnerCity",
            "type": "Element",
            "min_length": 0,
            "max_length": 30,
        },
    )
    rpt_owner_state: Optional[ReportingAddressRptOwnerState] = field(
        default=None,
        metadata={
            "name": "rptOwnerState",
            "type": "Element",
        },
    )
    rpt_owner_zip_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "rptOwnerZipCode",
            "type": "Element",
            "min_length": 0,
            "max_length": 10,
            "pattern": r"[0-9A-Za-z #-]*",
        },
    )
    rpt_owner_state_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "rptOwnerStateDescription",
            "type": "Element",
            "min_length": 0,
            "max_length": 50,
        },
    )
    rpt_owner_good_address: Optional[bool] = field(
        default=None,
        metadata={
            "name": "rptOwnerGoodAddress",
            "type": "Element",
        },
    )


@dataclass
class SecurityTitle:
    class Meta:
        name = "SECURITY_TITLE"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 60,
        },
    )
    footnote_id: List[FootnoteId] = field(
        default_factory=list,
        metadata={
            "name": "footnoteId",
            "type": "Element",
            "max_occurs": 99,
        },
    )


@dataclass
class TransactionCodingFor4:
    """The transactionFormType can be 4 or 5.

    The transactionCode is mandatory. The equitySwapInvolved flag is
    mandatory. A "4" transaction is assumed on-time. A "5" transaction
    is assumed early.
    """

    class Meta:
        name = "TRANSACTION_CODING_FOR_4"

    transaction_form_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "transactionFormType",
            "type": "Element",
            "required": True,
            "pattern": r"4|5",
        },
    )
    transaction_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "transactionCode",
            "type": "Element",
            "required": True,
            "pattern": r"A|C|D|E|F|G|H|I|J|L|M|O|P|S|U|W|X|Z",
        },
    )
    equity_swap_involved: Optional[bool] = field(
        default=None,
        metadata={
            "name": "equitySwapInvolved",
            "type": "Element",
            "required": True,
        },
    )
    footnote_id: List[FootnoteId] = field(
        default_factory=list,
        metadata={
            "name": "footnoteId",
            "type": "Element",
            "max_occurs": 99,
        },
    )


@dataclass
class TransactionTimeliness:
    class Meta:
        name = "TRANSACTION_TIMELINESS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "white_space": "collapse",
            "pattern": r"[E|L]{0,1}",
        },
    )
    footnote_id: List[FootnoteId] = field(
        default_factory=list,
        metadata={
            "name": "footnoteId",
            "type": "Element",
            "max_occurs": 99,
        },
    )


@dataclass
class DerivTransactAmounts:
    """Must provide a number of shares or a total dollar value.

    Must provide a price per share and/or a footnote. Must provide a
    code indicating Acquired or Disposed Of.
    """

    class Meta:
        name = "DERIV_TRANSACT_AMOUNTS"

    transaction_shares: Optional[NumberWithFootnote] = field(
        default=None,
        metadata={
            "name": "transactionShares",
            "type": "Element",
        },
    )
    transaction_total_value: Optional[NumberWithFootnote] = field(
        default=None,
        metadata={
            "name": "transactionTotalValue",
            "type": "Element",
        },
    )
    transaction_price_per_share: Optional[OptNumberWithFootnote] = field(
        default=None,
        metadata={
            "name": "transactionPricePerShare",
            "type": "Element",
            "required": True,
        },
    )
    transaction_acquired_disposed_code: Optional[AcqDispCode] = field(
        default=None,
        metadata={
            "name": "transactionAcquiredDisposedCode",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class DerivTransactNoFoot:
    """Must provide a number of shares or a total dollar value.

    Must provide a price per share and/or a footnote. Must provide a
    code indicating Acquired or Disposed Of.
    """

    class Meta:
        name = "DERIV_TRANSACT_NO_FOOT"

    transaction_shares: Optional[NumberWithFootnote] = field(
        default=None,
        metadata={
            "name": "transactionShares",
            "type": "Element",
        },
    )
    transaction_total_value: Optional[NumberWithFootnote] = field(
        default=None,
        metadata={
            "name": "transactionTotalValue",
            "type": "Element",
        },
    )
    transaction_price_per_share: Optional[OptNumberWithFootnote] = field(
        default=None,
        metadata={
            "name": "transactionPricePerShare",
            "type": "Element",
            "required": True,
        },
    )
    transaction_acquired_disposed_code: Optional[AcqDispNoFoot] = field(
        default=None,
        metadata={
            "name": "transactionAcquiredDisposedCode",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class NonderivTransactAmounts:
    """Must provide a number of shares.

    Must provide a dollar value and/or a footnote. Must provide a code
    indicating Acquired or Disposed Of.
    """

    class Meta:
        name = "NONDERIV_TRANSACT_AMOUNTS"

    transaction_shares: Optional[NumberWithFootnote] = field(
        default=None,
        metadata={
            "name": "transactionShares",
            "type": "Element",
            "required": True,
        },
    )
    transaction_price_per_share: Optional[OptNumberWithFootnote] = field(
        default=None,
        metadata={
            "name": "transactionPricePerShare",
            "type": "Element",
            "required": True,
        },
    )
    transaction_acquired_disposed_code: Optional[AcqDispCode] = field(
        default=None,
        metadata={
            "name": "transactionAcquiredDisposedCode",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class OwnershipNature:
    """
    If you set directOrIndirectOwnership to (I)ndirect, then natureOfOwnership is
    actually mandatory.
    """

    class Meta:
        name = "OWNERSHIP_NATURE"

    direct_or_indirect_ownership: Optional[OwnershipType] = field(
        default=None,
        metadata={
            "name": "directOrIndirectOwnership",
            "type": "Element",
            "required": True,
        },
    )
    nature_of_ownership: Optional[IndirectNature] = field(
        default=None,
        metadata={
            "name": "natureOfOwnership",
            "type": "Element",
        },
    )


@dataclass
class PostTransactionAmounts:
    class Meta:
        name = "POST_TRANSACTION_AMOUNTS"

    shares_owned_following_transaction: Optional[NumberWithFootnote] = field(
        default=None,
        metadata={
            "name": "sharesOwnedFollowingTransaction",
            "type": "Element",
        },
    )
    value_owned_following_transaction: Optional[NumberWithFootnote] = field(
        default=None,
        metadata={
            "name": "valueOwnedFollowingTransaction",
            "type": "Element",
        },
    )


@dataclass
class ReportingOwner:
    class Meta:
        name = "REPORTING_OWNER"

    reporting_owner_id: Optional[ReportingId] = field(
        default=None,
        metadata={
            "name": "reportingOwnerId",
            "type": "Element",
            "required": True,
        },
    )
    reporting_owner_address: Optional[ReportingAddress] = field(
        default=None,
        metadata={
            "name": "reportingOwnerAddress",
            "type": "Element",
        },
    )
    reporting_owner_relationship: Optional[ReportingRelationship] = field(
        default=None,
        metadata={
            "name": "reportingOwnerRelationship",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class UnderlyingSecurity:
    class Meta:
        name = "UNDERLYING_SECURITY"

    underlying_security_title: Optional[SecurityTitle] = field(
        default=None,
        metadata={
            "name": "underlyingSecurityTitle",
            "type": "Element",
            "required": True,
        },
    )
    underlying_security_shares: Optional[OptNumberWithFootnote] = field(
        default=None,
        metadata={
            "name": "underlyingSecurityShares",
            "type": "Element",
        },
    )
    underlying_security_value: Optional[OptNumberWithFootnote] = field(
        default=None,
        metadata={
            "name": "underlyingSecurityValue",
            "type": "Element",
        },
    )
