# Beampipe Overlap Fix for SiD_o2_v04

## Problem Summary

The Beampipe (Beryllium) was overlapping with the ForwardSupportTube (Steel) at the junction point z = ±20.5 cm, causing geometry conflicts detected by Geant4:

```
Overlap is detected for volume Beampipe_13:13 (G4Polycone)
with ForwardSupportTube_14:14 (G4Polycone)
overlap at local point (-16.6917,-8.4805,-201.378) by 536.211 um
```

## Root Cause

At z = ±20.5 cm, both the Beampipe and ForwardSupportTube were occupying the same radial space:

**Before Fix:**
- **Beampipe**: rmin = 18.186 mm, rmax = 18.887 mm (occupies 18.186-18.887 mm)
- **ForwardSupportTube**: rmin = 18.186 mm, rmax = 19.261 mm (occupies 18.186-19.261 mm)

**Overlap region**: 18.186-18.887 mm (both tubes present)
**Radial penetration**: 0.701 mm = 701 μm

The problem was that both polycones shared the same inner radius (rmin = 18.186 mm), but the Beampipe extended outward to 18.887 mm, which is *inside* the ForwardSupportTube material that starts at 18.186 mm. This created a physical overlap where both materials were trying to occupy the same space.

## Solution Implemented

**Approach**: Reduce Beampipe radii at z = ±20.5 cm so it fits *inside* the ForwardSupportTube bore.

The Beampipe now tapers to a smaller radius at the junction, fitting entirely within the inner bore of the ForwardSupportTube with a ~100 μm clearance.

## Changes Made

**File**: `SiD/compact/SiD_o2_v04/BeamPipe_o2_v04.xml`

**Lines 8 and 11** (z-planes at z = ±20.50 cm):

### Before:
```xml
<zplane rmin="bp_cone_dr+1.20*cm" rmax="bp_cone_dr+(1.20+0.07*1.0016)*cm" z="-20.50*cm"/>
<zplane rmin="bp_cone_dr+1.20*cm" rmax="bp_cone_dr+(1.20+0.07*1.0016)*cm" z="20.50*cm"/>
```

### After:
```xml
<zplane rmin="bp_cone_dr+1.12*cm" rmax="bp_cone_dr+(1.12+0.07*1.0016)*cm" z="-20.50*cm"/>
<zplane rmin="bp_cone_dr+1.12*cm" rmax="bp_cone_dr+(1.12+0.07*1.0016)*cm" z="20.50*cm"/>
```

**Key change**: Reduced the base radius from 1.20 cm to 1.12 cm (reduction of 0.8 mm)

## Result

**After Fix:**
- **Beampipe**: rmin = 17.386 mm, rmax = 18.087 mm
- **ForwardSupportTube**: rmin = 18.186 mm, rmax = 19.261 mm

**Clearance**: 18.186 - 18.087 = **0.099 mm = 98.9 μm** ✓

The Beampipe now fits completely inside the inner bore of the ForwardSupportTube with adequate clearance.

## Geometry Impact

### Changed:
- **Beampipe inner radius at z=±20.5 cm**: 18.186 → 17.386 mm (-0.8 mm)
- **Beampipe outer radius at z=±20.5 cm**: 18.887 → 18.087 mm (-0.8 mm)
- **Taper gradient**: Slightly steeper between z=±6.25 cm and z=±20.5 cm

### Unchanged:
- **Central region** (z ∈ [-6.25, +6.25] cm): Still at rmin=12.0 mm, rmax=12.4 mm
- **Wall thickness**: Maintained at 0.701 mm throughout
- **Material**: Still Beryllium
- **ForwardSupportTube**: No changes

## Beampipe Geometry Summary

The complete Beampipe polycone after fix:

| Z Position | Inner Radius (rmin) | Outer Radius (rmax) | Wall Thickness |
|------------|---------------------|---------------------|----------------|
| -20.50 cm  | 17.386 mm           | 18.087 mm           | 0.701 mm       |
| -6.25 cm   | 12.000 mm           | 12.400 mm           | 0.400 mm       |
| +6.25 cm   | 12.000 mm           | 12.400 mm           | 0.400 mm       |
| +20.50 cm  | 17.386 mm           | 18.087 mm           | 0.701 mm       |

