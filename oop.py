class User:

   def __init__(self,username,password,location) :

      self.username  = username

      self.password = password

      self.location = location

   def change_username(self,new_username):

         self.username = new_username

   def change_location(self,new_location):

          self.location = new_location

   def get_username(self):

         print(self.username)

   def get_loc(self):

         print(self.location)  


class admin(User):

      def __init__(self, username, password, location,delete_permission):

          super().__init__(username, password, location)

          self.delete = delete_permission

      def check_del_per(self):
            self.delete = "ok"

      def get_del_perm(self):
            print(self.delete)      


class admin_assistant(admin):
      def __init__(self, username, password, location, delete_permission):

          super().__init__(username, password, location, delete_permission)

      def set_del_perm(self):
            
            self.delete = "NULL"    






Admin = admin("Principal",12345,"meru","NULL")

Admin.get_del_perm()