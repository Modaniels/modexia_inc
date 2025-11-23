cle# Modexia Inc. - ISP Enterprise API Documentation

> **Note:** Modexia Inc. is a **fictional company** created for demonstration, training, and development purposes. All data, names, and scenarios are simulated.

## Overview

This repository contains the master operational data and API specification for **Modexia Inc.**, a fictional global Internet Service Provider (ISP) serving residential, SME, and enterprise customers across multiple continents. The API provides comprehensive access to all critical business systems including customer management, network operations, billing, support ticketing, and infrastructure monitoring.

## 🌐 About Modexia Inc.

Modexia is a modern ISP enterprise operating in major markets including:
- **North America** (New York, Boston)
- **Europe** (London, Madrid)
- **Africa** (Nairobi, Lagos, Accra)
- **Asia** (Mumbai, Singapore)

### Service Offerings
- **Residential Internet**: High-speed fiber connections (50 Mbps - 1 Gbps)
- **SME Business Solutions**: Reliable connectivity with business-grade SLAs
- **Enterprise Dedicated Lines**: Mission-critical fiber with 99.9%+ uptime guarantees
- **Dark Fiber Leasing**: Custom infrastructure for large organizations
- **Satellite Backup Links**: Redundant connectivity for critical operations

## 📁 Repository Structure

```
modexia_inc/
├── server/              # FastAPI server implementation
│   ├── main.py         # API server with all endpoints
│   ├── requirements.txt # Python dependencies
│   ├── API_SERVER.md   # Server documentation
│   └── __init__.py     # Package initialization
├── resources/           # Data files and documentation
│   ├── modexia_master_data.json  # OpenAPI 3.0.1 specification
│   ├── Modexia ai Brain - Sheet1.csv  # Business intelligence data
│   └── *.pdf           # Corporate documentation files
└── README.md           # This file
```

### 📦 Resources Folder

**`modexia_master_data.json`**  
OpenAPI 3.0.1 specification defining the complete Modexia Enterprise API with:
- **8 Core Endpoints** covering all operational domains
- **9 Data Schemas** for consistent data modeling
- **Realistic Sample Data** for testing and development
- **Query Parameters** for filtering and searching

**`Modexia ai Brain - Sheet1.csv`**  
Supplementary data export containing additional business intelligence and operational metrics.

**PDF Documentation**  
Corporate overview, data privacy policies, field operations safety, and network sales SOPs.

### 🖥️ Server Folder

Complete FastAPI implementation with all endpoints from the JSON specification. See `server/API_SERVER.md` for detailed server documentation.

## 🔌 API Endpoints

### 1. Customer Management (`/customers`)
Manage customer accounts, subscriptions, and contracts.

**Key Features:**
- Customer account information and contact details
- Subscription plan and billing cycle tracking
- Contract dates and renewal management
- Service address and installation dates
- Real-time bandwidth usage monitoring
- Support tier classification

**Use Cases:**
- View all active customers
- Filter suspended or churned accounts
- Track trial customers
- Monitor Monthly Recurring Revenue (MRR)

### 2. Human Resources (`/employees`)
Access employee records for field technicians, NOC staff, and corporate teams.

**Key Features:**
- Employee roles and department assignments
- Work shifts and rotation schedules
- Leave balance tracking
- Email and location information
- Employment status (Active, Probation, Onboarding)

**Use Cases:**
- Field technician dispatch
- NOC shift scheduling
- HR compliance reporting
- Leave management

### 3. Finance & Billing (`/invoices`)
Track invoices, payments, and financial obligations.

**Key Features:**
- Invoice status (Paid, Overdue, Pending, Failed)
- Service type breakdown
- Due date tracking
- Risk level assessment
- Account manager assignment

**Use Cases:**
- Identify overdue payments
- Track revenue by service type
- Monitor high-risk accounts
- Account receivables management

### 4. Support Operations (`/tickets`)
Manage customer support tickets and technical issues.

**Key Features:**
- Priority-based ticket management (Critical, High, Medium, Low)
- Issue categorization (Service Outage, Slow Speed, Billing Dispute, Installation)
- SLA breach tracking
- Technician assignment
- Estimated resolution times
- Affected services tracking

**Use Cases:**
- Critical outage response
- Customer complaint resolution
- Installation request tracking
- SLA compliance monitoring

### 5. Network Infrastructure (`/network-infrastructure`)
Monitor Points of Presence (POPs), core routers, and fiber routes.

**Key Features:**
- Real-time operational status
- Capacity and utilization metrics
- Equipment counts per location
- Uptime percentage tracking
- Maintenance scheduling
- Power and cooling status

**Use Cases:**
- Network capacity planning
- Proactive maintenance scheduling
- Performance monitoring
- Infrastructure health checks

### 6. Equipment Inventory (`/equipment-inventory`)
Track all network equipment from core routers to customer premises devices.

**Key Features:**
- Equipment type classification (Routers, Switches, ONTs)
- Manufacturer and model tracking
- Serial numbers and warranty dates
- Deployment status and location
- Cost tracking and asset management
- Firmware version control

**Use Cases:**
- Asset lifecycle management
- Warranty tracking
- Spare parts inventory
- Equipment deployment planning

