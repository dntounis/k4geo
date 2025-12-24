#!/usr/bin/env python3
"""
Verify SiD_o2_v04 hit boundaries for tracker barrel and endcap.
This calculates expected hit distributions from sensitive material only.
"""

import math

# User-provided boundaries (for hits)
user_boundaries = {
    "SiTrackerBarrelHits": [
        {"r_min": 210.155, "r_max": 271.355, "z_abs_min": 0.0, "z_abs_max": 577.128},
        {"r_min": 460.155, "r_max": 521.355, "z_abs_min": 0.0, "z_abs_max": 751.359325605901},
        {"r_min": 710.155, "r_max": 771.355, "z_abs_min": 0.0, "z_abs_max": 1014.7945205479452},
        {"r_min": 960.155, "r_max": 1021.355, "z_abs_min": 0.0, "z_abs_max": 1278.2297154899895},
        {"r_min": 1210.155, "r_max": 1271.355, "z_abs_min": 0.0, "z_abs_max": 1541.497},
    ],
}

# From XML analysis
def verify_tracker_barrel_hits():
    """
    Verify tracker barrel boundaries accounting for module tilt and sensitive material.

    Key geometry from SiTrackerBarrel_o2_v04.xml:
    - Modules are tilted (phi_tilt) which spreads hits radially
    - Sensitive silicon is offset from module center
    - Module width = 97.97mm
    """
    print("=" * 80)
    print("SiTrackerBarrel Hit Boundary Verification")
    print("=" * 80)
    print("\nCalculating expected hit distributions from tilted modules...")

    # Layer parameters from XML
    layers = [
        {
            "id": 1,
            "rc": 221.355,  # mm (with rc_dr)
            "rc_base": 216.355,  # mm (without rc_dr, for envelope calc)
            "phi_tilt": 0.17506,  # rad (~10 degrees)
            "z0": 512.128,
            "module_width": 97.97,  # mm
            "module_length": 97.97,  # mm
            "sensitive_offset": 1.145,  # mm (z position in module)
            "sensitive_thickness": 0.3,  # mm
        },
        {
            "id": 2,
            "rc": 471.355,
            "rc_base": 466.355,
            "phi_tilt": 0.12217,  # rad (~7 degrees)
            "z0": 686.3593,
            "module_width": 97.97,
            "module_length": 97.97,
            "sensitive_offset": 1.145,
            "sensitive_thickness": 0.3,
        },
        {
            "id": 3,
            "rc": 721.355,
            "rc_base": 716.355,
            "phi_tilt": 0.11493,  # rad (~6.6 degrees)
            "z0": 949.7945,
            "module_width": 97.97,
            "module_length": 97.97,
            "sensitive_offset": 1.145,
            "sensitive_thickness": 0.3,
        },
        {
            "id": 4,
            "rc": 971.355,
            "rc_base": 966.355,
            "phi_tilt": 0.11502,  # rad (~6.6 degrees)
            "z0": 1213.2297,
            "module_width": 97.97,
            "module_length": 97.97,
            "sensitive_offset": 1.145,
            "sensitive_thickness": 0.3,
        },
        {
            "id": 5,
            "rc": 1221.355,
            "rc_base": 1216.355,
            "phi_tilt": 0.11467,  # rad (~6.6 degrees)
            "z0": 1476.497,
            "module_width": 97.97,
            "module_length": 97.97,
            "sensitive_offset": 1.145,
            "sensitive_thickness": 0.3,
        },
    ]

    issues = []

    for layer in layers:
        layer_id = layer["id"]
        rc = layer["rc"]
        phi_tilt = layer["phi_tilt"]
        module_width = layer["module_width"]
        sensitive_offset = layer["sensitive_offset"]
        sensitive_thickness = layer["sensitive_thickness"]
        z0 = layer["z0"]

        print(f"\n{'─' * 80}")
        print(f"Layer {layer_id}:")
        print(f"  rc = {rc:.3f} mm, phi_tilt = {math.degrees(phi_tilt):.2f}°")

        # Calculate radial extent of hits due to module tilt
        # When a module is tilted, its width in phi creates a radial spread
        # Approximate radial spread: module_width * sin(phi_tilt)
        radial_spread_from_tilt = module_width * math.sin(phi_tilt)

        # Sensitive silicon center is at rc + offset
        sensitive_center = rc + sensitive_offset

        # Radial extent of sensitive material
        sensitive_half_thickness = sensitive_thickness / 2.0

        # Total radial range considering tilt
        # The tilted module sweeps a range in radius
        # Conservative estimate: center ± (half spread from tilt + half thickness)
        r_spread_half = radial_spread_from_tilt / 2.0

        calc_r_min = sensitive_center - r_spread_half - sensitive_half_thickness
        calc_r_max = sensitive_center + r_spread_half + sensitive_half_thickness

        # Add small margin for safety (~2-3mm for edge effects, overlap, tolerances)
        margin_r = 3.0  # mm
        calc_r_min -= margin_r
        calc_r_max += margin_r

        # Z extent: modules extend ±module_length/2 from z0, plus margin
        margin_z = 5.0  # mm
        calc_z_max = z0 + module_width/2.0 + margin_z

        print(f"\n  Hit distribution calculation:")
        print(f"    Sensitive center: rc + {sensitive_offset:.3f} = {sensitive_center:.3f} mm")
        print(f"    Radial spread from tilt: {module_width:.2f} * sin({math.degrees(phi_tilt):.2f}°) = {radial_spread_from_tilt:.2f} mm")
        print(f"    Sensitive thickness: {sensitive_thickness:.1f} mm")
        print(f"    Safety margin: ±{margin_r:.1f} mm")
        print(f"  → Calculated r_min: {calc_r_min:.3f} mm")
        print(f"  → Calculated r_max: {calc_r_max:.3f} mm")
        print(f"  → Calculated z_abs_max: {calc_z_max:.3f} mm")
        print(f"  → Total radial width: {calc_r_max - calc_r_min:.1f} mm")

        # Compare with user boundaries
        user = user_boundaries["SiTrackerBarrelHits"][layer_id - 1]
        user_width = user["r_max"] - user["r_min"]

        print(f"\n  User boundaries:")
        print(f"    r_min: {user['r_min']:.3f} mm")
        print(f"    r_max: {user['r_max']:.3f} mm")
        print(f"    z_abs_max: {user['z_abs_max']:.4f} mm")
        print(f"    Total radial width: {user_width:.1f} mm")

        # Check differences
        diff_r_min = calc_r_min - user['r_min']
        diff_r_max = calc_r_max - user['r_max']
        diff_z_max = calc_z_max - user['z_abs_max']

        print(f"\n  Differences (calculated - user):")
        print(f"    Δr_min: {diff_r_min:+.3f} mm", end="")
        if abs(diff_r_min) < 10:
            print(" ✓")
        else:
            print(f" ✗ (large difference)")
            issues.append(f"Layer {layer_id} r_min: calc {calc_r_min:.3f} vs user {user['r_min']:.3f}, diff {diff_r_min:.3f} mm")

        print(f"    Δr_max: {diff_r_max:+.3f} mm", end="")
        if abs(diff_r_max) < 10:
            print(" ✓")
        else:
            print(f" ✗ (large difference)")
            issues.append(f"Layer {layer_id} r_max: calc {calc_r_max:.3f} vs user {user['r_max']:.3f}, diff {diff_r_max:.3f} mm")

        print(f"    Δz_abs_max: {diff_z_max:+.3f} mm", end="")
        if abs(diff_z_max) < 10:
            print(" ✓")
        else:
            print(f" ✗ (large difference)")
            issues.append(f"Layer {layer_id} z_abs_max: calc {calc_z_max:.3f} vs user {user['z_abs_max']:.3f}, diff {diff_z_max:.3f} mm")

        # Analysis
        print(f"\n  Analysis:")
        if abs(diff_r_min) < 5 and abs(diff_r_max) < 5:
            print(f"    ✓ Boundaries are reasonable for hit filtering")
        else:
            print(f"    ⚠ Boundaries may not accurately represent hit distribution")
            print(f"    → Expected radial width: ~{calc_r_max - calc_r_min:.1f} mm (from tilt)")
            print(f"    → User radial width: {user_width:.1f} mm")
            if user_width > (calc_r_max - calc_r_min) * 2:
                print(f"    ✗ User boundaries are MUCH wider than expected hit distribution")
            elif user_width < (calc_r_max - calc_r_min) * 0.5:
                print(f"    ✗ User boundaries are MUCH narrower than expected hit distribution")

    return issues

def main():
    print("\nVerifying Hit Boundaries for SiD_o2_v04 Tracker")
    print("Focus: SiTrackerBarrel and SiTrackerEndcap")
    print("Purpose: Hit filtering/analysis (sensitive material only)")
    print("=" * 80)

    all_issues = []

    # Verify tracker barrel
    all_issues.extend(verify_tracker_barrel_hits())

    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)

    if all_issues:
        print(f"\nFound {len(all_issues)} potential issue(s):\n")
        for issue in all_issues:
            print(f"  ⚠ {issue}")
        print(f"\nNote: User boundaries appear to be based on barrel_envelope,")
        print(f"      not actual hit distributions from tilted modules.")
        print(f"\nExpected hit width: ~15-25mm (depending on tilt angle)")
        print(f"User boundary width: ~60mm (all layers)")
    else:
        print("\n✓ Boundaries match expected hit distributions!")

    return len(all_issues)

if __name__ == "__main__":
    exit(main())
