# Corrected Hit Boundaries for SiD_o2_v04 Tracker

## Purpose
These boundaries represent **actual hit distributions from sensitive material only**, suitable for hit filtering and analysis.

## Key Differences from Original

### SiTrackerBarrel
- **Original**: 61.2mm radial width (based on full detector envelope)
- **Corrected**: 17-23mm radial width (based on tilted module hit distribution)
- **Reduction**: ~3x narrower, matching observed ~20mm hit thickness

### SiTrackerEndcap
- **Original**: Fixed ±10mm z margin, inconsistent radial boundaries
- **Corrected**: ±2mm z margin (sensitive material), proper radial extent from trapezoid modules
- **Issues fixed**:
  - Z boundaries were 8mm too wide
  - Module2 rings had 12mm radial errors
  - Layer 4 Ring 12 had 47-71mm radial error

---

## Corrected Boundaries

### SiTrackerBarrelHits

Based on tilted module geometry with sensitive silicon at rc + 1.145mm offset:

```python
"SiTrackerBarrelHits": [
    # Layer 1: rc=221.355mm, tilt=10.03°, hit width=23.4mm
    {"r_min": 210.8, "r_max": 234.2, "z_abs_min": 0.0, "z_abs_max": 566.1},

    # Layer 2: rc=471.355mm, tilt=7.00°, hit width=18.2mm
    {"r_min": 463.4, "r_max": 481.6, "z_abs_min": 0.0, "z_abs_max": 740.3},

    # Layer 3: rc=721.355mm, tilt=6.59°, hit width=17.5mm
    {"r_min": 713.7, "r_max": 731.3, "z_abs_min": 0.0, "z_abs_max": 1003.8},

    # Layer 4: rc=971.355mm, tilt=6.59°, hit width=17.5mm
    {"r_min": 963.7, "r_max": 981.3, "z_abs_min": 0.0, "z_abs_max": 1267.2},

    # Layer 5: rc=1221.355mm, tilt=6.57°, hit width=17.5mm
    {"r_min": 1213.7, "r_max": 1231.3, "z_abs_min": 0.0, "z_abs_max": 1530.5},
]
```

**Calculation method:**
- Sensitive silicon position: `rc + 1.145mm` (offset from module center)
- Radial spread from tilt: `module_width × sin(phi_tilt) ≈ 97.97mm × sin(phi_tilt)`
- Sensitive thickness: `0.3mm`
- Safety margin: `±3mm` radial, accounts for edge effects and overlap

**Hit width breakdown:**
- Layer 1 (10° tilt): 17.1mm spread + 0.3mm sensor + 6mm margin = **23.4mm**
- Layers 2-5 (6-7° tilt): 11.2mm spread + 0.3mm sensor + 6mm margin = **17.5mm**

---

### SiTrackerEndcapHits

Based on trapezoid module radial extent with sensitive silicon:

```python
"SiTrackerEndcapHits": [
    # Layer 1 (3 rings, Module1: z_half=50.057mm)
    {"r_min": 203.659, "r_max": 309.773, "z_abs_min": 786.705, "z_abs_max": 791.005},
    {"r_min": 300.934, "r_max": 407.048, "z_abs_min": 778.376, "z_abs_max": 782.676},
    {"r_min": 396.123, "r_max": 502.237, "z_abs_min": 770.144, "z_abs_max": 774.444},

    # Layer 2 (6 rings, Module1+Module2)
    {"r_min": 203.659, "r_max": 309.773, "z_abs_min": 1072.893, "z_abs_max": 1077.193},
    {"r_min": 300.934, "r_max": 407.048, "z_abs_min": 1064.566, "z_abs_max": 1068.866},
    {"r_min": 396.123, "r_max": 502.237, "z_abs_min": 1056.334, "z_abs_max": 1060.634},
    {"r_min": 490.633, "r_max": 586.406, "z_abs_min": 1048.066, "z_abs_max": 1052.366},
    {"r_min": 577.768, "r_max": 673.540, "z_abs_min": 1040.667, "z_abs_max": 1044.967},
    {"r_min": 655.780, "r_max": 751.553, "z_abs_min": 1033.325, "z_abs_max": 1037.625},

    # Layer 3 (9 rings, Module1+Module2)
    {"r_min": 203.659, "r_max": 309.773, "z_abs_min": 1353.386, "z_abs_max": 1357.686},
    {"r_min": 300.934, "r_max": 407.048, "z_abs_min": 1345.057, "z_abs_max": 1349.357},
    {"r_min": 396.123, "r_max": 502.237, "z_abs_min": 1336.825, "z_abs_max": 1341.125},
    {"r_min": 490.633, "r_max": 586.406, "z_abs_min": 1328.557, "z_abs_max": 1332.857},
    {"r_min": 577.768, "r_max": 673.540, "z_abs_min": 1321.158, "z_abs_max": 1325.458},
    {"r_min": 655.780, "r_max": 751.553, "z_abs_min": 1313.817, "z_abs_max": 1318.117},
    {"r_min": 745.562, "r_max": 841.334, "z_abs_min": 1306.428, "z_abs_max": 1310.728},
    {"r_min": 826.353, "r_max": 922.125, "z_abs_min": 1299.086, "z_abs_max": 1303.386},
    {"r_min": 910.478, "r_max": 1006.250, "z_abs_min": 1291.789, "z_abs_max": 1296.089},

    # Layer 4 (12 rings, Module1+Module2)
    {"r_min": 203.659, "r_max": 309.773, "z_abs_min": 1638.764, "z_abs_max": 1643.064},
    {"r_min": 300.934, "r_max": 407.048, "z_abs_min": 1630.435, "z_abs_max": 1634.735},
    {"r_min": 396.123, "r_max": 502.237, "z_abs_min": 1622.203, "z_abs_max": 1626.503},
    {"r_min": 490.633, "r_max": 586.406, "z_abs_min": 1613.935, "z_abs_max": 1618.235},
    {"r_min": 577.768, "r_max": 673.540, "z_abs_min": 1606.536, "z_abs_max": 1610.836},
    {"r_min": 655.780, "r_max": 751.553, "z_abs_min": 1599.195, "z_abs_max": 1603.495},
    {"r_min": 745.562, "r_max": 841.334, "z_abs_min": 1591.806, "z_abs_max": 1596.106},
    {"r_min": 826.353, "r_max": 922.125, "z_abs_min": 1584.464, "z_abs_max": 1588.764},
    {"r_min": 910.478, "r_max": 1006.250, "z_abs_min": 1577.167, "z_abs_max": 1581.467},
    {"r_min": 993.084, "r_max": 1088.857, "z_abs_min": 1569.822, "z_abs_max": 1574.122},
    {"r_min": 1076.280, "r_max": 1172.053, "z_abs_min": 1562.516, "z_abs_max": 1566.816},
    {"r_min": 1099.370, "r_max": 1195.144, "z_abs_min": 1555.247, "z_abs_max": 1559.547},
]
```

