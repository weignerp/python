from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union

from model.sec.forms.eis_common import (
    AbsAssetClassTypes,
    AbsSubAssetClassTypes,
)
from model.sec.forms.eis_common2 import (
    ContactType,
    EdgarDocumentsType,
    LiveTestType,
    ModulesSegmentType,
    NewFileNumType,
    NotificationType,
    SrosType,
    YesNoType,
)
from model.sec.forms.eis_common_fee import (
    FeeOfferingType,
    FeeOffsetType,
    FeeType,
    SecuritySalesSharesType,
)

__NAMESPACE__ = "http://www.sec.gov/edgar/coregserial"


@dataclass
class FilerType:
    class Meta:
        name = "FILER_TYPE"

    filer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregserial",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    filer_ccc: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerCcc",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregserial",
            "required": True,
            "length": 8,
        },
    )
    file_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregserial",
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
            "namespace": "http://www.sec.gov/edgar/coregserial",
            "pattern": r"true|false",
        },
    )
    return_copy_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "returnCopyFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregserial",
            "pattern": r"true|false",
        },
    )
    delaying_amendment_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "delayingAmendmentFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregserial",
            "pattern": r"true|false",
        },
    )
    override_internet_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "overrideInternetFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregserial",
            "pattern": r"true|false",
        },
    )
    serial_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "serialFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregserial",
            "pattern": r"true|false",
        },
    )


@dataclass
class ReferenceType:
    class Meta:
        name = "REFERENCE_TYPE"

    references_429: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregserial",
            "pattern": r"\d{1,3}-\d{1,8}-[a-zA-Z0-9]{1,4}|\d{1,3}-\d{1,8}",
        },
    )
    references_462b: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregserial",
            "pattern": r"\d{1,3}-\d{1,8}-[a-zA-Z0-9]{1,4}|\d{1,3}-\d{1,8}",
        },
    )


@dataclass
class SerialNamesType:
    """Name of serial company to be created.

    Enter up to 150 characters.  Name entered must follow EDGAR Entity
    Name Conformance Rules listed in the EDGAR Interactive Help.
    """

    class Meta:
        name = "SERIAL_NAMES_TYPE"

    serial_company_name: List[str] = field(
        default_factory=list,
        metadata={
            "name": "serialCompanyName",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregserial",
            "min_occurs": 1,
            "min_length": 1,
            "max_length": 150,
            "pattern": r"([A-Za-z0-9\s!\\#$(),.:;=@'\-{}|/&]+)",
        },
    )


class SubmissionType(Enum):
    """Type of submission you are filing.

    Choose a value from the appropriate family of Submission Types.
    """

    VALUE_424_B1 = "424B1"
    VALUE_424_B2 = "424B2"
    VALUE_424_B3 = "424B3"
    VALUE_424_B4 = "424B4"
    VALUE_424_B5 = "424B5"
    VALUE_424_B7 = "424B7"
    VALUE_424_B8 = "424B8"
    VALUE_424_H = "424H"
    VALUE_424_H_A = "424H/A"
    VALUE_424_I = "424I"
    ABS_EE = "ABS-EE"
    ABS_EE_A = "ABS-EE/A"
    SF_1 = "SF-1"
    SF_1_A = "SF-1/A"
    SF_1_MEF = "SF-1MEF"
    SF_3 = "SF-3"
    SF_3_A = "SF-3/A"
    SF_3_MEF = "SF-3MEF"


@dataclass
class FilerType2:
    class Meta:
        name = "FILER_TYPE_2"

    filer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregserial",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    filer_ccc: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerCcc",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregserial",
            "required": True,
            "length": 8,
        },
    )
    file_number: Optional[Union[str, NewFileNumType]] = field(
        default=None,
        metadata={
            "name": "fileNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregserial",
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
            "namespace": "http://www.sec.gov/edgar/coregserial",
            "min_occurs": 1,
        },
    )


@dataclass
class EdgarSubmission:
    """
    This is the root element for an EDGARLink Online submission.

    :ivar schema_version:
    :ivar live_test_flag:
    :ivar flags:
    :ivar submission_type:
    :ivar contact:
    :ivar filer:
    :ivar depositor_id:
    :ivar sponsor_id:
    :ivar abs_asset_classes:
    :ivar abs_sub_asset_classes:
    :ivar start_period:
    :ivar end_period:
    :ivar accession_number:
    :ivar coregs:
    :ivar serials:
    :ivar sros:
    :ivar fee_table_included_flag:
    :ivar notifications:
    :ivar module_segments:
    :ivar references:
    :ivar documents:
    :ivar edgar_fee: Comment describing your root element
    """

    class Meta:
        name = "edgarSubmission"
        namespace = "http://www.sec.gov/edgar/coregserial"

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
    depositor_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "depositorId",
            "type": "Element",
            "pattern": r"\d{1,10}",
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
    accession_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "accessionNumber",
            "type": "Element",
            "pattern": r"[*]{0}|[0-9]{1,10}\-[0-9]{1,2}\-[0-9]{1,6}",
        },
    )
    coregs: Optional[FilersType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    serials: Optional[SerialNamesType] = field(
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
    references: Optional[ReferenceType] = field(
        default=None,
        metadata={
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
    edgar_fee: Optional["EdgarSubmission.EdgarFee"] = field(
        default=None,
        metadata={
            "name": "edgarFee",
            "type": "Element",
        },
    )

    @dataclass
    class EdgarFee:
        submission_fee: Optional[FeeType] = field(
            default=None,
            metadata={
                "name": "submissionFee",
                "type": "Element",
            },
        )
        submission_offering: List[FeeOfferingType] = field(
            default_factory=list,
            metadata={
                "name": "submissionOffering",
                "type": "Element",
            },
        )
        submission_offset: List[FeeOffsetType] = field(
            default_factory=list,
            metadata={
                "name": "submissionOffset",
                "type": "Element",
            },
        )
        submission_sales_shares: List[SecuritySalesSharesType] = field(
            default_factory=list,
            metadata={
                "name": "submissionSalesShares",
                "type": "Element",
            },
        )
