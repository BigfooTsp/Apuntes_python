# OBTENER DATOS DE UN OBJETO

import dropbox

dbx = dropbox.Dropbox(
    '1ZVMAg-du20AAAAAAAARj16-hunx2c6UfLXAHWzU0a75zEd6aZQzLIkn8fNM0XeB')


res = dbx.users_get_current_account()

# <class 'dropbox.users.FullAccount'>

print (str(res))
# objeto de tipo <class 'dropbox.users.FullAccount'>

# FullAccount(account_id='dbid:AAD-oKbDEWmh23JhubTi__OJecjPl5EmiSE', name=Name(given_name='BigfooTsp', surname='BigfooTsp', familiar_name='BigfooTsp', display_name='BigfooTsp BigfooTsp', abbreviated_name='BB'), email='pedrojosepinacuenca@gmail.com', email_verified=True, disabled=False, locale='es-ES', referral_link='https://db.tt/bNrczOcF', is_paired=False, account_type=AccountType('basic', None), profile_photo_url=None, country='ES', team=None, team_member_id=None)

print (res.account_id)
# dbid:AAD-oKbDEWmh23JhubTi__OJecjPl5EmiSE
# print (res.name)
# Name(given_name='BigfooTsp', surname='BigfooTsp', familiar_name='BigfooTsp', display_name='BigfooTsp BigfooTsp', abbreviated_name='BB')

print (type(res.name))
print (res.name)
# <class 'dropbox.users.Name'>
# Name(given_name='BigfooTsp', surname='BigfooTsp', familiar_name='BigfooTsp', display_name='BigfooTsp BigfooTsp', abbreviated_name='BB')


print ((res.name.given_name))
# BigfooTsp

		