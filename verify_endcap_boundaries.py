#!/usr/bin/env python3
"""
Generate corrected boundaries for SiTrackerEndcap based on hit distributions.
For endcap detectors, modules are trapezoids placed in rings.
"""

import math

# User-provided boundaries for SiTrackerEndcap
user_boundaries = [
    {"r_min": 205.081, "r_max": 308.351, "z_abs_min": 778.855, "z_abs_max": 798.855},
    {"r_min": 302.356, "r_max": 405.626, "z_abs_min": 770.526, "z_abs_max": 790.526},
    {"r_min": 397.545, "r_max": 500.815, "z_abs_min": 762.294, "z_abs_max": 782.294},
    {"r_min": 205.081, "r_max": 308.351, "z_abs_min": 1065.043, "z_abs_max": 1085.043},
    {"r_min": 302.356, "r_max": 405.626, "z_abs_min": 1056.716, "z_abs_max": 1076.716},
    {"r_min": 397.545, "r_max": 500.815, "z_abs_min": 1048.484, "z_abs_max": 1068.484},
    {"r_min": 478.84, "r_max": 598.2, "z_abs_min": 1040.216, "z_abs_max": 1060.216},
    {"r_min": 565.974, "r_max": 685.334, "z_abs_min": 1032.817, "z_abs_max": 1052.817},
    {"r_min": 643.986, "r_max": 763.346, "z_abs_min": 1025.475, "z_abs_max": 1045.475},
    {"r_min": 205.081, "r_max": 308.351, "z_abs_min": 1345.536, "z_abs_max": 1365.536},
    {"r_min": 302.356, "r_max": 405.626, "z_abs_min": 1337.207, "z_abs_max": 1357.207},
    {"r_min": 397.545, "r_max": 500.815, "z_abs_min": 1328.975, "z_abs_max": 1348.975},
    {"r_min": 478.84, "r_max": 598.2, "z_abs_min": 1320.707, "z_abs_max": 1340.707},
    {"r_min": 565.974, "r_max": 685.334, "z_abs_min": 1313.308, "z_abs_max": 1333.308},
    {"r_min": 643.986, "r_max": 763.346, "z_abs_min": 1305.967, "z_abs_max": 1325.967},
    {"r_min": 733.768, "r_max": 853.128, "z_abs_min": 1298.578, "z_abs_max": 1318.578},
    {"r_min": 814.559, "r_max": 933.919, "z_abs_min": 1291.236, "z_abs_max": 1311.236},
    {"r_min": 898.684, "r_max": 1018.044, "z_abs_min": 1283.939, "z_abs_max": 1303.939},
    {"r_min": 205.081, "r_max": 308.351, "z_abs_min": 1630.914, "z_abs_max": 1650.914},
    {"r_min": 302.356, "r_max": 405.626, "z_abs_min": 1622.585, "z_abs_max": 1642.585},
    {"r_min": 397.545, "r_max": 500.815, "z_abs_min": 1614.353, "z_abs_max": 1634.353},
    {"r_min": 478.84, "r_max": 598.2, "z_abs_min": 1606.085, "z_abs_max": 1626.085},
    {"r_min": 565.974, "r_max": 685.334, "z_abs_min": 1598.686, "z_abs_max": 1618.686},
    {"r_min": 643.986, "r_max": 763.346, "z_abs_min": 1591.345, "z_abs_max": 1611.345},
    {"r_min": 733.768, "r_max": 853.128, "z_abs_min": 1583.956, "z_abs_max": 1603.956},
    {"r_min": 814.559, "r_max": 933.919, "z_abs_min": 1576.614, "z_abs_max": 1596.614},
    {"r_min": 898.684, "r_max": 1018.044, "z_abs_min": 1569.317, "z_abs_max": 1589.317},
    {"r_min": 981.29, "r_max": 1100.65, "z_abs_min": 1561.972, "z_abs_max": 1581.972},
    {"r_min": 1064.487, "r_max": 1183.847, "z_abs_min": 1554.666, "z_abs_max": 1574.666},
    {"r_min": 1147.257, "r_max": 1266.617, "z_abs_min": 1547.397, "z_abs_max": 1567.397},
]

