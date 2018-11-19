def can_create_tickets(user):

    return (user.is_authenticated) and (user.is_active) and (user.is_superuser or user.groups.filter(name='Volunteer'))