### 7. SLA Metrics (`/sla-metrics`)
Monitor Service Level Agreement compliance and performance.

**Key Features:**
- Uptime percentage tracking (committed vs. actual)
- Latency measurements
- Packet loss monitoring
- Incident count tracking
- Mean Time To Repair (MTTR)
- SLA credits issued

**Use Cases:**
- Customer SLA reporting
- Performance optimization
- Credit calculation
- Service quality assurance

### 8. Vendor Management (`/vendor-contracts`)
Manage relationships with upstream providers and equipment vendors.

**Key Features:**
- Upstream transit providers
- Equipment maintenance contracts
- Dark fiber leases
- Submarine cable capacity
- Contract renewal tracking
- Cost management (monthly/annual)

**Use Cases:**
- Vendor relationship management
- Contract renewal planning
- Cost optimization
- Service dependency tracking

### 9. Analytics (`/bandwidth-usage`)
Analyze bandwidth consumption patterns and network utilization.

**Key Features:**
- Peak and average usage tracking
- Data transfer volumes
- Utilization percentages
- Burst incident detection
- Off-peak usage patterns

**Use Cases:**
- Capacity planning
- Customer upgrade recommendations
- Network congestion analysis
- Fair usage policy enforcement

## 📊 Data Schemas

All API responses follow standardized schemas:

| Schema | Purpose |
|--------|---------|
| `Customer` | Customer account and subscription information |
| `Employee` | HR records and employee details |
| `Invoice` | Billing and payment records |
| `Ticket` | Support tickets and technical issues |
| `NetworkNode` | Infrastructure nodes (POPs, routers, fiber routes) |
| `Equipment` | Hardware inventory and asset tracking |
| `SLAMetric` | Performance metrics and compliance data |
| `VendorContract` | Third-party vendor agreements |
| `BandwidthUsage` | Network utilization and consumption data |
| `Product` | Service catalog and pricing |

## 🚀 Getting Started

### API Servers

**Production Server:**
```
https://api.modexia.net/v1
```

**Mock Server (Development/Testing):**
```
http://localhost:3000
```

### Example API Calls

**Get all active customers:**
```bash
GET https://api.modexia.net/v1/customers?status=Active
```

**Get critical priority tickets:**
```bash
GET https://api.modexia.net/v1/tickets?priority=Critical
```

**Get overdue invoices:**
```bash
GET https://api.modexia.net/v1/invoices?status=Overdue
```

**Get network infrastructure status:**
```bash
GET https://api.modexia.net/v1/network-infrastructure
```

## 🎯 Use Cases & Applications

### AI Orchestrator Integration
This API is designed to power AI-driven operational systems that can:
- **Automated Customer Support**: AI agents can query tickets, customer info, and network status
- **Predictive Maintenance**: Analyze equipment status and SLA metrics to predict failures
- **Smart Routing**: Optimize ticket assignment based on technician location and expertise
- **Revenue Intelligence**: Identify upsell opportunities from bandwidth usage patterns
- **Proactive Outage Management**: Detect degraded network nodes before customer impact

### Business Intelligence
- Executive dashboards for MRR tracking
- Customer churn prediction
- Network capacity forecasting
- SLA compliance reporting
- Vendor cost optimization

### Operations Automation
- Automatic ticket creation from network monitoring
- Smart field technician dispatch
- Automated invoice generation
- Equipment lifecycle alerts
- Contract renewal reminders

## 📞 Contact & Support

**Technical Support:**
- Email: sysadmin@modexia.net
- System Admin: MDX-109

**Executive Leadership:**
- CEO: Alexander Thorne (alex.thorne@modexia.net)
- CTO: Amara Diallo (amara.diallo@modexia.net)

## 📝 API Version

**Current Version:** 1.0.0  
**Specification:** OpenAPI 3.0.1  
**Last Updated:** November 2025

## 🔒 Security & Authentication

This is a production API specification. Actual implementation requires:
- OAuth 2.0 or API key authentication
- Role-based access control (RBAC)
- TLS/SSL encryption
- Rate limiting and throttling
- Audit logging

## 📈 Key Metrics Overview

| Metric | Value |
|--------|-------|
| Active Customers | 4+ across all tiers |
| Employee Count | 10+ across 5 departments |
| Network POPs | 3 major locations |
| Total Bandwidth Capacity | 380+ Gbps |
| Average SLA Uptime | 99.9%+ |
| Support Tickets (Active) | Multiple priorities |
| Vendor Contracts | 4+ upstream/equipment providers |

## 🛠️ Technology Stack

- **API Standard**: REST API with OpenAPI 3.0.1
- **Data Format**: JSON
- **Authentication**: Enterprise-grade security (implementation-specific)
- **Monitoring**: Real-time metrics and alerting
- **Geographic Coverage**: Multi-continental presence

## 📚 Additional Resources

- Full API documentation available at the OpenAPI spec (`modexia_master_data.json`)
- Integration examples and SDKs available on request
- Developer sandbox environment at `http://localhost:3000`

---

**Built for the future of ISP operations** | Modexia Inc. © 2025
