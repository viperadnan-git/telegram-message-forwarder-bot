def parse_chats(chats):
    """

    [[chats]]
    from = "123456789"
    to = "123456789"

    [[chats]]
    from = ["123456789", "123456789"]
    to = "123456789"

    [[chats]]
    from = "123456789"
    to = ["123456789", "123456789"]

    [[chats]]
    from = ["123456789", "123456789"]
    to = ["123456789", "123456789"]
    """

    # Set all from values to a list and, from => [to, replace] in dict
    monitored_chats = set()
    chats_map = {}
    filter = []
    chats_map["filter"] = []

    for chat in chats:
        from_chats = chat["from"]
        to_chats = chat["to"]
        filter = chat.get("filter")
        replace = chat.get("replace")
        
        if not isinstance(from_chats, list):
            from_chats = [from_chats]

        if not isinstance(to_chats, list):
            to_chats = [to_chats]

        if not isinstance(filter, list) and filter is not None:
            filter = [filter]

        if filter:
            chats_map["filter"].extend(filter)

        for from_chat in from_chats:
            if from_chat not in chats_map:
                chats_map[from_chat] = {"to": set(), "replace": replace}

            for to_chat in to_chats:
                chats_map[from_chat]['to'].add(to_chat)
            
            monitored_chats.add(from_chat)

    return list(monitored_chats), chats_map
