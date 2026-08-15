# 3. Chapter Specifications and Content Standards (DCT CCS)

This reference outlines the required structure, mandatory subsections, content expectations, and diagrams for Chapters 1.0 through 5.0 of the Capstone Manuscript.

---

## 1.0 Introduction

### 1.1 Project Context
* **Length**: Must be **at least two (2) full pages** of comprehensive discussion.
* **Scope of Background**: Describe the existing and prevailing problem situation across global, national, and local/regional context.
* **Researcher Justification**: Establish why the researchers selected this problem (institutional familiarity, societal need, efficiency bottlenecks).
* **Guiding Questions to Answer**:
  1. *What is the primary function of the project?*
  2. *What is good/advantageous about your project compared to existing methods?*
  3. *What makes your project unique, innovative, and socially/academically relevant?*
* **Technology Inclusion**: Must introduce the key computing concepts, frameworks, and modern technologies utilized in developing the solution.

### 1.2 / 1.3 Project Objectives

#### General Objective (Major Objective)
* Stated in a **single clear, focused paragraph** describing the ultimate goal of the capstone project.

#### Specific Objectives (Minor Objectives)
* Numbered list of concrete engineering and research steps required to achieve the general objective.
* Must strictly follow the **SMART** criteria:
  * **S**pecific: Clearly states exact system functionality or target.
  * **M**easurable: Can be verified using quantifiable instruments, metrics, or test tools.
  * **A**chievable: Technically and operationally feasible within project timeline and team capacity.
  * **R**ealistic: Scientifically attainable and based on verifiable requirements.
  * **T**ime-Bound: Aligned with the semester timeline and milestones.

### 1.4 Scope and Limitations
* **Scope**: Defines the exact boundary of the prototype, target users, specific modules, data inputs/outputs, and evaluation parameters.
* **Limitations**: Explicitly states conditions beyond the proponents' control that place restrictions on findings or execution.
* *Rule*: Every single listed limitation **must be accompanied by a concrete justification**.

---

## 2.0 Review of Related Literature and Systems

### 2.1 Related Literature & Theories
* **Anchor Theory**: Start with a well-defined theoretical anchor that serves as the conceptual foundation.
* **Auxiliary / Supporting Theories**: Provide supporting theories that elaborate, support, and connect to the anchor.
* **Citation Rule**: Use the DCT alphanumeric format `[AUTH2024]` (no traditional footnotes).
* **Flow**: Maintain narrative fluidity and thematic continuity between paragraphs.

### 2.2 Related Projects & Systems
* **Inventory of Systems**: Review **3 to 6 existing related systems/studies** (mix of local and international).
* **Comparative Analysis Matrix**: Mandatory comparative table evaluating features, strengths, weaknesses, and gaps of existing systems vs. the proposed system.
* **Visual Evidence**: Include screenshots or UI breakdowns of referenced existing systems to support comparative claims.

---

## 3.0 Technical Background

Comprehensive analysis of the technical ecosystem comparing the current manual/legacy system against the proposed computerized solution across two main sections and four pillars:

### 3.1 Development
* Hardware, Software, Peopleware, and Network requirements during system construction.

### 3.2 Implementation
* Hardware, Software, Peopleware, and Network requirements for live production deployment.

#### Four Pillars Breakdown:
1. **Hardware**: Client machines, servers, IoT sensors, barcode/RFID scanners, mobile hardware specs.
2. **Software**: Operating systems, programming languages, backend frameworks, database management systems (DBMS), APIs, libraries.
3. **Peopleware**: User roles, system administrators, operators, technical support, required skillsets and training.
4. **Network**: Network infrastructure, transmission media, bandwidth requirements, protocol configurations (HTTP/HTTPS, TCP/IP, WebSockets).

---

## 4.0 Methodology, Results and Discussion

### 4.1 Methodology
* Identification and justification of the Software Engineering Systems Analysis & Design Methodology (e.g., Agile Scrum, Waterfall, Iterative, Prototyping, V-Model).
* Clear diagram illustrating the SDLC phases mapped directly to project activities.

### 4.2 Environment (Required for Organization-Specific Projects)
* **4.2.1 Locale**: Physical and geographic setting of the client organization.
* **4.2.2 Population of the Study**: Target user population, sampling method, and respondent breakdown.
* **4.2.3 Organizational Profile & Hierarchy**: Background of the client firm and organizational chart showing operational workflow.

### 4.3 Requirements Specification

#### 4.3.1 Operational Feasibility
* **Fishbone (Ishikawa) Diagram**: Root-cause analysis of the client's existing operational issues.
* **Functional Decomposition Diagram (FDD)**: Hierarchical breakdown of system functions into modular subsystems.

