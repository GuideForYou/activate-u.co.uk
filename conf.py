# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add any paths to sys.path if your modules are outside the root
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Activate U.co.uk Account'
copyright = '2025, U.co.uk'
author = 'U.co.uk Support Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Sphinx extensions (add more if needed, e.g., 'sphinx.ext.autodoc')
extensions = []

# Allow raw HTML inside .rst files (enabled by default in newer Sphinx versions)
raw_enabled = True

# Templates and patterns to ignore
templates_path = ['_templates']  # Enable if custom templates are used
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Choose your theme; uncomment and install if using a custom one
# html_theme = 'sphinx_rtd_theme'

# Meta info and branding
html_title = "Activate Your U.co.uk Account – Complete Guide"
html_short_title = "U.co.uk Activation Guide"
html_favicon = 'favicon.ico'  # Ensure favicon.ico exists in _static or root directory

# UI behavior
html_show_sourcelink = False  # Hide "View page source"
html_allow_unsafe = True      # Enable unsafe raw HTML (for buttons, styling, etc.)

# Optional: Customize theme (depends on theme capabilities)
html_theme_options = {
    'show_powered_by': False,
}

# Static assets (images, CSS, JS)
# html_static_path = ['_static']  # Uncomment if you are using static files like custom CSS or favicon
