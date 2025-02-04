from src.core.router.entity import Router
from src.core.app.entity import App


router: Router = Router(ignore_command_register=True)
app: App = App()


@router.command('u')
def command_u():
    print('eeeeeee')


@router.unknown_command
def command_unknown_command(command):
    print('dfvrgbrgndsrgngfn')



app.include_route(router)

app.start_polling()
