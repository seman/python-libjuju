class Juju(object):
    def add_cloud(self, name, definition, replace=False):
        """Add a user-defined cloud to Juju from among known cloud types.

        :param str name: Name of cloud
        :param dict definition: Cloud definition

        Example cloud definition, as yaml::

            type: openstack
            auth-types: [ userpass ]
            regions:
              london:
                endpoint: https://london.mycloud.com:35574/v3.0/

        """
        pass

    def agree(self, *terms):
        """Agree to the terms of a charm.

        :param str \*terms: Terms to agree to

        """
        pass

    def autoload_credentials(self):
        """Finds cloud credentials and caches them for use by Juju when
        bootstrapping.

        """
        pass

    def create_budget(self):
        """Create a new budget.

        """
        pass

    def get_agreements(self):
        """Return list of terms to which the current user has agreed.

        """
        pass

    def get_budgets(self):
        """Return list of available budgets.

        """
        pass

    def get_clouds(self):
        """Return list of all available clouds.

        """
        pass

    def get_controllers(self):
        """Return list of all available controllers.

        (maybe move this to Cloud?)
        """
        pass

    def get_plans(self, charm_url):
        """Return list of plans available for the specified charm.

        :param str charm_url: Charm url

        """
        pass

    def register(self, registration_string):
        """Register a user to a controller.

        :param str registration_string: The registration string

        """
        pass

    def set_budget(self, name, limit):
        """Set a monthly budget limit.

        :param str name: Name of budget
        :param int limit: Monthly limit

        """
        pass

    def get_cloud(self, name):
        """Get a cloud by name.

        :param str name: Name of cloud

        """
        pass

    def get_controller(self, name, include_passwords=False):
        """Get a controller by name.

        :param str name: Name of controller
        :param bool include_passwords: Include passwords for accounts

        (maybe move this to Cloud?)
        """
        pass

    def update_clouds(self):
        """Update public cloud info available to Juju.

        """
        pass

    def version(self):
        """Return the Juju version.

        """
        pass
