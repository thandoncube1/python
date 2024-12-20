from collections import ChainMap

LANGUAGE = 'language'
THEME = 'theme'
NOTIFICATIONS = 'notifications'

default_settings: dict[str, str | bool] = {
    THEME: 'Light',
    LANGUAGE: 'English',
    NOTIFICATIONS: True
}

user_preferences: dict[str, str | bool] = {
    THEME: 'Dark',
    NOTIFICATIONS: False
}

cm: ChainMap = ChainMap(user_preferences, default_settings)

print(cm['language'])
# Changing the theme for user preferences
cm.maps[0].update({'theme': 'Light'})
print(cm)
