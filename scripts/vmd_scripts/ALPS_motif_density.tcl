# VMD for MACOSXX86, version 1.9.1 (February 1, 2012)
# Log file '/Users/etjioe/Nup84_figures/vmd_density.tcl', created by user etjioe
# VMD for MACOSXX86, version 1.9.1 (February 1, 2012)
# end of log file.
volmap density [atomselect top "name CA and resid 252 to 270 and chain D"] -res 3.0 -radscale 3.0 -weight mass -allframes -combine avg -o Nup133_252-270.dx
volmap density [atomselect top "name CA and resid 135 to 152 and chain C"] -res 3.0 -radscale 3.0 -weight mass -allframes -combine avg -o Nup120_135-152.dx
volmap density [atomselect top "name CA and resid 197 to 216 and chain C"] -res 3.0 -radscale 3.0 -weight mass -allframes -combine avg -o Nup120_197-216.dx
quit
