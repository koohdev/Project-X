# 5. Research Areas, Intellectual Property, and Academic Integrity (DCT CCS)

## 5.1 Suggested Project Areas & Mandatory Quantitative Baselines

All capstone projects must solve a genuine problem for an actual client or address a demonstrable research gap.

### A. Transaction Processing Systems (TPS)
*Must feature normalized databases, backup & recovery, archiving, audit logs, validation/error trapping, and network setup.*

| System Type | Minimum Scope & Quantitative Criteria | Valid Test Data Baseline |
| :--- | :--- | :--- |
| **Payroll System** | $\ge 50$ employees; timekeeping; tax & government deduction tables (SSS, BIR, PhilHealth, Pag-IBIG); payslip generation; payroll summaries. | 50 employee profiles |
| **Sales & Inventory System** | $\ge 1,000$ inventory items; $5\text{ to }10$ product lines ($5\text{–}10$ items/line); purchase orders, critical reorder points, backorders. | 5–10 product lines; 5–10 items/line |
| **Library System** | $\ge 2,000$ book titles (CHED standard); $\ge 500$ students/members; cataloguing, circulation, overdue penalty computation, CHED reports. | 50 book titles; 50 borrowers |
| **Accounting System** | Accounts receivable & payable; aging of accounts; general ledger journal posting; financial statement generation. | 30 account ledgers |
| **Enrollment System** | $\ge 200$ students; $\ge 2$ sections per year level; registration, assessment, cashiering/billing, prerequisites checking, grading. | Full student cohort dataset |
| **Hotel Reservation & Billing** | $\ge 20$ rooms; $\ge 100$ customer capacity; room status, online/walk-in booking, check-in/out, automated billing. | 50 customer profiles |
| **Patient / Hospital Information** | $\ge 20$ beds; $\ge 50$ patients; admitting, medical history, diagnosis/treatment logs, physician profiles, billing. | 50 patient records |

---

### B. Specialized & Advanced Computing Categories

#### 1. Multimedia Systems
* **Media Integration**: Must incorporate **at least 4 media types** (text, graphics, audio, video/animation).
* **Core Requirements**: Dynamic content management, database for media/metadata, search/filter, save & print, multi-level user access (admin, viewer/researcher), and copyright compliance.

#### 2. Computer-Aided Instruction (CAI)
* **Media Integration**: At least 4 media types.
* **Instructional Pedagogy**: 2 to 3 methods of topic presentation across major categories (drills/practice, tutorials, simulation, games).
* **Pedagogical Controls**: Target age bracket identification, lesson & quiz difficulty levels, randomized test item generation, performance analytics & feedback.
* **Testing Baseline**: **50 test items per topic**.
* **Design Modeling Rule**: ⚠️ **Data Flow Diagrams (DFDs) must NOT be used** for CAI modeling. Use Storyboarding, Flowcharting, and HIPO instead.

#### 3. Web Applications
* **Host Client Requirement**: Real client/host company required with formal Certificate of Acceptance.
* **Live Deployment**: Must be **uploaded/deployed on live servers** (minimum alpha testing on public URL).
* **Required Modules**: Database-driven dynamic pages, e-consultation module (message board / email inquiry), search functionality, automated reports, meta tags, and data security.
* **Common Types**:
  * *Online Ordering with Inventory*: $\ge 1,000$ items, catalog, order tracking, payment integration.
  * *Online Hotel Reservation*: Room inventory, interactive maps, online approval/cancellation.
  * *Online Job Portal*: $\ge 100$ applicants, $\ge 10$ job offerings, applicant matching & tracking.
  * *Online Pre-Enrollment / Registration*: Tertiary level only, curriculum tracking, student portal.

#### 4. Management Information Systems (MIS)
* Required reports: Trend analysis, summary reports, exception reports, on-demand reports, and ad-hoc query builders.

#### 5. Decision Support Systems (DSS)
* Mandatory three components: **Database**, **Model Base** (algorithms/criteria), and **Dialogue Module** (interactive interface).

#### 6. Geographical Information Systems (GIS)
* Spatial data storage, multi-layer map overlays, topological modeling, routing algorithms (e.g. shortest path), and GIS export formats.

#### 7. Artificial Intelligence (AI / ICAI)
* Expert Systems (Inference engine + knowledge base), Neural Networks, Computer Vision, Robotics, Intelligent Agents.

---

## 5.2 Unacceptable Capstone Projects

The following project concepts are **strictly rejected** by the DCT CCS department:

* ❌ **DAMATH** or simple board games
* ❌ **Video / Media Rental Systems**
* ❌ **Generic Games** (non-educational games, standard card games)
* ❌ **Basic Record-Keeping Systems** (systems that merely perform CRUD without analytical/operational depth)
* ❌ **Generic Monitoring Systems** without automated control, analytics, or hardware telemetry
* ❌ **Static Websites** (Barangay, Municipal, City, or Provincial promotional websites without transactional functionality)

---

## 5.3 Intellectual Property (IP) and Ownership Policy

1. **Initial Ownership & Transfer**:
   * Projects are initially recognized as the intellectual property of student researchers.
   * Upon final approval and submission, ownership of source code, documentation, designs, and architecture transfers to the Dominican College of Tarlac - College of Computer Studies (CCS).
2. **Institutional Rights**:
   * DCT reserves non-exclusive, royalty-free rights to archive, demonstrate, exhibit, and utilize projects for accreditation and promotional purposes with student attribution.
3. **Adviser & Faculty Co-Authorship**:
   * Advisers and faculty who contribute substantial technical, architectural, or research direction beyond routine evaluation must be recognized as **co-authors** in publications, presentations, and patent applications.
4. **Sponsored / External Projects**:
   * Projects with third-party industry partners are governed by a formal **Memorandum of Agreement (MOA)**.
5. **Third-Party Compliance & Data Privacy**:
   * Mandatory compliance with the **Data Privacy Act of 2012 (RA 10173)**.
   * Strict adherence to open-source software licenses for external libraries and APIs.

---

## 5.4 Academic Integrity & Plagiarism Standards

1. **Zero-Tolerance Policy**: Plagiarism, code duplication without attribution, falsification of test data, and fabrication of research results are grounds for immediate failure and disciplinary action.
2. **Mandatory Plagiarism Clearance**:
   * **Pre-Defense Check**: Manuscript must be submitted to the DCT Research Office / Library for similarity checking before scheduling the oral defense.
   * **Pre-Publication Check**: Final revised hardbound manuscript must be re-checked before final archiving.
3. **Similarity Index**: Must meet the acceptable threshold defined by the Research Office. Any uncredited text or structure will be flagged regardless of overall percentage.
4. **Sanctions**: Include mandatory manuscript rewriting, re-defense, automatic course failure, or graduation disqualification.
