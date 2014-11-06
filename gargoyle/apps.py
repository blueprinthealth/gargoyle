try:
    from django.apps import AppConfig
except ImportError:
    pass
else:
    class GargoyleAppConfig(AppConfig):
        name = 'gargoyle'

        def ready(self):
            try:
                import nexus
            except ImportError:
                pass
            else:
                from gargoyle.nexus_modules import GargoyleModule
                nexus.site.register(GargoyleModule, 'gargoyle')
