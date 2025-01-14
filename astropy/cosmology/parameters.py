# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""This module contains dictionaries with sets of parameters for a
given cosmology.

Each cosmology has the following parameters defined:

    ==========  =====================================
    Oc0         Omega cold dark matter at z=0
    Ob0         Omega baryon at z=0
    Om0         Omega matter at z=0
    flat        Is this assumed flat?  If not, Ode0 must be specified
    Ode0        Omega dark energy at z=0 if flat is False
    H0          Hubble parameter at z=0 in km/s/Mpc
    n           Density perturbation spectral index
    Tcmb0       Current temperature of the CMB
    Neff        Effective number of neutrino species
    m_nu        Assumed mass of neutrino species, in eV.
    sigma8      Density perturbation amplitude
    tau         Ionisation optical depth
    z_reion     Redshift of hydrogen reionisation
    t0          Age of the universe in Gyr
    reference   Reference for the parameters
    ==========  =====================================

The list of cosmologies available are given by the tuple
`available`. Current cosmologies available:

Planck 2018 (Planck18) parameters from Planck Collaboration 2020,
 A&A, 641, A6 (Paper VI), Table 2 (TT, TE, EE + lowE + lensing + BAO)

Planck 2018 (Planck18_arXiv_v2) parameters from Planck Collaboration 2018,
 arXiv:1807.06209v2 (Paper VI), Table 2 (TT, TE, EE + lowE + lensing + BAO)

Planck 2015 (Planck15) parameters from Planck Collaboration 2016, A&A, 594, A13
 (Paper XIII), Table 4 (TT, TE, EE + lowP + lensing + ext)

Planck 2013 (Planck13) parameters from Planck Collaboration 2014, A&A, 571, A16
 (Paper XVI), Table 5 (Planck + WP + highL + BAO)

WMAP 9 year (WMAP9) parameters from Hinshaw et al. 2013, ApJS, 208, 19,
doi: 10.1088/0067-0049/208/2/19. Table 4 (WMAP9 + eCMB + BAO + H0)

WMAP 7 year (WMAP7) parameters from Komatsu et al. 2011, ApJS, 192, 18,
doi: 10.1088/0067-0049/192/2/18. Table 1 (WMAP + BAO + H0 ML).

WMAP 5 year (WMAP5) parameters from Komatsu et al. 2009, ApJS, 180, 330,
doi: 10.1088/0067-0049/180/2/330. Table 1 (WMAP + BAO + SN ML).

