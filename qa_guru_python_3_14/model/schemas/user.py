from voluptuous import Schema, PREVENT_EXTRA

create_user_schema = Schema(
    {
        "name": str,
        "job": str,
        "id": str,
        "createdAt": str
    },
    extra=PREVENT_EXTRA,
    required=True
)
