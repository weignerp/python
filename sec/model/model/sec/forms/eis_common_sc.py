from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

__NAMESPACE__ = "http://www.sec.gov/edgar/sccommon"


class MergeInvCompanyType(Enum):
    N_1_A = "N-1A"
    N_1 = "N-1"
    N_2 = "N-2"
    N_3 = "N-3"
    N_4 = "N-4"
    N_5 = "N-5"
    N_6 = "N-6"
    S_1_OR_S_3 = "S-1 or S-3"
    S_6 = "S-6"
    NOT_AN_INVESTMENT_COMPANY = "Not an Investment Company"


@dataclass
class MultiAccessionNumbersType:
    class Meta:
        name = "MULTI_ACCESSION_NUMBERS_TYPE"

    accession_number: List[str] = field(
        default_factory=list,
        metadata={
            "name": "accessionNumber",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sccommon",
            "min_occurs": 1,
            "pattern": r"[*]{0}|[0-9]{1,10}\-[0-9]{1,2}\-[0-9]{1,6}",
        },
    )


@dataclass
class NewClassType:
    class Meta:
        name = "NEW_CLASS_TYPE"

    class_name: List[str] = field(
        default_factory=list,
        metadata={
            "name": "className",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sccommon",
            "min_length": 1,
            "max_length": 150,
            "pattern": r"[A-Za-z0-9!#-$%():;'@\*\+\-/=\?\^_`~{|},. \\\s<>&\"\[\]]{1,150}",
        },
    )
    use_comp_name_as_class_name_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "useCompNameAsClassNameFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sccommon",
            "pattern": r"true|false",
        },
    )


@dataclass
class NewClassType2:
    class Meta:
        name = "NEW_CLASS_TYPE_2"

    series_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "seriesId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sccommon",
            "pattern": r"[S|s][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",
        },
    )
    class_name: List[str] = field(
        default_factory=list,
        metadata={
            "name": "className",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sccommon",
            "min_occurs": 1,
            "min_length": 1,
            "max_length": 150,
            "pattern": r"[A-Za-z0-9!#-$%():;'@\*\+\-/=\?\^_`~{|},. \\\s<>&\"\[\]]{1,150}",
        },
    )


@dataclass
class NewSeriesClassType:
    class Meta:
        name = "NEW_SERIES_CLASS_TYPE"

    series_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "seriesName",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sccommon",
            "required": True,
            "min_length": 1,
            "max_length": 150,
            "pattern": r"[A-Za-z0-9!#-$%():;'@\*\+\-/=\?\^_`~{|},. \\\s<>&\"\[\]]{1,150}",
        },
    )
    use_comp_name_as_series_name_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "useCompNameAsSeriesNameFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sccommon",
            "pattern": r"true|false",
        },
    )
    class_name: List[str] = field(
        default_factory=list,
        metadata={
            "name": "className",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sccommon",
            "min_occurs": 1,
            "min_length": 1,
            "max_length": 150,
            "pattern": r"[A-Za-z0-9!#-$%():;'@\*\+\-/=\?\^_`~{|},. \\\s<>&\"\[\]]{1,150}",
        },
    )
    use_series_name_as_class_name_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "useSeriesNameAsClassNameFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sccommon",
            "pattern": r"true|false",
        },
    )


@dataclass
class RptClassType:
    class Meta:
        name = "RPT_CLASS_TYPE"

    rpt_include_all_classes_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "rptIncludeAllClassesFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sccommon",
            "pattern": r"true|false",
        },
    )
    rpt_class_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "rptClassId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sccommon",
            "pattern": r"[C|c][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",
        },
    )


@dataclass
class SeriesClassPairType:
    class Meta:
        name = "SERIES_CLASS_PAIR_TYPE"

    series_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "seriesId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sccommon",
            "required": True,
            "pattern": r"[S|s][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",
        },
    )
    include_all_classes_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "includeAllClassesFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sccommon",
            "pattern": r"true|false",
        },
    )
    class_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "classId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sccommon",
            "pattern": r"[C|c][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",
        },
    )


@dataclass
class AcquiringType:
    """Identifies the investment company type of the acquiring company.

    Choose a value from the list displayed when the arrow is selected.
    """

    class Meta:
        name = "ACQUIRING_TYPE"

    acquiring_inv_company_type: Optional[MergeInvCompanyType] = field(
        default=None,
        metadata={
            "name": "acquiringInvCompanyType",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sccommon",
            "required": True,
        },
    )
    acquiring_cik: Optional[str] = field(
        default=None,
        metadata={
            "name": "acquiringCik",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sccommon",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    acquiring_series_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "acquiringSeriesId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sccommon",
            "pattern": r"[S|s][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",
        },
    )
    acquiring_class_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "acquiringClassId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sccommon",
            "pattern": r"[C|c][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",
        },
    )


@dataclass
class RptSeriesType:
    class Meta:
        name = "RPT_SERIES_TYPE"

    rpt_include_all_series_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "rptIncludeAllSeriesFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sccommon",
            "pattern": r"true|false",
        },
    )
    rpt_series_class_info: List[SeriesClassPairType] = field(
        default_factory=list,
        metadata={
            "name": "rptSeriesClassInfo",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sccommon",
        },
    )


@dataclass
class TargetType:
    class Meta:
        name = "TARGET_TYPE"

    target_inv_company_type: Optional[MergeInvCompanyType] = field(
        default=None,
        metadata={
            "name": "targetInvCompanyType",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sccommon",
            "required": True,
        },
    )
    target_cik: Optional[str] = field(
        default=None,
        metadata={
            "name": "targetCik",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sccommon",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    target_include_all_series_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "targetIncludeAllSeriesFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sccommon",
            "pattern": r"true|false",
        },
    )
    target_series_class_info: List[SeriesClassPairType] = field(
        default_factory=list,
        metadata={
            "name": "targetSeriesClassInfo",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sccommon",
        },
    )
    target_class_info: Optional[RptClassType] = field(
        default=None,
        metadata={
            "name": "targetClassInfo",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sccommon",
        },
    )


@dataclass
class AcquiringTargetType:
    class Meta:
        name = "ACQUIRING_TARGET_TYPE"

    acquiring_info: Optional[AcquiringType] = field(
        default=None,
        metadata={
            "name": "acquiringInfo",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sccommon",
            "required": True,
        },
    )
    target_info: Optional[TargetType] = field(
        default=None,
        metadata={
            "name": "targetInfo",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sccommon",
            "required": True,
        },
    )


@dataclass
class MgrSeriesClassType:
    class Meta:
        name = "MGR_SERIES_CLASS_TYPE"

    mgr_series_class: List[AcquiringTargetType] = field(
        default_factory=list,
        metadata={
            "name": "mgrSeriesClass",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/sccommon",
            "min_occurs": 1,
        },
    )
