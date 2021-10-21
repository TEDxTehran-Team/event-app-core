GRAPHENE = {
    'SCHEMA': 'event_app.schema.schema',
    'MIDDLEWARE': (
        'graphql_jwt.middleware.JSONWebTokenMiddleware',
        # 'event_app.middleware.OrganizerMiddleware',
    ),
}
