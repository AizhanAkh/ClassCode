#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 10:54:08 2018

@author: aizhan.akh
"""

from classy import Class
dmeff = Class()
dmeff.struct_cleanup()
dmeff.set({'omega_dmeff':0.1205, "omega_cdm": 0.0,"omega_b":0.02218, "h":0.67, "tau_reio":0.07})
dmeff.set({"m_dmeff":1e-3,"sigma_dmeff":1.0e-36, "npow_dmeff":-4})
dmeff.set({"dmeff_Vrms_dynamic":"yes","dmeff_niter_dynamic_max":15, "Vrms_convergence_tol":1e-2})
dmeff.set({"tau_reio":0.07,"ln10^{10}A_s":3.056,"n_s":0.9619})
dmeff.compute()
dmeff.set({"Vrel_dmeff_rate":0})
dmeff.set({"tight_coupling_trigger_tau_c_over_tau_h":0.0, "tight_coupling_trigger_tau_c_over_tau_k":0.0})

dmeff.set({"output":"tCl, lCl, pCl, mPk", "root":"test_output/dmeff_","recombination":"recfast", "gauge":"synchronous"})
dmeff.set({"write thermodynamics":"yes", "write background":"yes", "lensing":"yes"})
dmeff.set({"k_per_decade_for_pk":100, "P_k_max_h/Mpc":5})
dmeff.set({"sigma_dmeff_security":"yes"})
dmeff.compute()