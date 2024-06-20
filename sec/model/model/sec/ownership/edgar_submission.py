from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class EdgarDocument:
    class Meta:
        name = "EDGAR_DOCUMENT"

    document_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "documentName",
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 32,
        },
    )
    document_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "documentType",
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 20,
        },
    )
    document_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "documentDescription",
            "type": "Element",
            "max_length": 255,
        },
    )
    document_mime_block: Optional[str] = field(
        default=None,
        metadata={
            "name": "documentMimeBlock",
            "type": "Element",
            "required": True,
            "min_length": 1,
        },
    )


@dataclass
class NotifyGroup:
    class Meta:
        name = "NOTIFY_GROUP"

    notification_email_address: List[str] = field(
        default_factory=list,
        metadata={
            "name": "notificationEmailAddress",
            "type": "Element",
            "max_occurs": 30,
            "max_length": 80,
        },
    )


@dataclass
class PointOfContact:
    class Meta:
        name = "POINT_OF_CONTACT"

    contact_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "contactName",
            "type": "Element",
            "max_length": 30,
        },
    )
    contact_phone_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "contactPhoneNumber",
            "type": "Element",
            "max_length": 20,
        },
    )
    contact_email_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "contactEmailAddress",
            "type": "Element",
            "max_length": 80,
        },
    )


@dataclass
class EdgarSubmission:
    class Meta:
        name = "edgarSubmission"

    submission_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "submissionType",
            "type": "Element",
            "required": True,
            "pattern": r"3|4|5|3/A|4/A|5/A",
        },
    )
    test_or_live: Optional[str] = field(
        default=None,
        metadata={
            "name": "testOrLive",
            "type": "Element",
            "required": True,
            "pattern": r"LIVE|TEST",
        },
    )
    point_of_contact: Optional[PointOfContact] = field(
        default=None,
        metadata={
            "name": "pointOfContact",
            "type": "Element",
        },
    )
    return_copy: Optional[bool] = field(
        default=None,
        metadata={
            "name": "returnCopy",
            "type": "Element",
        },
    )
    notification_addresses: Optional[NotifyGroup] = field(
        default=None,
        metadata={
            "name": "notificationAddresses",
            "type": "Element",
        },
    )
    edgar_document: List[EdgarDocument] = field(
        default_factory=list,
        metadata={
            "name": "edgarDocument",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 611,
        },
    )
