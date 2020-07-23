# obps_dashboard
The obps_dashboard is a django application developed at the IOC Ocean Best Practices System (IOC-OBPS) https://www.oceanbestpractices.org/ in order to provide metrics about the own OBPS performance that are dispalyed in a set of html web front-ends.

## Prerequisites:

    See requirements file for extralibraries needed.

## How to install and run obps_dashboard:
- Create a virtual environment and install the requirements.
- With a postgresql database administrator, create the schema for the obpr database.
- Download gentelela alela template https://github.com/ColorlibHQ/gentelella and allocate the whole folder into /obps_dashboard/templates/ directory.
- Copy the whole sub-folder "static" into /obps_dashboard/static_pro/
- Workon the virtual environment.   ```workon obps_dashboard```
- Migrate the django models to the obpr schema.   ```python manage.py migrate```




## The following features are planned or in development:

  

## Copyright

Copyright (C) 2019 International Oceanographic Data and Information Exchange" (IODE) of the "Intergovernmental Oceanographic Commission" (IOC) of UNESCO http://www.iode.org

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.

Colorlib is the original author of the frontend web template, that is a project developed and maintained by Colorlib and Aigars Silkalns. Further information about the template can be found in https://github.com/ColorlibHQ/gentelella
