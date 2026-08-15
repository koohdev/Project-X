# 4. Formatting Standards and Official Templates (DCT CCS)

## 4.1 Page Layout & Typography Standards

| Parameter | Mandatory Specification |
| :--- | :--- |
| **Paper Size** | Standard Letter ($8.5 \times 11\text{ inches}$) |
| **Paper Substance** | Substance 20 |
| **Orientation** | Portrait (Landscape permitted strictly for wide diagrams/tables) |
| **Line Spacing** | Strictly **1.5 lines** throughout manuscript |
| **Paragraph Indentation** | **1.0 inch** first-line indent |
| **Top Margin** | 1.0 inch |
| **Left Margin** | **1.5 inches** (binding margin) |
| **Bottom Margin** | 1.0 inch |
| **Right Margin** | 1.0 inch |
| **Gutter** | 0 inch |
| **Header / Footer** | 0.5 inch |
| **Font Family** | Strictly **Times New Roman** (Color: Black / Automatic) |
| **Heading 1 Font** | 12 pt, Bold, Title Case |
| **Heading 2 Font** | 12 pt, Bold, Title Case |
| **Heading 3 & Body Text** | 11 pt, Regular |
| **Pagination Position** | Bottom-Right (clean numeral, no dashes or extra characters) |
| **Pagination Rules** | **Roman numerals** for Preliminary Pages (e.g., `i`, `ii`, `iii`). **Decimal numbers** starting at `1` for Chapter 1. **No page number displayed on the first page of any chapter.** |
| **Page Breaks** | Used strictly when starting a new chapter or major section. |

---

## 4.2 Citation and Bibliography Coding Format

DCT CCS uses an author-year coding format within square brackets. Traditional footnotes are **strictly prohibited**.

### Citation Key Syntax
* First four uppercase characters of lead author's surname + 4-digit publication year:
  * Example: Author *Faron Miller* (1991) $\rightarrow$ `[MILL1991]`
  * If same author has multiple publications in the same year, append lowercase letter: `[MILL1991a]`, `[MILL1991b]`.

### Reference Entry Formats

```text
Books:
[CODE] <Author Name> (<Year>). <Book Title>, <Location of Publication>: <Complete Name of Publisher>.
Example:
[CHIC1986] J. M. Chiclov (1986). An Introduction to Distributed and Parallel Computing, Hemel Hempstead: Prentice-Hall International (UK), Ltd.

Journals:
[CODE] <Author Name> (<Year>). '<Article Title>', <Journal Title>, <Volume>(<Issue>), pp. <Page Range>.
Example:
[BAET1988] J. C. M. Baeten & J. A. Bergstra (1988). 'Global Renaming Operators in Concrete Process Algebra', Information and Computation, 78(3), pp. 205–245.

Conference Proceedings:
[CODE] <Author Name> (<Year>). '<Paper Title>', In: <Conference Name> (<Editors>, ed.), pp. <Page Range>. <Location>: <Publisher>.
Example:
[PARK1981] D. H. E. Park (1981). 'Concurrency and Automata on Infinite Sequences', In: Fifth GI Conference (P. Deussen, ed.), pp. 167–183. Berlin: Springer-Verlag.

World Wide Web / Online Resources:
[CODE] <Author / Organization> (<Year>). '<Page/Article Title>', Available at: <URL> [Accessed Date].
Example:
[CRUZ1996] J. Cruz (1996). 'The Home Page of Juan De La Cruz', Available at: <http://dlsu.edu.ph/aguinaldo>.
```

---

## 4.3 Captions for Tables and Figures

* **Table Caption Format**: Placed **above** the table.
  * `Table <Chapter#>-<Table#> <Table Caption>` (e.g., `Table 1-2 Percentage Ratio of Sophomores vs. Seniors`)
* **Figure Caption Format**: Placed **below** the figure.
  * `Figure <Chapter#>-<Figure#> <Figure Caption>` (e.g., `Figure 4-1 Data Flow Diagram`)

---

## 4.4 Preliminary Page Templates

### Abstract Guidelines
* **Length**: Strictly **150 to 200 words** in short, direct, and complete sentences.
* **Content**: Context, problem, general & specific objectives, methodology, main results, and conclusions.
* **Prohibited**: Do NOT include citations or quotes. Do NOT begin with phrases like *"This paper/study/project..."*.

