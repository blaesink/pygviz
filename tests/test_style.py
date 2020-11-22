from pygviz.style import *

def test_add_color():
   data = [
      "Jhomas -- Pizza Bagels",
      "Jhomas -- Kale"
   ]

   expected = [
      "Jhomas -- Pizza Bagels [fillcolor = green]",
      "Jhomas -- Kale [fillcolor = red]"
   ]

   actual = [
      add_color_to_link(data[0], "green"),
      add_color_to_link(data[1], "red")
   ]

   assert actual == expected

def test_add_linestyle():
   data = [
      "Jhomas -- Pizza Bagels",
      "Jhomas -- Kale"
   ]

   expected = [
      "Jhomas -- Pizza Bagels [linestyle = dashed]",
      "Jhomas -- Kale [linestyle = dotted]"
   ]

   actual = [
      add_linestyle(data[0], "dashed"),
      add_linestyle(data[1], "dotted")
   ]

   assert actual == expected

def test_multistyle():
   data = [
      "Jhomas -- Pizza Bagels",
      "Jhomas -- Kale"
   ]

   expected = "Jhomas -- Pizza Bagels [fillcolor = green;linestyle = dashed;]",
   style = {
      "color": "green",
      "linestyle": "dashed"
   }
   actual = multistyle(data[0], style)

   assert actual == expected
