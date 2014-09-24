# VMD for MACOSXX86, version 1.9.1 (February 1, 2012)
# Log file '/Users/etjioe/Nup84_figures/vmd_density.tcl', created by user etjioe
# VMD for MACOSXX86, version 1.9.1 (February 1, 2012)
# end of log file.
volmap density [atomselect top "name CA and chain A"] -res 4.0 -radscale 3.0 -weight mass -allframes -combine avg -o 3-xray_Nup84.dx
volmap density [atomselect top "name CA and chain B"] -res 4.0 -radscale 3.0 -weight mass -allframes -combine avg -o 3-xray_Nup85.dx
volmap density [atomselect top "name CA and chain C"] -res 4.0 -radscale 3.0 -weight mass -allframes -combine avg -o 3-xray_Nup120.dx
volmap density [atomselect top "name CA and resid 713 to 1037 and chain C"] -res 4.0 -radscale 3.0 -weight mass -allframes -combine avg -o 3-xray_Nup120-CTD.dx
volmap density [atomselect top "name CA and chain D"] -res 4.0 -radscale 3.0 -weight mass -allframes -combine avg -o 3-xray_Nup133.dx
volmap density [atomselect top "name CA and resid 1 to 125 and chain E"] -res 6.0 -radscale 3.0 -weight mass -allframes -combine avg -o 3-xray_Nup145c-NTD.dx
volmap density [atomselect top "name CA and resid 126 to 553 and chain E"] -res 4.0 -radscale 3.0 -weight mass -allframes -combine avg -o 3-xray_Nup145c-middle.dx
volmap density [atomselect top "name CA and resid 554 to 712 and chain E"] -res 6.0 -radscale 3.0 -weight mass -allframes -combine avg -o 3-xray_Nup145c-CTD.dx
volmap density [atomselect top "name CA and chain F"] -res 4.0 -radscale 3.0 -weight mass -allframes -combine avg -o 3-xray_Seh1.dx
volmap density [atomselect top "name CA and chain G"] -res 4.0 -radscale 3.0 -weight mass -allframes -combine avg -o 3-xray_Sec13.dx
volmap density [atomselect top "name CA"] -res 4.0 -radscale 3.0 -weight mass -allframes -combine avg -o 3-xray_Nup84_complex.dx
quit
