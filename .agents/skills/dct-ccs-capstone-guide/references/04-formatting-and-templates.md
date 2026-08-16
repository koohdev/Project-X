# 4. Formatting Standards and Official Templates (DCT CCS)

## 4.1 Page Layout & Typography Standards

| Parameter | Mandatory Specification |
| :--- | :--- |
| **Paper Size** | Standard Letter ($8.5 \times 11\text{ inches}$) |
| **Paper Substance** | Substance 20 |
| **Orientation** | Portrait (Landscape permitted strictly for wide diagrams/tables) |
| **Line Spacing** | Strictly **1.5 lines** |
| **Paragraph Indentation** | Strictly **1.0 inch** first-line indent |
| **Top Margin** | 1.0 inch |
| **Left Margin** | **1.5 inches** (binding margin) |
| **Bottom Margin** | 1.0 inch |
| **Right Margin** | 1.0 inch |
| **Gutter** | 0 inch |
| **Header / Footer** | 0.5 inch |
| **Font Family** | Strictly **Times New Roman** |
| **Font Color** | Black (automatic) |
| **Heading 1 Font** | 12 pt, Bold |
| **Heading 2 Font** | 12 pt, Bold |
| **Heading 3 & Content** | 11 pt, Regular |
| **Pagination Position** | Bottom-Right (clean numeral, no dashes or extra characters) |
| **Pagination Rules** | **Roman numerals** for Preliminary Pages (e.g., `i`, `ii`, `iii`). **Decimal numbers** starting at `1` for Chapter 1. **No page number displayed on the first page of any chapter.** |
| **Page Breaks** | Used strictly when starting a new chapter. |

---

## 4.2 Citation and Bibliography Coding Format

DCT CCS uses an author-year coding format within square brackets. Traditional footnoting is **strictly prohibited**.

### Citation Key Syntax
* First four uppercase characters of the lead author's surname + 4-digit publication year:
  * Example: Author *Faron Miller* (1991) $\rightarrow$ `[MILL1991]`
  * If the same author has multiple publications in the same year, append lowercase letters: `[MILL1991a]`, `[MILL1991b]`.

### Bibliography Entry Formats

```text
Books:
[CODE] <Author's Name> (<Year of Publication>). <Book Title>, <Site of Publication>: <Complete Name of Publisher>.
Example:
[CHIC1986] J M Chiclov (1986). An Introduction to Distributed and Parallel Computing. Hemel Hempstead: Prentice-Hall International (UK), Ltd.

Journals:
[CODE] <Author's Name> (<Year of Publication>). '<Article Title>', Journal Title, volume number (issue number), <Pages where article could be found>.
Example:
[BAET1988] J C M Baeten & J A Bergstra (1988). 'Global Renaming Operators in Concrete Process Algebra', Information and Computation, 78(3), pp 205–245.

Conference Proceedings:
[CODE] <Author's Name> (<Year of Publication>). '<Article Title>', In: Conference Name (editors of the proceedings, ed), <Pages where article could be found>. <Site of Publication>: <Complete Name of Publisher>.
Example:
[PARK1981] D H E Park (1981). 'Concurrency and Automata on Infinite Sequences', In: Fifth GI Conference (P Deussen, ed), pp 167–183. Berlin: Springer-Verlag.

World Wide Web:
[CODE] <Author of the page> (<Year>). '<Homepage Title>', URL site.
Example:
[CRUZ1996] J Cruz (1996). 'The Home Page of Juan De La Cruz'. http://dlsu.edu.ph/aguinaldo.
```

---

## 4.3 Captions for Tables and Figures

* **Table Caption Format**: Placed **above** the table.
  * In text: `<Table No.>: <Table Title>` or `Table <Chapter#>-<Table#> <Table Caption>`
  * In List of Tables (14pt Bold): `Table <chapter#>-<table#>   <Table Caption>   <page>`
  * Example: `Table 1-2 Percentage Ratio of Sophomore vs. Seniors`
* **Figure Caption Format**: Placed **below** the figure.
  * In text: `<Figure No.>: <Figure Title>` or `Figure <Chapter#>-<Figure#> <Figure Caption>`
  * In List of Figures (14pt Bold): `Figure <chapter#>-<figure#>   <Figure Caption>   <page>`
  * Example: `Figure 4-1 Data Flow Diagram`

---

## 4.4 Preliminary Page Layouts & Official Templates

### Abstract Guidelines
* **Length**: Strictly **150 to 200 words** of short, direct, and complete sentences.
* **Content**: Rationale and objectives of the project; serves as a substitute for reading the paper.
* **Prohibitions**: Do NOT put citations or quotes. Avoid beginning with *"This paper/document/project/study..."*.

### Preliminary Page Layouts

