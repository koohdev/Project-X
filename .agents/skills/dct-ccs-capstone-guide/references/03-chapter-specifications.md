# 3. Chapter Specifications and Content Standards (DCT CCS)

This reference defines the required structure, mandatory subsections, content expectations, and diagrams for Chapters 1.0 through 5.0 of the Capstone Manuscript.

---

## 1.0 Introduction

### 1.1 Project Context
* **Length**: Must be **at least two (2) full pages** of presentation and discussions.
* **Problem Scope**: Describe the existing and prevailing problem situation across **global, national, or regional and local** scope.
* **Researcher Justification**: Give strong justification for selecting such research problem in the capacity as a researcher (e.g., being part of the organization or systems, and the desire/concern to improve the systems).
* **Rationale Link**: State a sentence or two that explicitly shows the link and relationship of the rationale of the study to the proposed research problem.
* **Guiding Questions to Address**:
  1. *What is the function of the project?*
  2. *What is good in your project?*
  3. *What makes your project unique, innovative, and relevant?*
* **Topic & Tech Discussion**: Include discussion of relevant topics, concepts, and technologies that will be utilized in developing the software.

### 1.2 Objectives

#### 1.2.1 General Objective / Major Objective
* A **single concise paragraph** describing the general objective of the capstone project.

#### 1.2.2 Specific Objectives / Minor Objectives
* A numbered list of specific tasks the proponents expect to address to accomplish the general objective.
* Must strictly follow the **SMART** criteria:
  * **Specific**: The problem should be specifically stated.
  * **Measurable**: Easy to measure using research instruments, apparatus, or equipment.
  * **Achievable**: Solutions to research problems are achievable and feasible.
  * **Realistic**: Real results attained through scientific gathering without manipulation.
  * **Time-Bound**: Clear time frame required in every activity (shorter completion is better).
* *Rule*: Phrased with active infinitive verbs (**"To develop..."**, **"To design..."**, **"To implement..."**, **"To engineer..."**, **"To integrate..."**).

### 1.3 Scope and Limitations
* **Scope**: Extent of the prototype to be developed and the means by which the proposed system is to be evaluated on its capability of solving the problem.
* **Limitations**: Conditions beyond the control of the proponents that may place restrictions on the conclusions of the study and their application to other situations.
* *Rule*: **Every single listed limitation must be explicitly justified.**

---

## 2.0 Review of Related Literature / Systems

### 2.1 Related Theories
* Outline first, starting off with an **Anchor Theory** that provides solid background.
* Present **Supporting / Auxiliary Theories** that elaborate the anchor theory.
* Maintain narrative fluidity and continuity.
* Use DCT citation coding `[AUTH2024]` (traditional footnoting strictly prohibited).

### 2.2 Related Projects
* Overview of current system/project.
* Inventory of every related and existing project/system (**3 to 6 related studies/projects**).
* **Comparative Matrix**: Mandatory comparison of features, strengths, and limitations.
* **Screenshots**: Screen captures of existing systems to support comparative claims.

---

## 3.0 Technical Background

Comprehensive discussion of technologies involved in the project (current vs. proposed).

### 3.1 Development
* **3.1.1 Hardware**: Equipment used by developers (PCs, laptops, testing devices).
* **3.1.2 Software**:
  * **A. Frontend**: UI frameworks, engines (e.g., RPG Maker MZ, HTML5/WebGL, CSS).
  * **B. Backend**: Scripting/programming languages (JavaScript ES6, Node.js), IDEs (VS Code), specialized libraries (PeerJS).
  * **C. Multimedia and Asset Development Tools**: Image editors (GIMP), graphic design (Canva), diagramming tools (Draw.io).
  * **D. Deployment and Runtime Platform**: Executable wrappers (NW.js), browsers (Chrome, Edge), version control (Git, GitHub), web hosts (Vercel, Hostinger).
* **3.1.3 Peopleware**: Roles of proponents (PM, SA/DD, ND/UID, SE/P, QA/TW) and Capstone Adviser.
* **3.1.4 Network**: Local Area Network (LAN) and Cloud Staging configurations.

### 3.2 Implementation
* **3.2.1 Hardware**: End-user target machines (PCs, laptops, mobile devices, tablets).
* **3.2.2 Software**: Operating Systems (Windows 10 64-bit, Android 10, iOS 14) and modern Chromium-based browsers.
* **3.2.3 Peopleware**: Target user profiles (primary students, teachers, general users).
* **3.2.4 Network**: Client connectivity requirements (e.g., 5 to 10 Mbps internet connection).

---

## 4.0 Methodology, Results and Discussion

### 4.1 Methodology
* Identification and justification of formal Software Engineering SDLC methodology (e.g., Prototyping Model, Waterfall, Agile Scrum).
* SDLC Model Diagram mapped to project phases (e.g., 4.1.1 Requirements Gathering, 4.1.2 Quick Design, 4.1.3 Building Prototype, 4.1.4 Customer Evaluation, 4.1.5 Refining Prototype, 4.1.6 Engineer Product).

