# Django Vendor Management System

This project implements a Vendor Management System using Django and Django REST Framework. The system includes features for managing vendor profiles, tracking purchase orders, and calculating vendor performance metrics.

## Core Features

1. **Vendor Profile Management:**
   - Create, retrieve, update, and delete vendor profiles.
   - API Endpoints:
     - `POST /api/vendors/`: Create a new vendor.
     - `GET /api/vendors/`: List all vendors.
     - `GET /api/vendors/{vendor_id}/`: Retrieve a specific vendor's details.
     - `PUT /api/vendors/{vendor_id}/`: Update a vendor's details.
     - `DELETE /api/vendors/{vendor_id}/`: Delete a vendor.

2. **Purchase Order Tracking:**
   - Create, retrieve, update, and delete purchase orders.
   - API Endpoints:
     - `POST /api/purchase_orders/`: Create a purchase order.
     - `GET /api/purchase_orders/`: List all purchase orders with filtering options.
     - `GET /api/purchase_orders/{po_id}/`: Retrieve details of a specific purchase order.
     - `PUT /api/purchase_orders/{po_id}/`: Update a purchase order.
     - `DELETE /api/purchase_orders/{po_id}/`: Delete a purchase order.

3. **Vendor Performance Evaluation:**
   - Calculate performance metrics such as on-time delivery rate, quality rating average, average response time, and fulfillment rate.
   - API Endpoint:
     - `GET /api/vendors/{vendor_id}/performance`: Retrieve a vendor's performance metrics.

## Data Models

1. **Vendor Model**
   - Stores vendor information including performance metrics.
   - Fields:
     - `name`: Vendor's name.
     - `contact_details`: Contact information of the vendor.
     - `address`: Physical address of the vendor.
     - `vendor_code`: A unique identifier for the vendor.
     - `on_time_delivery_rate`: Percentage of on-time deliveries.
     - `quality_rating_avg`: Average rating of quality based on purchase orders.
     - `average_response_time`: Average time taken to acknowledge purchase orders.
     - `fulfillment_rate`: Percentage of purchase orders fulfilled successfully.

2. **Purchase Order (PO) Model**
   - Captures details of each purchase order and is used to calculate performance metrics.
   - Fields:
     - `po_number`: Unique number identifying the PO.
     - `vendor`: Link to the Vendor model.
     - `order_date`: Date when the order was placed.
     - `delivery_date`: Expected or actual delivery date of the order.
     - `items`: Details of items ordered.
     - `quantity`: Total quantity of items in the PO.
     - `status`: Current status of the PO.
     - `quality_rating`: Rating given to the vendor for this PO (nullable).
     - `issue_date`: Timestamp when the PO was issued to the vendor.
     - `acknowledgment_date`: Timestamp when the vendor acknowledged the PO.

3. **Historical Performance Model** (Optional)
   - Stores historical data on vendor performance for trend analysis.
   - Fields:
     - `vendor`: Link to the Vendor model.
     - `date`: Date of the performance record.
     - `on_time_delivery_rate`: Historical record of the on-time delivery rate.
     - `quality_rating_avg`: Historical record of the quality rating average.
     - `average_response_time`: Historical record of the average response time.
     - `fulfillment_rate`: Historical record of the fulfillment rate.

## Backend Logic for Performance Metrics

The backend logic calculates various performance metrics based on interactions recorded in the Purchase Order model:
- **On-Time Delivery Rate**
- **Quality Rating Average**
- **Average Response Time**
- **Fulfillment Rate**

## API Endpoint Implementation

- **Vendor Performance Endpoint** (`GET /api/vendors/{vendor_id}/performance`)
  - Retrieves the calculated performance metrics for a specific vendor.

- **Update Acknowledgment Endpoint** (`POST /api/purchase_orders/{po_id}/acknowledge`)
  - Updates acknowledgment date and triggers the recalculation of average response time.

## Additional Technical Considerations

- Efficient Calculation
- Data Integrity
- Real-time Updates

## Technical Requirements

- Django and Django REST Framework
- RESTful API design
- Comprehensive data validations
- Django ORM for database interactions
- Token-based authentication
- PEP 8 style guidelines for Python code
- Thorough documentation for each API endpoint

## Postman Documentation

For detailed documentation of API endpoints, refer to the [Postman documentation](https://documenter.getpostman.com/view/33222895/2sA3JFA4br).

This project tests your ability to create a functional Django-based system for vendor management, integrating data handling, API development, and performance metric calculations.