```text
================================================================================
                                TITLE PAGE (i)
                          (Number does not appear)
================================================================================

                          DOMINICAN COLLEGE OF TARLAC
                       (In bold characters, font size 16)

                                <THESIS TITLE>
                (In bold characters, underlined, font size 14)

                  A <Thesis / Thesis Proposal> Presented to
                         Dominican College of Tarlac

                            In Partial Fulfillment
                    of the Requirements for the Degree of
                Bachelor of Science in Information Technology

                                     by:

          <last name, first name, middle initial of proponent 1>
          <last name, first name, middle initial of proponent 2>
          <last name, first name, middle initial of proponent 3>
          <last name, first name, middle initial of proponent 4>

                            <Thesis Adviser's Name>
                                 Thesis Adviser

                              <date of submission>
                               (month and year)
```

```text
================================================================================
                     ADVISER'S RECOMMENDATION SHEET (ii)
                          (Number does not appear)
================================================================================

                          DOMINICAN COLLEGE OF TARLAC
                       (In bold characters, font size 16)

                        ADVISER'S RECOMMENDATION SHEET
                (In bold characters, underlined, font size 14)

         This <Capstone Project / Capstone Project Proposal> entitled

                                 <Thesis Title>
                       (in bold characters, font size 14)

                                     by:

          <last name, first name, middle initial of proponent 1>
          <last name, first name, middle initial of proponent 2>
          <last name, first name, middle initial of proponent 3>
          <last name, first name, middle initial of proponent 4>

       And submitted in partial fulfillment of the requirements of the
    Bachelor of Science in Information Technology degree has been examined
                 and is recommended for acceptance and approval

                          <Thesis Adviser's Signature>
                            <Thesis Adviser's Name>
                                 Thesis Adviser

                              <Date of submission>
                                     Date
```

```text
================================================================================
                         DEAN'S ACCEPTANCE SHEET (iii)
                          (Number does not appear)
================================================================================

                          DOMINICAN COLLEGE OF TARLAC
                       (In bold characters, font size 16)

                            DEAN'S ACCEPTANCE SHEET
                (In bold characters, underlined, font size 14)

                   This <Thesis / Thesis Proposal> entitled

                                 <Thesis Title>
                       (in bold characters, font size 14)

         After having been recommended and approved is hereby accepted
                 by the College of Computer Studies Department
                         of Dominican College of Tarlac

                               <Dean's Signature>
                                  <Dean's Name>
                                      Dean

                              <Date of submission>
                                     Date
```

```text
================================================================================
                        PANEL'S APPROVAL SHEET (iv)
                          (Number does not appear)
================================================================================

                          DOMINICAN COLLEGE OF TARLAC
                       (In bold characters, font size 16)

                             PANEL'S APPROVAL SHEET
                (In bold characters, underlined, font size 14)

                   This <Thesis / Thesis Proposal> entitled

                                 <Thesis Title>
                       (in bold characters, font size 14)

                                 developed by:

          <last name, first name, middle initial of proponent 1>
          <last name, first name, middle initial of proponent 2>
          <last name, first name, middle initial of proponent 3>
          <last name, first name, middle initial of proponent 4>

                 after having been presented is hereby approved
                      by the following members of the panel:

         <Panelist 1's Signature>             <Panelist 2's Signature>
                Panelist                             Panelist

                          <Lead Panelist's Signature>
                                 Lead Panelist

                                    <date>
```

---

## 4.5 Mandatory Appendices List (Appendices A to J)

* **Appendix A. Work Assignment**: Identifies the project involvement / participation of each group member.
* **Appendix B. Definition of Terms**: Operational definitions of technical, domain, and research terms.
* **Appendix C. Evaluation Tool or Test Documents**: Evaluation instruments, questionnaires, and testing sheets.
* **Appendix D. User's Manual**: User's guide in using the system with sample screens, descriptions, instructions for specific tasks, and illustrations of system usage.
* **Appendix E. Program Listing**: Printed copy of all programs, modules, functions, and procedures of the developed system.
* **Appendix F. Certifications**:
  - Certificate of Interview
  - Certificate to Use Company's Data / Information
  - Certificate of Acceptance
* **Appendix G. Accomplished Forms**: Adviser consultation logs, defense application forms, plagiarism clearance certificates.
* **Appendix H. Screen Design**: Screen layout specifications using the format:
  ```text
  Screen No. <screen#>
  Screen Name: <name of the screen>
  Narrative Overview: <brief description about the different components of the screen describing its functionality>
  Screen Layout: <include the screen layout / design>
  ```
* **Appendix I. Other Documentation**:
  - Transcript of Interview (documentation of questions and answers during data gathering)
  - Survey Forms / Questionnaires
  - Pictures showcasing data gathering and investigation done (e.g., floor plans, building layouts, photos)
* **Appendix J. Curriculum Vitae**: One-page CV per team member.

---

## 4.6 Resource Persons Format

```text
<Full name and Title>: Maria Jose, MIT
<Profession>: Faculty
<Department>: College of Computer Studies
<Name of Institution>: Dominican College of Tarlac
<e-mail address / tel. no>: mariajose@yahoo.com / 045-322967
```
