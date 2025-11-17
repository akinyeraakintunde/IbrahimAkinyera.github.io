# NxtAbroad AI – Architecture Overview

This document describes the architecture and design of the **NxtAbroad AI Core** engine used for student eligibility analysis and lead scoring.

---

## 1. Objectives

NxtAbroad AI Core is designed to:

1. Provide **consistent, auditable decisions** on student eligibility and risk.
2. Score leads from 0–100 so advisors can focus on **high-potential** applicants.
3. Encode business logic in code (not spreadsheets or “in someone’s head”).
4. Be easily extended to new **countries, programmes and rules**.

---

## 2. High-Level Architecture

```text
                     +-------------------------+
                     |   Data Sources          |
                     |  - Web forms            |
                     |  - CRM                  |
                     |  - CSV uploads          |
                     +------------+------------+
                                  |
                                  v
                         [ Data Pipeline ]
                                  |
                                  v
                     +-------------------------+
                     |    Rules Engine         |
                     |  - Eligibility rules    |
                     |  - Risk classification  |
                     +------------+------------+
                                  |
                                  v
                     +-------------------------+
                     |    Lead Scoring         |
                     |  - 0–100 score          |
                     |  - Explanations         |
                     +------------+------------+
                                  |
                                  v
                         [ Downstream Systems ]
                         Dashboards • CRM • Advisors