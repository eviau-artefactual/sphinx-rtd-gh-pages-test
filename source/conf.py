import os

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Demo'
copyright = '2024, Artefactual'
author = 'Artefactual'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [

    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

 
############################
# SETUP THE RTD LOWER-LEFT #
############################
try:
   html_context
except NameError:
   html_context = dict()
html_context['display_lower_left'] = True
 
if 'REPO_NAME' in os.environ:
   REPO_NAME = os.environ['REPO_NAME']
else:
   REPO_NAME = ''
 
# SET CURRENT_LANGUAGE
if 'current_language' in os.environ:
   # get the current_language env var set by buildDocs.sh
   current_language = os.environ['current_language']
else:
   # the user is probably doing `make html`
   # set this build's current language to english
   current_language = 'en'
 
# tell the theme which language to we're currently building
html_context['current_language'] = current_language
 
# SET CURRENT_VERSION
from git import Repo
repo = Repo( search_parent_directories=True )
 
if 'current_version' in os.environ:
   # get the current_version env var set by buildDocs.sh
   current_version = os.environ['current_version']
else:
   # the user is probably doing `make html`
   # set this build's current version by looking at the branch
   current_version = repo.active_branch.name
 
# tell the theme which version we're currently on ('current_version' affects
# the lower-left rtd menu and 'version' affects the logo-area version)
html_context['current_version'] = current_version
html_context['version'] = current_version
 
# POPULATE LINKS TO OTHER LANGUAGES
html_context['languages'] = [ ('en', '/' +REPO_NAME+ '/en/' +current_version+ '/') ]
 
languages = [lang.name for lang in os.scandir('source/locales') if lang.is_dir()]
for lang in languages:
   html_context['languages'].append( (lang, '/' +REPO_NAME+ '/' +lang+ '/' +current_version+ '/') )
 
# POPULATE LINKS TO OTHER VERSIONS
html_context['versions'] = list()
 
versions = [branch.name for branch in repo.branches]
for version in versions:
   html_context['versions'].append( (version, '/' +REPO_NAME+ '/'  +current_language+ '/' +version+ '/') )
 
# POPULATE LINKS TO OTHER FORMATS/DOWNLOADS

master_doc = 'index'

# settings for creating PDF with rinoh
rinoh_documents = [(
 master_doc,
 'target',
 project+ ' Documentation',
 '© ' +copyright,
)]
today_fmt = "%B %d, %Y"
 
# settings for EPUB
epub_basename = 'target'
 
html_context['downloads'] = list()
html_context['downloads'].append( ('pdf', '/' +REPO_NAME+ '/' +current_language+ '/' +current_version+ '/' +project+ '-docs_' +current_language+ '_' +current_version+ '.pdf') )
 
html_context['downloads'].append( ('epub', '/' +REPO_NAME+ '/' +current_language+ '/' +current_version+ '/' +project+ '-docs_' +current_language+ '_' +current_version+ '.epub') )

##########################
# "EDIT ON GITHUB" LINKS #
##########################
 
html_context['display_github'] = True
html_context['github_user'] = 'maltfield'
html_context['github_repo'] = 'rtd-github-pages'
html_context['github_version'] = 'master/docs/'

