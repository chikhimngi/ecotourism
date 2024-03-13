from ._anvil_designer import geologyTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..ophites import ophites
from ..phosphateDyr import phosphateDyr
from ..synclinal import synclinal
from ..kt import kt
from ..grotte import grotte
from ..ammonite import ammonite
from ..slata import slata
from ..sraouertane import sraouertane
from ..slump import slump
from ..jerissa import jerissa

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

  def synclinal_click(self, **event_args):
    self.content_ophite.clear()
    self.content_ophite.add_component(synclinal())

  def kt_click(self, **event_args):
    self.content_ophite.clear()
    self.content_ophite.add_component(kt())

  def grotte_click(self, **event_args):
    self.content_ophite.clear()
    self.content_ophite.add_component(grotte())

  def ammonite_click(self, **event_args):
    self.content_ophite.clear()
    self.content_ophite.add_component(ammonite())

  def recif_click(self, **event_args):
    self.content_ophite.clear()
    self.content_ophite.add_component(slata())

  def link_8_click(self, **event_args):
    self.content_ophite.clear()
    self.content_ophite.add_component(sraouertane())

  def link_9_click(self, **event_args):
    self.content_ophite.clear()
    self.content_ophite.add_component(slump())

  def jerissa_click(self, **event_args):
    self.content_ophite.clear()
    self.content_ophite.add_component(jerissa())













