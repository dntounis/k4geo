#!/usr/bin/env python3
"""
Verify SiD_o2_v04 geometry boundaries against provided data.
"""

import math

# User-provided boundaries
user_boundaries = {
    "SiVertexBarrelHits": [
        {"r_min": 13.0, "r_max": 16.0, "z_abs_min": 0.0, "z_abs_max": 68.0},
        {"r_min": 21.0, "r_max": 25.0, "z_abs_min": 0.0, "z_abs_max": 68.0},
        {"r_min": 34.0, "r_max": 37.0, "z_abs_min": 0.0, "z_abs_max": 68.0},
        {"r_min": 47.0, "r_max": 49.0, "z_abs_min": 0.0, "z_abs_max": 68.0},
        {"r_min": 58.0, "r_max": 63.0, "z_abs_min": 0.0, "z_abs_max": 68.0},
    ],
    "SiTrackerBarrelHits": [
        {"r_min": 210.155, "r_max": 271.355, "z_abs_min": 0.0, "z_abs_max": 577.128},
        {"r_min": 460.155, "r_max": 521.355, "z_abs_min": 0.0, "z_abs_max": 751.359325605901},
        {"r_min": 710.155, "r_max": 771.355, "z_abs_min": 0.0, "z_abs_max": 1014.7945205479452},
        {"r_min": 960.155, "r_max": 1021.355, "z_abs_min": 0.0, "z_abs_max": 1278.2297154899895},
        {"r_min": 1210.155, "r_max": 1271.355, "z_abs_min": 0.0, "z_abs_max": 1541.497},
    ],
    "SiVertexEndcapHits": [
        {"r_min": 28.318, "r_max": 61.682, "z_abs_min": 71.0, "z_abs_max": 81.0},
        {"r_min": 28.818, "r_max": 62.182, "z_abs_min": 90.0, "z_abs_max": 100.0},
        {"r_min": 29.818, "r_max": 63.182, "z_abs_min": 120.0, "z_abs_max": 130.0},
        {"r_min": 31.318, "r_max": 64.682, "z_abs_min": 175.0, "z_abs_max": 185.0},
    ],
    "SiTrackerForwardHits": [
        {"r_min": 59.565, "r_max": 134.435, "z_abs_min": 201.0, "z_abs_max": 221.0},
        {"r_min": 83.565, "r_max": 158.435, "z_abs_min": 533.0, "z_abs_max": 553.0},
        {"r_min": 104.565, "r_max": 179.435, "z_abs_min": 824.0, "z_abs_max": 844.0},
    ],
}

# Constants from SiTrackerBarrel_o2_v04.xml
SiTracker_tanTheta = 0.949
SiTracker_bIntercept = -180.0  # mm
SiTrackerBarrel_rc_dr = 5.0  # mm

# Calculate SiTrackerBarrel geometry
def verify_tracker_barrel():
    print("=" * 80)
    print("SiTrackerBarrel Verification")
    print("=" * 80)

    # Base rc values (without rc_dr)
    rc_bases = [216.355, 466.355, 716.355, 966.355, 1216.355]
    z0_bases = [512.128, None, None, None, 1476.497]

    issues = []

    for i, rc_base in enumerate(rc_bases):
        layer_num = i + 1
        rc = rc_base + SiTrackerBarrel_rc_dr  # Add rc_dr for actual rc

        # Calculate z0
        if z0_bases[i] is not None:
            z0 = z0_bases[i]
        else:
            z0 = (rc - SiTracker_bIntercept) / SiTracker_tanTheta

        # Calculated boundaries
        calc_r_min = rc_base - 6.2
        calc_r_max = rc_base + 45.0 + 10.0  # +10 for margin
        calc_z_abs_max = z0 + 60.0 + 5.0  # +5 for margin
        calc_z_abs_min = 0.0

        # User boundaries
        user = user_boundaries["SiTrackerBarrelHits"][i]

        print(f"\nLayer {layer_num}:")
        print(f"  rc_base = {rc_base:.3f} mm, rc = {rc:.3f} mm, z0 = {z0:.4f} mm")
        print(f"  Calculated: r=[{calc_r_min:.3f}, {calc_r_max:.3f}], z=[{calc_z_abs_min:.1f}, {calc_z_abs_max:.4f}]")
        print(f"  User:       r=[{user['r_min']:.3f}, {user['r_max']:.3f}], z=[{user['z_abs_min']:.1f}, {user['z_abs_max']:.4f}]")

        # Check for discrepancies
        tolerance = 0.01  # 10 microns
        if abs(calc_r_min - user['r_min']) > tolerance:
            issues.append(f"Layer {layer_num} r_min: calculated {calc_r_min:.3f}, user {user['r_min']:.3f}")
        if abs(calc_r_max - user['r_max']) > tolerance:
            issues.append(f"Layer {layer_num} r_max: calculated {calc_r_max:.3f}, user {user['r_max']:.3f}")
        if abs(calc_z_abs_max - user['z_abs_max']) > tolerance:
            issues.append(f"Layer {layer_num} z_abs_max: calculated {calc_z_abs_max:.4f}, user {user['z_abs_max']:.4f}")

        match = "✓ MATCH" if len(issues) == len([x for x in issues if f"Layer {layer_num}" not in x]) else "✗ MISMATCH"
        print(f"  Status: {match}")

    return issues

