from ._anvil_designer import OuertanePhosphateTemplate
from anvil import *
import anvil.server

class OuertanePhosphate(OuertanePhosphateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def sraa_phosphate_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass
