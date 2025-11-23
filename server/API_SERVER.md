# Modexia ISP API Server

## Quick Start

### Installation

1. Navigate to the server directory:
```bash
cd server
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Server

From the `server` directory:
```bash
python main.py
```

Or using uvicorn directly:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The server will start at `http://localhost:8000`

### API Documentation

Once the server is running, visit:
- **Interactive API Docs (Swagger UI)**: http://localhost:8000/docs
- **Alternative Docs (ReDoc)**: http://localhost:8000/redoc

## Available Endpoints

| Endpoint | Method | Description | Query Parameters |
|----------|--------|-------------|------------------|
| `/` | GET | Welcome message | - |
| `/customers` | GET | List all customers | `status` (Active, Suspended, Churned, Trial) |
| `/employees` | GET | List all employees | - |
| `/invoices` | GET | List all invoices | `status` (Paid, Overdue, Pending, Failed) |
| `/tickets` | GET | List support tickets | `priority`, `status` |
| `/network-infrastructure` | GET | List network nodes | - |
| `/equipment-inventory` | GET | List equipment | - |
| `/sla-metrics` | GET | Get SLA metrics | - |
| `/vendor-contracts` | GET | List vendor contracts | - |
| `/bandwidth-usage` | GET | Get bandwidth statistics | - |
| `/products` | GET | Get product catalog | - |

## Example API Calls

### Get all active customers
```bash
curl http://localhost:8000/customers?status=Active
```

### Get critical priority tickets
```bash
curl http://localhost:8000/tickets?priority=Critical
```

### Get overdue invoices
```bash
curl http://localhost:8000/invoices?status=Overdue
```

### Get all employees
```bash
curl http://localhost:8000/employees
```

## Features

✅ Full FastAPI implementation with Pydantic models  
✅ Auto-generated OpenAPI/Swagger documentation  
✅ CORS enabled for cross-origin requests  
✅ Query parameter filtering for customers, invoices, and tickets  
✅ Type-safe responses with Pydantic validation  
✅ All data from the JSON specification included  

## Development

The server includes:
- **Hot reload** enabled when running with `--reload` flag
- **Type hints** throughout for better IDE support
- **Automatic validation** via Pydantic models
- **Interactive documentation** at `/docs`

---

**Note:** Modexia Inc. is a fictional company created for demonstration purposes.
