from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Union

from model.sec.forms.eis_common2 import SubmissionType

__NAMESPACE__ = "http://www.sec.gov/edgar/feecommon"


class PaymentType(Enum):
    PAY_IN_ADVANCE = "Pay In Advance"
    PAY_AS_YOU_GO = "Pay As You Go"
    INDETERMINATE = "Indeterminate"


@dataclass
class PayorType:
    class Meta:
        name = "PAYOR_TYPE"

    filer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    filer_ccc: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerCcc",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
            "required": True,
            "length": 8,
        },
    )


@dataclass
class SalesType:
    class Meta:
        name = "SALES_TYPE"

    sale_shares_series_or_class_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "saleSharesSeriesOrClassId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
            "pattern": r"[S|s][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",
        },
    )
    sales_shares_sales_proceeds: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "salesSharesSalesProceeds",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
            "required": True,
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("99999999999999.99"),
            "fraction_digits": 2,
        },
    )
    sales_shares_redeemed_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "salesSharesRedeemedValue",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("99999999999999.99"),
            "fraction_digits": 2,
        },
    )
    sales_shares_net_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "salesSharesNetValue",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
            "required": True,
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("99999999999999.99"),
            "fraction_digits": 2,
        },
    )
    sales_shares_fee_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "salesSharesFeeAmount",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
            "required": True,
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999.9999"),
            "fraction_digits": 4,
        },
    )


@dataclass
class SecuritySalesType:
    class Meta:
        name = "SECURITY_SALES_TYPE"

    sales_shares_sales_proceeds: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "salesSharesSalesProceeds",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
            "required": True,
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("99999999999999.99"),
            "fraction_digits": 2,
        },
    )
    sales_shares_redeemed_value_current: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "salesSharesRedeemedValueCurrent",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("99999999999999.99"),
            "fraction_digits": 2,
        },
    )
    sales_shares_redeemed_value_prior: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "salesSharesRedeemedValuePrior",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("99999999999999.99"),
            "fraction_digits": 2,
        },
    )
    sales_shares_redeemed_value_credit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "salesSharesRedeemedValueCredit",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("99999999999999.99"),
            "fraction_digits": 2,
        },
    )
    sales_shares_net_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "salesSharesNetValue",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
            "required": True,
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("99999999999999.99"),
            "fraction_digits": 2,
        },
    )
    sales_shares_fee_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "salesSharesFeeAmount",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
            "required": True,
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999.9999"),
            "fraction_digits": 4,
        },
    )


class SecurityTypeBase(Enum):
    DEBT = "Debt"
    NON_CONVERTIBLE_DEBT = "Non-Convertible Debt"
    DEBT_CONVERTIBLE_INTO_EQUITY = "Debt Convertible into Equity"
    EQUITY = "Equity"
    ASSET_BACKED_SECURITIES = "Asset-Backed Securities"
    MORTGAGE_BACKED_SECURITIES = "Mortgage Backed Securities"
    LIMITED_PARTNERSHIP_INTERESTS = "Limited Partnership Interests"
    UNALLOCATED_UNIVERSAL_SHELF = "Unallocated (Universal) Shelf"
    ADRS_ADSS = "ADRs/ADSs"
    FACE_AMOUNT_CERTIFICATES = "Face Amount Certificates"
    EXCHANGE_TRADED_VEHICLE_SECURITIES = "Exchange Traded Vehicle Securities"
    OTHER = "Other"


@dataclass
class FeeOfferingType:
    class Meta:
        name = "FEE_OFFERING_TYPE"

    fee_offering_type_of_payment: Optional[PaymentType] = field(
        default=None,
        metadata={
            "name": "feeOfferingTypeOfPayment",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
        },
    )
    fee_offering_security_name: Optional[Union[SecurityTypeBase, str]] = field(
        default=None,
        metadata={
            "name": "feeOfferingSecurityName",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
            "pattern": r"Other\..{1,106}",
        },
    )
    fee_offering_shares: Optional[int] = field(
        default=None,
        metadata={
            "name": "feeOfferingShares",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
        },
    )
    fee_offering_amount_per_share: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "feeOfferingAmountPerShare",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999.9999"),
            "fraction_digits": 4,
        },
    )
    fee_offering_aggregate_price: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "feeOfferingAggregatePrice",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("99999999999999.99"),
            "fraction_digits": 2,
        },
    )


@dataclass
class FeeOffsetType:
    """The calculated total of all offset payments.

    This field is not editable.
    """

    class Meta:
        name = "FEE_OFFSET_TYPE"

    offset_cik: Optional[str] = field(
        default=None,
        metadata={
            "name": "offsetCik",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    offset_form_type: Optional[SubmissionType] = field(
        default=None,
        metadata={
            "name": "offsetFormType",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
        },
    )
    offset_file_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "offsetFileNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
            "required": True,
            "pattern": r"\d{1,3}-\d{1,8}-[a-zA-Z0-9]{1,4}|\d{1,3}-\d{1,8}",
        },
    )
    offset_filing_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "offsetFilingDate",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
            "required": True,
            "pattern": r"\d{1,2}-\d{1,2}-\d{4}",
        },
    )
    offset_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "offsetAmount",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
            "required": True,
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("99999999999999.99"),
            "fraction_digits": 2,
        },
    )


@dataclass
class FeeType:
    class Meta:
        name = "FEE_TYPE"

    fee_payor_information: Optional[PayorType] = field(
        default=None,
        metadata={
            "name": "feePayorInformation",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
        },
    )
    fee_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "feeAmount",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
            "required": True,
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("99999999999999.99"),
            "fraction_digits": 2,
        },
    )
    fee_basis: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "feeBasis",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("99999999999999.99"),
            "fraction_digits": 2,
        },
    )


@dataclass
class SalesSharesType:
    class Meta:
        name = "SALES_SHARES_TYPE"

    sales_shares_itemize_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "salesSharesItemizeFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
            "pattern": r"true|false",
        },
    )
    sales_shares_information: List[SalesType] = field(
        default_factory=list,
        metadata={
            "name": "salesSharesInformation",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
            "min_occurs": 1,
        },
    )


@dataclass
class SecuritySalesSharesType:
    class Meta:
        name = "SECURITY_SALES_SHARES_TYPE"

    sales_shares_last_filing_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "salesSharesLastFilingFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
            "pattern": r"true|false",
        },
    )
    sales_shares_payment_year: Optional[str] = field(
        default=None,
        metadata={
            "name": "salesSharesPaymentYear",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
            "pattern": r"\d{4,4}",
        },
    )
    sales_shares_fiscal_year_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "salesSharesFiscalYearEnd",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
            "required": True,
            "pattern": r"\d{2,2}/\d{2,2}",
        },
    )
    sales_shares_information: List[SecuritySalesType] = field(
        default_factory=list,
        metadata={
            "name": "salesSharesInformation",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
            "min_occurs": 1,
        },
    )


@dataclass
class FeeSalesShareType:
    class Meta:
        name = "FEE_SALES_SHARE_TYPE"

    submission_fee: Optional[FeeType] = field(
        default=None,
        metadata={
            "name": "submissionFee",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
            "required": True,
        },
    )
    submission_sales_shares: Optional[SalesSharesType] = field(
        default=None,
        metadata={
            "name": "submissionSalesShares",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/feecommon",
        },
    )
