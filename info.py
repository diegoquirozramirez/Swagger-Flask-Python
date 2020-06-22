import schemas
import json

pwg = schemas.Schemas()

info = {
    "swagger": "2.0",
    "info": {
        "description": "Customer API INformations",
        "version": "1.0.0",
        "title": "Customer",
        "contact": {
            "name": "Diego Quiroz Ramirez (Software Developer)",
            "email": "ingquirozramirez@gmail.com",
            "url": "https://github.com/diegoquirozramirez"
        },
        "license": {
            "name": "MIT",
            "url": ""
        },
        "servers": [
            {
                "url": "http://localhst:5000",
                "description": "Local Server"
            }
        ],
    },
    "host": "localhost:3003",
    "basePath": "/v1",
    "tags": [
        {
            "name": "customers",
            "description": "Customer API REST"
        }
    ],
    "paths": {
        "/customers": {
            "get": {
                "tags": ['customers'],
                "description": "All Customers",
                "responses": {
                    "00": {
                        "description": "successful operation",
                        "schema": pwg.schemaCustomer00()
                    },
                    "01": {
                        "description": "success operation with dirty",
                        "schema": pwg.schemaCustomer01()
                    },
                    "99": {
                        "description": "Error in the process",
                        "schema": pwg.schemaCustomer99()
                    }
                }
            }
        },
        "/customer/{id}": {
            "get": {
                "description": "",
                "tags": ['customers'],
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "type": "string",
                        "description": "Identificator Customer",
                        "example": "202015",
                        "required": True
                    }
                ],
                "responses": {
                    "00": {
                        "description": "Process Success",
                        "schema": pwg.schemaCustomer00()
                    },
                    "01": {
                        "description": "Process Success with dirty",
                        "schema": pwg.schemaCustomer01()
                    },
                    "99": {
                        "description": "Error Process",
                        "schema": pwg.schemaCustomer99()
                    }
                }
            }
        },
        "/edit/customer/{id}": {
            "put": {
                "description": "Edit Customer",
                "tags": ['customers'],
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "type": "string",
                        "example": "202015",
                        "description": "Identificator Customer",
                        "required": True
                    }
                ],
                "responses": {
                    "00": {
                        "description": "Success Proccess",
                        "schema": pwg.schemaCustomer00()
                    },
                    "01": {
                        "description": "Success Proccess with Dirty",
                        "schema": pwg.schemaCustomer01()
                    },
                    "99": {
                        "description": "Error in the Process",
                        "schema": pwg.schemaCustomer99()
                    }
                }
            }
        },
        "/delete/customer/{id}": {
            "delete": {
                "description": "Delete Customer",
                "tags": ['customers'],
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "type": "string",
                        "example": "202015",
                        "description": "Identificator Customer",
                        "required": True
                    }
                ],
                "responses": {
                    "00": {
                        "description": "Success Proccess",
                        "schema": pwg.schemaCustomer00()
                    },
                    "01": {
                        "description": "Success Proccess with Dirty",
                        "schema": pwg.schemaCustomer01()
                    },
                    "99": {
                        "description": "Error in the Process",
                        "schema": pwg.schemaCustomer99()
                    }
                }
            }
        },
        "/new/customer": {
            "post": {
                "description": "New Customer",
                "tags": ['customers'],
                "parameters": [
                    {
                        "name": "values",
                        "in": "body",
                        "description": "Identificator Customer",
                        "required": True,
                        "schema": pwg.schemaNewCustomer()
                    }
                ],
                "responses": {
                    "00": {
                        "description": "Success Proccess",
                        "schema": pwg.schemaCustomer00()
                    },
                    "01": {
                        "description": "Success Proccess with Dirty",
                        "schema": pwg.schemaCustomer01()
                    },
                    "99": {
                        "description": "Error in the Process",
                        "schema": pwg.schemaCustomer99()
                    }
                }
            }
        }
    }
}