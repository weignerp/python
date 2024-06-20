from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union

from model.sec.forms.eis_common2 import (
    AcceleratedStatusType,
    ActType,
    ContactType,
    EdgarDocumentsType,
    InvCompanyType,
    InvestmentCompanyType,
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
)

__NAMESPACE__ = "http://www.sec.gov/edgar/coregfee"


class ComboFormType(Enum):
    """Used to specify a different form type for a co-registrant filing.

    Choose the value from the list displayed when the arrow is selected.
    """

    S_1 = "S-1"
    S_1_A = "S-1/A"
    S_3 = "S-3"
    S_3_A = "S-3/A"
    S_1_MEF = "S-1MEF"
    S_3_MEF = "S-3MEF"


@dataclass
class FlagType:
    class Meta:
        name = "FLAG_TYPE"

    confirming_copy_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "confirmingCopyFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregfee",
            "pattern": r"true|false",
        },
    )
    delaying_amendment_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "delayingAmendmentFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregfee",
            "pattern": r"true|false",
        },
    )
    override_internet_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "overrideInternetFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregfee",
            "pattern": r"true|false",
        },
    )
    return_copy_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "returnCopyFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregfee",
            "pattern": r"true|false",
        },
    )


class SubmissionType(Enum):
    """Type of submission you are filing.

    Choose a value from the appropriate family of Submission Types.
    """

    F_1 = "F-1"
    F_1_A = "F-1/A"
    F_10 = "F-10"
    F_10_A = "F-10/A"
    F_10_EF = "F-10EF"
    F_1_MEF = "F-1MEF"
    F_3 = "F-3"
    F_3_A = "F-3/A"
    F_3_ASR = "F-3ASR"
    F_3_D = "F-3D"
    F_3_MEF = "F-3MEF"
    F_4 = "F-4"
    F_4_A = "F-4/A"
    F_4_EF = "F-4EF"
    F_4_MEF = "F-4MEF"
    F_7 = "F-7"
    F_7_A = "F-7/A"
    F_8 = "F-8"
    F_8_A = "F-8/A"
    F_80 = "F-80"
    F_80_A = "F-80/A"
    F_9 = "F-9"
    F_9_A = "F-9/A"
    F_9_EF = "F-9EF"
    N_14_8_C = "N-14 8C"
    N_14_8_C_A = "N-14 8C/A"
    N_14_MEF = "N-14MEF"
    N_2 = "N-2"
    N_2_A = "N-2/A"
    N_2_MEF = "N-2MEF"
    N_2_ASR = "N-2ASR"
    N_2_POSASR = "N-2 POSASR"
    N_5 = "N-5"
    N_5_A = "N-5/A"
    POSASR = "POSASR"
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
    S_3_MEF = "S-3MEF"
    S_4 = "S-4"
    S_4_A = "S-4/A"
    S_4_EF = "S-4EF"
    S_4_MEF = "S-4MEF"
    S_8 = "S-8"
    S_B = "S-B"
    S_B_A = "S-B/A"
    S_BMEF = "S-BMEF"


@dataclass
class FilerType:
    class Meta:
        name = "FILER_TYPE"

    filer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregfee",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    filer_ccc: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerCcc",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregfee",
            "required": True,
            "length": 8,
        },
    )
    file_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregfee",
            "pattern": r"\d{1,3}-\d{1,8}-[a-zA-Z0-9]{1,4}|\d{1,3}-\d{1,8}",
        },
    )
    filer_form_type: Optional[ComboFormType] = field(
        default=None,
        metadata={
            "name": "filerFormType",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregfee",
        },
    )


@dataclass
class FilerType2:
    class Meta:
        name = "FILER_TYPE_2"

    filer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregfee",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    filer_ccc: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerCcc",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregfee",
            "required": True,
            "length": 8,
        },
    )
    file_number: Optional[Union[str, NewFileNumType]] = field(
        default=None,
        metadata={
            "name": "fileNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregfee",
            "pattern": r"\d{1,3}-\d{1,8}-[a-zA-Z0-9]{1,4}|\d{1,3}-\d{1,8}",
        },
    )
    filer_form_type: Optional[ComboFormType] = field(
        default=None,
        metadata={
            "name": "filerFormType",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregfee",
        },
    )
    emerging_growth_company_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "emergingGrowthCompanyFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregfee",
            "pattern": r"true|false",
        },
    )
    ex_transition_period_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "exTransitionPeriodFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregfee",
            "pattern": r"true|false",
        },
    )


@dataclass
class InvestCompType:
    """Identifies the investment company type of the filer.

    Choose a value from the list displayed when the arrow is selected.
    """

    class Meta:
        name = "INVEST_COMP_TYPE"

    invest_company: Optional[InvCompanyType] = field(
        default=None,
        metadata={
            "name": "investCompany",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregfee",
        },
    )
    investment_company: Optional[InvestmentCompanyType] = field(
        default=None,
        metadata={
            "name": "investmentCompany",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/coregfee",
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
            "namespace": "http://www.sec.gov/edgar/coregfee",
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
    :ivar coregs:
    :ivar sros:
    :ivar fee_table_included_flag:
    :ivar small_business_flag:
    :ivar inv_company:
    :ivar well_known_seasoned_issuer_flag:
    :ivar filer_new_registrant_flag:
    :ivar pursuant_general_instruction_flag:
    :ivar eligible_fund_flag:
    :ivar emerging_growth_company_flag:
    :ivar ex_transition_period_flag:
    :ivar accelerated_filer_status:
    :ivar references:
    :ivar effective_date:
    :ivar act:
    :ivar notifications:
    :ivar module_segments:
    :ivar documents:
    :ivar edgar_fee: Comment describing your root element
    """

    class Meta:
        name = "edgarSubmission"
        namespace = "http://www.sec.gov/edgar/coregfee"

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
    fee_table_included_flag: Optional[YesNoType] = field(
        default=None,
        metadata={
            "name": "feeTableIncludedFlag",
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
    inv_company: Optional[InvestCompType] = field(
        default=None,
        metadata={
            "name": "invCompany",
            "type": "Element",
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
    eligible_fund_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "eligibleFundFlag",
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
    references: Optional["EdgarSubmission.References"] = field(
        default=None,
        metadata={
            "type": "Element",
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
    act: Optional[ActType] = field(
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
    edgar_fee: Optional["EdgarSubmission.EdgarFee"] = field(
        default=None,
        metadata={
            "name": "edgarFee",
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
                "pattern": r"\d{1,3}-\d{1,8}-[a-zA-Z0-9]{1,4}|\d{1,3}-\d{1,8}",
            },
        )
        references_462b: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "pattern": r"\d{1,3}-\d{1,8}-[a-zA-Z0-9]{1,4}|\d{1,3}-\d{1,8}",
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
