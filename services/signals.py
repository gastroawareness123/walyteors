def post_save_activities_for_language_save(sender, instance, created, *args, **kwargs):
    if not instance.name.islower():
        instance.name = instance.name.lower()
        instance.save()