from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union

from model.sec.forms.eis_common2 import (
    BaseDocumentType,
    ContactType,
    LiveTestType,
    NotificationType,
)

__NAMESPACE__ = "http://www.sec.gov/edgar/modulessegments"


@dataclass
class FilerType:
    class Meta:
        name = "FILER_TYPE"

    filer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerId",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/modulessegments",
            "required": True,
            "pattern": r"\d{1,10}",
        },
    )
    filer_ccc: Optional[str] = field(
        default=None,
        metadata={
            "name": "filerCcc",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/modulessegments",
            "required": True,
            "length": 8,
        },
    )


@dataclass
class FlagType:
    class Meta:
        name = "FLAG_TYPE"

    override_internet_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "overrideInternetFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/modulessegments",
            "pattern": r"true|false",
        },
    )
    return_copy_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "returnCopyFlag",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/modulessegments",
            "pattern": r"true|false",
        },
    )


class SubmissionType(Enum):
    """Type of submission you are filing.

    Choose a value from the appropriate family of Submission Types.
    """

    MODULE = "MODULE"
    SEGMENT = "SEGMENT"


class Type1DocumentType(Enum):
    TYPE1 = "TYPE1"


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

    nick_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "nickName",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/modulessegments",
            "required": True,
            "min_length": 1,
            "max_length": 15,
            "pattern": r"[a-zA-Z][-_a-zA-Z0-9]*",
        },
    )
    conformed_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "conformedName",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/modulessegments",
            "required": True,
            "min_length": 1,
            "max_length": 32,
            "pattern": r"([a-zA-Z0-9]+[\w\._\-]*)([\.](([hH][tT][mM])|([tT][xX][tT])|([pP][dD][fF])|([xX][mM][lL])|([jJ][pP][gG])|([gG][iI][fF])|([fF][iI][lL])|([xX][sS][dD])))",
        },
    )
    conformed_document_type: Optional[
        Union[BaseDocumentType, str, Type1DocumentType]
    ] = field(
        default=None,
        metadata={
            "name": "conformedDocumentType",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/modulessegments",
            "required": True,
        },
    )
    master_seg_cik: Optional[str] = field(
        default=None,
        metadata={
            "name": "masterSegCik",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/modulessegments",
            "pattern": r"\d{1,10}",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/modulessegments",
            "min_length": 1,
            "max_length": 255,
            "pattern": r"[A-Za-z0-9!#-$%():;'@\*\+\-/=\?\^_`~{|},. \\\s<>&\"\[\]]{1,255}",
        },
    )
    contents: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/modulessegments",
            "required": True,
            "min_length": 1,
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
            "namespace": "http://www.sec.gov/edgar/modulessegments",
            "min_occurs": 1,
        },
    )


@dataclass
class EdgarSubmission:
    class Meta:
        name = "edgarSubmission"
        namespace = "http://www.sec.gov/edgar/modulessegments"

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
    notifications: Optional[NotificationType] = field(
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