# Ring definitions from XML
rings = [
    # Layer 1 (3 rings)
    {"layer": 1, "ring": 1, "r": 256.716, "zstart": 788.855, "module": "Module1", "z_half": 50.057},
    {"layer": 1, "ring": 2, "r": 353.991, "zstart": 780.526, "module": "Module1", "z_half": 50.057},
    {"layer": 1, "ring": 3, "r": 449.180, "zstart": 772.294, "module": "Module1", "z_half": 50.057},

    # Layer 2 (6 rings)
    {"layer": 2, "ring": 1, "r": 256.716, "zstart": 1075.043, "module": "Module1", "z_half": 50.057},
    {"layer": 2, "ring": 2, "r": 353.991, "zstart": 1066.716, "module": "Module1", "z_half": 50.057},
    {"layer": 2, "ring": 3, "r": 449.180, "zstart": 1058.484, "module": "Module1", "z_half": 50.057},
    {"layer": 2, "ring": 4, "r": 538.520, "zstart": 1050.216, "module": "Module2", "z_half": 44.8865},
    {"layer": 2, "ring": 5, "r": 625.654, "zstart": 1042.817, "module": "Module2", "z_half": 44.8865},
    {"layer": 2, "ring": 6, "r": 703.666, "zstart": 1035.475, "module": "Module2", "z_half": 44.8865},

    # Layer 3 (9 rings)
    {"layer": 3, "ring": 1, "r": 256.716, "zstart": 1355.536, "module": "Module1", "z_half": 50.057},
    {"layer": 3, "ring": 2, "r": 353.991, "zstart": 1347.207, "module": "Module1", "z_half": 50.057},
    {"layer": 3, "ring": 3, "r": 449.180, "zstart": 1338.975, "module": "Module1", "z_half": 50.057},
    {"layer": 3, "ring": 4, "r": 538.520, "zstart": 1330.707, "module": "Module2", "z_half": 44.8865},
    {"layer": 3, "ring": 5, "r": 625.654, "zstart": 1323.308, "module": "Module2", "z_half": 44.8865},
    {"layer": 3, "ring": 6, "r": 703.666, "zstart": 1315.967, "module": "Module2", "z_half": 44.8865},
    {"layer": 3, "ring": 7, "r": 793.448, "zstart": 1308.578, "module": "Module2", "z_half": 44.8865},
    {"layer": 3, "ring": 8, "r": 874.239, "zstart": 1301.236, "module": "Module2", "z_half": 44.8865},
    {"layer": 3, "ring": 9, "r": 958.364, "zstart": 1293.939, "module": "Module2", "z_half": 44.8865},

    # Layer 4 (12 rings)
    {"layer": 4, "ring": 1, "r": 256.716, "zstart": 1640.914, "module": "Module1", "z_half": 50.057},
    {"layer": 4, "ring": 2, "r": 353.991, "zstart": 1632.585, "module": "Module1", "z_half": 50.057},
    {"layer": 4, "ring": 3, "r": 449.180, "zstart": 1624.353, "module": "Module1", "z_half": 50.057},
    {"layer": 4, "ring": 4, "r": 538.520, "zstart": 1616.085, "module": "Module2", "z_half": 44.8865},
    {"layer": 4, "ring": 5, "r": 625.654, "zstart": 1608.686, "module": "Module2", "z_half": 44.8865},
    {"layer": 4, "ring": 6, "r": 703.666, "zstart": 1601.345, "module": "Module2", "z_half": 44.8865},
    {"layer": 4, "ring": 7, "r": 793.448, "zstart": 1593.956, "module": "Module2", "z_half": 44.8865},
    {"layer": 4, "ring": 8, "r": 874.239, "zstart": 1586.614, "module": "Module2", "z_half": 44.8865},
    {"layer": 4, "ring": 9, "r": 958.364, "zstart": 1579.317, "module": "Module2", "z_half": 44.8865},
    {"layer": 4, "ring": 10, "r": 1040.970, "zstart": 1571.972, "module": "Module2", "z_half": 44.8865},
    {"layer": 4, "ring": 11, "r": 1124.167, "zstart": 1564.666, "module": "Module2", "z_half": 44.8865},
    {"layer": 4, "ring": 12, "r": 1147.257, "zstart": 1557.397, "module": "Module2", "z_half": 44.8865},
]

