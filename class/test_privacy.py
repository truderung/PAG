from privacy import *
import pytest
import copy


def test_access_from_outside():
    assert PKW.definition == "this is public"
    a = PKW()
    assert a.definition == "this is public"

    with pytest.raises(Exception):
        try:
            a.__definition 
        except:
            raise Exception('ERROR! Access to private attribute failed')
    
    assert a._PKW__definition == "this is private" # because at least two leading underscores are replaced with _classname__ ...


def test_access_to_private_through_member_function():
    a = PKW()  
    assert a.make_private_definition_public() == "this is private"


def test_access_to_private_in_dict():
    a = PKW()
    with pytest.raises(Exception):
        a.access_to_private_in_dict()


def test_exists_private_in_dict():
    a = PKW()
    assert not a.exists_private_in_dict()


def test_exists_public_in_dict():
    a = PKW()
    assert a.exists_public_in_dict()


def test_dictionaries():
    assert PKW.__dict__["definition"] == "this is public"
    with pytest.raises(Exception):
        try:
            PKW.__dict__["__definition"]
        except:
            raise Exception('ERROR! Access to private attribute failed')
    
    assert PKW.__dict__["_PKW__definition"] == "this is private"
    
    assert PKW().__class__.__dict__["definition"] == "this is public"
    with pytest.raises(Exception):
        try:
            PKW().__class__.__dict__["__definition"]
        except:
            raise Exception('ERROR! Access to private attribute failed')
    
    assert PKW().__class__.__dict__["_PKW__definition"] == "this is private"


# change the attribute with global effect
def test_global_attribute():
    a = PKW()
    b = PKW()

    assert a.definition == "this is public"
    
    temp = copy.copy(PKW.definition)
    PKW.definition = "modified"

    assert a.definition == "modified"
    assert b.definition == "modified"
    
    PKW.definition = temp


# set value to definition. This creates a instance variable,
# which is primarily returned
def test_instance_variable():
    a = PKW()

    assert a.definition == "this is public"
    a.definition = "modified"

    assert a.definition == "modified"
    assert PKW.definition == "this is public"

    assert a.__class__.__dict__["definition"] == "this is public"
    assert a.__dict__["definition"] == "modified"


# Be careful! Mutable variables are shared by a pointer.
# This affects to all instances of the class.    
def test_attribute_mutation():
    temp = copy.copy(PKW.definition) # store the original value
    PKW.definition = list() # change to a mutable class type

    a = PKW()
    b = PKW()
    assert a.definition == []
    assert b.definition == []

    a.definition.append(3)
    assert a.definition == [3]
    assert b.definition == [3]

    b.definition.append(98)
    assert a.definition == [3, 98]
    assert b.definition == [3, 98]

    PKW.definition = temp # restore the original