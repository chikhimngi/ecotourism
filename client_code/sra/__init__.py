from ._anvil_designer import sraTemplate
from anvil import *
import anvil.server

class sra(sraTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
