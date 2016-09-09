def left_join(phrases):
    return ",".join([x.replace('right', 'left') for x in phrases])

