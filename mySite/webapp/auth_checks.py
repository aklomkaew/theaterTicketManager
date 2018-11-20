def can_create_tickets(user):

    #TODO: Check change and create permission for ticket, SeasonTicketHolder, Customer

    in_group = False

    for group in user.groups.all():
        if "Volunteer" in group.name:
            in_group = True


    return ((user.is_authenticated) and (user.is_active)) and (user.is_superuser or in_group == True)