from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDate

from ownership4_document import (
    DateAndOrFootnote,
    DateWithFootnote,
    DerivTransactNoFoot,
    FootnoteGroup,
    FootnoteId,
    Issuer,
    NonderivTransactAmounts,
    OptDateWithFootnote,
    OptNumberWithFootnote,
    OwnershipNature,
    PostTransactionAmounts,
    ReportingOwner,
    SecurityTitle,
    Signature,
    TransactionTimelinessNofoot,
    UnderlyingSecurity,
)


@dataclass
class TransactionCodeForHolding:
    """
    To indicate a late holding that should have reported via a "3" submission, set
    the form type to "3".
    """

    class Meta:
        name = "TRANSACTION_CODE_FOR_HOLDING"

    transaction_form_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "transactionFormType",
            "type": "Element",
            "pattern": r"[3]{0,1}",
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
class TransactionCodingFor5:
    """The transactionFormType can be 4 or 5.

    The transactionCode is mandatory. The equitySwapInvolved flag is
    mandatory. A "4" transaction is assumed late. A "5" transaction can
    be on-time or late.
    """

    class Meta:
        name = "TRANSACTION_CODING_FOR_5"

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
class DerivativeHolding:
    class Meta:
        name = "DERIVATIVE_HOLDING"

    security_title: Optional[SecurityTitle] = field(
        default=None,
        metadata={
            "name": "securityTitle",
            "type": "Element",
            "required": True,
        },
    )
    conversion_or_exercise_price: Optional[OptNumberWithFootnote] = field(
        default=None,
        metadata={
            "name": "conversionOrExercisePrice",
            "type": "Element",
            "required": True,
        },
    )
    transaction_coding: Optional[TransactionCodeForHolding] = field(
        default=None,
        metadata={
            "name": "transactionCoding",
            "type": "Element",
        },
    )
    exercise_date: Optional[OptDateWithFootnote] = field(
        default=None,
        metadata={
            "name": "exerciseDate",
            "type": "Element",
            "required": True,
        },
    )
    expiration_date: Optional[OptDateWithFootnote] = field(
        default=None,
        metadata={
            "name": "expirationDate",
            "type": "Element",
            "required": True,
        },
    )
    underlying_security: Optional[UnderlyingSecurity] = field(
        default=None,
        metadata={
            "name": "underlyingSecurity",
            "type": "Element",
            "required": True,
        },
    )
    post_transaction_amounts: Optional[PostTransactionAmounts] = field(
        default=None,
        metadata={
            "name": "postTransactionAmounts",
            "type": "Element",
            "required": True,
        },
    )
    ownership_nature: Optional[OwnershipNature] = field(
        default=None,
        metadata={
            "name": "ownershipNature",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class DerivativeTransaction:
    class Meta:
        name = "DERIVATIVE_TRANSACTION"

    security_title: Optional[SecurityTitle] = field(
        default=None,
        metadata={
            "name": "securityTitle",
            "type": "Element",
            "required": True,
        },
    )
    conversion_or_exercise_price: Optional[OptNumberWithFootnote] = field(
        default=None,
        metadata={
            "name": "conversionOrExercisePrice",
            "type": "Element",
            "required": True,
        },
    )
    transaction_date: Optional[DateWithFootnote] = field(
        default=None,
        metadata={
            "name": "transactionDate",
            "type": "Element",
            "required": True,
        },
    )
    deemed_execution_date: Optional[DateAndOrFootnote] = field(
        default=None,
        metadata={
            "name": "deemedExecutionDate",
            "type": "Element",
        },
    )
    transaction_coding: Optional[TransactionCodingFor5] = field(
        default=None,
        metadata={
            "name": "transactionCoding",
            "type": "Element",
        },
    )
    transaction_timeliness: Optional[TransactionTimelinessNofoot] = field(
        default=None,
        metadata={
            "name": "transactionTimeliness",
            "type": "Element",
        },
    )
    transaction_amounts: Optional[DerivTransactNoFoot] = field(
        default=None,
        metadata={
            "name": "transactionAmounts",
            "type": "Element",
            "required": True,
        },
    )
    exercise_date: Optional[OptDateWithFootnote] = field(
        default=None,
        metadata={
            "name": "exerciseDate",
            "type": "Element",
            "required": True,
        },
    )
    expiration_date: Optional[OptDateWithFootnote] = field(
        default=None,
        metadata={
            "name": "expirationDate",
            "type": "Element",
            "required": True,
        },
    )
    underlying_security: Optional[UnderlyingSecurity] = field(
        default=None,
        metadata={
            "name": "underlyingSecurity",
            "type": "Element",
            "required": True,
        },
    )
    post_transaction_amounts: Optional[PostTransactionAmounts] = field(
        default=None,
        metadata={
            "name": "postTransactionAmounts",
            "type": "Element",
            "required": True,
        },
    )
    ownership_nature: Optional[OwnershipNature] = field(
        default=None,
        metadata={
            "name": "ownershipNature",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class NonderivativeHolding:
    class Meta:
        name = "NONDERIVATIVE_HOLDING"

    security_title: Optional[SecurityTitle] = field(
        default=None,
        metadata={
            "name": "securityTitle",
            "type": "Element",
            "required": True,
        },
    )
    transaction_coding: Optional[TransactionCodeForHolding] = field(
        default=None,
        metadata={
            "name": "transactionCoding",
            "type": "Element",
        },
    )
    post_transaction_amounts: Optional[PostTransactionAmounts] = field(
        default=None,
        metadata={
            "name": "postTransactionAmounts",
            "type": "Element",
            "required": True,
        },
    )
    ownership_nature: Optional[OwnershipNature] = field(
        default=None,
        metadata={
            "name": "ownershipNature",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class NonderivativeTransaction:
    class Meta:
        name = "NONDERIVATIVE_TRANSACTION"

    security_title: Optional[SecurityTitle] = field(
        default=None,
        metadata={
            "name": "securityTitle",
            "type": "Element",
            "required": True,
        },
    )
    transaction_date: Optional[DateWithFootnote] = field(
        default=None,
        metadata={
            "name": "transactionDate",
            "type": "Element",
            "required": True,
        },
    )
    deemed_execution_date: Optional[DateAndOrFootnote] = field(
        default=None,
        metadata={
            "name": "deemedExecutionDate",
            "type": "Element",
        },
    )
    transaction_coding: Optional[TransactionCodingFor5] = field(
        default=None,
        metadata={
            "name": "transactionCoding",
            "type": "Element",
        },
    )
    transaction_timeliness: Optional[TransactionTimelinessNofoot] = field(
        default=None,
        metadata={
            "name": "transactionTimeliness",
            "type": "Element",
        },
    )
    transaction_amounts: Optional[NonderivTransactAmounts] = field(
        default=None,
        metadata={
            "name": "transactionAmounts",
            "type": "Element",
            "required": True,
        },
    )
    post_transaction_amounts: Optional[PostTransactionAmounts] = field(
        default=None,
        metadata={
            "name": "postTransactionAmounts",
            "type": "Element",
            "required": True,
        },
    )
    ownership_nature: Optional[OwnershipNature] = field(
        default=None,
        metadata={
            "name": "ownershipNature",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class DerivativeTable:
    """Can have up to 30 entries in the Derivative Table.

    This is Table 2 on the printed form. Can have any combination of
    Transactions and Holdings in any order.
    """

    class Meta:
        name = "DERIVATIVE_TABLE"

    derivative_transaction: List[DerivativeTransaction] = field(
        default_factory=list,
        metadata={
            "name": "derivativeTransaction",
            "type": "Element",
            "max_occurs": 30,
        },
    )
    derivative_holding: List[DerivativeHolding] = field(
        default_factory=list,
        metadata={
            "name": "derivativeHolding",
            "type": "Element",
            "max_occurs": 30,
        },
    )


@dataclass
class NonderivativeTable:
    """Can have up to 30 entries in the Non-Derivative Table.

    This is Table 1 on the printed form. Can have any combination of
    Transactions and Holdings in any order.
    """

    class Meta:
        name = "NONDERIVATIVE_TABLE"

    non_derivative_transaction: List[NonderivativeTransaction] = field(
        default_factory=list,
        metadata={
            "name": "nonDerivativeTransaction",
            "type": "Element",
            "max_occurs": 30,
        },
    )
    non_derivative_holding: List[NonderivativeHolding] = field(
        default_factory=list,
        metadata={
            "name": "nonDerivativeHolding",
            "type": "Element",
            "max_occurs": 30,
        },
    )


@dataclass
class OwnershipDocument:
    class Meta:
        name = "ownershipDocument"

    schema_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemaVersion",
            "type": "Element",
            "length": 5,
        },
    )
    document_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "documentType",
            "type": "Element",
            "required": True,
            "pattern": r"5",
        },
    )
    period_of_report: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "periodOfReport",
            "type": "Element",
            "required": True,
        },
    )
    not_subject_to_section16: Optional[bool] = field(
        default=None,
        metadata={
            "name": "notSubjectToSection16",
            "type": "Element",
        },
    )
    form3_holdings_reported: Optional[bool] = field(
        default=None,
        metadata={
            "name": "form3HoldingsReported",
            "type": "Element",
        },
    )
    form4_transactions_reported: Optional[bool] = field(
        default=None,
        metadata={
            "name": "form4TransactionsReported",
            "type": "Element",
        },
    )
    issuer: Optional[Issuer] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    reporting_owner: List[ReportingOwner] = field(
        default_factory=list,
        metadata={
            "name": "reportingOwner",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 10,
        },
    )
    aff10b5_one: Optional[bool] = field(
        default=None,
        metadata={
            "name": "aff10b5One",
            "type": "Element",
            "required": True,
        },
    )
    non_derivative_table: Optional[NonderivativeTable] = field(
        default=None,
        metadata={
            "name": "nonDerivativeTable",
            "type": "Element",
        },
    )
    derivative_table: Optional[DerivativeTable] = field(
        default=None,
        metadata={
            "name": "derivativeTable",
            "type": "Element",
        },
    )
    footnotes: Optional[FootnoteGroup] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    remarks: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 2000,
        },
    )
    owner_signature: List[Signature] = field(
        default_factory=list,
        metadata={
            "name": "ownerSignature",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 10,
        },
    )
