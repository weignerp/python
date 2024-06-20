from dataclasses import dataclass, field
from typing import List, Optional

from model.sec.forms.eis_common2 import LiveTestType

__NAMESPACE__ = "http://www.sec.gov/edgar/bulkfiling"


@dataclass
class EdgarSubmissionType:
    """Document names must be lower case and no longer than thirty-two (32)
    characters in length.

    The names must start with a letter (a-z) and may contain numbers
    (0-9) with no spaces.  Document names may contain one period (.),
    one hyphen (-), and one underscore (_) character and must end with
    *.htm, *.txt, *.pdf, *.fil, *.jpg, *.gif, *.xml or *.xsd extensions.
    """

    class Meta:
        name = "EDGAR_SUBMISSION_TYPE"

    submission_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "submissionName",
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/bulkfiling",
            "required": True,
            "min_length": 1,
            "max_length": 32,
            "pattern": r"([a-zA-Z0-9]+[\w\._\-]*)([\.]([xX][mM][lL])|([eE][iI][sS]))",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/bulkfiling",
            "min_length": 1,
            "max_length": 255,
            "pattern": r"[A-Za-z0-9!#-$%():;'@\*\+\-/=\?\^_`~{|},. \\\s<>&\"\[\]]{1,255}",
        },
    )
    contents: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/bulkfiling",
            "required": True,
            "min_length": 1,
        },
    )


@dataclass
class EdgarSubmissionsType:
    class Meta:
        name = "EDGAR_SUBMISSIONS_TYPE"

    attachment: List[EdgarSubmissionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.sec.gov/edgar/bulkfiling",
            "min_occurs": 1,
        },
    )


@dataclass
class EdgarBulkSubmission:
    class Meta:
        name = "edgarBulkSubmission"
        namespace = "http://www.sec.gov/edgar/bulkfiling"

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
    attachments: Optional[EdgarSubmissionsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
