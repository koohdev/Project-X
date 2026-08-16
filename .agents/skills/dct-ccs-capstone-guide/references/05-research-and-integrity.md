# 5. Research Areas, Intellectual Property, and Academic Integrity (DCT CCS)

## 5.1 Areas of Research & Quantitative Project Baselines

### A. Transaction Processing Systems (TPS)
Computer-based versions of manual organization systems dedicated to handling transactions.

#### General Requirements:
a. Complete file structure (normalized tables, master and transaction files).  
b. Backup and recovery features (for DBMS lacking native features).  
c. Archiving.  
d. Complete data entry components.  
e. Proper maintenance features.  
f. Complete report generation.  
g. Data entry validation and error trapping.  
h. Validation, security, data accuracy, and integrity features.  
i. Network setup.  

#### System Types and Scope Thresholds:

| System Type | Mandatory Scope & Quantitative Criteria | Test Data Baseline |
| :--- | :--- | :--- |
| **1. Payroll System** | $\ge 50$ employees; regular/contractual/part-time/consultant; timekeeping; allowable leaves/deductions; frequency of payroll; pay slip generation; payroll summary; table of variables (SSS, Tax, PhilHealth, Pag-IBIG); agency reports (BIR, SSS). | 50 employees |
| **2. Sales and Inventory** | $\ge 1,000$ inventory items; $5\text{ to }10$ product lines ($5\text{–}10$ items per line); warehouse capacity; purchase orders to/from suppliers; critical level ceiling/flooring; backorder/reorder lists. | 5–10 product lines; 5–10 items/line |
| **3. Library System** | $\ge 2,000$ book titles (CHED requirement); $\ge 500$ students/members; acquisition, cataloguing, circulation, borrowing/returning, reservations, penalty computation, CHED reports. | 50 titles; 50 borrowers |
| **4. Accounting System** | Accounts receivable and payable monitoring; aging of accounts; transaction posting to general journal; financial reports. | 30 accounts |
| **5. Enrollment System** | $\ge 200$ students; $\ge 2$ sections per year level; registration, advising, assessment, cashiering/billing, prerequisites/co-requisites, class scheduling, student grades, SIS/FIS integration. | Full cohort dataset |
| **6. Hotel Reservation & Billing** | $\ge 20$ rooms; $\ge 100$ customers; room status, check-in/out, automated billing, reservation/cancellation, fee maintenance. | 50 customers |
| **7. Patient Information & Billing** | $\ge 20$ beds; $\ge 50$ patients; admitting, medical history, diagnosis, prognosis, medication, physician records, automated billing. | 50 patients |

---

### B. Specialized Computing Categories

#### 1. Management Information Systems (MIS)
Provides standard reports for managers about transaction data:
- Trend analysis reports
- Summary reports
- Exception reports
- On-demand reports
- Ad-hoc reports

#### 2. Decision Support Systems (DSS)
Designed to assist decision-makers; requires **three mandatory components**:
- **Database**
- **Model Base** (algorithms, analytical criteria)
- **Dialogue Module** (interactive interface)

#### 3. Geographical Information Systems (GIS)
Assembles, stores, manipulates, and displays geographically referenced data:
- Information retrieval
- Topological modeling
- Network analysis
- Map overlays (multi-layer maps)
- Algorithms (e.g., shortest path)

#### 4. Scientific and Office Information Systems
Administrative and operational support systems evaluating information quality, quantity, and user categories.

#### 5. Multimedia Systems
Encapsulates multiple digital media (text, images, audio, video, graphics, animation, music):
- **Mandatory integration of at least 4 media types** (text, graphics, audio, video).
- Dynamic content management and maintenance features.
- Database storage for multi-format assets.
- Search, save, and print functions.
- Multi-level user access (system administrator, viewer/researcher).
- Copyright compliance for all utilized media assets.

#### 6. Computer-Aided Instruction (CAI)
Facilitates learning through multimedia, lessons, exams/drills, and feedback:
- Incorporation of **at least 4 media types** and dynamic content management.
- Major categories: drills & practice, tutorials, simulation, games.
- **2 to 3 methods** of presenting topics.
- Target age bracket identification and structured difficulty levels.
- **50 test items per topic** with random question generation and result analysis.
- Required design tools: Storyboarding, Flowcharting, HIPO.
- ⚠️ **CRITICAL RULE**: **Data Flow Diagrams (DFDs) must NOT be used** in modeling CAI features and functions.

