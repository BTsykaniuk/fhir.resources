#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-13.
#  2019, SMART Health IT.

import os
import pytest
import io
import unittest
import json

from .fixtures import force_bytes
from .. import codesystem
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class CodeSystemTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("CodeSystem", js["resourceType"])
        return codesystem.CodeSystem(js)
    
    def testCodeSystem1(self):
        inst = self.instantiate_from("codesystem-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a CodeSystem instance")
        self.implCodeSystem1(inst)
        
        js = inst.as_json()
        self.assertEqual("CodeSystem", js["resourceType"])
        inst2 = codesystem.CodeSystem(js)
        self.implCodeSystem1(inst2)
    
    def implCodeSystem1(self, inst):
        self.assertTrue(inst.caseSensitive)
        self.assertEqual(force_bytes(inst.concept[0].code), force_bytes("chol-mmol"))
        self.assertEqual(force_bytes(inst.concept[0].definition), force_bytes("Serum Cholesterol, in mmol/L"))
        self.assertEqual(force_bytes(inst.concept[0].designation[0].use.code), force_bytes("internal-label"))
        self.assertEqual(force_bytes(inst.concept[0].designation[0].use.system), force_bytes("http://acme.com/config/fhir/codesystems/internal"))
        self.assertEqual(force_bytes(inst.concept[0].designation[0].value), force_bytes("From ACME POC Testing"))
        self.assertEqual(force_bytes(inst.concept[0].display), force_bytes("SChol (mmol/L)"))
        self.assertEqual(force_bytes(inst.concept[1].code), force_bytes("chol-mass"))
        self.assertEqual(force_bytes(inst.concept[1].definition), force_bytes("Serum Cholesterol, in mg/L"))
        self.assertEqual(force_bytes(inst.concept[1].designation[0].use.code), force_bytes("internal-label"))
        self.assertEqual(force_bytes(inst.concept[1].designation[0].use.system), force_bytes("http://acme.com/config/fhir/codesystems/internal"))
        self.assertEqual(force_bytes(inst.concept[1].designation[0].value), force_bytes("From Paragon Labs"))
        self.assertEqual(force_bytes(inst.concept[1].display), force_bytes("SChol (mg/L)"))
        self.assertEqual(force_bytes(inst.concept[2].code), force_bytes("chol"))
        self.assertEqual(force_bytes(inst.concept[2].definition), force_bytes("Serum Cholesterol"))
        self.assertEqual(force_bytes(inst.concept[2].designation[0].use.code), force_bytes("internal-label"))
        self.assertEqual(force_bytes(inst.concept[2].designation[0].use.system), force_bytes("http://acme.com/config/fhir/codesystems/internal"))
        self.assertEqual(force_bytes(inst.concept[2].designation[0].value), force_bytes("Obdurate Labs uses this with both kinds of units..."))
        self.assertEqual(force_bytes(inst.concept[2].display), force_bytes("SChol"))
        self.assertEqual(force_bytes(inst.contact[0].name), force_bytes("FHIR project team"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].system), force_bytes("url"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].value), force_bytes("http://hl7.org/fhir"))
        self.assertEqual(force_bytes(inst.content), force_bytes("complete"))
        self.assertEqual(inst.date.date, FHIRDate("2016-01-28").date)
        self.assertEqual(inst.date.as_json(), "2016-01-28")
        self.assertEqual(force_bytes(inst.description), force_bytes("This is an example code system that includes all the ACME codes for serum/plasma cholesterol from v2.36."))
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.filter[0].code), force_bytes("acme-plasma"))
        self.assertEqual(force_bytes(inst.filter[0].description), force_bytes("An internal filter used to select codes that are only used with plasma"))
        self.assertEqual(force_bytes(inst.filter[0].operator[0]), force_bytes("="))
        self.assertEqual(force_bytes(inst.filter[0].value), force_bytes("the value of this filter is either 'true' or 'false'"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://acme.com/identifiers/codesystems"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("internal-cholesterol-inl"))
        self.assertEqual(force_bytes(inst.meta.profile[0]), force_bytes("http://hl7.org/fhir/StructureDefinition/shareablecodesystem"))
        self.assertEqual(force_bytes(inst.name), force_bytes("ACMECholCodesBlood"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("Acme Co"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("ACME Codes for Cholesterol in Serum/Plasma"))
        self.assertEqual(force_bytes(inst.url), force_bytes("http://hl7.org/fhir/CodeSystem/example"))
        self.assertEqual(force_bytes(inst.version), force_bytes("20160128"))
    
    def testCodeSystem2(self):
        inst = self.instantiate_from("codesystem-examplescenario-actor-type.json")
        self.assertIsNotNone(inst, "Must have instantiated a CodeSystem instance")
        self.implCodeSystem2(inst)
        
        js = inst.as_json()
        self.assertEqual("CodeSystem", js["resourceType"])
        inst2 = codesystem.CodeSystem(js)
        self.implCodeSystem2(inst2)
    
    def implCodeSystem2(self, inst):
        self.assertTrue(inst.caseSensitive)
        self.assertEqual(force_bytes(inst.concept[0].code), force_bytes("person"))
        self.assertEqual(force_bytes(inst.concept[0].definition), force_bytes("A person."))
        self.assertEqual(force_bytes(inst.concept[0].display), force_bytes("Person"))
        self.assertEqual(force_bytes(inst.concept[1].code), force_bytes("entity"))
        self.assertEqual(force_bytes(inst.concept[1].definition), force_bytes("A system."))
        self.assertEqual(force_bytes(inst.concept[1].display), force_bytes("System"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].system), force_bytes("url"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].value), force_bytes("http://hl7.org/fhir"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[1].system), force_bytes("email"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[1].value), force_bytes("fhir@lists.hl7.org"))
        self.assertEqual(force_bytes(inst.content), force_bytes("complete"))
        self.assertEqual(inst.date.date, FHIRDate("2018-12-27T22:37:54+11:00").date)
        self.assertEqual(inst.date.as_json(), "2018-12-27T22:37:54+11:00")
        self.assertEqual(force_bytes(inst.description), force_bytes("The type of actor - system or human."))
        self.assertFalse(inst.experimental)
        self.assertEqual(force_bytes(inst.extension[0].url), force_bytes("http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"))
        self.assertEqual(force_bytes(inst.extension[0].valueCode), force_bytes("fhir"))
        self.assertEqual(force_bytes(inst.extension[1].url), force_bytes("http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status"))
        self.assertEqual(force_bytes(inst.extension[1].valueCode), force_bytes("trial-use"))
        self.assertEqual(force_bytes(inst.extension[2].url), force_bytes("http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"))
        self.assertEqual(inst.extension[2].valueInteger, 0)
        self.assertEqual(force_bytes(inst.id), force_bytes("examplescenario-actor-type"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("urn:oid:2.16.840.1.113883.4.642.1.859"))
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2018-12-27T22:37:54.724+11:00").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2018-12-27T22:37:54.724+11:00")
        self.assertEqual(force_bytes(inst.name), force_bytes("ExampleScenarioActorType"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("ExampleScenarioActorType"))
        self.assertEqual(force_bytes(inst.url), force_bytes("http://hl7.org/fhir/examplescenario-actor-type"))
        self.assertEqual(force_bytes(inst.valueSet), force_bytes("http://hl7.org/fhir/ValueSet/examplescenario-actor-type"))
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.0"))
    
    def testCodeSystem3(self):
        inst = self.instantiate_from("codesystem-list-example-codes.json")
        self.assertIsNotNone(inst, "Must have instantiated a CodeSystem instance")
        self.implCodeSystem3(inst)
        
        js = inst.as_json()
        self.assertEqual("CodeSystem", js["resourceType"])
        inst2 = codesystem.CodeSystem(js)
        self.implCodeSystem3(inst2)
    
    def implCodeSystem3(self, inst):
        self.assertTrue(inst.caseSensitive)
        self.assertEqual(force_bytes(inst.concept[0].code), force_bytes("alerts"))
        self.assertEqual(force_bytes(inst.concept[0].definition), force_bytes("A list of alerts for the patient."))
        self.assertEqual(force_bytes(inst.concept[0].display), force_bytes("Alerts"))
        self.assertEqual(force_bytes(inst.concept[1].code), force_bytes("adverserxns"))
        self.assertEqual(force_bytes(inst.concept[1].definition), force_bytes("A list of part adverse reactions."))
        self.assertEqual(force_bytes(inst.concept[1].display), force_bytes("Adverse Reactions"))
        self.assertEqual(force_bytes(inst.concept[2].code), force_bytes("allergies"))
        self.assertEqual(force_bytes(inst.concept[2].definition), force_bytes("A list of Allergies for the patient."))
        self.assertEqual(force_bytes(inst.concept[2].display), force_bytes("Allergies"))
        self.assertEqual(force_bytes(inst.concept[3].code), force_bytes("medications"))
        self.assertEqual(force_bytes(inst.concept[3].definition), force_bytes("A list of medication statements for the patient."))
        self.assertEqual(force_bytes(inst.concept[3].display), force_bytes("Medication List"))
        self.assertEqual(force_bytes(inst.concept[4].code), force_bytes("problems"))
        self.assertEqual(force_bytes(inst.concept[4].definition), force_bytes("A list of problems that the patient is known of have (or have had in the past)."))
        self.assertEqual(force_bytes(inst.concept[4].display), force_bytes("Problem List"))
        self.assertEqual(force_bytes(inst.concept[5].code), force_bytes("worklist"))
        self.assertEqual(force_bytes(inst.concept[5].definition), force_bytes("A list of items that constitute a set of work to be performed (typically this code would be specialized for more specific uses, such as a ward round list)."))
        self.assertEqual(force_bytes(inst.concept[5].display), force_bytes("Worklist"))
        self.assertEqual(force_bytes(inst.concept[6].code), force_bytes("waiting"))
        self.assertEqual(force_bytes(inst.concept[6].definition), force_bytes("A list of items waiting for an event (perhaps a surgical patient waiting list)."))
        self.assertEqual(force_bytes(inst.concept[6].display), force_bytes("Waiting List"))
        self.assertEqual(force_bytes(inst.concept[7].code), force_bytes("protocols"))
        self.assertEqual(force_bytes(inst.concept[7].definition), force_bytes("A set of protocols to be followed."))
        self.assertEqual(force_bytes(inst.concept[7].display), force_bytes("Protocols"))
        self.assertEqual(force_bytes(inst.concept[8].code), force_bytes("plans"))
        self.assertEqual(force_bytes(inst.concept[8].definition), force_bytes("A set of care plans that apply in a particular context of care."))
        self.assertEqual(force_bytes(inst.concept[8].display), force_bytes("Care Plans"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].system), force_bytes("url"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].value), force_bytes("http://hl7.org/fhir"))
        self.assertEqual(force_bytes(inst.content), force_bytes("complete"))
        self.assertEqual(force_bytes(inst.description), force_bytes("Example use codes for the List resource - typical kinds of use."))
        self.assertFalse(inst.experimental)
        self.assertEqual(force_bytes(inst.extension[0].url), force_bytes("http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"))
        self.assertEqual(force_bytes(inst.extension[0].valueCode), force_bytes("fhir"))
        self.assertEqual(force_bytes(inst.extension[1].url), force_bytes("http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status"))
        self.assertEqual(force_bytes(inst.extension[1].valueCode), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.extension[2].url), force_bytes("http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"))
        self.assertEqual(inst.extension[2].valueInteger, 1)
        self.assertEqual(force_bytes(inst.id), force_bytes("list-example-codes"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("urn:oid:2.16.840.1.113883.4.642.1.1105"))
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2018-12-27T22:37:54.724+11:00").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2018-12-27T22:37:54.724+11:00")
        self.assertEqual(force_bytes(inst.meta.profile[0]), force_bytes("http://hl7.org/fhir/StructureDefinition/shareablecodesystem"))
        self.assertEqual(force_bytes(inst.name), force_bytes("ExampleUseCodesForList"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("FHIR Project"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("Example Use Codes for List"))
        self.assertEqual(force_bytes(inst.url), force_bytes("http://terminology.hl7.org/CodeSystem/list-example-use-codes"))
        self.assertEqual(force_bytes(inst.valueSet), force_bytes("http://hl7.org/fhir/ValueSet/list-example-codes"))
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.0"))
    
    def testCodeSystem4(self):
        inst = self.instantiate_from("codesystem-example-summary.json")
        self.assertIsNotNone(inst, "Must have instantiated a CodeSystem instance")
        self.implCodeSystem4(inst)
        
        js = inst.as_json()
        self.assertEqual("CodeSystem", js["resourceType"])
        inst2 = codesystem.CodeSystem(js)
        self.implCodeSystem4(inst2)
    
    def implCodeSystem4(self, inst):
        self.assertTrue(inst.caseSensitive)
        self.assertEqual(force_bytes(inst.contact[0].name), force_bytes("FHIR project team"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].system), force_bytes("url"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].value), force_bytes("http://hl7.org/fhir"))
        self.assertEqual(force_bytes(inst.content), force_bytes("not-present"))
        self.assertEqual(inst.count, 92)
        self.assertEqual(force_bytes(inst.description), force_bytes("This is an example code system summary for the ACME codes for body site."))
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.id), force_bytes("summary"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].code), force_bytes("CA"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].system), force_bytes("urn:iso:std:iso:3166"))
        self.assertEqual(force_bytes(inst.name), force_bytes("Code system summary example for ACME body sites"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 International"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.url), force_bytes("http://hl7.org/fhir/CodeSystem/summary"))
        self.assertEqual(force_bytes(inst.useContext[0].code.code), force_bytes("species"))
        self.assertEqual(force_bytes(inst.useContext[0].code.system), force_bytes("http://example.org/CodeSystem/contexttype"))
        self.assertEqual(force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].code), force_bytes("337915000"))
        self.assertEqual(force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].display), force_bytes("Homo sapiens (organism)"))
        self.assertEqual(force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.0"))
    
    def testCodeSystem5(self):
        inst = self.instantiate_from("codesystem-example-supplement.json")
        self.assertIsNotNone(inst, "Must have instantiated a CodeSystem instance")
        self.implCodeSystem5(inst)
        
        js = inst.as_json()
        self.assertEqual("CodeSystem", js["resourceType"])
        inst2 = codesystem.CodeSystem(js)
        self.implCodeSystem5(inst2)
    
    def implCodeSystem5(self, inst):
        self.assertEqual(force_bytes(inst.concept[0].code), force_bytes("chol-mmol"))
        self.assertEqual(force_bytes(inst.concept[0].property[0].code), force_bytes("legacy"))
        self.assertFalse(inst.concept[0].property[0].valueBoolean)
        self.assertEqual(force_bytes(inst.concept[1].code), force_bytes("chol-mass"))
        self.assertEqual(force_bytes(inst.concept[1].property[0].code), force_bytes("legacy"))
        self.assertTrue(inst.concept[1].property[0].valueBoolean)
        self.assertEqual(force_bytes(inst.concept[2].code), force_bytes("chol"))
        self.assertEqual(force_bytes(inst.concept[2].property[0].code), force_bytes("legacy"))
        self.assertTrue(inst.concept[2].property[0].valueBoolean)
        self.assertEqual(force_bytes(inst.contact[0].name), force_bytes("FHIR project team"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].system), force_bytes("url"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].value), force_bytes("http://hl7.org/fhir"))
        self.assertEqual(force_bytes(inst.content), force_bytes("supplement"))
        self.assertEqual(inst.date.date, FHIRDate("2016-01-28").date)
        self.assertEqual(inst.date.as_json(), "2016-01-28")
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.id), force_bytes("example-supplement"))
        self.assertEqual(force_bytes(inst.name), force_bytes("CholCodeLegacyStatus"))
        self.assertEqual(force_bytes(inst.property[0].code), force_bytes("legacy"))
        self.assertEqual(force_bytes(inst.property[0].description), force_bytes("hether the test is currently performed"))
        self.assertEqual(force_bytes(inst.property[0].type), force_bytes("boolean"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("ACME Co"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.supplements), force_bytes("http://hl7.org/fhir/CodeSystem/example"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.url), force_bytes("http://hl7.org/fhir/CodeSystem/example-supplement"))
        self.assertEqual(force_bytes(inst.version), force_bytes("201801103"))

