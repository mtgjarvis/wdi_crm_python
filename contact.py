class Contact:

  contacts = []
  next_id = 1

  def __init__(self, first_name, last_name, email, note):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.note = note
    self.id = Contact.next_id
    Contact.next_id += 1
    """This method should initialize the contact's attributes"""

  def __str__(self):
    return ('Id: {}, First Name: {}, Last Name: {}, Email: {}, Note: {}'.format (self.id, self.first_name, self.last_name, self.email, self.note))

  @classmethod
  def create(cls, first_name, last_name, email, note):
    contact = Contact(first_name, last_name, email, note)
    cls.contacts.append(contact)
    return contact


  @classmethod
  def all(cls):
    """This method should return all of the existing contacts"""
    return cls.contacts


  @classmethod
  def find(cls, id):
    for contact in cls.contacts:
      if contact.id == id:
        return contact
    """ This method should accept an id as an argument
    and return the contact who has that id
    """

  def update(self, attribute_to_update, new_data):
    if attribute_to_update == 'first name':
      self.first_name = new_data
    elif attribute_to_update == 'last name':
      self.last_name = new_data
    elif attribute_to_update == 'email':
      self.email = new_data
    elif attribute_to_update == 'note':
      self.note = new_data


    """ This method should allow you to specify
    1. which of the contact's attributes you want to update
    2. the new value for that attribute
    and then make the appropriate change to the contact
    """


  @classmethod
  def find_by(cls, attribute, value):
    for contact in cls.contacts:
      if value == getattr(contact, attribute):
        return contact
    return "Not found"

      # selection = {
      #   'first_name': contact.first_name,
      #   'last_name': contact.last_name,
      #   'email': contact.email,
      #   'note': contact.note
      # }[attribute]

      # if selection == value:
      #   return contact
    """This method should work similarly to the find method above
    but it should allow you to search for a contact using attributes other than id
    by specifying both the name of the attribute and the value
    eg. searching for 'first_name', 'Betty' should return the first contact named Betty
    """


  @classmethod
  def delete_all(cls):
    cls.contacts.clear()
    """This method should delete all of the contacts"""


  def full_name(self):
    """Returns the full (first and last) name of the contact"""
    return (f'{self.first_name.capitalize} {self.last_name.capitalize}')

  def delete(self, contact_to_delete):
    Contact.contacts.remove(contact_to_delete)
    """This method should delete the contact
    HINT: Check the Array class docs for built-in methods that might be useful here
    """

  # Feel free to add other methods here, if you need them.

# contact1 = Contact.create('Betty', 'Maker', 'bettymakes@bitmakerlabs.com', 'Loves Pokemon')
# contact2 = Contact.create('Mark', 'Jarvis', 'mtgjarvis@gmail.com', 'Loves surfing')
# contact3 = Contact.create('James', 'Sedge', 'james@sedge.com', 'Good dad')
# print(len(Contact.contacts))
# print(Contact.all())
# print(contact1)
# print(contact2)
# print(contact3)
# print(Contact.find(1))
# print(Contact.find(2))
# print(contact2)
# Contact.delete_all()
# print("Find Mark")
# print(Contact.find_by('last_name', 'Jarvis'))
# print("Find Betty")
# print(Contact.find_by('last_name', 'Maker'))
# print(contact1.full_name())
# contact1.delete()
# print("Find Mark")
# print(Contact.find_by('last_name', 'Jarvis'))
# print("Find Betty")
# print(Contact.find_by('last_name', 'Maker'))