# **LinPEAS‑Analyser‑Tool (LPA)**

The **LinPEAS‑Analyser‑Tool (LPA)** is a structured analysis engine that processes raw LinPEAS output and converts it into a clear, modular, vulnerability‑focused privilege‑escalation report.

LPA does **not** replace LinPEAS — it **extends** it.  
LinPEAS is one of the most widely used Linux privilege‑escalation enumeration tools, and without LinPEAS this analyser would not exist.

👉 [**LinPEAS Repository**](https://github.com/peass-ng/PEASS-ng/tree/master/linPEAS) 

---

## **What LPA Does**
LPA takes the raw, unstructured LinPEAS output and:

- extracts relevant sections using profile markers  
- processes each subsection through modular analysis engines  
- matches findings against a structured vulnerability knowledge base  
- produces a clean Markdown report  
- aligns findings with Privilege‑Escalation‑Principles  
- provides remediation guidance where applicable  

This makes LinPEAS output easier to understand, easier to navigate, and easier to act upon.

---

## **Documentation Overview**

### **📘 [lpa.md](https://github.com/Mark-a-Hamilton/LinPEAS-Analyser-Tool/blob/main/lpa/docs/lpa.md) — How LPA Works**
- Running LPA  
- Input/output  
- Internal workflow  
- Flowchart  
- Module/profile interaction  
- Report interpretation  

### **📘 [profiles.md](https://github.com/Mark-a-Hamilton/LinPEAS-Analyser-Tool/blob/main/lpa/docs/profilles.md) — Profiles & Structure**
- How `lpa-default.json` defines sections, markers, and subsections  
- How `lpa-kb.json` defines vulnerabilities  
- Naming conventions  
- Alphabetical ordering rules  

### **📘 Privilege‑Escalation‑Principles.md**
- The methodology used to interpret findings  
- How to evaluate risk  
- How to identify exploit paths  
- How to prioritise remediation  

---

## **Why LPA Exists**
LinPEAS produces a huge amount of valuable information — but it is raw, dense, and unstructured.

LPA exists to:

- reduce analysis time  
- highlight actionable findings  
- provide structured vulnerability intelligence  
- make privilege‑escalation enumeration easier to understand  
- support both learning and professional use  

---

## **Acknowledgements**
Special thanks to the creators of **LinPEAS** and **PEASS‑NG**.  
Their work is foundational to Linux privilege‑escalation research and tooling.

---
