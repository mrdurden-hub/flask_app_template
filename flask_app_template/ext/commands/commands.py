def init_app(app, db):
    @app.cli.command()
    def create_db():
        """create sql database"""
        db.create_all()
