import os
from app import app

app.config.from_object('settings')

if __name__ == "__main__":
    os.environ['FLASK_APP'] = __name__
    os.environ['FLASK_DEBUG'] = '1'

    from flask.cli import main, run_command

    run_port_param = next(o for o in run_command.params if o.name == 'port')
    run_port_param.default = app.config.get('PORT', run_port_param)
    main(False)