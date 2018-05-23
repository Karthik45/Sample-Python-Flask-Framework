from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db
import coverage

# Initializing the manager
manager = Manager(app)

# Initialize Flask Migrate
migrate = Migrate(app, db)

# Add the flask migrate
manager.add_command('db', MigrateCommand)

# Test coverage configuration
COV = coverage.coverage(
    branch=True,
    include='app/*',
    omit=[
        'app/auth/__init__.py',
    ]
)
COV.start()

# Run the manager
if __name__ == '__main__':
    manager.run()