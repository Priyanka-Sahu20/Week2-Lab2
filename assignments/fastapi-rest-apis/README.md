# 🚀 Building REST APIs with FastAPI

## 🎯 Objective

Create a functional REST API using the FastAPI framework to understand HTTP methods, request/response handling, data validation, and API design patterns. You'll build a complete API with CRUD operations and learn how to structure modern Python web applications.

## 📝 Tasks

### 🛠️ Build a Basic REST API with CRUD Operations

#### Description
Create a FastAPI application that serves as an API for managing a collection of items. Implement endpoints for creating, reading, updating, and deleting items using HTTP methods (GET, POST, PUT, DELETE).

#### Requirements
Your API must:

- Set up a FastAPI application with proper initialization
- Define a data model using Pydantic for type validation
- Implement GET endpoint to retrieve all items
- Implement GET endpoint to retrieve a single item by ID
- Implement POST endpoint to create new items
- Implement PUT endpoint to update existing items
- Implement DELETE endpoint to remove items
- Use appropriate HTTP status codes for each operation

### 🛠️ Add Data Validation and Error Handling

#### Description
Enhance your API with robust error handling and input validation to ensure data integrity and provide helpful error messages to API consumers. Implement validation rules and appropriate HTTP error responses.

#### Requirements
Your API must:

- Validate all request data using Pydantic models
- Handle cases where requested items don't exist (404 errors)
- Return meaningful error messages with appropriate HTTP status codes
- Include docstrings for all endpoints
- Implement input constraints (e.g., required fields, string length limits)
- Use type hints throughout the code for clarity
