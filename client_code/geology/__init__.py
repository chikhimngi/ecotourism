from ._anvil_designer import geologyTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..ophites import ophites
from ..phosphateDyr import phosphateDyr

class geology(geologyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    

  def home_click(self, **event_args):
    open_form('home')

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

  def ophite_click(self, **event_args):
    self.content_ophite.clear()
    self.content_ophite.add_component(ophites())

  def phospate_click(self, **event_args):
    self.content_ophite.clear()
    self.content_ophite.add_component(phosphateDyr())





