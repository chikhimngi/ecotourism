from ._anvil_designer import homeTemplate
from anvil import *
from ..kef import kef

class home(homeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def vist_kef_click(self, **event_args):
    self.column_panel01.clear()
    self.content_panel01.add_component(kef())