def calculate_endcap_boundaries():
    """
    Calculate hit boundaries for SiTrackerEndcap.

    For endcap disks:
    - Modules are trapezoids extending radially from ring radius r
    - Sensitive material is 0.3mm thick in z direction
    - Module radial extent: r ± z_half
    """

    print("=" * 80)
    print("SiTrackerEndcap Hit Boundary Calculation")
    print("=" * 80)
    print("\nCalculating boundaries from sensitive material in trapezoid modules...")

    corrected_boundaries = []
    issues = []

    # Module parameters
    sensitive_thickness_z = 0.3  # mm (same as barrel)
    margin_r = 3.0  # mm safety margin in radial direction
    margin_z = 2.0  # mm safety margin in z direction

    for i, ring in enumerate(rings):
        layer = ring["layer"]
        ring_num = ring["ring"]
        r = ring["r"]
        zstart = ring["zstart"]
        z_half = ring["z_half"]
        module = ring["module"]

        # Calculate radial extent of sensitive material
        # Trapezoid extends from r - z_half to r + z_half
        calc_r_min = r - z_half - margin_r
        calc_r_max = r + z_half + margin_r

        # Calculate z extent
        # Sensitive silicon is 0.3mm thick, centered at zstart
        calc_z_min = zstart - sensitive_thickness_z/2.0 - margin_z
        calc_z_max = zstart + sensitive_thickness_z/2.0 + margin_z

        # User boundary
        user = user_boundaries[i]

        # Calculate differences
        diff_r_min = calc_r_min - user['r_min']
        diff_r_max = calc_r_max - user['r_max']
        diff_z_min = calc_z_min - user['z_abs_min']
        diff_z_max = calc_z_max - user['z_abs_max']

        # Store corrected boundary
        corrected = {
            "r_min": round(calc_r_min, 3),
            "r_max": round(calc_r_max, 3),
            "z_abs_min": round(calc_z_min, 3),
            "z_abs_max": round(calc_z_max, 3),
        }
        corrected_boundaries.append(corrected)

        # Print details every few rings
        if ring_num == 1:
            print(f"\n{'─' * 80}")
            print(f"Layer {layer}:")

        print(f"\n  Ring {ring_num}: r={r:.3f} mm, z={zstart:.3f} mm, {module} (z_half={z_half:.3f} mm)")
        print(f"    Calculated: r=[{calc_r_min:.3f}, {calc_r_max:.3f}], z=[{calc_z_min:.3f}, {calc_z_max:.3f}]")
        print(f"    User:       r=[{user['r_min']:.3f}, {user['r_max']:.3f}], z=[{user['z_abs_min']:.3f}, {user['z_abs_max']:.3f}]")
        print(f"    Δr: [{diff_r_min:+.3f}, {diff_r_max:+.3f}] mm, Δz: [{diff_z_min:+.3f}, {diff_z_max:+.3f}] mm", end="")

        # Check if significant differences
        if abs(diff_r_min) > 5 or abs(diff_r_max) > 5:
            print(" ✗ RADIAL MISMATCH")
            issues.append(f"Layer {layer} Ring {ring_num}: radial boundaries off by {abs(diff_r_min):.1f}-{abs(diff_r_max):.1f} mm")
        elif abs(diff_z_min) > 5 or abs(diff_z_max) > 5:
            print(" ⚠ Z MISMATCH")
            issues.append(f"Layer {layer} Ring {ring_num}: z boundaries off by {abs(diff_z_min):.1f}-{abs(diff_z_max):.1f} mm")
        else:
            print(" ✓")

    return corrected_boundaries, issues

def print_corrected_boundaries(boundaries):
    """Print corrected boundaries in Python format."""
    print("\n" + "=" * 80)
    print("CORRECTED BOUNDARIES FOR SiTrackerEndcapHits")
    print("=" * 80)
    print("\n\"SiTrackerEndcapHits\": [")

    layer_breaks = [0, 3, 9, 18, 30]  # Start indices for each layer

    for i, bound in enumerate(boundaries):
        # Add layer comments
        if i in layer_breaks[:-1]:
            layer_num = layer_breaks.index(i) + 1
            if i > 0:
                print()
            print(f"    # Layer {layer_num}")

        print(f"    {{\"r_min\": {bound['r_min']:.3f}, \"r_max\": {bound['r_max']:.3f}, "
              f"\"z_abs_min\": {bound['z_abs_min']:.3f}, \"z_abs_max\": {bound['z_abs_max']:.3f}}},")

    print("]")

def main():
    print("\nVerifying and Correcting SiTrackerEndcap Boundaries")
    print("Purpose: Hit filtering (sensitive material only)")
    print("=" * 80)

    corrected, issues = calculate_endcap_boundaries()

    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)

    if issues:
        print(f"\nFound {len(issues)} issue(s):")
        for issue in issues:
            print(f"  ⚠ {issue}")
        print(f"\nUser boundaries appear to use fixed ±10mm z margin")
        print(f"but don't account for actual module radial extent.")
    else:
        print("\n✓ User boundaries are close to calculated values!")

    print_corrected_boundaries(corrected)

    return len(issues)

if __name__ == "__main__":
    exit(main())
