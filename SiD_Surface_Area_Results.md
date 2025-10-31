# SiD_o2_v04 Sensitive Detector Surface Area Calculations

## Summary

This document presents the total sensitive detector surface area calculations for the SiD_o2_v04 geometry. All measurements are based on the XML geometry files in `/home/user/k4geo/SiD/compact/SiD_o2_v04/`.

**Important Note:** The detector named "TrackerBarrel" does not exist in the SiD_o2_v04 geometry. The outer tracker barrel is called "SiTrackerBarrel". The assembly "SiTrackers" contains both SiTrackerBarrel and SiTrackerEndcap.

---

## Results Table

### Barrel Detectors

| Detector          | Surface Area (cm²) | Layers | Geometry Type |
|-------------------|-------------------:|-------:|---------------|
| SiVertexBarrel    | 1,593.00          | 5      | Cylindrical modules |
| SiTrackerBarrel   | 679,947.91        | 5      | Tilted rectangular modules |
| ECALBarrel        | 8,895,024.88      | 31     | 12-fold polygon (Silicon) |
| HCALBarrel        | 21,338,359.02     | 40     | 12-fold polygon (Scintillator) |
| MuonBarrel        | 14,415,533.65     | 11     | 12-fold polygon (Scintillator) |
| **TOTAL BARREL**  | **45,330,458.46** | —      | — |

### Endcap/Forward Detectors

| Detector          | Surface Area (cm²) | Layers | Geometry Type | ±z Replication |
|-------------------|-------------------:|-------:|---------------|----------------|
| SiVertexEndcap    | 330.48            | 4      | Trapezoidal disks | Yes (×2) |
| SiTrackerForward  | 941.60            | 3      | Trapezoidal disks | Yes (×2) |
| SiTrackerEndcap   | 62,552.48         | 4      | Trapezoidal disks | Yes (×2) |
| ECALEndcap        | 3,021,898.67      | 31     | 12-fold polygon annulus (Silicon) | Yes (×2) |
| HCALEndcap        | 5,413,890.03      | 44     | 12-fold polygon annulus (Scintillator) | Yes (×2) |
| LumiCal           | 64,889.60         | 30     | Cylindrical annulus (Silicon) | Yes (×2) |
| BeamCal           | 52,011.93         | 50     | Cylindrical annulus (Silicon) | Yes (×2) |
| MuonEndcap        | 51,663,162.89     | 22†    | 12-fold polygon annulus (Scintillator) | Yes (×2) |
| **TOTAL ENDCAP**  | **60,279,677.67** | —      | — | — |

† MuonEndcap has 11 structural layers, each containing 2 sensitive scintillator layers (22 total)

---

## Grand Total

| Category          | Surface Area (cm²) | Surface Area (m²) |
|-------------------|-------------------:|------------------:|
| Total Barrel      | 45,330,458.46     | 4,533.05         |
| Total Endcap      | 60,279,677.67     | 6,027.97         |
| **GRAND TOTAL**   | **105,610,136.13** | **10,561.01**    |

---

## Detailed Breakdown

### SiVertexBarrel (1,593.00 cm²)
- **Layer 1:** 12 modules × (9.6 × 125.0 mm²) = 14,400 mm²
- **Layer 2:** 12 modules × (13.8 × 125.0 mm²) = 20,700 mm²
- **Layer 3:** 18 modules × (13.8 × 125.0 mm²) = 31,050 mm²
- **Layer 4:** 24 modules × (13.8 × 125.0 mm²) = 41,400 mm²
- **Layer 5:** 30 modules × (13.8 × 125.0 mm²) = 51,750 mm²

### SiTrackerBarrel (679,947.91 cm²)
- **Module size:** 92.031 × 92.031 mm² (sensitive)
- **Layer 1:** 18 φ × 13 z = 234 modules
- **Layer 2:** 38 φ × 17 z = 646 modules
- **Layer 3:** 59 φ × 23 z = 1,357 modules
- **Layer 4:** 79 φ × 29 z = 2,291 modules
- **Layer 5:** 100 φ × 35 z = 3,500 modules
- **Total:** 8,028 modules

### ECALBarrel (8,895,024.88 cm²)
- **Geometry:** 12-fold regular polygon
- **Inner radius:** 1264.0 mm (inscribed)
- **Half length:** 1765.0 mm
- **Layers:** 31 (1 + 20 + 10)
- **Material:** Silicon (0.32 mm thick per layer)

### HCALBarrel (21,338,359.02 cm²)
- **Geometry:** 12-fold regular polygon
- **Inner radius:** 1406.0 mm (inscribed)
- **Half length:** 2950.0 mm
- **Layers:** 40
- **Material:** Polystyrene scintillator (3.0 mm thick)

### MuonBarrel (14,415,533.65 cm²)
- **Geometry:** 12-fold regular polygon
- **Inner radius:** 3454.0 mm (inscribed)
- **Half length:** 2950.0 mm
- **Layers:** 11 (1 sensitive layer per structural layer)
- **Material:** Polystyrene scintillator (3.0 mm thick)