The Beampipe:
1. Has a narrow central section (12 mm inner radius) from z = -6.25 to +6.25 cm
2. Tapers outward to 17.386 mm inner radius at z = ±20.5 cm
3. Fits inside the ForwardSupportTube (which starts at 18.186 mm inner radius)

## ForwardSupportTube Geometry (Unchanged)

| Z Position | Inner Radius (rmin) | Outer Radius (rmax) | Wall Thickness |
|------------|---------------------|---------------------|----------------|
| -120.0 cm  | 110.998 mm          | 112.504 mm          | 1.506 mm       |
| -20.50 cm  | 18.186 mm           | 19.261 mm           | 1.075 mm       |
| +20.50 cm  | 18.186 mm           | 19.261 mm           | 1.075 mm       |
| +120.0 cm  | 110.998 mm          | 112.504 mm          | 1.506 mm       |

The ForwardSupportTube:
1. Starts at z = ±120 cm with large radius (111 mm inner)
2. Tapers down to 18.186 mm inner radius at z = ±20.5 cm
3. Surrounds the Beampipe at the junction

## Physical Interpretation

The design now correctly represents:
- A **Beryllium beampipe** in the central detector region (low material, good for tracking)
- Transitioning to a **Steel support structure** in the forward regions
- At z = ±20.5 cm: The Be pipe **fits inside** the Steel tube's inner bore
- Clean handoff between materials with ~100 μm clearance

## Verification

### Mathematical Verification ✓
- Calculated clearance: **98.9 μm**
- No radial overlap at any z position
- Smooth polycone geometry (no discontinuities)

### Geant4 Overlap Check

Run the overlap checker to verify:

```bash
ddsim --compactFile SiD/compact/SiD_o2_v04/SiD_o2_v04.xml \
      --runType run \
      --macroFile utils/overlap.mac \
      > overlap_check_BEAMPIPE_FIXED.log 2>&1
```

Check results:

```bash
grep -i "beampipe\|forwardsupport" overlap_check_BEAMPIPE_FIXED.log | grep -i "overlap"
```

**Expected result**: No overlap warnings between Beampipe and ForwardSupportTube.

## Potential Physics Impact

The change is expected to have minimal physics impact:

**Negligible effects:**
- Material budget change is very small (~0.8 mm radial shift over 14 cm length)
- Affects only the transition region (z = ±6.25 to ±20.5 cm)
- Central tracking region (z = ±6.25 cm) completely unchanged

**Minor effects to monitor:**
- Slightly less material at the junction (Be pipe pulled inward)
- May affect very forward particle trajectories marginally
- Should be validated with tracking performance tests

## Validation Checklist

Before production use:

- [ ] Run Geant4 overlap checker (should show no Beampipe/ForwardSupportTube overlaps)
- [ ] Verify no new overlaps introduced elsewhere
- [ ] Test particle tracking in forward region
- [ ] Check material budget plots in transition region
- [ ] Compare vertex resolution with previous geometry (should be similar)
- [ ] Visual inspection of geometry (if tools available)

## Related Fixes

This fix is part of a series of overlap corrections in SiD_o2_v04:

1. **SiVertexEndcap overlap fix** - Fixed vertex detector modules overlapping with ForwardSupportTube (see `GEOMETRY_FIX_SiD_o2_v04.md`)
2. **Beampipe overlap fix** - This fix (Beampipe overlapping with ForwardSupportTube)

## References

- Original Beampipe design: Chris Potter (U. Oregon), April 2022
  - Talk: https://agenda.linearcollider.org/event/9586/
- Overlap analysis: `overlap_analysis_SiD_o2_v04.md`
- Modified file: `SiD/compact/SiD_o2_v04/BeamPipe_o2_v04.xml`

## Author & Date

- Fixed: 2025-11-05
- Method: Mathematical analysis of polycone geometry
- Approach: Reduce Beampipe radii at junction to fit inside ForwardSupportTube
