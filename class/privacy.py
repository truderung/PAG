
class PKW:
  definition = "this is public"
  __definition = "this is private"

  print("-1--- output inside class while interpreting ----------------------")
  print(definition)
  print(__definition)

  #def __init__(self):
  #  self.definition = "public instance variable"
  #  self.__definition = "private instance variable"

  def make_private_definition_public(self):
    return self.__definition
    
  def access_to_private_in_dict(self):
    try:
      return self.__class__.__dict__["__definition"]
    except:
      raise Exception("ERROR! Variable doesn't exist")

  def exists_private_in_dict(self):
    return "__definition" in self.__class__.__dict__

  def exists_public_in_dict(self):
    return "definition" in self.__class__.__dict__
