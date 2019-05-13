#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/FamilyMemberHistory) on 2019-05-13.
#  2019, SMART Health IT.


from . import domainresource

class FamilyMemberHistory(domainresource.DomainResource):
    """ Information about patient's relatives, relevant for patient.

    Significant health conditions for a person related to the patient relevant
    in the context of care for the patient.
    """

    resource_type = "FamilyMemberHistory"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.ageAge = None
        """ (approximate) age.
        Type `Age` (represented as `dict` in JSON). """

        self.ageRange = None
        """ (approximate) age.
        Type `Range` (represented as `dict` in JSON). """

        self.ageString = None
        """ (approximate) age.
        Type `str`. """

        self.bornDate = None
        """ (approximate) date of birth.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.bornPeriod = None
        """ (approximate) date of birth.
        Type `Period` (represented as `dict` in JSON). """

        self.bornString = None
        """ (approximate) date of birth.
        Type `str`. """

        self.condition = None
        """ Condition that the related person had.
        List of `FamilyMemberHistoryCondition` items (represented as `dict` in JSON). """

        self.dataAbsentReason = None
        """ subject-unknown | withheld | unable-to-obtain | deferred.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.date = None
        """ When history was recorded or last updated.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.deceasedAge = None
        """ Dead? How old/when?.
        Type `Age` (represented as `dict` in JSON). """

        self.deceasedBoolean = None
        """ Dead? How old/when?.
        Type `bool`. """

        self.deceasedDate = None
        """ Dead? How old/when?.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.deceasedRange = None
        """ Dead? How old/when?.
        Type `Range` (represented as `dict` in JSON). """

        self.deceasedString = None
        """ Dead? How old/when?.
        Type `str`. """

        self.estimatedAge = None
        """ Age is estimated?.
        Type `bool`. """

        self.identifier = None
        """ External Id(s) for this record.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.instantiatesCanonical = None
        """ Instantiates FHIR protocol or definition.
        List of `str` items. """

        self.instantiatesUri = None
        """ Instantiates external protocol or definition.
        List of `str` items. """

        self.name = None
        """ The family member described.
        Type `str`. """

        self.note = None
        """ General note about related person.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.patient = None
        """ Patient history is about.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.reasonCode = None
        """ Why was family member history performed?.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.reasonReference = None
        """ Why was family member history performed?.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.relationship = None
        """ Relationship to the subject.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.sex = None
        """ male | female | other | unknown.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.status = None
        """ partial | completed | entered-in-error | health-unknown.
        Type `str`. """

        super(FamilyMemberHistory, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(FamilyMemberHistory, self).elementProperties()
        js.extend([
            ("ageAge", "ageAge", age.Age, "Age", False, "age", False),
            ("ageRange", "ageRange", range.Range, "Range", False, "age", False),
            ("ageString", "ageString", str, "string", False, "age", False),
            ("bornDate", "bornDate", fhirdate.FHIRDate, "date", False, "born", False),
            ("bornPeriod", "bornPeriod", period.Period, "Period", False, "born", False),
            ("bornString", "bornString", str, "string", False, "born", False),
            ("condition", "condition", FamilyMemberHistoryCondition, "FamilyMemberHistoryCondition", True, None, False),
            ("dataAbsentReason", "dataAbsentReason", codeableconcept.CodeableConcept, "CodeableConcept", False, None, False),
            ("date", "date", fhirdate.FHIRDate, "dateTime", False, None, False),
            ("deceasedAge", "deceasedAge", age.Age, "Age", False, "deceased", False),
            ("deceasedBoolean", "deceasedBoolean", bool, "boolean", False, "deceased", False),
            ("deceasedDate", "deceasedDate", fhirdate.FHIRDate, "date", False, "deceased", False),
            ("deceasedRange", "deceasedRange", range.Range, "Range", False, "deceased", False),
            ("deceasedString", "deceasedString", str, "string", False, "deceased", False),
            ("estimatedAge", "estimatedAge", bool, "boolean", False, None, False),
            ("identifier", "identifier", identifier.Identifier, "Identifier", True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, "canonical", True, None, False),
            ("instantiatesUri", "instantiatesUri", str, "uri", True, None, False),
            ("name", "name", str, "string", False, None, False),
            ("note", "note", annotation.Annotation, "Annotation", True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, "Reference", False, None, True),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, "CodeableConcept", True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, "Reference", True, None, False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, "CodeableConcept", False, None, True),
            ("sex", "sex", codeableconcept.CodeableConcept, "CodeableConcept", False, None, False),
            ("status", "status", str, "code", False, None, True),
        ])
        return js


from . import backboneelement

class FamilyMemberHistoryCondition(backboneelement.BackboneElement):
    """ Condition that the related person had.

    The significant Conditions (or condition) that the family member had. This
    is a repeating section to allow a system to represent more than one
    condition per resource, though there is nothing stopping multiple resources
    - one per condition.
    """

    resource_type = "FamilyMemberHistoryCondition"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Condition suffered by relation.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.contributedToDeath = None
        """ Whether the condition contributed to the cause of death.
        Type `bool`. """

        self.note = None
        """ Extra information about condition.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.onsetAge = None
        """ When condition first manifested.
        Type `Age` (represented as `dict` in JSON). """

        self.onsetPeriod = None
        """ When condition first manifested.
        Type `Period` (represented as `dict` in JSON). """

        self.onsetRange = None
        """ When condition first manifested.
        Type `Range` (represented as `dict` in JSON). """

        self.onsetString = None
        """ When condition first manifested.
        Type `str`. """

        self.outcome = None
        """ deceased | permanent disability | etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(FamilyMemberHistoryCondition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(FamilyMemberHistoryCondition, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, "CodeableConcept", False, None, True),
            ("contributedToDeath", "contributedToDeath", bool, "boolean", False, None, False),
            ("note", "note", annotation.Annotation, "Annotation", True, None, False),
            ("onsetAge", "onsetAge", age.Age, "Age", False, "onset", False),
            ("onsetPeriod", "onsetPeriod", period.Period, "Period", False, "onset", False),
            ("onsetRange", "onsetRange", range.Range, "Range", False, "onset", False),
            ("onsetString", "onsetString", str, "string", False, "onset", False),
            ("outcome", "outcome", codeableconcept.CodeableConcept, "CodeableConcept", False, None, False),
        ])
        return js


import sys
try:
    from . import age
except ImportError:
    age = sys.modules[__package__ + '.age']
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
