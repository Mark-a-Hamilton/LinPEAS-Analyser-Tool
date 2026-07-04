
# **LinPEAS Analyser Tool Profiles Specification**  
*(Updated to reflect actual `lpa-default.json` and `lpa-kb.json` formats)*

## **Overview**
Profiles define how the LinPEAS‑Analyser‑Tool interprets raw LinPEAS output and transforms it into a structured, multi‑section privilege‑escalation report.

Profiles act as the mapping layer between:

- raw LinPEAS text  
- report sections  
- subsections  
- analysis modules  
- vulnerability knowledge base (KB) entries  

Two JSON files define the profile system:

- **`lpa-default.json`** — defines the report structure  
- **`lpa-kb.json`** — defines vulnerabilities, extended descriptions, and remediation steps  

These files work together to ensure consistent, predictable, and extensible analysis.

---

# **1. `lpa-default.json` — Report Structure Definition**

## **Purpose**
`lpa-default.json` defines:

- top‑level report **sections**  
- subsection **markers**  
- the **analysis module** used for each section  
- whether a section is **enabled**  
- how LinPEAS output is mapped into structured report components  

This file determines the *shape* of the final report.

---

## **Actual Structure**
Below is the real structure used by LPA:

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

---

## **Field Definitions**

### **`id`**
Unique identifier for the section.  
Used internally for module resolution and report assembly.

### **`markers`**
List of strings used to locate the section in LinPEAS output.

### **`analysis_type`**
Name of the Python module responsible for analysing this section.  
Must match the module filename:

```
system_overview.py
```

### **`enabled`**
Boolean flag controlling whether the section is processed.

### **`subsections`**
Array of subsection definitions.

Each subsection contains:

- **`id`** — unique identifier  
- **`markers`** — strings used to extract subsection‑specific content  

---

## **Design Principles**
- Sections represent **major privilege‑escalation categories**.  
- Subsections represent **specific analysis units**.  
- Markers must be **stable**, **unique**, and **present in LinPEAS output**.  
- `analysis_type` must match the module filename exactly.  
- Section IDs should be **lowercase**, **snake_case**, and **descriptive**.

---

# **2. `lpa-kb.json` — Vulnerability Knowledge Base**

## **Purpose**
`lpa-kb.json` defines all vulnerabilities known to the LinPEAS‑Analyser‑Tool.

Each entry provides:

- title  
- severity  
- category  
- explanation (“why”)  
- impact  
- remediation  
- ATT&CK mappings  
- CWE mappings  
- external references  

This file is the **intelligence layer** of the tool.

---

## **Actual Structure**
Below is the real format used in your KB:

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

---

## **Field Definitions**

### **`title`**
Human‑readable vulnerability name.

### **`severity`**
One of:

- `info`  
- `low`  
- `medium`  
- `high`  
- `critical`  

### **`category`**
High‑level grouping used for sorting and filtering.

### **`why`**
Explanation of *why* this finding matters.

### **`impact`**
Description of the potential security impact.

### **`recommendation`**
Actionable remediation steps.

### **`attck`**
MITRE ATT&CK technique IDs.

### **`cwe`**
CWE identifiers.

### **`references`**
External links for further reading.

---

## **Alphabetical Ordering Rule**
All vulnerability keys must be sorted alphabetically:

```
available_shells
capabilities_misconfig
cron_writable
kernel_cve_2021_3156
sudo_nopasswd
```

This ensures:

- predictable diffs  
- easy manual editing  
- consistent merges  
- reduced cognitive load  

---

# **3. How Profiles Drive the LPA Engine**

## **Processing Flow**
1. LinPEAS raw output is ingested.  
2. Section markers locate relevant blocks.  
3. Subsection markers extract fine‑grained content.  
4. Analysis modules process each subsection.  
5. KB entries enrich findings with vulnerability intelligence.  
6. Final report is assembled using the defined structure.

---

# **4. Adding New Sections or KB Entries**

## **Adding a Section**
1. Add a new section object to `lpa-default.json`.  
2. Define markers and subsections.  
3. Create a matching analysis module.  
4. Test extraction against real LinPEAS output.

## **Adding a KB Entry**
1. Choose a unique key.  
2. Insert alphabetically.  
3. Provide title, severity, category, why, impact, remediation.  
4. Add ATT&CK, CWE, and references if applicable.  
5. Validate detection logic.

---

# **5. Best Practices**
- Keep markers simple and stable.  
- Avoid overly granular subsections.  
- Ensure module names match `analysis_type`.  
- Maintain alphabetical ordering in KB.  
- Document new sections and vulnerabilities immediately.  
- Test against multiple LinPEAS outputs.

---
