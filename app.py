from app_factory import create_app
from routes import member_routes_bp, travel_routes_bp, map_routes_bp, log_routes_bp, home_bp
# import routes
app = create_app()

# Register Blueprints
app.register_blueprint(home_bp)
app.register_blueprint(member_routes_bp)
app.register_blueprint(travel_routes_bp)
app.register_blueprint(map_routes_bp)
app.register_blueprint(log_routes_bp)

if __name__ == '__main__':
    app.run(debug=False,port=8080)