#### 4.3.2 Technical Feasibility
* **Compatibility Checking**: Hardware/software compatibility assessment with client environment.
* **Relevance of Technologies**: Justification for chosen tech stack against alternatives.

#### 4.3.3 Schedule Feasibility
* **Gantt Chart**: Detailed timeline marking phases, milestones, start/end dates, and task durations across Planning, Analysis, Design, Development, and Implementation.

#### 4.3.4 Economic Feasibility
* **Cost and Benefit Analysis (CBA)**: Tangible and intangible costs (development, hardware, recurring) vs. tangible/intangible benefits.
* **Cost Recovery Scheme**: Payback period, Return on Investment (ROI), and break-even calculations.

#### 4.3.5 Requirements Modeling (Include applicable approach or combination)
* **A. Data and Process Modeling**:
  * Context Diagram (Level 0)
  * Data Flow Diagrams (DFD Level 1 & Child Diagrams) — ⚠️ *Note: DFDs must NOT be used for Computer-Aided Instruction (CAI) projects. Use Storyboarding, Flowcharting, and HIPO instead.*
  * System Flowcharts
  * Program Flowcharts (Key algorithmic highlights)
* **B. Object-Oriented Modeling (UML)**:
  * Use Case Diagram (with detailed Use Case narrative specifications)
  * Class Diagram
  * Sequence Diagram
  * Activity Diagram

#### 4.3.6 Risk Assessment / Analysis
* Identification of operational, technical, security, and project management risks with risk mitigation strategies.

### 4.4 System Design

* **4.4.1 Output and UI Design Forms**:
  * Design tokens: Color palette, typography standards, icon sets.
  * Wireframes / High-fidelity mockups following the DCT Screen Design format (Screen No., Screen Name, Narrative Overview, Screen Layout).
* **4.4.2 Data Design**:
  * Entity Relationship Diagram (ERD) with full cardinality and relationship definitions (*Note: MS Access discouraged as production DBMS*).
  * Data Dictionary: Tables, attributes, data types, field lengths, constraints, primary keys, foreign keys, and descriptions.
* **4.4.3 System Architecture**:
  * Network Model & Topology Diagram (Client-Server, Multi-tier, Cloud Architecture).
  * System Security Architecture (Authentication, authorization, data encryption, RBAC).

### 4.5 Development

* **4.5.1 Software Specifications**: Detailed developer dependencies and production environment tools.
* **4.5.2 Hardware Specifications**: Minimum and recommended developer and server hardware specs.
* **4.5.3 Program Specifications**: Functional breakdown of core modules and classes.
* **4.5.4 Programming Environment**: Front-end technologies, Back-end stack, and specific programming issues/considerations handled.
* **4.5.5 Deployment Diagram**: Physical nodes, artifact deployment, and hosting configuration.
* **4.5.6 Test Plan & Test Data**: Test strategy, test matrix, and sample datasets used for verification.

### 4.6 Verification, Validation, and Testing

* **4.6.1 Unit Testing**: Test cases verifying isolated functions, methods, and individual component logic.
* **4.6.2 Integration Testing**:
  * Compatibility Testing
  * Performance Testing
  * Stress Testing
  * Load Testing (concurrency limits)
* **4.6.3 System Testing**:
  * System Functional Testing
  * Comprehensive Test Data (e.g. CAI: 50 test items/topic; TPS: 50 accounts/employees), Actual Results vs. Expected Results, Observations.
* **4.6.4 User Acceptance Testing (UAT)**:
  * ISO/IEC 25010 or standard CCS evaluation instrument administered to end-users and IT experts.
  * Likert-scale statistical analysis and overall acceptability rating.

### 4.7 Implementation Plan
Addresses all environmental integration factors:
1. **Physical Environment**: Server placement, space requirements, power backup, cooling, environmental restrictions.
2. **Interfaces**: External APIs, legacy system bridges, data interchange formats (JSON, XML).
3. **Functionality**: Cut-over schedule, maintenance protocols, upgrade pathways.
4. **Data Specifications**: Data migration procedures, frequency of transfers, backup schedules, precision requirements.
5. **Security**: Access control policies, data isolation, OS sandboxing, disaster recovery.

### 4.8 Installation & Conversion Processes
Detailed conversion strategy:
* **Selected Conversion Strategy**: Direct Cutover, Phased / Step-by-Step, or Parallel Run with detailed justification.
* Step-by-step migration, database seeding, staff user training, and rollout activities.

---

## 5.0 Conclusion and Recommendations

### 5.1 Conclusions
* Directly answers each SMART specific objective formulated in Section 1.3.
* Summarizes major engineering achievements, evaluation outcomes, and research findings.

### 5.2 Recommendations
* Actionable, feasible future enhancements based directly on system limitations and findings.
* Outlines potential domain applications, advanced feature expansions (e.g., AI integration, mobile apps), and institutional policy suggestions.
