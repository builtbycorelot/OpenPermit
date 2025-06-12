# OpenPermit Templates

## Available Templates

### Building Permits
- `building-permit` - General building permit
- `building-residential` - Residential construction
- `building-commercial` - Commercial construction
- `building-renovation` - Renovation permits

### Business Licenses
- `business-license` - General business license
- `business-food` - Food service license
- `business-retail` - Retail business license
- `business-home` - Home-based business

### Zoning Applications
- `zoning-variance` - Zoning variance request
- `zoning-conditional` - Conditional use permit
- `zoning-appeal` - Zoning board appeal

## Template Structure
Each template includes:
- JSON-LD schema definition
- Validation rules
- Workflow configuration
- UI form configuration
- Documentation

## Custom Templates
Create custom templates using:
```bash
openpermit template create my-custom-permit
openpermit template edit my-custom-permit
openpermit template validate my-custom-permit
```
