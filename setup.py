from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='collective.ptg.allnewest',
      version=version,
      description="Installs all and the newest truegalleries",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plonetruegaller gallery plone addon',
      author='Espen Moe-Nilssen',
      author_email='espen@medialog.no',
      url='https://github.com/collective/collective.ptg.allnewest',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.ptg'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'collective.plonetruegallery',
          'collective.ptg.carousel',
          'collective.ptg.contactsheet',
          'collective.ptg.contentflow',
          'collective.ptg.easyslider',
          'collective.ptg.fancybox',
          'collective.ptg.galleria',
          'collective.ptg.gallerific',
          'collective.ptg.highslide',
          'collective.ptg.nivogallery',
          'collective.ptg.nivoslider',
          'collective.ptg.pikachoose',
          'collective.ptg.presentation',
          'collective.ptg.s3slider',
          'collective.ptg.scrollable',
          'collective.ptg.sheetgallery',
          'collective.ptg.supersized',
          'collective.ptg.thumbnailzoom',
          'collective.ptg.uigallery',
          'setuptools',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
