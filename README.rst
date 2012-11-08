Add arbitrary data to your django users. This app adds `user.meta` which acts like a dictionary and stores whatever the hell you want. But you could add `.meta` to any of your models.

Add `meta` to your installed_apps if you want to use the included `user.meta`. If you just want to add meta to your models, extend `meta.models.ModelMeta` and add a foreign key to something.

There's not much to it. Just read the code.