### Preliminary Page Layouts

```text
================================================================================
                                TITLE PAGE (i)
                          (Number does not appear)
================================================================================

                          DOMINICAN COLLEGE OF TARLAC
                       (In bold characters, font size 16)

                               <CAPSTONE TITLE>
                (In bold characters, underlined, font size 14)

                    A <Thesis / Thesis Proposal> Presented to
                           Dominican College of Tarlac

                              In Partial Fulfillment
                      of the Requirements for the Degree of
                  Bachelor of Science in Information Technology

                                      by:

            <Last Name, First Name, Middle Initial of Proponent 1>
            <Last Name, First Name, Middle Initial of Proponent 2>
            <Last Name, First Name, Middle Initial of Proponent 3>
            <Last Name, First Name, Middle Initial of Proponent 4>

                            <Thesis Adviser's Name>
                                 Thesis Adviser

                              <Month and Year>
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

                                <Capstone Title>
                       (In bold characters, font size 14)

                                      by:

            <Last Name, First Name, Middle Initial of Proponent 1>
            <Last Name, First Name, Middle Initial of Proponent 2>
            <Last Name, First Name, Middle Initial of Proponent 3>
            <Last Name, First Name, Middle Initial of Proponent 4>

       and submitted in partial fulfillment of the requirements of the
     Bachelor of Science in Information Technology degree has been examined
                 and is recommended for acceptance and approval.


                         <Thesis Adviser's Signature>
                            <Thesis Adviser's Name>
                                 Thesis Adviser

                                     <Date>
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

         This <Capstone Project / Capstone Project Proposal> entitled

                                <Capstone Title>
                       (In bold characters, font size 14)

         After having been recommended and approved is hereby accepted
                 by the College of Computer Studies Department
                         of Dominican College of Tarlac.


                                <Dean's Signature>
                                   <Dean's Name>
                                       Dean

                                      <Date>
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

         This <Capstone Project / Capstone Project Proposal> entitled

                                <Capstone Title>
                       (In bold characters, font size 14)

                                 developed by:

            <Last Name, First Name, Middle Initial of Proponent 1>
            <Last Name, First Name, Middle Initial of Proponent 2>
            <Last Name, First Name, Middle Initial of Proponent 3>
            <Last Name, First Name, Middle Initial of Proponent 4>

                 after having been presented is hereby approved
                      by the following members of the panel:


         <Panelist 1 Signature>                 <Panelist 2 Signature>
               Panelist                               Panelist

                          <Lead Panelist Signature>
                                Lead Panelist

                                    <Date>
```

---

## 4.5 Mandatory Appendices List (Appendices A to J)

* **Appendix A. Work Assignment**: Matrix outlining individual role participation and contributions of each team member.
* **Appendix B. Definition of Terms**: Operational definitions of technical and domain terms used in the study.
* **Appendix C. Evaluation Tool or Test Documents**: ISO/IEC 25010 evaluation questionnaires and testing log sheets.
* **Appendix D. User's Manual**: Step-by-step end-user guide complete with screen captures, workflows, and troubleshooting.
* **Appendix E. Program Listing**: Core source code listings, data structures, and major backend procedures.
* **Appendix F. Certifications**:
  * Certificate of Interview
  * Certificate to Use Company's Data / Information (Client Authorization)
  * Certificate of Acceptance (Signed client deployment acceptance)
* **Appendix G. Accomplished Forms**: Adviser consultation logs, defense application forms, plagiarism clearance certificates.
* **Appendix H. Screen Design**: Detailed UI screen specifications formatted as:
  ```text
  Screen No. <Screen#>
  Screen Name: <Name of Screen>
  Narrative Overview: <Brief description of screen functionality and components>
  Screen Layout: <Visual layout / mockup diagram>
  ```
* **Appendix I. Other Documentation**: Transcripts of interviews, raw survey data, office floor plans, and investigation photos.
* **Appendix J. Curriculum Vitae**: One-page academic/technical CV per team member.

---

## 4.6 Resource Persons Format

```text
<Full Name and Title>: Maria Jose, MIT
<Profession>: Faculty Member / Systems Consultant
<Department>: College of Computer Studies
<Name of Institution>: Dominican College of Tarlac
<Email / Tel. No.>: mariajose@dct.edu.ph / (045) 322-967
```
