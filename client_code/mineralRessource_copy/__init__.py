from ._anvil_designer import mineralRessource_copyTemplate
from anvil import *
import anvil.server
from ..OuertanePhosphate import OuertanePhosphate
from ..jerissa import jerissa

class mineralRessource_copy(mineralRessource_copyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def sraa_phosphate_click(self, **event_args):
    self.column_panel_4.clear()
    self.column_panel_4.add_component(OuertanePhosphate())

  def Jerissa_Mine_click(self, **event_args):
    self.column_panel_4.clear()
    self.column_panel_4.add_component(jerissa())
