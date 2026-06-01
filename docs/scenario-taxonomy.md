# Manufacturing Scenario Taxonomy

This project uses a simple taxonomy to organize manufacturing knowledge.

## Core domains

| Domain | Typical questions | Example data |
| --- | --- | --- |
| ERP | sales order, purchasing, finance, cost | order number, customer, price, delivery date |
| MES | work order, reporting, shop-floor execution | work order, process, machine, operator |
| WMS | inventory, warehouse, batch, barcode | warehouse, location, lot, quantity |
| APS | planning and scheduling | capacity, due date, priority |
| BOM / MRP | material structure and requirement planning | BOM version, material code, substitute material |
| QC | quality inspection and nonconformance | defect code, inspection result, disposition |
| Delivery | shipment and fulfillment risk | delivery order, carrier, promised date |
| Finance | revenue, cost, margin, cash flow | invoice, cost item, margin, receivable |

## Recommended record fields

- `id`: stable unique ID
- `title`: short human-readable title
- `scenario`: business scenario
- `source_type`: SOP, implementation note, exception playbook, analysis template
- `tags`: semicolon-separated tags
- `content`: practical explanation
