basic.show_string("Bonjour")
basic.pause(500)
basic.show_number(10853)
basic.pause(500)
basic.show_arrow(ArrowNames.SOUTH)
basic.pause(500)
basic.show_icon(IconNames.HAPPY)

def on_forever():
    pass
basic.forever(on_forever)
