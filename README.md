# Telemedicine Slot Booking & Prescription Portal

PES University — Department of CSE  
Lab 1: Requirements Engineering & UML Use-Case Modelling  
Problem Statement #11: Healthcare & Telemedicine

## Contents

- `requirements-table.docx` — Complete requirements table with five functional requirements and two non-functional requirements.
- `requirements.md` — Editable requirements source.
- `use-case-diagram.pdf` — UML use-case diagram.
- `use-case-flow-specification.docx` — One-page use-case flow specification.
- `use-case-flow-specification.pdf` — PDF version of the use-case flow specification.

## Actors

- **Patient** — Views doctor specialties, books video consultation slots, joins consultations, and accesses prescriptions.
- **Attending Physician** — Conducts consultations and authors/digitally signs prescriptions.
- **License Verification Service** — Verifies the physician’s license before a prescription is digitally signed.

## Main Use Cases

- UC-01: View Doctor Specialties
- UC-02: Book Video Consultation Slot
- UC-03: Join Video Consultation
- UC-04: Download Digital Prescription
- UC-05: Author and Digitally Sign Prescription

## UML Relationships

- Booking a video consultation slot `«include»` generates an encrypted consultation link.
- Authoring and digitally signing a prescription `«include»` validates the doctor’s license.
- Viewing a digital prescription `«extend»` downloads the digital prescription.

## Core Scope

The portal allows patients to find appropriate physicians, book secure telemedicine appointments, join encrypted consultation rooms, and obtain digitally signed prescription records.
