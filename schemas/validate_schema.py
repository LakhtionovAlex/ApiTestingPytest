CATEGORY_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "title": {
            "type": "string"
        },
        "image": {
            "type": ["string", "null"],
            "format": "uri"
        },
        "has_products": {
            "type": "boolean"
        },
        "filters": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string"
                    },
                    "values": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    }
                },
                "required": ["title", "values"]
            }
        },
        "nested_categories": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer"
                    },
                    "title": {
                        "type": "string"
                    },
                    "image": {
                        "type": ["string", "null"],
                        "format": "uri"
                    },
                    "description": {
                        "type": ["string", "null"]
                    }
                },
                "required": ["id", "title"]
            }
        },
        "description": {
            "type": ["string", "null"]
        }
    },
    "required": ["id", "title", "has_products", "filters", "nested_categories"]
}

TAGS_LIST_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "description": {"type": "string"},
            "is_displayed_on_card": {"type": ["boolean", "null"]},
            "position_on_card": {"type": ["integer", "null"]},
            "color_icon": {"type": ["string", "null"]},
            "color_text": {"type": ["string", "null"]}
        },
        "required": ["id", "title", "description", "color_text"],
    }
}

LIST_USERS_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "email": {"type": ["string", "null"], "format": "email"},
            "name": {"type": "string"},
            "role": {"type": "string"},
            "gender": {"type": ["string", "null"], "enum": ["male", "female", None]},
            "birthday_date": {"type": ["string", "null"], "format": "date"},
            "phone_number": {"type": ["string", "null"]},
            "mailing_permission": {"type": ["boolean", "null"]},
        },
        "required": ["id", "email", "name", "role", "gender", "birthday_date", "phone_number", "mailing_permission"]
    }
}