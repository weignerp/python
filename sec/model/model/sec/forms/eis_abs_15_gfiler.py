from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from model.sec.forms.eis_common2 import (
    ContactType,
    DepositorType,
    EdgarDocumentsType,
    LiveTestType,
    ModulesSegmentType,
    NotificationType,
    SrosType,
    YesNoType,
)

__NAMESPACE__ = "http://www.sec.gov/edgar/abs15gfiler"


class AssetClassType(Enum):
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
    EQUIPMENT_LOANS = "Equipment loans"
    EQUIPMENT_LEASES = "Equipment leases"
    STUDENT_LOANS = "Student loans"
    FLOORPLAN_FINANCINGS = "Floorplan financings"
    DEBT_SECURITIES = "Debt Securities"
    RESECURITIZATION = "Resecuritization"
    CREDIT_CARD = "Credit card"
    OTHER = "Other"


@dataclass
class FilerType:
    class Meta:
        name = "FILER_TYPE"

    filer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/abs15gfiler",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    filer_ccc: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerCcc",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/abs15gfiler",
            "required": True,
            "length": 8,
        },
    )
    file_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/abs15gfiler",
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
            "namespace": "http://www.sec.gov/edgar/abs15gfiler",
            "pattern": r"true|false",
        },
    )
    override_internet_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "overrideInternetFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/abs15gfiler",
            "pattern": r"true|false",
        },
    )
    return_copy_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "returnCopyFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/abs15gfiler",
            "pattern": r"true|false",
        },
    )


class Rule15Ga1ItemType(Enum):
    VALUE_1_01 = "1.01"
    VALUE_1_02 = "1.02"
    VALUE_1_03 = "1.03"


class Rule15Ga2ItemType(Enum):
    VALUE_2_01 = "2.01"
    VALUE_2_02 = "2.02"


class SubmissionType(Enum):
    """Type of submission you are filing.

    Choose a value from the appropriate family of Submission Types.
    """

    ABS_15_G = "ABS-15G"
    ABS_15_G_A = "ABS-15G/A"


@dataclass
class IssuerType:
    class Meta:
        name = "ISSUER_TYPE"

    issuing_entity_cik: Optional[str] = field(
        default=None,
        metadata={
            "name": "issuingEntityCik",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/abs15gfiler",
            "pattern": r"\d{1,10}",
        },
    )
    issuing_entity_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "issuingEntityName",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/abs15gfiler",
            "min_length": 1,
            "max_length": 150,
            "pattern": r"([A-Za-z0-9\s!\\#$(),.:;=@'\-{}|/&]+)",
        },
    )
    issuing_entity_has_file_number: Optional[YesNoType] = field(
        default=None,
        metadata={
            "name": "issuingEntityHasFileNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/abs15gfiler",
        },
    )
    issuing_entity_file_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "issuingEntityFileNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/abs15gfiler",
            "pattern": r"\d{1,3}-\d{1,8}-[a-zA-Z0-9]{1,4}|\d{1,3}-\d{1,8}",
        },
    )


@dataclass
class Rule15Ga1Type:
    class Meta:
        name = "RULE15GA1_TYPE"

    is_rule15_ga1: Optional[str] = field(
        default=None,
        metadata={
            "name": "isRule15Ga1",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/abs15gfiler",
            "required": True,
            "pattern": r"true|false",
        },
    )
    rule15_ga1_item: Optional[Rule15Ga1ItemType] = field(
        default=None,
        metadata={
            "name": "rule15Ga1Item",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/abs15gfiler",
            "required": True,
        },
    )
    filed_item101: Optional[YesNoType] = field(
        default=None,
        metadata={
            "name": "filedItem101",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/abs15gfiler",
        },
    )
    file_number_item101: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileNumberItem101",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/abs15gfiler",
            "pattern": r"\d{1,3}-\d{1,8}-[a-zA-Z0-9]{1,4}|\d{1,3}-\d{1,8}",
        },
    )
    no_activity_initial: Optional[YesNoType] = field(
        default=None,
        metadata={
            "name": "noActivityInitial",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/abs15gfiler",
        },
    )
    no_activity_qtr: Optional[YesNoType] = field(
        default=None,
        metadata={
            "name": "noActivityQtr",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/abs15gfiler",
        },
    )
    no_activity_annual: Optional[YesNoType] = field(
        default=None,
        metadata={
            "name": "noActivityAnnual",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/abs15gfiler",
        },
    )


