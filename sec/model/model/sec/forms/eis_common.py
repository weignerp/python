from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union

from model.sec.forms.eis_common2 import (
    BaseDocumentType,
    SubmissionType,
    YesNoType,
)

__NAMESPACE__ = "http://www.sec.gov/edgar/common"


class AbsAssetClassType(Enum):
    RESIDENTIAL_MORTGAGES_PRIME = "Residential mortgages - Prime"
    RESIDENTIAL_MORTGAGES_NON_PRIME = "Residential mortgages - Non-Prime"
    RESIDENTIAL_MORTGAGES_HELOC = "Residential mortgages - HELOC"
    RESIDENTIAL_MORTGAGES_REVERSE_MORTGAGES = (
        "Residential mortgages - Reverse Mortgages"
    )
    RESIDENTIAL_MORTGAGES_MANUFACTURED_HOUSING = (
        "Residential mortgages - Manufactured Housing"
    )
    RESIDENTIAL_MORTGAGES_OTHER_COMBINED = (
        "Residential mortgages - Other/Combined"
    )
    COMMERCIAL_MORTGAGES = "Commercial mortgages"
    AUTO_LOANS = "Auto loans"
    AUTO_LEASES = "Auto leases"
    EQUIPMENT_LEASES = "Equipment leases"
    EQUIPMENT_LOANS = "Equipment loans"
    STUDENT_LOANS = "Student loans"
    FLOORPLAN_FINANCINGS = "Floorplan financings"
    DEBT_SECURITIES = "Debt Securities"
    RESECURITIZATION = "Resecuritization"
    CREDIT_CARD = "Credit card"
    OTHER = "Other"


class AbsSubAssetClassType(Enum):
    RESIDENTIAL_MORTGAGES_PRIME = "Residential mortgages - Prime"
    RESIDENTIAL_MORTGAGES_NON_PRIME = "Residential mortgages - Non-Prime"
    RESIDENTIAL_MORTGAGES_HELOC = "Residential mortgages - HELOC"
    RESIDENTIAL_MORTGAGES_REVERSE_MORTGAGES = (
        "Residential mortgages - Reverse Mortgages"
    )
    RESIDENTIAL_MORTGAGES_MANUFACTURED_HOUSING = (
        "Residential mortgages - Manufactured Housing"
    )
    RESIDENTIAL_MORTGAGES_OTHER_COMBINED = (
        "Residential mortgages - Other/Combined"
    )
    COMMERCIAL_MORTGAGES = "Commercial mortgages"
    AUTO_LOANS = "Auto loans"
    AUTO_LEASES = "Auto leases"
    EQUIPMENT_LEASES = "Equipment leases"
    EQUIPMENT_LOANS = "Equipment loans"
    STUDENT_LOANS = "Student loans"
    FLOORPLAN_FINANCINGS = "Floorplan financings"
    DEBT_SECURITIES = "Debt Securities"
    CREDIT_CARD = "Credit card"
    OTHER = "Other"


class ExactOrExplanationOptions(Enum):
    EXACT = "Exact"
    EXPLANATION = "Explanation"


@dataclass
class IndividualNameType:
    class Meta:
        name = "INDIVIDUAL_NAME_TYPE"

    prefix: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "min_length": 1,
            "max_length": 30,
        },
    )
    first_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "firstName",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "min_length": 1,
            "max_length": 40,
        },
    )
    middle_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "middleName",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "min_length": 1,
            "max_length": 30,
        },
    )
    last_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastName",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "min_length": 1,
            "max_length": 30,
        },
    )
    suffix: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "min_length": 1,
            "max_length": 30,
        },
    )


@dataclass
class IrsOrSsn:
    class Meta:
        name = "IRS_OR_SSN"

    irs_num: Optional[str] = field(
        default=None,
        metadata={
            "name": "irsNum",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "pattern": r"\d{2}[\-]?\d{7}",
        },
    )
    ssn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "pattern": r"\d{3}-\d{2}-\d{4}",
        },
    )


@dataclass
class OtherType2:
    class Meta:
        name = "OTHER_TYPE_2"

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
            "min_length": 1,
            "max_length": 1000,
        },
    )


@dataclass
class AbsAssetClassTypes:
    class Meta:
        name = "ABS_ASSET_CLASS_TYPES"

    abs_asset_class: List[AbsAssetClassType] = field(
        default_factory=list,
        metadata={
            "name": "absAssetClass",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "max_occurs": 17,
        },
    )


@dataclass
class AbsSubAssetClassTypes:
    class Meta:
        name = "ABS_SUB_ASSET_CLASS_TYPES"

    abs_sub_asset_class: List[AbsSubAssetClassType] = field(
        default_factory=list,
        metadata={
            "name": "absSubAssetClass",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "max_occurs": 16,
        },
    )


@dataclass
class ConfidentialDocumentType:
    """Document names must be lower case and no longer than thirty-two (32)
    characters in length.

    The names must start with a letter (a-z) and may contain numbers
    (0-9) with no spaces. Document names may contain one period (.), one
    hyphen (-), and one underscore (_) character and must end with
    *.htm, *.txt, *.pdf, *.fil, *.jpg, *.gif, *.xml or *.xsd extensions.
    """

    class Meta:
        name = "CONFIDENTIAL_DOCUMENT_TYPE"

    conformed_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "conformedName",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
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
            "min_length": 1,
        },
    )
    confidentiality: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "pattern": r"true|false",
        },
    )


@dataclass
class ConfidentialDocumentType1:
    """Document names must be lower case and no longer than thirty-two (32)
    characters in length.

    The names must start with a letter (a-z) and may contain numbers
    (0-9) with no spaces. Document names may contain one period (.), one
    hyphen (-), and one underscore (_) character and must end with
    *.htm, *.txt, *.pdf, *.fil, *.jpg, *.gif, *.xml or *.xsd extensions.
    """

    class Meta:
        name = "CONFIDENTIAL_DOCUMENT_TYPE1"

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
    confidentiality: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "pattern": r"true|false",
        },
    )


@dataclass
class ExactOrExplanation:
    class Meta:
        name = "EXACT_OR_EXPLANATION"

    date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
            "pattern": r"\d{1,2}-\d{1,2}-\d{4}",
        },
    )
    exact_or_explanation: Optional[ExactOrExplanationOptions] = field(
        default=None,
        metadata={
            "name": "exactOrExplanation",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
        },
    )
    explanation_info: Optional[str] = field(
        default=None,
        metadata={
            "name": "explanationInfo",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "min_length": 1,
            "max_length": 1000,
        },
    )


@dataclass
class SuccessorType:
    class Meta:
        name = "SUCCESSOR_TYPE"

    successor_filing_flag: Optional[YesNoType] = field(
        default=None,
        metadata={
            "name": "successorFilingFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "required": True,
        },
    )
    successor_file_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "successorFileNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "pattern": r"\d{1,3}-\d{1,8}-[a-zA-Z0-9]{1,4}|\d{1,3}-\d{1,8}",
        },
    )


@dataclass
class ConfidentialDocumentsType:
    class Meta:
        name = "CONFIDENTIAL_DOCUMENTS_TYPE"

    document: List[ConfidentialDocumentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
        },
    )


@dataclass
class ConfidentialDocumentsType1:
    class Meta:
        name = "CONFIDENTIAL_DOCUMENTS_TYPE1"

    document: List[ConfidentialDocumentType1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/common",
            "min_occurs": 1,
        },
    )
