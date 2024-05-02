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
    
## Installation

Open Terminal and follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/KarunShaji/VendorManagementSystem-API
    ```
2. **Navigate to the project directory:**
   ```bash
   cd VendorManagementSystem-API
   ```
   
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
   
5. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Access the API Endpoints in Postman:

## Accessing the API Endpoints in Postman

Follow these steps to interact with the API using Postman:

1. **Import the provided Postman collection:**
   - Click on the following button to view the Postman documentation:
   
     [![Postman](https://run.pstmn.io/button.svg)](https://www.postman.com/karunshaji/workspace/vendor-management-system/collection/33222895-bbc47f22-27d2-4331-a4e2-86403e2055c6)

2. **Set up the environment in Postman:**
   - After importing the collection, set up your environment variables, such as the base URL (`http://localhost:8000/`).

3. **Obtain an authentication token:**
   - Use the provided superuser account credentials to log in and obtain an authentication token.

4. **Authenticate requests:**
   - Set the obtained authentication token in the Authorization header of your requests to authenticate.

5. **Send requests using example data:**
   - Explore the endpoints documented in the collection and use the example data provided in the documentation as test inputs.


## Backend Logic for Performance Metrics

The backend logic calculates various performance metrics based on interactions recorded in the Purchase Order model:
- **On-Time Delivery Rate**
- **Quality Rating Average**
- **Average Response Time**
- **Fulfillment Rate**


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