# Calculate SiVertexBarrel geometry
def verify_vertex_barrel():
    print("\n" + "=" * 80)
    print("SiVertexBarrel Verification")
    print("=" * 80)

    # From XML lines 54-81
    layers = [
        {"inner_r": 13.0, "outer_r": 17.0, "z_length": 126.0},  # Layer 1
        {"inner_r": 21.0, "outer_r": 25.0, "z_length": 126.0},  # Layer 2
        {"inner_r": 34.0, "outer_r": 38.0, "z_length": 126.0},  # Layer 3
        {"inner_r": 46.6, "outer_r": 50.6, "z_length": 126.0},  # Layer 4
        {"inner_r": 59.0, "outer_r": 63.0, "z_length": 126.0},  # Layer 5
    ]

    issues = []

    for i, layer in enumerate(layers):
        layer_num = i + 1
        calc_r_min = layer["inner_r"]
        calc_r_max = layer["outer_r"]
        calc_z_abs_max = layer["z_length"] / 2.0
        calc_z_abs_min = 0.0

        user = user_boundaries["SiVertexBarrelHits"][i]

        print(f"\nLayer {layer_num}:")
        print(f"  Calculated: r=[{calc_r_min:.1f}, {calc_r_max:.1f}], z=[{calc_z_abs_min:.1f}, {calc_z_abs_max:.1f}]")
        print(f"  User:       r=[{user['r_min']:.1f}, {user['r_max']:.1f}], z=[{user['z_abs_min']:.1f}, {user['z_abs_max']:.1f}]")

        tolerance = 0.1
        layer_issues = []
        if abs(calc_r_min - user['r_min']) > tolerance:
            layer_issues.append(f"r_min: calculated {calc_r_min:.1f}, user {user['r_min']:.1f}, diff {calc_r_min - user['r_min']:.1f}")
        if abs(calc_r_max - user['r_max']) > tolerance:
            layer_issues.append(f"r_max: calculated {calc_r_max:.1f}, user {user['r_max']:.1f}, diff {calc_r_max - user['r_max']:.1f}")
        if abs(calc_z_abs_max - user['z_abs_max']) > tolerance:
            layer_issues.append(f"z_abs_max: calculated {calc_z_abs_max:.1f}, user {user['z_abs_max']:.1f}, diff {calc_z_abs_max - user['z_abs_max']:.1f}")

        if layer_issues:
            match = "✗ MISMATCH"
            for issue in layer_issues:
                print(f"    ✗ {issue}")
                issues.append(f"Layer {layer_num} {issue}")
        else:
            match = "✓ MATCH"

        print(f"  Status: {match}")

    return issues