### SiVertexEndcap (330.48 cm²)
- **4 layers** with trapezoidal modules
- **16 modules per layer**
- **Both ±z endcaps included**

### SiTrackerForward (941.60 cm²)
- **3 layers** with trapezoidal modules
- **16 modules per layer**
- **Both ±z endcaps included**

### SiTrackerEndcap (62,552.48 cm²)
- **Layer 1:** 3 rings (96 total modules)
- **Layer 2:** 6 rings (246 total modules)
- **Layer 3:** 9 rings (396 total modules)
- **Layer 4:** 12 rings (546 total modules)
- **Both ±z endcaps included**

### ECALEndcap (3,021,898.67 cm²)
- **Geometry:** 12-fold polygon annulus
- **Inner radius:** 216.0 mm, **Outer radius:** 1250.0 mm
- **Layers:** 31 (1 + 20 + 10)
- **Material:** Silicon (0.32 mm thick per layer)
- **Both ±z endcaps included**

### HCALEndcap (5,413,890.03 cm²)
- **Geometry:** 12-fold polygon annulus
- **Inner radius:** 216.0 mm, **Outer radius:** 1400.0 mm
- **Layers:** 44
- **Material:** Polystyrene scintillator (3.0 mm thick)
- **Both ±z endcaps included**

### LumiCal (64,889.60 cm²)
- **Geometry:** Cylindrical annulus
- **Inner radius:** 60.0 mm, **Outer radius:** 195.0 mm
- **Layers:** 30 (20 + 10)
- **Material:** Silicon (0.32 mm thick per layer)
- **Both ±z endcaps included**

### BeamCal (52,011.93 cm²)
- **Geometry:** Cylindrical annulus
- **Inner radius:** 15.5 mm, **Outer radius:** 129.6 mm
- **Layers:** 50
- **Material:** Silicon (0.32 mm thick per layer)
- **Both ±z endcaps included**

### MuonEndcap (51,663,162.89 cm²)
- **Geometry:** 12-fold polygon annulus
- **Inner radius:** 366.0 mm, **Outer radius:** 6054.0 mm
- **Structural layers:** 11
- **Sensitive layers:** 22 (2 per structural layer)
- **Material:** Polystyrene scintillator (3.0 mm thick)
- **Both ±z endcaps included**

---

## Methodology

### Barrel Detectors

1. **Modular trackers** (SiVertexBarrel, SiTrackerBarrel): Surface area calculated by summing individual module areas across all layers.

2. **Polygon barrels** (ECAL, HCAL, Muon): For a 12-fold regular polygon with inscribed radius *r* and half-length *L*:
   - Side length: *s = 2r tan(π/12)*
   - Perimeter: *P = 12s*
   - Surface area per layer: *A = P × 2L*
   - Total: *A_total = A × n_layers*

### Endcap Detectors

1. **Modular trackers** (endcaps/forward): Surface area calculated by summing trapezoidal module areas.
   - Trapezoid area: *A = (x₁ + x₂) × z / 2*

2. **Polygon annuli** (ECAL, HCAL, Muon endcaps): For 12-fold regular polygon:
   - Convert inscribed radii to circumradii: *R = r / cos(π/12)*
   - Area: *A = 12 × (R_outer² - R_inner²) × sin(2π/12) / 2*

3. **Cylindrical annuli** (LumiCal, BeamCal):
   - Area: *A = π(r_outer² - r_inner²)*

4. **All endcap/forward detectors:** Multiplied by 2 to account for ±z replication (as specified by `reflect="true"` in XML).

---

## Cross-Checks Performed

✓ **Manual verification** of sample calculations
✓ **Module counting** for tracker systems
✓ **Layer counting** from XML files
✓ **±z replication** verified for all endcaps
✓ **Physical reasonableness** (radii increase outward)
✓ **Unit consistency** (all inputs in mm, outputs in cm²)
✓ **Polygon approximation** validated (2.35% difference from circular for 12-sided)
✓ **Sensitive vs non-sensitive** layers correctly identified

All validation checks passed successfully.

---

## Source Files

- **Geometry:** `/home/user/k4geo/SiD/compact/SiD_o2_v04/`
- **Calculation script:** `calculate_sid_surface_areas.py`
- **Validation script:** `validate_calculations.py`
- **SiD version:** o2_v04 (Option 2, Version 4, June 2022)

---

## Notes

1. **TrackerBarrel**: This detector does not exist in SiD_o2_v04. The correct name is **SiTrackerBarrel**.

2. **MuonBarrel vs MuonEndcap**: The barrel has only 1 sensitive layer per structural layer, while the endcap has 2 sensitive layers per structural layer.

3. **Polygon approximation**: The 12-fold polygons are calculated using exact geometric formulas. The difference from a circular approximation is ~2.35%.

4. **BeamCal**: The calculation includes the full annular area. The actual geometry has cutouts for the beam pipe crossing angle, which would slightly reduce the sensitive area.

5. All areas represent the **sensitive detector surfaces only** (marked as `sensitive="yes"` in the XML files).