@dataclass
class SecuritizerType:
    class Meta:
        name = "SECURITIZER_TYPE"

    securitizer_has_cik: Optional[YesNoType] = field(
        default=None,
        metadata={
            "name": "securitizerHasCik",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/abs15gfiler",
            "required": True,
        },
    )
    securitizer_cik: Optional[str] = field(
        default=None,
        metadata={
            "name": "securitizerCik",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/abs15gfiler",
            "pattern": r"\d{1,10}",
        },
    )
    securitizer_has025_file_number: Optional[YesNoType] = field(
        default=None,
        metadata={
            "name": "securitizerHas025FileNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/abs15gfiler",
        },
    )
    securitizer_file_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "securitizerFileNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/abs15gfiler",
            "pattern": r"\d{1,3}-\d{1,8}-[a-zA-Z0-9]{1,4}|\d{1,3}-\d{1,8}",
        },
    )


@dataclass
class Rule15Ga2Type:
    class Meta:
        name = "RULE15GA2_TYPE"

    is_rule15_ga2: Optional[str] = field(
        default=None,
        metadata={
            "name": "isRule15Ga2",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/abs15gfiler",
            "required": True,
            "pattern": r"true|false",
        },
    )
    rule15_ga2_item: Optional[Rule15Ga2ItemType] = field(
        default=None,
        metadata={
            "name": "rule15Ga2Item",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/abs15gfiler",
            "required": True,
        },
    )
    is_registered: Optional[YesNoType] = field(
        default=None,
        metadata={
            "name": "isRegistered",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/abs15gfiler",
            "required": True,
        },
    )
    securitizer: Optional[SecuritizerType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/abs15gfiler",
            "required": True,
        },
    )
    depositor: Optional[DepositorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/abs15gfiler",
            "required": True,
        },
    )
    issuer: Optional[IssuerType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/abs15gfiler",
            "required": True,
        },
    )
    underwriter_cik: Optional[str] = field(
        default=None,
        metadata={
            "name": "underwriterCik",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/abs15gfiler",
            "pattern": r"\d{1,10}",
        },
    )


@dataclass
class Rule15GaType:
    class Meta:
        name = "RULE15GA_TYPE"

    rule15_ga1_type: Optional[Rule15Ga1Type] = field(
        default=None,
        metadata={
            "name": "rule15Ga1Type",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/abs15gfiler",
        },
    )
    rule15_ga2_type: Optional[Rule15Ga2Type] = field(
        default=None,
        metadata={
            "name": "rule15Ga2Type",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/abs15gfiler",
        },
    )


@dataclass
class EdgarSubmission:
    class Meta:
        name = "edgarSubmission"
        namespace = "http://www.sec.gov/edgar/abs15gfiler"

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
    contact: Optional[ContactType] = field(
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
    start_period_of_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "startPeriodOfReport",
            "type": "Element",
            "pattern": r"\d{1,2}-\d{1,2}-\d{4}",
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
    submission_type: Optional[SubmissionType] = field(
        default=None,
        metadata={
            "name": "submissionType",
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
    asset_class_type: Optional[AssetClassType] = field(
        default=None,
        metadata={
            "name": "assetClassType",
            "type": "Element",
            "required": True,
        },
    )
    filer: Optional[FilerType] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    rule15_ga_type: Optional[Rule15GaType] = field(
        default=None,
        metadata={
            "name": "rule15GaType",
            "type": "Element",
            "required": True,
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
