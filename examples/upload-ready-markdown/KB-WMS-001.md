---
id: "KB-WMS-001"
scenario: "WMS/MES exception"
source_type: "Exception playbook"
tags: ["WMS", "MES", "inventory", "material consumption"]
---

# Inventory inconsistency between WMS and MES

If WMS inventory differs from MES material consumption, the assistant should ask for material code, warehouse, batch number, work order, and transaction time. Typical causes include delayed posting, manual adjustment, barcode scanning error, or cross-warehouse transfer not synchronized.
