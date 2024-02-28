from ._anvil_designer import geoparkTemplate
from anvil import *

class geopark(geoparkTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.