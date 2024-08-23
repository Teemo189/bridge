# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '简立得®操作手册'
copyright = '哈尔滨工业大学重庆研究院' 

language ='zh'
extensions = ['myst_parser']
templates_path = ['_templates']
html_static_path = ['_static']

html_css_files = ['css/custom.css']
html_style = 'css/custom.css'

html_js_files = ['js/MathJax.js']
html_style = 'js/MathJax.js'

mathjax3_config = {
    'extensions': ['tex3jax.js'],
    'jax': ['input/TeX', 'output/HTML-CSS'],
}

exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
#html_theme = 'sphinx_book_theme'
html_title = "简立得®操作手册"
#html_logo = "_static/logo.png"
html_favicon = "_static/favicon.ico"


extensions = ['recommonmark']
from recommonmark.parser import CommonMarkParser
source_parsers = {
    '.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']

extensions = [
    'sphinx.ext.mathjax'
]
extensions = [
    'sphinx_tabs'
]

extensions = [
    'sphinx_toolbox.collapse',
    'sphinx_toolbox.assets',
    'sphinx_toolbox.changeset',
    'sphinx_toolbox.code',
    'sphinx_toolbox.confval',
    'sphinx_toolbox.rest_example',
    'sphinx_toolbox.shields',
] 
extensions = [
    'sphinx.ext.viewcode',
    'sphinx_tabs.tabs',
    'sphinx-prompt',
    'sphinx_toolbox',
    ]
github_username = '<Teemo189>'
github_repository = '<bridge>'



latex_engine = 'xelatex'
latex_elements = {
    
    'fontpkg': r'''
        \\setmainfont{DejaVu Serif}
        \\setsansfont{DejaVu Sans}
        \\setmonofont{DejaVu Sans Mono}
    ''',
    'preamble': r'''
        \\usepackage[titles]{tocloft}
        \\cftsetpnumwidth {1.25cm}\\cftsetrmarg{1.5cm}
        \\setlength{\\cftchapnumwidth}{0.75cm}
        \\setlength{\\cftsecindent}{\\cftchapnumwidth}
        \\setlength{\\cftsecnumwidth}{1.25cm}
        \\usepackage{amsmath}\n\\usepackage{amssymb}
        \\input{mystyle.tex.txt}',
        \\usepackage{mystyle}',
    ''',
    'fncychap': r'\\usepackage[Bjornstrup]{fncychap}',
    'printindex': r'\\footnotesize\\raggedright\\printindex',
}
latex_show_urls = 'footnote'

latex_additional_files = ["mystyle.sty"]
latex_elements = {
    'sphinxsetup': 'key1=value1, key2=value2, ...',
}
latex_elements = {
    'passoptionstopackages': r'\\PassOptionsToPackage{svgnames}{xcolor}',
}
latex_elements = {

    'preamble': '''
    \\hypersetup{unicode=true}
    \\usepackage{CJKutf8}
    \\AtBeginDocument{\\begin{CJK}{UTF8}{gbsn}}
    \\AtEndDocument{\\end{CJK}}
    ''',
}
extensions = [
    'sphinx.ext.ifconfig',
    'sphinx.ext.graphviz',
]