**Calculation method:**
- Radial extent: `r ± module_z_half ± 3mm` (trapezoid extent + safety margin)
  - Module1: r ± 50.057mm ± 3mm = **106.1mm radial width**
  - Module2: r ± 44.886mm ± 3mm = **95.8mm radial width**
- Z extent: `zstart ± 0.15mm ± 2mm` (sensitive thickness + safety margin) = **4.3mm z width**

---

## Comparison with Original

### SiTrackerBarrel - All Layers TOO WIDE

| Layer | Original Width | Correct Width | Difference | Original r_max | Correct r_max | Error |
|-------|----------------|---------------|------------|----------------|---------------|-------|
| 1 | 61.2mm | 23.4mm | **-37.8mm** | 271.4mm | 234.2mm | **-37mm** |
| 2 | 61.2mm | 18.2mm | **-43.0mm** | 521.4mm | 481.6mm | **-40mm** |
| 3 | 61.2mm | 17.5mm | **-43.7mm** | 771.4mm | 731.3mm | **-40mm** |
| 4 | 61.2mm | 17.5mm | **-43.7mm** | 1021.4mm | 981.3mm | **-40mm** |
| 5 | 61.2mm | 17.5mm | **-43.7mm** | 1271.4mm | 1231.3mm | **-40mm** |

**All r_max values are 37-40mm too large!**

### SiTrackerEndcap - Z Bounds TOO WIDE, Mixed Radial Errors

**Module1 rings (slight radial errors):**
- Radial: ~1-2mm difference (acceptable)
- Z: **8mm too wide** (±10mm instead of ±2mm)

**Module2 rings (significant radial errors):**
- Radial: **12mm too wide** on each side (user used larger envelope)
- Z: **8mm too wide** (same issue)

**Layer 4 Ring 12 (critical error):**
- User r_min: 1147.257mm (SAME as ring radius!)
- Correct r_min: 1099.370mm
- **Error: Module starts 48mm too far inward, completely wrong**

---

## Implementation

### Python Dictionary Format

```python
geometry_windows = {
    "SiTrackerBarrelHits": [
        {"r_min": 210.8, "r_max": 234.2, "z_abs_min": 0.0, "z_abs_max": 566.1},
        {"r_min": 463.4, "r_max": 481.6, "z_abs_min": 0.0, "z_abs_max": 740.3},
        {"r_min": 713.7, "r_max": 731.3, "z_abs_min": 0.0, "z_abs_max": 1003.8},
        {"r_min": 963.7, "r_max": 981.3, "z_abs_min": 0.0, "z_abs_max": 1267.2},
        {"r_min": 1213.7, "r_max": 1231.3, "z_abs_min": 0.0, "z_abs_max": 1530.5},
    ],
    "SiTrackerEndcapHits": [
        # [Copy full list from above]
    ],
}
```

---

## Verification Scripts

Three verification scripts are provided:

1. **`verify_geometry.py`**: Original envelope-based verification
2. **`verify_hit_boundaries.py`**: SiTrackerBarrel hit distribution analysis
3. **`verify_endcap_boundaries.py`**: SiTrackerEndcap hit distribution analysis

Run any script to see detailed comparisons:
```bash
python3 verify_hit_boundaries.py
python3 verify_endcap_boundaries.py
```

---

## Notes

### Safety Margins Used

- **Barrel**: ±3mm radial (accounts for module overlap, tilt variations)
- **Endcap**: ±3mm radial, ±2mm z (accounts for module positioning tolerances)

### Why Original Boundaries Were Wrong

1. **SiTrackerBarrel**: Used `barrel_envelope` which includes:
   - Full module volume (3mm thick vs 0.3mm sensitive)
   - Support structures
   - Large safety margins (±45mm outer envelope)
   - Not appropriate for hit filtering

2. **SiTrackerEndcap**: Mixed approach:
   - Fixed ±10mm z margin (4x too large)
   - Radial boundaries didn't properly account for module extent
   - Some rings had arbitrary values (e.g., Layer 4 Ring 12)

### Validation

These corrected boundaries match the observed **~20mm hit thickness** in actual data, confirming they properly represent hit distributions from sensitive material.
