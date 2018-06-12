#!/usr/bin/env python

import os
from app import create_app, db
from app.models import User, Job
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('CONFIG_NAME') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

@manager.command
def test():
    ''' python manage.py test '''
    import unittest
    test = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(test)

def make_shell_context():
    return dict(app=app, db=db, User=User, Job=Job)

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand) 
    
if __name__ == '__main__':
    manager.run()
    # pass

