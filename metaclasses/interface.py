from abc import ABC, abstractmethod


class interface(ABC):

  @abstractmethod
  def talk(self):
    pass


class implement(interface):

  def talk(self):
    print("method implemented")


class not_implement(interface):

  def __init__(self):
    pass


obj = implement()
obj2 = not_implement()
