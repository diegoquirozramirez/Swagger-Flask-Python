class Schemas():
    def schemaCustomer00(self):
        schema00 = {
            "type": "object",
            "properties": {
                "codRes": {
                    "type": "string",
                    "example": "00"
                },
                "message": {
                    "type": "string",
                    "example": "Customer All Get Success"
                }
            }
        }
        return  schema00

    def schemaCustomer01(self):
        schema01 = {
            "type": "object",
            "properties": {
                "codRes": {
                    "type": "string",
                    "example": "01"
                },
                "message": {
                    "type": "string",
                    "example": "Customer All Not Found"
                }
            }
        }
        return schema01

    def schemaCustomer99(self):
        schema99 = {
            "type": "object",
            "properties": {
                "codRes": {
                    "type": "string",
                    "example": "99"
                },
                "message": {
                    "type": "string",
                    "example": "Error in the process"
                }
            }
        }
        return schema99

    def schemaNewCustomer(self):
        schema = {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": "User name of customer",
                    "example": "diegoquirozramirez"
                },
                "nombres": {
                    "type": "string",
                    "description": "User name of customer",
                    "example": "Diego Antonio"
                },
                "apellidos": {
                    "type": "string",
                    "description": "User name of customer",
                    "example": "Quiroz Ramirez"
                },
                "email": {
                    "type": "string",
                    "description": "User name of customer",
                    "example": "ingquirozramirez@gmail.com"
                }
            }
        }
        return schema

