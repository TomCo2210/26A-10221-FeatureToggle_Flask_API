from controllers.feature_toggle import feature_toggle_blueprints

def init_routes(app):
    app.register_blueprint(feature_toggle_blueprints)