"""

import astropy.units as u

# Note: if you add a new cosmology, please also update the table
# in the 'Built-in Cosmologies' section of astropy/docs/cosmology/index.rst
# in addition to the list above.  You also need to add them to the 'available'
# list at the bottom of this file.

# Planck 2018 paper VI
# Unlike Planck 2015, the paper includes massive neutrinos in Om0, which here
# are included in m_nu.  Hence, the Om0 value differs slightly from the paper.
Planck18 = dict(
    cosmology="FlatLambdaCDM",
    Oc0=0.2607,
    Ob0=0.04897,
    Om0=0.30966,
    H0=67.66 * (u.km / u.s / u.Mpc),
    n=0.9665,
    sigma8=0.8102,
    tau=0.0561,
    z_reion=7.82,
    t0=13.787 * u.Gyr,
    Tcmb0=2.7255 * u.K,
    Neff=3.046,
    flat=True,
    m_nu=[0., 0., 0.06] * u.eV,
    reference=("Planck Collaboration 2018, 2020, A&A, 641, A6  (Paper VI),"
               " Table 2 (TT, TE, EE + lowE + lensing + BAO)")
)

# Planck 2018 paper VI v2.  Identical to Planck18 above.
# Warning: deprecated and will be removed in future versions.
Planck18_arXiv_v2 = dict(
    cosmology="FlatLambdaCDM",
    Oc0=0.2607,
    Ob0=0.04897,
    Om0=0.30966,
    H0=67.66 * (u.km / u.s / u.Mpc),
    n=0.9665,
    sigma8=0.8102,
    tau=0.0561,
    z_reion=7.82,
    t0=13.787 * u.Gyr,
    Tcmb0=2.7255 * u.K,
    Neff=3.046,
    flat=True,
    m_nu=[0., 0., 0.06] * u.eV,
    reference=("DEPRECATED: Planck Collaboration 2018, arXiv:1807.06209 v2 (Paper VI),"
               " Table 2 (TT, TE, EE + lowE + lensing + BAO)")
)

# Planck 2015 paper XII Table 4 final column (best fit)
Planck15 = dict(
    cosmology="FlatLambdaCDM",
    Oc0=0.2589,
    Ob0=0.04860,
    Om0=0.3075,
    H0=67.74 * (u.km / u.s / u.Mpc),
    n=0.9667,
    sigma8=0.8159,
    tau=0.066,
    z_reion=8.8,
    t0=13.799 * u.Gyr,
    Tcmb0=2.7255 * u.K,
    Neff=3.046,
    flat=True,
    m_nu=[0., 0., 0.06] * u.eV,
    reference=("Planck Collaboration 2016, A&A, 594, A13 (Paper XIII),"
               " Table 4 (TT, TE, EE + lowP + lensing + ext)")
)

# Planck 2013 paper XVI Table 5 penultimate column (best fit)
Planck13 = dict(
    cosmology="FlatLambdaCDM",
    Oc0=0.25886,
    Ob0=0.048252,
    Om0=0.30712,
    H0=67.77 * (u.km / u.s / u.Mpc),
    n=0.9611,
    sigma8=0.8288,
    tau=0.0952,
    z_reion=11.52,
    t0=13.7965 * u.Gyr,
    Tcmb0=2.7255 * u.K,
    Neff=3.046,
    flat=True,
    m_nu=[0., 0., 0.06] * u.eV,
    reference=("Planck Collaboration 2014, A&A, 571, A16 (Paper XVI),"
               " Table 5 (Planck + WP + highL + BAO)")
)


WMAP9 = dict(
    cosmology="FlatLambdaCDM",
    Oc0=0.2402,
    Ob0=0.04628,
    Om0=0.2865,
    H0=69.32 * (u.km / u.s / u.Mpc),
    n=0.9608,
    sigma8=0.820,
    tau=0.081,
    z_reion=10.1,
    t0=13.772 * u.Gyr,
    Tcmb0=2.725 * u.K,
    Neff=3.04,
    m_nu=0.0 * u.eV,
    flat=True,
    reference=("Hinshaw et al. 2013, ApJS, 208, 19, "
               "doi: 10.1088/0067-0049/208/2/19. "
               "Table 4 (WMAP9 + eCMB + BAO + H0, last column)")
)

WMAP7 = dict(
    cosmology="FlatLambdaCDM",
    Oc0=0.226,
    Ob0=0.0455,
    Om0=0.272,
    H0=70.4 * (u.km / u.s / u.Mpc),
    n=0.967,
    sigma8=0.810,
    tau=0.085,
    z_reion=10.3,
    t0=13.76 * u.Gyr,
    Tcmb0=2.725 * u.K,
    Neff=3.04,
    m_nu=0.0 * u.eV,
    flat=True,
    reference=("Komatsu et al. 2011, ApJS, 192, 18, "
               "doi: 10.1088/0067-0049/192/2/18. "
               "Table 1 (WMAP + BAO + H0 ML).")
)

WMAP5 = dict(
    cosmology="FlatLambdaCDM",
    Oc0=0.231,
    Ob0=0.0459,
    Om0=0.277,
    H0=70.2 * (u.km / u.s / u.Mpc),
    n=0.962,
    sigma8=0.817,
    tau=0.088,
    z_reion=11.3,
    t0=13.72 * u.Gyr,
    Tcmb0=2.725 * u.K,
    Neff=3.04,
    m_nu=0.0 * u.eV,
    flat=True,
    reference=("Komatsu et al. 2009, ApJS, 180, 330, "
               "doi: 10.1088/0067-0049/180/2/330. "
               "Table 1 (WMAP + BAO + SN ML).")
)

# If new parameters are added, this list must be updated
available = ['Planck18', 'Planck18_arXiv_v2', 'Planck15', 'Planck13',
             'WMAP9', 'WMAP7', 'WMAP5']
