# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RCdcfluview(RPackage):
    """The 'U.S.' Centers for Disease Control ('CDC') maintains a portal
    <http://gis.cdc.gov/grasp/fluview/fluportaldashboard.html> for accessing
    state, regional and national influenza statistics as well as Mortality
    Surveillance Data. The web interface makes it difficult and time-consuming
    to select and retrieve influenza data. Tools are provided to access the
    data provided by the portal's underlying 'API'."""

    homepage = "https://cran.r-project.org/package=cdcfluview"
    url      = "https://cran.r-project.org/src/contrib/cdcfluview_0.7.0.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/cdcfluview"

    version('0.7.0', 'd592606fab3da3536f39a15c0fdbcd17')

    depends_on('r-httr', type=('build', 'run'))
    depends_on('r-dplyr', type=('build', 'run'))
    depends_on('r-jsonlite', type=('build', 'run'))
    depends_on('r-sf', type=('build', 'run'))
    depends_on('r-xml2', type=('build', 'run'))
    depends_on('r-purrr', type=('build', 'run'))
    depends_on('r-readr', type=('build', 'run'))
    depends_on('r-mmwrweek', type=('build', 'run'))
    depends_on('r-units@0.4-6:', type=('build', 'run'))
    depends_on('r@3.2.0:', type=('build', 'run'))