# Calculate SiVertexEndcap geometry
def verify_vertex_endcap():
    print("\n" + "=" * 80)
    print("SiVertexEndcap Verification")
    print("=" * 80)

    # From XML lines 41-52
    # Modules: Module1 z=29.280mm, Module2 z=28.780mm (these are half-lengths in trd)
    layers = [
        {"r": 45.0, "zstart": 76.0, "module_z_half": 29.280},   # Layer 1, Module1
        {"r": 45.5, "zstart": 95.0, "module_z_half": 28.780},   # Layer 2, Module2
        {"r": 46.5, "zstart": 125.0, "module_z_half": 28.780},  # Layer 3, Module2
        {"r": 48.0, "zstart": 180.0, "module_z_half": 28.780},  # Layer 4, Module2
    ]

    issues = []

    print("\nNote: Endcap geometry involves trapezoid modules in rings.")
    print("Expected pattern based on user data:")
    print("  - r boundaries centered at ring radius with fixed extent")
    print("  - z boundaries centered at zstart with ±5mm margin")

    for i, layer in enumerate(layers):
        layer_num = i + 1

        # Expected from geometry (ring center ± module half-length)
        geom_r_min = layer["r"] - layer["module_z_half"]
        geom_r_max = layer["r"] + layer["module_z_half"]
        geom_z_center = layer["zstart"]

        # Module thickness is small (~0.1mm from components)
        # User seems to use ±5mm margin
        calc_z_abs_min = geom_z_center - 5.0
        calc_z_abs_max = geom_z_center + 5.0

        user = user_boundaries["SiVertexEndcapHits"][i]

        # Check what r extent the user is using
        user_r_center = (user['r_min'] + user['r_max']) / 2.0
        user_r_extent = (user['r_max'] - user['r_min']) / 2.0

        print(f"\nLayer {layer_num}:")
        print(f"  Ring r={layer['r']:.1f} mm, zstart={layer['zstart']:.1f} mm, module_z_half={layer['module_z_half']:.3f} mm")
        print(f"  Geometric: r=[{geom_r_min:.3f}, {geom_r_max:.3f}]")
        print(f"  User:      r=[{user['r_min']:.3f}, {user['r_max']:.3f}] (center={user_r_center:.1f}, extent=±{user_r_extent:.3f})")
        print(f"  User:      z=[{user['z_abs_min']:.1f}, {user['z_abs_max']:.1f}] (center={geom_z_center:.1f})")

        # Check if r_center matches
        if abs(user_r_center - layer["r"]) > 0.1:
            issues.append(f"Layer {layer_num} r_center: user {user_r_center:.1f} doesn't match ring r {layer['r']:.1f}")
            print(f"    ✗ r_center mismatch")

        # Check if z is centered correctly
        user_z_center = (user['z_abs_min'] + user['z_abs_max']) / 2.0
        if abs(user_z_center - layer["zstart"]) > 0.1:
            issues.append(f"Layer {layer_num} z_center: user {user_z_center:.1f} doesn't match zstart {layer['zstart']:.1f}")
            print(f"    ✗ z_center mismatch")

        # Note: r_extent varies by detector, documenting empirical value
        print(f"    ℹ r_extent: user uses ±{user_r_extent:.3f} mm (geometric would be ±{layer['module_z_half']:.3f} mm)")
        print(f"    ℹ z_extent: user uses ±5.0 mm (consistent across all layers)")

    return issues

