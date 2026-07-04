# **LinPEAS‑Analyser‑Tool Profiles Specification**

## **Overview**
Profiles define how the LinPEAS‑Analyser‑Tool interprets raw LinPEAS output and transforms it into a structured, multi‑section privilege‑escalation report.  
They act as the **mapping layer** between:

- raw LinPEAS text  
- report sections  
- subsections  
- analysis modules  
- vulnerability knowledge base (KB) entries  

Two distinct JSON files make up the profile system:

- **`lpa-default.json`** — defines the *report structure*  
- **`lpa-kb.json`** — defines *vulnerabilities, extended descriptions, and remediation steps*

These files work together to ensure consistent, predictable, and extensible analysis.

---

## **1. `lpa-default.json` — Report Structure Definition**

### **Purpose**
`lpa-default.json` defines the **sections**, **subsections**, and **markers** used to extract relevant content from LinPEAS output.  
It also specifies which **analysis module** should process each subsection.

This file determines the *shape* of the final report.

### **Structure**
```json
{
  "sections": [
    {
      "name": "Kernel",
      "marker": "Kernel",
      "subsections": [
        {
          "name": "Kernel Version",
          "marker": "Kernel version",
          "analysis_type": "lpa_kernel_version"
        }
      ]
    }
  ]
}
```

### **Key Fields**
- **`name`**  
  Human‑readable section title.

- **`marker`**  
  A unique string used to locate the start of the section in LinPEAS output.

- **`subsections`**  
  Fine‑grained analysis units within the section.

- **`analysis_type`**  
  The name of the module used to process this subsection.  
  **Must match the Python module filename**, e.g.:

  ```
  lpa_kernel_version.py
  lpa_sudo_rules.py
  lpa_env_vars.py
  ```

### **Naming Convention**
All LPA modules must follow:

```
lpa_<section>_<subsection>.py
```

This ensures predictable module resolution and prevents ambiguity.

### **Design Principles**
- Sections should represent **major privilege‑escalation categories**.  
- Subsections should be **specific and actionable**.  
- Markers must be **unique**, **stable**, and **present in LinPEAS output**.  
- Analysis types must **exactly match** module filenames.

---

## **2. `lpa-kb.json` — Vulnerability Knowledge Base**

### **Purpose**
`lpa-kb.json` defines all known vulnerabilities detected by LinPEAS‑Analyser‑Tool.  
Each entry provides:

- vulnerability identifier  
- extended description  
- affected versions  
- severity  
- remediation steps  

This file is the **intelligence layer** of the tool.

### **Structure**
```json
{
  "CVE-2021-3156": {
    "description": "Heap-based buffer overflow in sudo leading to privilege escalation.",
    "affected_versions": "<= 1.8.31",
    "severity": "High",
    "remediation": "Update sudo to the latest patched version.",
    "notes": "Also known as Baron Samedit."
  }
}
```

### **Key Fields**
- **`description`**  
  Clear, extended explanation of the vulnerability.

- **`affected_versions`**  
  Version ranges or conditions that trigger detection.

- **`severity`**  
  One of: `Low`, `Medium`, `High`, `Critical`.

- **`remediation`**  
  Practical steps to eliminate or mitigate the vulnerability.

- **`notes`**  
  Optional contextual information.

### **Alphabetical Ordering Rule**
All vulnerability categories **must be sorted alphabetically** by key:

```
CVE-2019-14287
CVE-2020-8835
CVE-2021-3156
CVE-2022-0847
```

This ensures:

- predictable diffs  
- easier manual editing  
- consistent merges  
- faster scanning  
- reduced cognitive load  

### **Design Principles**
- Keep descriptions **clear and actionable**.  
- Ensure remediation steps are **practical and realistic**.  
- Avoid overly verbose entries — focus on exploitability and fixes.  
- Maintain strict alphabetical ordering.

---

## **3. How Profiles Drive the LPA Engine**

### **Processing Flow**
1. **LinPEAS raw output is ingested.**  
2. **Markers** from `lpa-default.json` locate relevant sections.  
3. **Subsection markers** extract fine‑grained content.  
4. **Analysis modules** process each subsection.  
5. **KB entries** enrich findings with vulnerability intelligence.  
6. **Final report** is assembled using the defined structure.

### **Why This Matters**
This separation ensures:

- modularity  
- maintainability  
- predictable behaviour  
- easy extension  
- safe updates  
- clear privilege‑escalation logic  

---

## **4. Adding New Sections or KB Entries**

### **Adding a Section**
1. Add a new section object to `lpa-default.json`.  
2. Define markers and subsections.  
3. Create matching module files.  
4. Test extraction against real LinPEAS output.

### **Adding a KB Entry**
1. Choose a unique key (CVE or custom identifier).  
2. Add the entry in alphabetical order.  
3. Provide extended description and remediation.  
4. Validate detection logic in the relevant module.

---

## **5. Best Practices**
- Keep markers simple and stable.  
- Avoid overly granular subsections.  
- Ensure module names match `analysis_type`.  
- Maintain alphabetical ordering in KB.  
- Document new sections and vulnerabilities immediately.  
- Test against multiple LinPEAS outputs.  

---

