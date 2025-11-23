"""
Modexia Inc. ISP Enterprise API
FastAPI server implementing all endpoints from the OpenAPI specification
"""

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(
    title="Modexia ISP Enterprise API",
    description="Core operational API for Modexia Inc. (ISP Division). Provides access to HR records, Billing Invoices, and Product Catalog for the AI Orchestrator.",
    version="1.0.0",
    contact={
        "name": "Modexia IT Support",
        "email": "sysadmin@modexia.net"
    }
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================
# DATA MODELS
# ============================================

class Customer(BaseModel):
    customer_id: str
    account_name: str
    customer_type: str
    subscription_plan: str
    monthly_recurring_revenue: float
    contract_start_date: str
    contract_end_date: str
    status: str
    billing_cycle: str
    payment_method: str
    primary_contact: str
    contact_email: str
    contact_phone: str
    service_address: str
    installation_date: str
    bandwidth_usage_percent: float
    support_tier: str

class Employee(BaseModel):
    employee_id: str
    full_name: str
    role: str
    department: str
    email: str
    status: str
    current_shift: str
    leave_balance_days: int
    location: str

class Invoice(BaseModel):
    invoice_id: str
    client_name: str
    service_type: str
    amount_usd: float
    due_date: str
    status: str
    risk_level: str
    account_manager: str

class Ticket(BaseModel):
    ticket_id: str
    customer_id: str
    customer_name: str
    issue_type: str
    priority: str
    status: str
    created_date: str
    assigned_to: str
    description: str
    estimated_resolution: str
    sla_breach: bool
    affected_services: List[str]
    location: str

class NetworkNode(BaseModel):
    node_id: str
    node_type: str
    location: str
    address: str
    status: str
    capacity_gbps: float
    current_utilization_percent: float
    equipment_count: int
    uptime_percent: float
    last_maintenance: str
    next_maintenance: str
    power_source: str
    cooling_status: str

class Equipment(BaseModel):
    equipment_id: str
    equipment_type: str
    manufacturer: str
    model: str
    serial_number: str
    purchase_date: str
    warranty_expiry: str
    status: str
    location: str
    assigned_to: str
    cost_usd: float
    firmware_version: str
    last_updated: str

class SLAMetric(BaseModel):
    customer_id: str
    customer_name: str
    service_plan: str
    reporting_period: str
    committed_uptime_percent: float
    actual_uptime_percent: float
    total_downtime_minutes: float
    sla_met: bool
    avg_latency_ms: float
    committed_latency_ms: float
    packet_loss_percent: float
    committed_packet_loss_percent: float
    incident_count: int
    mean_time_to_repair_minutes: float
    credits_issued_usd: float

class VendorContract(BaseModel):
    contract_id: str
    vendor_name: str
    vendor_type: str
    service_description: str
    contract_start_date: str
    contract_end_date: str
    monthly_cost_usd: float
    annual_cost_usd: float
    status: str
    payment_terms: str
    contact_person: str
    contact_email: str
    contact_phone: str
    renewal_notice_days: int

class BandwidthUsage(BaseModel):
    customer_id: str
    customer_name: str
    measurement_date: str
    subscribed_bandwidth_mbps: float
    peak_usage_mbps: float
    average_usage_mbps: float
    off_peak_usage_mbps: float
    total_data_transferred_gb: float
    utilization_percent: float
    burst_incidents: int
    throttling_events: int

class Product(BaseModel):
    sku: str
    product_name: str
    category: str
    bandwidth: str
    monthly_cost_usd: float
    sla_uptime: str

# ============================================
# MOCK DATA
# ============================================

CUSTOMERS = [
    {"customer_id": "CUST-10001", "account_name": "Apex Logistics HQ", "customer_type": "Enterprise", "subscription_plan": "MDX-ENT-1G", "monthly_recurring_revenue": 1200, "contract_start_date": "2023-06-15", "contract_end_date": "2026-06-14", "status": "Active", "billing_cycle": "Monthly", "payment_method": "Wire Transfer", "primary_contact": "John Smith", "contact_email": "john.smith@apexlogistics.com", "contact_phone": "+1-555-0100", "service_address": "123 Industrial Blvd, New York, NY", "installation_date": "2023-06-20", "bandwidth_usage_percent": 78, "support_tier": "Premium"},
    {"customer_id": "CUST-10045", "account_name": "TechNova Hub", "customer_type": "SME", "subscription_plan": "MDX-BIZ-100", "monthly_recurring_revenue": 150, "contract_start_date": "2024-03-10", "contract_end_date": "2025-03-09", "status": "Suspended", "billing_cycle": "Monthly", "payment_method": "Credit Card", "primary_contact": "Maria Chen", "contact_email": "maria@technovahub.io", "contact_phone": "+1-555-0245", "service_address": "456 Tech Park, San Francisco, CA", "installation_date": "2024-03-15", "bandwidth_usage_percent": 0, "support_tier": "Standard"},
    {"customer_id": "CUST-10082", "account_name": "Global Bank Corp", "customer_type": "Enterprise", "subscription_plan": "MDX-DARK", "monthly_recurring_revenue": 5000, "contract_start_date": "2022-01-10", "contract_end_date": "2027-01-09", "status": "Active", "billing_cycle": "Quarterly", "payment_method": "Wire Transfer", "primary_contact": "Robert Lee", "contact_email": "r.lee@globalbank.com", "contact_phone": "+44-20-5550-1234", "service_address": "789 Financial District, London, UK", "installation_date": "2022-01-20", "bandwidth_usage_percent": 45, "support_tier": "Platinum"},
    {"customer_id": "CUST-10091", "account_name": "HomeTech Solutions", "customer_type": "Residential", "subscription_plan": "MDX-HOME-50", "monthly_recurring_revenue": 40, "contract_start_date": "2024-11-01", "contract_end_date": "2025-10-31", "status": "Trial", "billing_cycle": "Monthly", "payment_method": "Direct Debit", "primary_contact": "Sarah Johnson", "contact_email": "sarah.j@email.com", "contact_phone": "+1-555-0789", "service_address": "12 Maple Street, Boston, MA", "installation_date": "2024-11-05", "bandwidth_usage_percent": 62, "support_tier": "Basic"}
]

EMPLOYEES = [
    {"employee_id": "MDX-101", "full_name": "Alexander Thorne", "role": "CEO", "department": "Executive", "email": "alex.thorne@modexia.net", "status": "Active", "current_shift": "Day", "leave_balance_days": 30, "location": "New York"},
    {"employee_id": "MDX-102", "full_name": "Amara Diallo", "role": "CTO", "department": "Network Operations", "email": "amara.diallo@modexia.net", "status": "Active", "current_shift": "Day", "leave_balance_days": 25, "location": "Nairobi"},
    {"employee_id": "MDX-103", "full_name": "Sarah Jenkins", "role": "Head of NOC", "department": "Network Operations", "email": "sarah.j@modexia.net", "status": "Active", "current_shift": "Night-Rotation", "leave_balance_days": 18, "location": "London"},
    {"employee_id": "MDX-104", "full_name": "David Kimani", "role": "Fiber Field Technician", "department": "Field Services", "email": "david.k@modexia.net", "status": "Probation", "current_shift": "Day", "leave_balance_days": 10, "location": "Nairobi"},
    {"employee_id": "MDX-105", "full_name": "Elena Rodriguez", "role": "VP of Enterprise Sales", "department": "Sales", "email": "elena.r@modexia.net", "status": "Active", "current_shift": "Day", "leave_balance_days": 22, "location": "Madrid"},
    {"employee_id": "MDX-106", "full_name": "Kwame Mensah", "role": "Corporate Account Manager", "department": "Sales", "email": "kwame.m@modexia.net", "status": "Active", "current_shift": "Day", "leave_balance_days": 15, "location": "Accra"},
    {"employee_id": "MDX-107", "full_name": "Jessica Wu", "role": "HR Director", "department": "Human Resources", "email": "jessica.w@modexia.net", "status": "Active", "current_shift": "Day", "leave_balance_days": 20, "location": "Singapore"},
    {"employee_id": "MDX-108", "full_name": "Samuel Abiodun", "role": "Field Safety Officer", "department": "Human Resources", "email": "sam.a@modexia.net", "status": "Onboarding", "current_shift": "Day", "leave_balance_days": 0, "location": "Lagos"},
    {"employee_id": "MDX-109", "full_name": "System Admin", "role": "Core Network Architect", "department": "IT", "email": "sysadmin@modexia.net", "status": "Active", "current_shift": "On-Call", "leave_balance_days": 99, "location": "Remote"},
    {"employee_id": "MDX-110", "full_name": "Priya Patel", "role": "Billing Manager", "department": "Finance", "email": "priya.p@modexia.net", "status": "Active", "current_shift": "Day", "leave_balance_days": 25, "location": "Mumbai"}
]

INVOICES = [
    {"invoice_id": "INV-25-001", "client_name": "Apex Logistics HQ", "service_type": "Dedicated Fiber (1Gbps)", "amount_usd": 12000, "due_date": "2025-01-31", "status": "Paid", "risk_level": "Low", "account_manager": "Elena Rodriguez"},
    {"invoice_id": "INV-25-045", "client_name": "TechNova Hub", "service_type": "SME Broadband (100Mbps)", "amount_usd": 450, "due_date": "2025-02-25", "status": "Overdue", "risk_level": "High", "account_manager": "Kwame Mensah"},
    {"invoice_id": "INV-25-050", "client_name": "Global Bank Corp", "service_type": "Dark Fiber Lease", "amount_usd": 8500, "due_date": "2025-03-20", "status": "Pending", "risk_level": "Low", "account_manager": "Elena Rodriguez"},
    {"invoice_id": "INV-25-052", "client_name": "AfriHealth NGO", "service_type": "Satellite Backup Link", "amount_usd": 1200, "due_date": "2025-03-22", "status": "Pending", "risk_level": "Medium", "account_manager": "Kwame Mensah"},
    {"invoice_id": "INV-25-060", "client_name": "Retail Kings Ltd", "service_type": "Public IP Block (/29)", "amount_usd": 50, "due_date": "2025-02-28", "status": "Failed", "risk_level": "High", "account_manager": "System Admin"},
    {"invoice_id": "INV-25-065", "client_name": "City Construct", "service_type": "Fiber Installation Fee", "amount_usd": 2500, "due_date": "2025-03-31", "status": "Pending", "risk_level": "Medium", "account_manager": "Kwame Mensah"}
]

TICKETS = [
    {"ticket_id": "TKT-2025-001", "customer_id": "CUST-10001", "customer_name": "Apex Logistics HQ", "issue_type": "Service Outage", "priority": "Critical", "status": "In Progress", "created_date": "2025-11-20T08:30:00Z", "assigned_to": "David Kimani", "description": "Complete fiber cut on main connection - no connectivity", "estimated_resolution": "2025-11-23T18:00:00Z", "sla_breach": False, "affected_services": ["Primary Internet", "VoIP"], "location": "123 Industrial Blvd, New York, NY"},
    {"ticket_id": "TKT-2025-002", "customer_id": "CUST-10045", "customer_name": "TechNova Hub", "issue_type": "Billing Dispute", "priority": "Medium", "status": "Open", "created_date": "2025-11-22T14:15:00Z", "assigned_to": "Priya Patel", "description": "Customer disputes overdue charges - claims payment was made", "estimated_resolution": "2025-11-25T17:00:00Z", "sla_breach": False, "affected_services": ["Account Status"], "location": "N/A"},
    {"ticket_id": "TKT-2025-003", "customer_id": "CUST-10091", "customer_name": "HomeTech Solutions", "issue_type": "Slow Speed", "priority": "Low", "status": "Resolved", "created_date": "2025-11-18T10:00:00Z", "assigned_to": "Sarah Jenkins", "description": "Customer reports speeds below 50Mbps - testing showed WiFi router issue", "estimated_resolution": "2025-11-19T12:00:00Z", "sla_breach": False, "affected_services": ["Internet Speed"], "location": "12 Maple Street, Boston, MA"},
    {"ticket_id": "TKT-2025-004", "customer_id": "CUST-10082", "customer_name": "Global Bank Corp", "issue_type": "Installation Request", "priority": "High", "status": "In Progress", "created_date": "2025-11-15T09:00:00Z", "assigned_to": "David Kimani", "description": "New branch office fiber installation - 1Gbps dedicated line", "estimated_resolution": "2025-11-30T17:00:00Z", "sla_breach": False, "affected_services": ["New Service"], "location": "42 Branch Ave, London, UK"}
]

NETWORK_INFRASTRUCTURE = [
    {"node_id": "POP-NY-01", "node_type": "Point of Presence", "location": "New York Data Center", "address": "100 Tech Way, New York, NY", "status": "Operational", "capacity_gbps": 100, "current_utilization_percent": 67, "equipment_count": 12, "uptime_percent": 99.95, "last_maintenance": "2025-10-15", "next_maintenance": "2026-01-15", "power_source": "Dual Feed + Generator", "cooling_status": "Normal"},
    {"node_id": "POP-LON-01", "node_type": "Point of Presence", "location": "London Data Center", "address": "50 Fiber Street, London, UK", "status": "Operational", "capacity_gbps": 80, "current_utilization_percent": 54, "equipment_count": 10, "uptime_percent": 99.98, "last_maintenance": "2025-09-20", "next_maintenance": "2025-12-20", "power_source": "Dual Feed + UPS", "cooling_status": "Normal"},
    {"node_id": "CORE-NAI-01", "node_type": "Core Router", "location": "Nairobi Hub", "address": "25 Network Plaza, Nairobi, Kenya", "status": "Operational", "capacity_gbps": 200, "current_utilization_percent": 72, "equipment_count": 8, "uptime_percent": 99.92, "last_maintenance": "2025-11-01", "next_maintenance": "2026-02-01", "power_source": "Triple Feed + Battery", "cooling_status": "Normal"},
    {"node_id": "FIBER-RT-105", "node_type": "Fiber Route", "location": "NY-BOS Backbone", "address": "Route 1 Corridor", "status": "Degraded", "capacity_gbps": 40, "current_utilization_percent": 88, "equipment_count": 4, "uptime_percent": 98.50, "last_maintenance": "2025-08-10", "next_maintenance": "2025-12-01", "power_source": "N/A", "cooling_status": "N/A"}
]

EQUIPMENT = [
    {"equipment_id": "EQ-RTR-001", "equipment_type": "Core Router", "manufacturer": "Cisco", "model": "ASR 9000", "serial_number": "FCW2145G0XY", "purchase_date": "2022-03-15", "warranty_expiry": "2027-03-14", "status": "Deployed", "location": "POP-NY-01", "assigned_to": "Network Operations", "cost_usd": 45000, "firmware_version": "7.5.2", "last_updated": "2025-10-01"},
    {"equipment_id": "EQ-SW-045", "equipment_type": "Distribution Switch", "manufacturer": "Juniper", "model": "EX4300-48T", "serial_number": "JN1234567890", "purchase_date": "2023-06-10", "warranty_expiry": "2026-06-09", "status": "Deployed", "location": "POP-LON-01", "assigned_to": "Network Operations", "cost_usd": 8500, "firmware_version": "18.4R2", "last_updated": "2025-09-15"},
    {"equipment_id": "EQ-ONT-1024", "equipment_type": "ONT (Customer Premises)", "manufacturer": "Nokia", "model": "G-010G-Q", "serial_number": "NOK987654321", "purchase_date": "2024-03-01", "warranty_expiry": "2026-03-01", "status": "Deployed", "location": "CUST-10045 Site", "assigned_to": "TechNova Hub", "cost_usd": 85, "firmware_version": "3.1.0", "last_updated": "2024-03-15"},
    {"equipment_id": "EQ-RTR-089", "equipment_type": "Edge Router", "manufacturer": "MikroTik", "model": "CCR1072-1G-8S+", "serial_number": "MTK445566778", "purchase_date": "2024-01-20", "warranty_expiry": "2025-01-19", "status": "Spare", "location": "Warehouse - Nairobi", "assigned_to": "Inventory", "cost_usd": 1200, "firmware_version": "7.11", "last_updated": "2024-01-25"}
]

SLA_METRICS = [
    {"customer_id": "CUST-10001", "customer_name": "Apex Logistics HQ", "service_plan": "MDX-ENT-1G", "reporting_period": "2025-10", "committed_uptime_percent": 99.9, "actual_uptime_percent": 99.94, "total_downtime_minutes": 26, "sla_met": True, "avg_latency_ms": 12, "committed_latency_ms": 20, "packet_loss_percent": 0.01, "committed_packet_loss_percent": 0.1, "incident_count": 1, "mean_time_to_repair_minutes": 45, "credits_issued_usd": 0},
    {"customer_id": "CUST-10045", "customer_name": "TechNova Hub", "service_plan": "MDX-BIZ-100", "reporting_period": "2025-10", "committed_uptime_percent": 98.0, "actual_uptime_percent": 96.5, "total_downtime_minutes": 1512, "sla_met": False, "avg_latency_ms": 28, "committed_latency_ms": 30, "packet_loss_percent": 0.15, "committed_packet_loss_percent": 0.5, "incident_count": 3, "mean_time_to_repair_minutes": 320, "credits_issued_usd": 75},
    {"customer_id": "CUST-10082", "customer_name": "Global Bank Corp", "service_plan": "MDX-DARK", "reporting_period": "2025-10", "committed_uptime_percent": 99.99, "actual_uptime_percent": 99.99, "total_downtime_minutes": 4, "sla_met": True, "avg_latency_ms": 5, "committed_latency_ms": 10, "packet_loss_percent": 0.001, "committed_packet_loss_percent": 0.01, "incident_count": 0, "mean_time_to_repair_minutes": 0, "credits_issued_usd": 0}
]

VENDOR_CONTRACTS = [
    {"contract_id": "VND-001", "vendor_name": "Level 3 Communications", "vendor_type": "Upstream Transit Provider", "service_description": "10Gbps IP Transit - New York", "contract_start_date": "2024-01-01", "contract_end_date": "2026-12-31", "monthly_cost_usd": 8000, "annual_cost_usd": 96000, "status": "Active", "payment_terms": "Net 30", "contact_person": "Tom Harrison", "contact_email": "tom.h@level3.com", "contact_phone": "+1-800-555-0199", "renewal_notice_days": 90},
    {"contract_id": "VND-002", "vendor_name": "Cisco Systems", "vendor_type": "Equipment Vendor", "service_description": "SmartNet Total Care - ASR 9000 Series", "contract_start_date": "2023-03-15", "contract_end_date": "2026-03-14", "monthly_cost_usd": 1200, "annual_cost_usd": 14400, "status": "Active", "payment_terms": "Net 45", "contact_person": "Lisa Wong", "contact_email": "l.wong@cisco.com", "contact_phone": "+1-888-555-0234", "renewal_notice_days": 60},
    {"contract_id": "VND-003", "vendor_name": "SEACOM", "vendor_type": "Submarine Cable Capacity", "service_description": "1Gbps Protected Capacity - African Segment", "contract_start_date": "2023-06-01", "contract_end_date": "2028-05-31", "monthly_cost_usd": 15000, "annual_cost_usd": 180000, "status": "Active", "payment_terms": "Net 30", "contact_person": "Ahmed Osman", "contact_email": "a.osman@seacom.com", "contact_phone": "+254-20-555-0567", "renewal_notice_days": 180},
    {"contract_id": "VND-004", "vendor_name": "Crown Castle Fiber", "vendor_type": "Dark Fiber Lease", "service_description": "Dark Fiber Route - NY to Boston (285km)", "contract_start_date": "2022-08-01", "contract_end_date": "2027-07-31", "monthly_cost_usd": 12000, "annual_cost_usd": 144000, "status": "Active", "payment_terms": "Quarterly", "contact_person": "Mark Stevens", "contact_email": "m.stevens@crowncastle.com", "contact_phone": "+1-877-555-0888", "renewal_notice_days": 120}
]

BANDWIDTH_USAGE = [
    {"customer_id": "CUST-10001", "customer_name": "Apex Logistics HQ", "measurement_date": "2025-11-22", "subscribed_bandwidth_mbps": 1000, "peak_usage_mbps": 780, "average_usage_mbps": 542, "off_peak_usage_mbps": 320, "total_data_transferred_gb": 1248, "utilization_percent": 78, "burst_incidents": 2, "throttling_events": 0},
    {"customer_id": "CUST-10082", "customer_name": "Global Bank Corp", "measurement_date": "2025-11-22", "subscribed_bandwidth_mbps": 1000, "peak_usage_mbps": 450, "average_usage_mbps": 315, "off_peak_usage_mbps": 180, "total_data_transferred_gb": 725, "utilization_percent": 45, "burst_incidents": 0, "throttling_events": 0},
    {"customer_id": "CUST-10091", "customer_name": "HomeTech Solutions", "measurement_date": "2025-11-22", "subscribed_bandwidth_mbps": 50, "peak_usage_mbps": 48, "average_usage_mbps": 31, "off_peak_usage_mbps": 12, "total_data_transferred_gb": 71, "utilization_percent": 96, "burst_incidents": 5, "throttling_events": 0}
]

PRODUCTS = [
    {"sku": "MDX-HOME-50", "product_name": "Modexia Home Fiber", "category": "Residential", "bandwidth": "50 Mbps", "monthly_cost_usd": 40, "sla_uptime": "95%"},
    {"sku": "MDX-BIZ-100", "product_name": "SME Business Connect", "category": "Business", "bandwidth": "100 Mbps", "monthly_cost_usd": 150, "sla_uptime": "98%"},
    {"sku": "MDX-ENT-1G", "product_name": "Enterprise Dedicated", "category": "Enterprise", "bandwidth": "1 Gbps", "monthly_cost_usd": 1200, "sla_uptime": "99.9%"},
    {"sku": "MDX-DARK", "product_name": "Dark Fiber Mile", "category": "Enterprise", "bandwidth": "Custom", "monthly_cost_usd": 5000, "sla_uptime": "99.99%"}
]

# ============================================
# API ENDPOINTS
# ============================================

@app.get("/")
async def root():
    """Welcome endpoint"""
    return {
        "message": "Welcome to Modexia ISP Enterprise API",
        "version": "1.0.0",
        "documentation": "/docs",
        "note": "Modexia Inc. is a fictional company for demonstration purposes"
    }

@app.get("/customers", response_model=List[Customer], tags=["Customer Management"])
async def get_customers(status: Optional[str] = Query(None, enum=["Active", "Suspended", "Churned", "Trial"])):
    """List all customers with optional status filter"""
    if status:
        return [c for c in CUSTOMERS if c["status"] == status]
    return CUSTOMERS

@app.get("/employees", response_model=List[Employee], tags=["HR"])
async def get_employees():
    """List all employees"""
    return EMPLOYEES

@app.get("/invoices", response_model=List[Invoice], tags=["Finance"])
async def get_invoices(status: Optional[str] = Query(None, enum=["Paid", "Overdue", "Pending", "Failed"])):
    """List all invoices with optional status filter"""
    if status:
        return [i for i in INVOICES if i["status"] == status]
    return INVOICES

@app.get("/tickets", response_model=List[Ticket], tags=["Support"])
async def get_tickets(
    priority: Optional[str] = Query(None, enum=["Critical", "High", "Medium", "Low"]),
    status: Optional[str] = Query(None, enum=["Open", "In Progress", "Resolved", "Closed"])
):
    """List support tickets with optional priority and status filters"""
    result = TICKETS
    if priority:
        result = [t for t in result if t["priority"] == priority]
    if status:
        result = [t for t in result if t["status"] == status]
    return result

@app.get("/network-infrastructure", response_model=List[NetworkNode], tags=["Network Operations"])
async def get_network_infrastructure():
    """List network infrastructure nodes"""
    return NETWORK_INFRASTRUCTURE

@app.get("/equipment-inventory", response_model=List[Equipment], tags=["Inventory"])
async def get_equipment_inventory():
    """List equipment inventory"""
    return EQUIPMENT

@app.get("/sla-metrics", response_model=List[SLAMetric], tags=["Performance"])
async def get_sla_metrics():
    """Get SLA performance metrics"""
    return SLA_METRICS

@app.get("/vendor-contracts", response_model=List[VendorContract], tags=["Vendors"])
async def get_vendor_contracts():
    """List vendor contracts"""
    return VENDOR_CONTRACTS

@app.get("/bandwidth-usage", response_model=List[BandwidthUsage], tags=["Analytics"])
async def get_bandwidth_usage():
    """Get bandwidth usage statistics"""
    return BANDWIDTH_USAGE

@app.get("/products", response_model=List[Product], tags=["Sales"])
async def get_products():
    """Get product catalog"""
    return PRODUCTS

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