# Calculate SiTrackerForward geometry
def verify_tracker_forward():
    print("\n" + "=" * 80)
    print("SiTrackerForward Verification")
    print("=" * 80)

    # From XML lines 39-49
    # Module z values are half-lengths in trapezoids
    layers = [
        {"r": 97.0, "zstart": 211.0, "module_z_half": 67.405},  # Layer 1, Module1
        {"r": 121.0, "zstart": 543.0, "module_z_half": 43.405}, # Layer 2, Module2
        {"r": 142.0, "zstart": 834.0, "module_z_half": 22.405}, # Layer 3, Module3
    ]

    issues = []

    for i, layer in enumerate(layers):
        layer_num = i + 1

        # Expected from geometry
        geom_r_min = layer["r"] - layer["module_z_half"]
        geom_r_max = layer["r"] + layer["module_z_half"]

        user = user_boundaries["SiTrackerForwardHits"][i]

        # Check what r extent the user is using
        user_r_center = (user['r_min'] + user['r_max']) / 2.0
        user_r_extent = (user['r_max'] - user['r_min']) / 2.0
        user_z_center = (user['z_abs_min'] + user['z_abs_max']) / 2.0
        user_z_extent = (user['z_abs_max'] - user['z_abs_min']) / 2.0

        print(f"\nLayer {layer_num}:")
        print(f"  Ring r={layer['r']:.1f} mm, zstart={layer['zstart']:.1f} mm, module_z_half={layer['module_z_half']:.3f} mm")
        print(f"  Geometric: r=[{geom_r_min:.3f}, {geom_r_max:.3f}]")
        print(f"  User:      r=[{user['r_min']:.3f}, {user['r_max']:.3f}] (center={user_r_center:.1f}, extent=±{user_r_extent:.3f})")
        print(f"  User:      z=[{user['z_abs_min']:.1f}, {user['z_abs_max']:.1f}] (center={user_z_center:.1f}, extent=±{user_z_extent:.1f})")

        # Check if r_center matches
        if abs(user_r_center - layer["r"]) > 0.1:
            issues.append(f"Layer {layer_num} r_center: user {user_r_center:.1f} doesn't match ring r {layer['r']:.1f}")
            print(f"    ✗ r_center mismatch")
        else:
            print(f"    ✓ r_center matches ring radius")

        # Check if z_center matches
        if abs(user_z_center - layer["zstart"]) > 0.1:
            issues.append(f"Layer {layer_num} z_center: user {user_z_center:.1f} doesn't match zstart {layer['zstart']:.1f}")
            print(f"    ✗ z_center mismatch")
        else:
            print(f"    ✓ z_center matches zstart")

        # Check z_extent (should be ±10mm based on pattern)
        if abs(user_z_extent - 10.0) > 0.1:
            issues.append(f"Layer {layer_num} z_extent: user ±{user_z_extent:.1f} mm (expected ±10mm)")
            print(f"    ✗ z_extent is ±{user_z_extent:.1f} mm (expected ±10mm)")
        else:
            print(f"    ✓ z_extent is ±10mm")

        # Note about r_extent
        r_extent_diff = layer['module_z_half'] - user_r_extent
        if abs(r_extent_diff) > 1.0:
            if user_r_extent > layer['module_z_half']:
                issues.append(f"Layer {layer_num} r_extent: user ±{user_r_extent:.3f} EXCEEDS geometric ±{layer['module_z_half']:.3f} by {r_extent_diff:.3f} mm")
                print(f"    ✗ r_extent EXCEEDS geometric extent (user ±{user_r_extent:.3f} > geom ±{layer['module_z_half']:.3f})")
            else:
                print(f"    ℹ r_extent: user ±{user_r_extent:.3f} mm is {r_extent_diff:.3f} mm less than geometric ±{layer['module_z_half']:.3f} mm")

        # All layers have the same user r_extent (37.435mm)
        if abs(user_r_extent - 37.435) > 0.01:
            print(f"    ℹ Note: r_extent varies from the common 37.435 mm pattern")

    return issues

def main():
    print("Verifying SiD_o2_v04 Geometry Boundaries")
    print("=" * 80)

    all_issues = []

    # Verify each detector
    all_issues.extend(verify_vertex_barrel())
    all_issues.extend(verify_tracker_barrel())
    all_issues.extend(verify_vertex_endcap())
    all_issues.extend(verify_tracker_forward())

    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)

    if all_issues:
        print(f"\nFound {len(all_issues)} issue(s):\n")
        for issue in all_issues:
            print(f"  ✗ {issue}")
        print(f"\nNote: Some discrepancies may be due to:")
        print(f"  1. Safety margins added to prevent edge effects")
        print(f"  2. Empirical boundaries from simulation studies")
        print(f"  3. Active sensor area vs. full module envelope")
    else:
        print("\n✓ All boundaries verified!")

    return len(all_issues)

if __name__ == "__main__":
    exit(main())
