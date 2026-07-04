# **LinPEAS‑Analyser (LPA) — Tool Overview & Usage Guide**

## **Introduction**
The LinPEAS‑Analyser (LPA) is a structured analysis engine designed to process raw LinPEAS output and convert it into a clean, modular, vulnerability‑focused privilege‑escalation report.

This document explains:

- how LPA works  
- how to run it  
- what input it expects  
- what output it produces  
- how modules and profiles interact  
- how to interpret the final report using *Privilege‑Escalation‑Principles.md*  

It is intended for both users and developers.

---

# **1. How to Run LPA**

### **Basic Usage**
LPA is executed by providing a LinPEAS output file:

```bash
python3 lpa.py -i linpeas-output.txt
```

### **Options**
| Flag | Description |
|------|-------------|
| `-i` | Input LinPEAS output file |
| `-o` | Output report file (optional) |
| `--profile` | Use a custom profile instead of `lpa-default.json` |
| `--kb` | Use a custom knowledge base instead of `lpa-kb.json` |
| `--debug` | Enable verbose debugging output |

### **Example**
```bash
python3 lpa.py -i linpeas.txt -o report.md
```

---

# **2. What the Input Is**

LPA expects **raw LinPEAS output**, typically generated using:

```bash
./linpeas.sh > linpeas.txt
```

The input file must contain:

- section headers  
- markers  
- raw system information  
- privilege‑escalation indicators  

LPA does **not** require any formatting — it parses the raw text using markers defined in `lpa-default.json`.

---

# **3. What the Output Is**

LPA produces a structured **Markdown report** containing:

- system overview  
- detected vulnerabilities  
- matched KB entries  
- severity ratings  
- remediation steps  
- contextual analysis  
- references  

The report is designed to be:

- readable  
- actionable  
- consistent  
- aligned with privilege‑escalation methodology  

Example output sections:

- System Overview  
- Users & Groups  
- Sudo Configuration  
- Kernel & CVEs  
- Capabilities  
- Cron Jobs  
- Writable Paths  
- Environment Variables  
- Vulnerability Summary  

---

# **4. How LPA Works Internally**

LPA operates using a modular pipeline:

---

## **4.1 Profiles (`lpa-default.json`)**

Profiles define:

- **sections**  
- **subsections**  
- **markers**  
- **analysis modules**  
- **whether a section is enabled**  

Example (actual format):

```json
{
  "id": "system_overview",
  "markers": ["OS", "Operating System", "Distro", "Hostname", "Uptime", "Hardware"],
  "analysis_type": "system_overview",
  "enabled": true,
  "subsections": [
    { "id": "os_info", "markers": ["OS", "Distro"] },
    { "id": "hostname_info", "markers": ["Hostname"] },
    { "id": "uptime_info", "markers": ["Uptime"] },
    { "id": "users_list", "markers": ["Users"] },
    { "id": "groups_list", "markers": ["Groups"] }
  ]
}
```

Profiles determine **what** LPA looks for and **how** it extracts content.

---

## **4.2 Modules (`lpa/modules/*.py`)**

Each section has a corresponding module, e.g.:

- `system_overview.py`  
- `sudo_rules.py`  
- `kernel_version.py`  
- `capabilities.py`  

Modules:

- receive extracted subsection text  
- analyse it  
- detect vulnerabilities  
- match KB entries  
- return structured findings  

Modules are the **logic layer** of LPA.

---

## **4.3 Knowledge Base (`lpa-kb.json`)**

The KB defines:

- vulnerability title  
- severity  
- category  
- explanation (“why”)  
- impact  
- remediation  
- ATT&CK  
- CWE  
- references  

Example (actual format):

```json
"available_shells": {
  "title": "Available shells",
  "severity": "info",
  "category": "system",
  "why": "Shells listed in /etc/shells, indicating available user environments.",
  "impact": "",
  "recommendation": "",
  "attck": [],
  "cwe": [],
  "references": []
}
```

All KB entries must be **alphabetically ordered**.

---

# **5. LPA Processing Flowchart**

```
                ┌──────────────────────────┐
                │      LinPEAS Output      │
                └─────────────┬────────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │   Profile (lpa-default)  │
                │  - sections              │
                │  - markers               │
                │  - subsections           │
                └─────────────┬────────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │   Extraction Engine      │
                │  - locate markers        │
                │  - slice text blocks     │
                └─────────────┬────────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │   Analysis Modules       │
                │  - parse subsection      │
                │  - detect issues         │
                └─────────────┬────────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │ Knowledge Base (lpa-kb)  │
                │  - severity              │
                │  - remediation           │
                │  - ATT&CK/CWE            │
                └─────────────┬────────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │     Report Builder       │
                │  - markdown output       │
                │  - structured sections   │
                └─────────────┬────────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │     Final Report.md      │
                └──────────────────────────┘
```

---

# **6. Analysing the Report Using Privilege‑Escalation‑Principles.md**

The final report should be interpreted using your **Privilege‑Escalation‑Principles.md**, which provides:

- the methodology  
- the decision‑making framework  
- the exploitation logic  
- the remediation logic  
- the risk‑ranking approach  

Each finding in the report maps to one or more principles, such as:

- **Weak File Permissions**  
- **Misconfigured Sudo Rules**  
- **Kernel CVEs**  
- **Writable Cron Jobs**  
- **Environment Variable Abuse**  
- **Capabilities Misconfiguration**  
- **Service Misconfiguration**  

This ensures the report is not just informational — it is **actionable**.

---

# **7. Summary**

LPA provides:

- structured extraction  
- modular analysis  
- KB‑driven vulnerability intelligence  
- clean Markdown reporting  
- alignment with privilege‑escalation methodology  

This document explains how to run LPA, how it works internally, and how to interpret its output effectively.

---