#### 7. Web Applications
Focuses on innovative web applications with a mandatory host client:
- Database-driven dynamic pages.
- E-consultation module (bulletin board, message board, or browser email inquiry).
- Search engine, report generation, meta tags & hyperlinks.
- Uploaded and deployed on a live server (at least alpha testing on live URL).
- Core types: Online Ordering with Inventory, Online Hotel Reservation, Online Job Application ($\ge 100$ applicants, $\ge 10$ job offerings, job matching), Online Pre-Enrollment (Tertiary level only).

#### 8. Artificial Intelligence (AI)
- Expert Systems (ES): Database, dialogue module, inference engine, knowledge acquisition.
- Neural Networks, Robotics, Intelligent Agents, Intelligent CAI (ICAI).

#### 9. Software Engineering, Systems Analysis & Design, Networking
- Systems software, cost models, automated CASE tools, network topology implementations.

---

## 5.2 Unacceptable Capstone Projects

The following project categories are **strictly rejected**:
* ❌ **DAMATH**
* ❌ **Video Rental System**
* ❌ **Games** (card games, non-educational games)
* ❌ **Record Keeping Systems** (basic CRUD without operational depth)
* ❌ **Monitoring Systems** (without hardware integration, telemetry, or analytics)
* ❌ **Static Websites** (Barangay, Municipality, City, or Provincial promotional websites)

*Note: DCT may reject any project depending on scope, feasibility, practicality, and originality.*

---

## 5.3 Intellectual Property (IP) and Ownership Policy

1. **Ownership and Transfer of IP**: Projects are initially recognized as the intellectual property of student developers. Upon final approval and submission, ownership of source code, system architecture, documentation, multimedia assets, and deployment rights transfers to the College of Computer Studies (CCS) via the signed IP Transfer and Acknowledgment Form.
2. **School's Rights and Usage**: The College reserves non-exclusive, royalty-free rights to archive, display, demonstrate for instructional/accreditation/research purposes, and use non-sensitive portions with proper student acknowledgment.
3. **Adviser and Panel Contributions**: Advisers and faculty who provide substantial intellectual, technical, or creative direction beyond routine supervision automatically qualify for **mandatory co-authorship** in all official submissions, presentations, publications, and patents.
4. **Sponsored / Externally Funded Projects**: Governed by a separate Memorandum of Agreement (MOA).
5. **Use of Third-Party Materials**: Students are strictly responsible for licensing of third-party libraries, APIs, datasets, open-source compliance, and documentation citations.
6. **Commercialization & Future Development**: Students may further develop or commercialize outputs after completion; the College claims no financial rights unless agreed upon in writing.
7. **Confidentiality & Data Protection**: Full compliance with the **Data Privacy Act of 2012 (RA 10173)**.
8. **Acknowledgment Requirement**: Any public presentation or publication must acknowledge Dominican College of Tarlac, the College of Computer Studies, and the academic program.
9. **Policy Acceptance**: Submission of proposals or deliverables constitutes formal acceptance of this policy.

---

## 5.4 Academic Integrity & Plagiarism Guidelines

1. **Policy Statement**: CCS upholds strict honesty, originality, and ethical scholarship. Plagiarism, falsification, and misrepresentation are treated as serious offenses.
2. **Definition of Plagiarism**: Copying text/code/designs without citation, paraphrasing without acknowledgment, submitting work generated/purchased from others, and self-plagiarism. Applies to manuscripts, source code, designs, and research outputs.
3. **Other Academic Anomalies**: Fabrication of data/results, misrepresentation of system functionality, unauthorized use of AI/automated tools, and tampered documents.
4. **Plagiarism Detection Mechanisms**:
   - **Mandatory Pre-Oral Defense Check**: All capstone papers must be officially cleared by the DCT Research Office or Library before oral defense.
   - **Post-Final Defense Check**: Approved revised manuscripts must be re-checked before book binding and archiving.
   - **Manual Review**: Faculty assessment of originality and citation integrity.
5. **Acceptable Similarity Index**: Determined by the Research Office. Any submission exceeding thresholds or showing improper attribution is subject to review regardless of percentage.
6. **Sanctions**: Mandatory revision, re-defense, automatic failure of capstone course, graduation delay/disqualification, and referral to the Ethics Committee.
7. **Due Process**: Written notification, opportunity to respond, and formal deliberation by the academic body.
