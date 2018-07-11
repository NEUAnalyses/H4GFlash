


#cuts['t4gamma'] = 'tp_mass > 100 && tp_mass < 180 && dp1_mass/tp_mass < 0.55   \
               #&& dp2_mass/tp_mass < 0.50 \
               #'



#cuts['t4gamma-supercut'] = 'tp_mass > 100 && tp_mass < 180 && dp1_mass/tp_mass < 0.55    \
                             # && dp2_mass/tp_mass < 0.50 \
               #&& dp2_mass/tp_mass > 0.01 \
               #'
              
cuts['for4Gamma'] = 'tp_mass > 100 && tp_mass < 180  && dp1_mass/tp_mass < 0.55 \
                     && dp1_mass/tp_mass > 0.05 && dp2_mass/tp_mass < 0.55 \
                     && dp2_mass/tp_mass > 0.05 \
                     && (dp1_mass-dp2_mass)/tp_mass < 0.25 \
                     && tp_pt/tp_mass < 1.5 \
                     '
                     