### 4.2 Environment (Required for organization-specific projects)
* **4.2.1 Locale**: Geographic and institutional setting.
* **4.2.2 Population of the Study**: Target user count, sampling, respondent distribution.
* **4.2.3 Organizational Chart / Profile**: Background and organizational hierarchy.

### 4.3 Requirements Specification

#### 4.3.1 Operational Feasibility
* **Fishbone Diagram (Ishikawa)**: Cause-and-effect problem analysis.
* **Functional Decomposition Diagram (FDD)**: Hierarchical decomposition of system functions.

#### 4.3.2 Technical Feasibility
* **4.3.2.1 Compatibility Checking**: Hardware and software compatibility analysis.
* **4.3.2.2 Relevance of Technologies**: Technical justification of tools against alternatives.

#### 4.3.3 Schedule Feasibility
* **Gantt Chart**: Tables illustrating activities across months/weeks with horizontal timeline bars from project inception to completion.

#### 4.3.4 Economic Feasibility
* **4.3.4.1 Cost and Benefit Analysis (CBA)**: Category, items, costs, and tangible benefits table.
* **4.3.4.2 Cost Recovery Scheme**: Investment recovery strategy, ROI, or funding sustainability plan.

#### 4.3.5 Requirements Modeling
* Input, Process, Output, Performance, Control specifications.
* Modeling Approaches (either or combined):
  * **Data and Process Modeling**: Context Diagram, Data Flow Diagram (DFD Level 1 & Child), System Flowchart, Program Flowcharts (highlights).  
    *⚠️ CRITICAL RULE: Data Flow Diagrams must NOT be used in modeling Computer-Aided Instruction (CAI) features/functions.*
  * **Object Modeling (UML)**: Use Case Diagram, Class Diagram, Sequence Diagrams, Activity Diagram.

#### 4.3.6 Risk Assessment / Analysis
* Risk identification, potential impacts, and proactive mitigation measures.

### 4.4 Design

#### 4.4.1 Output and User-Interface Design Forms
* Design tokens: Color palette (Hex codes), Typography, Icons.
* Screen design wireframes/mockups following DCT Screen Design standards.

#### 4.4.2 Data Design
* **Entity Relationship Diagram (ERD)**: Complete entity relationships and cardinalities (*Note: MS Access format preferred for presentation, but MS Access is discouraged as DBMS*).
* **Data Dictionary**: Comprehensive tables with Field Name, Data Type, Length, Constraints, and Description.

#### 4.4.3 System Architecture
* **Network Model & Network Topology**: Network structure diagrams.
* **Security**: Data protection, authentication, authorization, session controls.

### 4.5 Development
* **4.5.1 Software Specification**: Full software stack.
* **4.5.2 Hardware Specification**: Development machine specs.
* **4.5.3 Program Specification**: Core module/class definitions.
* **4.5.4 Programming Environment**: Front-End, Back-End, and Programming Considerations/Issues.
* **4.5.5 Deployment Diagram**: Node deployment architecture.
* **4.5.6 Test Plan & Test Data**: Testing strategy and baseline test sets.

### 4.6 Verification, Validation, Testing
* **4.6.1 Unit Testing**: Component-level testing.
* **4.6.2 Integration Testing**: Compatibility, Performance, Stress, Load testing.
* **4.6.3 System Testing**: System function tests, test data execution, test results and observations.
* **4.6.4 Acceptance Testing**: Evaluation against user requirements and ISO standards.

### 4.7 Implementation Plan
Describes system interaction with its operational environment across five core areas:
* **4.7.1 Physical Environment**: Where equipment functions, number of locations, physical space required, environmental restrictions (temperature, humidity, magnetic interference), power/heating/air-conditioning requirements.
* **4.7.2 Interfaces**: Inputs coming from external systems, outputs going to external systems, data formulation rules, communication media.
* **4.7.3 Functionality**: What system does, operational schedule, how/when system can be enhanced, throughput and response time constraints.
* **4.7.4 Data**: Input/output data formats, transmission frequency, accuracy and precision requirements, data volume/flow, retention periods.
* **4.7.5 Security**: Access control, user data isolation, program/OS isolation, backup frequencies.

### 4.8 Installation Processes
Discusses transition from existing systems to the new improved system:
* Identification and thorough discussion of conversion strategy: **Direct Changeover**, **Phased / Step-by-Step Changeover**, or **Parallel System Changeover**.
* Detailed activities and processes performed to complete the installation.

---

## 5.0 Conclusion and Recommendations

### 5.1 Conclusions
* Directly discusses achievements mapped to each specific objective.
* Subdivided/numbered with respect to research problems and sub-problems.

### 5.2 Recommendations
* Actionable future undertakings, other potential solutions, feature enhancements, and broader domain applications.
