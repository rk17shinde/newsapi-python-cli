newsapi-python-cli
A Python commandline client interface for newsapi top headlines api to export top 100 news items to csv

PyPI version
3.7

Provided by Rajkumar Shinde.
Note: this library may be subtly broken or buggy.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

General
This is a Python client library for commandline client interface for newsapi top headlines api to export top 100 news items to csv


Requirements

Required packages
    'db-sqlite3==0.0.1',
    'newsapi-python==0.2.3',
    'Click==7.0'

Please refer requirements.txt for more details about dependencies


#Creating Virtual Environment
The module used to create and manage virtual environments is called venv. venv will usually install the most recent version of Python that you have available. If you have multiple versions of Python on your system, you can select a specific Python version by running python3 or whichever version you want.

To create a virtual environment, decide upon a directory where you want to place it, and run the venv module as a script with the directory path:

python3 -m venv tutorial-env
This will create the tutorial-env directory if it doesn’t exist, and also create directories inside it containing a copy of the Python interpreter, the standard library, and various supporting files.

Once you’ve created a virtual environment, you may activate it.

On Windows, run:

tutorial-env\Scripts\activate.bat

On Unix or MacOS, run:

source tutorial-env/bin/activate


#Leaving the virtualenv
If you want to switch projects or otherwise leave your virtualenv, simply run:

deactivate


Installation

1) Dependency Package Installation:

You could install the dependencies by
    pip install -r requirements.txt

2) Download the newsapi_cli package from the repository

3) Set the value of SAMPLE_API_KEY in const.py

4) Now you could use the commanline utitlity 
    Run the news CLI

    python news.py <output_file_name>

