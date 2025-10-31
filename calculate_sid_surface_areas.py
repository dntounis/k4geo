#!/usr/bin/env python3
"""
Calculate sensitive detector surface areas for SiD_o2_v04 geometry
All areas are in cm^2
"""

import math

# Constants from SiD_o2_v04.xml
MM_TO_CM = 0.1

# ============================================================================
# BARREL DETECTORS
# ============================================================================

def calculate_sivertexbarrel():
    """
    SiVertexBarrel: 5 layers of silicon sensors
    """
    # Layer 1: VtxBarrelModuleInner
    # Sensitive component: width=9.6mm, length=125.0mm
    layer1_nphi = 12
    layer1_nz = 1
    layer1_module_area = 9.6 * 125.0  # mm^2
    layer1_area = layer1_nphi * layer1_nz * layer1_module_area

    # Layers 2-5: VtxBarrelModuleOuter
    # Sensitive component: width=13.8mm, length=125.0mm
    layer2_nphi = 12
    layer2_nz = 1
    layer3_nphi = 18
    layer3_nz = 1
    layer4_nphi = 24
    layer4_nz = 1
    layer5_nphi = 30
    layer5_nz = 1

    module_area_outer = 13.8 * 125.0  # mm^2

    layer2_area = layer2_nphi * layer2_nz * module_area_outer
    layer3_area = layer3_nphi * layer3_nz * module_area_outer
    layer4_area = layer4_nphi * layer4_nz * module_area_outer
    layer5_area = layer5_nphi * layer5_nz * module_area_outer

    total_area_mm2 = layer1_area + layer2_area + layer3_area + layer4_area + layer5_area
    total_area_cm2 = total_area_mm2 * MM_TO_CM**2

    print(f"\n=== SiVertexBarrel ===")
    print(f"Layer 1: {layer1_nphi} modules × {layer1_module_area:.1f} mm² = {layer1_area:.1f} mm²")
    print(f"Layer 2: {layer2_nphi} modules × {module_area_outer:.1f} mm² = {layer2_area:.1f} mm²")
    print(f"Layer 3: {layer3_nphi} modules × {module_area_outer:.1f} mm² = {layer3_area:.1f} mm²")
    print(f"Layer 4: {layer4_nphi} modules × {module_area_outer:.1f} mm² = {layer4_area:.1f} mm²")
    print(f"Layer 5: {layer5_nphi} modules × {module_area_outer:.1f} mm² = {layer5_area:.1f} mm²")
    print(f"Total: {total_area_cm2:.2f} cm²")

    return total_area_cm2


def calculate_sitrackerbarrel():
    """
    SiTrackerBarrel: 5 layers of silicon sensors
    Each module has sensitive component: 92.031mm × 92.031mm
    """
    # Module sensitive area
    module_width = 92.031  # mm
    module_length = 92.031  # mm
    module_area = module_width * module_length  # mm^2

    # Layer parameters from SiTrackerBarrel_o2_v04.xml
    # nphi values
    layer1_nphi = 18
    layer2_nphi = 38
    layer3_nphi = 59
    layer4_nphi = 79
    layer5_nphi = 100

    # nz values (calculated from floor(z0/spacing))
    layer1_nz = 13
    layer2_nz = 17
    layer3_nz = 23
    layer4_nz = 29
    layer5_nz = 35

    layer1_area = layer1_nphi * layer1_nz * module_area
    layer2_area = layer2_nphi * layer2_nz * module_area
    layer3_area = layer3_nphi * layer3_nz * module_area
    layer4_area = layer4_nphi * layer4_nz * module_area
    layer5_area = layer5_nphi * layer5_nz * module_area

    total_area_mm2 = layer1_area + layer2_area + layer3_area + layer4_area + layer5_area
    total_area_cm2 = total_area_mm2 * MM_TO_CM**2

    print(f"\n=== SiTrackerBarrel ===")
    print(f"Module size: {module_width:.3f} × {module_length:.3f} mm² = {module_area:.3f} mm²")
    print(f"Layer 1: {layer1_nphi} × {layer1_nz} modules = {layer1_area:.1f} mm²")
    print(f"Layer 2: {layer2_nphi} × {layer2_nz} modules = {layer2_area:.1f} mm²")
    print(f"Layer 3: {layer3_nphi} × {layer3_nz} modules = {layer3_area:.1f} mm²")
    print(f"Layer 4: {layer4_nphi} × {layer4_nz} modules = {layer4_area:.1f} mm²")
    print(f"Layer 5: {layer5_nphi} × {layer5_nz} modules = {layer5_area:.1f} mm²")
    print(f"Total: {total_area_cm2:.2f} cm²")

    return total_area_cm2


def calculate_polygon_inner_area(rmin, half_length, nsides):
    """
    Calculate inner surface area of a regular polygon barrel
    rmin: inscribed radius (distance from center to middle of side) in mm
    half_length: half length along z in mm
    nsides: number of sides
    Returns area in mm^2
    """
    # For a regular polygon with inscribed radius r and n sides:
    # Side length s = 2 * r * tan(pi/n)
    # Total surface area = n * s * (2 * half_length)
    side_length = 2 * rmin * math.tan(math.pi / nsides)
    total_area = nsides * side_length * (2 * half_length)
    return total_area


def calculate_ecalbarrel():
    """
    ECalBarrel: 31 layers (1 + 20 + 10) of Silicon sensors
    12-fold symmetry polyhedra
    """
    rmin = 1264.0  # mm
    half_length = 1765.0  # mm
    nsides = 12
    nlayers = 31  # 1 + 20 + 10

    # Calculate inner surface area of the 12-sided polygon
    surface_area_mm2 = calculate_polygon_inner_area(rmin, half_length, nsides)

    # Total sensitive area = surface area × number of layers
    total_area_mm2 = surface_area_mm2 * nlayers
    total_area_cm2 = total_area_mm2 * MM_TO_CM**2

    print(f"\n=== ECalBarrel ===")
    print(f"12-fold polygon: rmin={rmin} mm, half_length={half_length} mm")
    print(f"Inner surface area per layer: {surface_area_mm2:.1f} mm²")
    print(f"Number of layers: {nlayers}")
    print(f"Total: {total_area_cm2:.2f} cm²")

    return total_area_cm2


def calculate_hcalbarrel():
    """
    HCalBarrel: 40 layers of Polystyrene scintillator
    12-fold symmetry polyhedra
    """
    rmin = 1406.0  # mm
    half_length = 2950.0  # mm
    nsides = 12
    nlayers = 40

    # Calculate inner surface area of the 12-sided polygon
    surface_area_mm2 = calculate_polygon_inner_area(rmin, half_length, nsides)

    # Total sensitive area = surface area × number of layers
    total_area_mm2 = surface_area_mm2 * nlayers
    total_area_cm2 = total_area_mm2 * MM_TO_CM**2

    print(f"\n=== HCalBarrel ===")
    print(f"12-fold polygon: rmin={rmin} mm, half_length={half_length} mm")
    print(f"Inner surface area per layer: {surface_area_mm2:.1f} mm²")
    print(f"Number of layers: {nlayers}")
    print(f"Total: {total_area_cm2:.2f} cm²")

    return total_area_cm2


def calculate_muonbarrel():
    """
    MuonBarrel: 11 layers, each with 1 sensitive Polystyrene scintillator
    (Note: each layer has 2 polystyrene slices, but only the first is sensitive)
    12-fold symmetry polyhedra
    """
    rmin = 3454.0  # mm
    half_length = 2950.0  # mm
    nsides = 12
    nlayers = 11  # Only counting sensitive layers

    # Calculate inner surface area of the 12-sided polygon
    surface_area_mm2 = calculate_polygon_inner_area(rmin, half_length, nsides)

    # Total sensitive area = surface area × number of sensitive layers
    total_area_mm2 = surface_area_mm2 * nlayers
    total_area_cm2 = total_area_mm2 * MM_TO_CM**2

    print(f"\n=== MuonBarrel ===")
    print(f"12-fold polygon: rmin={rmin} mm, half_length={half_length} mm")
    print(f"Inner surface area per layer: {surface_area_mm2:.1f} mm²")
    print(f"Number of sensitive layers: {nlayers}")
    print(f"Total: {total_area_cm2:.2f} cm²")

    return total_area_cm2


# ============================================================================
# ENDCAP DETECTORS
# ============================================================================

def calculate_trapezoid_area(x1, x2, z):
    """
    Calculate area of a trapezoid
    x1, x2: parallel sides
    z: height
    """
    return (x1 + x2) * z / 2.0


def calculate_sivertexendcap():
    """
    SiVertexEndcap: 4 layers of trapezoidal silicon sensors
    Each layer is a ring of modules, reflected in +z and -z
    """
    # Module definitions (trapezoids)
    modules = {
        'SiVertexEndcapModule1': {'x1': 3.034, 'x2': 14.682, 'z': 29.280},
        'SiVertexEndcapModule2': {'x1': 3.233, 'x2': 14.682, 'z': 28.780},
        'SiVertexEndcapModule3': {'x1': 3.630, 'x2': 14.682, 'z': 27.780},
        'SiVertexEndcapModule4': {'x1': 4.227, 'x2': 14.682, 'z': 26.280},
    }

    # Layer configurations
    layers = [
        {'module': 'SiVertexEndcapModule1', 'nmodules': 16},
        {'module': 'SiVertexEndcapModule2', 'nmodules': 16},
        {'module': 'SiVertexEndcapModule2', 'nmodules': 16},
        {'module': 'SiVertexEndcapModule2', 'nmodules': 16},
    ]

    total_area_mm2 = 0
    print(f"\n=== SiVertexEndcap ===")
    for i, layer in enumerate(layers, 1):
        mod_name = layer['module']
        nmodules = layer['nmodules']
        mod = modules[mod_name]
        area = calculate_trapezoid_area(mod['x1'], mod['x2'], mod['z'])
        layer_area = nmodules * area
        total_area_mm2 += layer_area
        print(f"Layer {i}: {nmodules} × {mod_name} ({area:.3f} mm²) = {layer_area:.1f} mm²")

    # Multiply by 2 for both +z and -z endcaps
    total_area_mm2 *= 2
    total_area_cm2 = total_area_mm2 * MM_TO_CM**2

    print(f"Total (one side): {total_area_mm2/2:.1f} mm²")
    print(f"Total (both ±z): {total_area_cm2:.2f} cm²")

    return total_area_cm2


def calculate_sitrackerforward():
    """
    SiTrackerForward: 3 layers of trapezoidal silicon sensors
    Reflected in +z and -z
    """
    # Module definitions
    modules = {
        'SiTrackerForwardModule1': {'x1': 5.620, 'x2': 32.435, 'z': 67.405},
        'SiTrackerForwardModule2': {'x1': 15.167, 'x2': 32.435, 'z': 43.405},
        'SiTrackerForwardModule3': {'x1': 23.522, 'x2': 32.435, 'z': 22.405},
    }

    layers = [
        {'module': 'SiTrackerForwardModule1', 'nmodules': 16},
        {'module': 'SiTrackerForwardModule2', 'nmodules': 16},
        {'module': 'SiTrackerForwardModule3', 'nmodules': 16},
    ]

    total_area_mm2 = 0
    print(f"\n=== SiTrackerForward ===")
    for i, layer in enumerate(layers, 1):
        mod_name = layer['module']
        nmodules = layer['nmodules']
        mod = modules[mod_name]
        area = calculate_trapezoid_area(mod['x1'], mod['x2'], mod['z'])
        layer_area = nmodules * area
        total_area_mm2 += layer_area
        print(f"Layer {i}: {nmodules} × {mod_name} ({area:.3f} mm²) = {layer_area:.1f} mm²")

    # Multiply by 2 for both +z and -z endcaps
    total_area_mm2 *= 2
    total_area_cm2 = total_area_mm2 * MM_TO_CM**2

    print(f"Total (one side): {total_area_mm2/2:.1f} mm²")
    print(f"Total (both ±z): {total_area_cm2:.2f} cm²")

    return total_area_cm2


def calculate_sitrackerendcap():
    """
    SiTrackerEndcap: 4 layers, each with multiple rings of trapezoidal modules
    Reflected in +z and -z
    """
    # Module definitions
    modules = {
        'Module1': {'x1': 36.112, 'x2': 46.635, 'z': 100.114/2},
        'Module2': {'x1': 45.245, 'x2': 54.680, 'z': 89.773/2},
    }

    # Layer configurations
    layers = {
        1: [
            {'module': 'Module1', 'nmodules': 24},
            {'module': 'Module1', 'nmodules': 32},
            {'module': 'Module1', 'nmodules': 40},
        ],
        2: [
            {'module': 'Module1', 'nmodules': 24},
            {'module': 'Module1', 'nmodules': 32},
            {'module': 'Module1', 'nmodules': 40},
            {'module': 'Module2', 'nmodules': 40},
            {'module': 'Module2', 'nmodules': 48},
            {'module': 'Module2', 'nmodules': 54},
        ],
        3: [
            {'module': 'Module1', 'nmodules': 24},
            {'module': 'Module1', 'nmodules': 32},
            {'module': 'Module1', 'nmodules': 40},
            {'module': 'Module2', 'nmodules': 40},
            {'module': 'Module2', 'nmodules': 48},
            {'module': 'Module2', 'nmodules': 54},
            {'module': 'Module2', 'nmodules': 58},
            {'module': 'Module2', 'nmodules': 64},
            {'module': 'Module2', 'nmodules': 68},
        ],
        4: [
            {'module': 'Module1', 'nmodules': 24},
            {'module': 'Module1', 'nmodules': 32},
            {'module': 'Module1', 'nmodules': 40},
            {'module': 'Module2', 'nmodules': 40},
            {'module': 'Module2', 'nmodules': 48},
            {'module': 'Module2', 'nmodules': 54},
            {'module': 'Module2', 'nmodules': 58},
            {'module': 'Module2', 'nmodules': 64},
            {'module': 'Module2', 'nmodules': 68},
            {'module': 'Module2', 'nmodules': 72},
            {'module': 'Module2', 'nmodules': 78},
            {'module': 'Module2', 'nmodules': 84},
        ],
    }

    total_area_mm2 = 0
    print(f"\n=== SiTrackerEndcap ===")

    for layer_id, rings in layers.items():
        layer_area = 0
        for ring in rings:
            mod_name = ring['module']
            nmodules = ring['nmodules']
            mod = modules[mod_name]
            area = calculate_trapezoid_area(mod['x1'], mod['x2'], mod['z'])
            ring_area = nmodules * area
            layer_area += ring_area
        total_area_mm2 += layer_area
        print(f"Layer {layer_id}: {len(rings)} rings, total area = {layer_area:.1f} mm²")

    # Multiply by 2 for both +z and -z endcaps
    total_area_mm2 *= 2
    total_area_cm2 = total_area_mm2 * MM_TO_CM**2

    print(f"Total (one side): {total_area_mm2/2:.1f} mm²")
    print(f"Total (both ±z): {total_area_cm2:.2f} cm²")

    return total_area_cm2


def calculate_polygon_endcap_area(rmin, rmax, nsides):
    """
    Calculate area of a regular polygon endcap (annulus)
    rmin: inner radius in mm
    rmax: outer radius in mm
    nsides: number of sides (0 for circle)
    Returns area in mm^2
    """
    if nsides == 0:
        # Circular annulus
        return math.pi * (rmax**2 - rmin**2)
    else:
        # Regular polygon annulus
        # Area = n * rmax^2 * sin(2π/n) / 2 - n * rmin^2 * sin(2π/n) / 2
        # For inscribed radius (distance to side center), use different formula
        # Circumradius = inscribed_radius / cos(π/n)
        # But typically for polygons, rmax and rmin refer to inscribed radii
        # Let's use the approximation: polygon area ≈ circle area
        # For more accuracy with 12-sided polygon:
        outer_circumradius = rmax / math.cos(math.pi / nsides)
        inner_circumradius = rmin / math.cos(math.pi / nsides)
        area = nsides * (outer_circumradius**2 - inner_circumradius**2) * math.sin(2 * math.pi / nsides) / 2
        return area


def calculate_ecalendcap():
    """
    ECalEndcap: 31 layers (1 + 20 + 10) of Silicon sensors
    12-fold symmetry polyhedra, reflected in +z and -z
    """
    rmin = 216.0  # mm
    rmax = 1250.0  # mm
    nsides = 12
    nlayers = 31  # 1 + 20 + 10

    # Calculate endcap area (annular polygon)
    area_per_layer = calculate_polygon_endcap_area(rmin, rmax, nsides)

    # Total area for one endcap
    total_area_one_side = area_per_layer * nlayers

    # Multiply by 2 for both endcaps
    total_area_mm2 = total_area_one_side * 2
    total_area_cm2 = total_area_mm2 * MM_TO_CM**2

    print(f"\n=== ECalEndcap ===")
    print(f"12-fold polygon annulus: rmin={rmin} mm, rmax={rmax} mm")
    print(f"Area per layer: {area_per_layer:.1f} mm²")
    print(f"Number of layers: {nlayers}")
    print(f"Total (one side): {total_area_one_side:.1f} mm²")
    print(f"Total (both ±z): {total_area_cm2:.2f} cm²")

    return total_area_cm2


def calculate_hcalendcap():
    """
    HCalEndcap: 44 layers of Polystyrene scintillator
    12-fold symmetry polyhedra, reflected in +z and -z
    """
    rmin = 216.0  # mm
    rmax = 1400.0  # mm
    nsides = 12
    nlayers = 44

    # Calculate endcap area (annular polygon)
    area_per_layer = calculate_polygon_endcap_area(rmin, rmax, nsides)

    # Total area for one endcap
    total_area_one_side = area_per_layer * nlayers

    # Multiply by 2 for both endcaps
    total_area_mm2 = total_area_one_side * 2
    total_area_cm2 = total_area_mm2 * MM_TO_CM**2

    print(f"\n=== HCalEndcap ===")
    print(f"12-fold polygon annulus: rmin={rmin} mm, rmax={rmax} mm")
    print(f"Area per layer: {area_per_layer:.1f} mm²")
    print(f"Number of layers: {nlayers}")
    print(f"Total (one side): {total_area_one_side:.1f} mm²")
    print(f"Total (both ±z): {total_area_cm2:.2f} cm²")

    return total_area_cm2


def calculate_lumical():
    """
    LumiCal: 30 layers (20 + 10) of Silicon sensors
    Cylindrical, reflected in +z and -z
    """
    rmin = 60.0  # mm
    rmax = 195.0  # mm
    nlayers = 30  # 20 + 10

    # Cylindrical annulus
    area_per_layer = math.pi * (rmax**2 - rmin**2)

    # Total area for one endcap
    total_area_one_side = area_per_layer * nlayers

    # Multiply by 2 for both endcaps
    total_area_mm2 = total_area_one_side * 2
    total_area_cm2 = total_area_mm2 * MM_TO_CM**2

    print(f"\n=== LumiCal ===")
    print(f"Cylindrical annulus: rmin={rmin} mm, rmax={rmax} mm")
    print(f"Area per layer: {area_per_layer:.1f} mm²")
    print(f"Number of layers: {nlayers}")
    print(f"Total (one side): {total_area_one_side:.1f} mm²")
    print(f"Total (both ±z): {total_area_cm2:.2f} cm²")

    return total_area_cm2


def calculate_beamcal():
    """
    BeamCal: 50 layers of Silicon sensors
    Cylindrical, reflected in +z and -z
    Note: Has beam pipe holes, but we calculate full annulus area
    """
    rmin = 15.5  # mm (outer beam pipe radius)
    rmax = 129.6  # mm
    nlayers = 50

    # Cylindrical annulus
    area_per_layer = math.pi * (rmax**2 - rmin**2)

    # Total area for one endcap
    total_area_one_side = area_per_layer * nlayers

    # Multiply by 2 for both endcaps
    total_area_mm2 = total_area_one_side * 2
    total_area_cm2 = total_area_mm2 * MM_TO_CM**2

    print(f"\n=== BeamCal ===")
    print(f"Cylindrical annulus: rmin={rmin} mm, rmax={rmax} mm")
    print(f"Area per layer: {area_per_layer:.1f} mm²")
    print(f"Number of layers: {nlayers}")
    print(f"Total (one side): {total_area_one_side:.1f} mm²")
    print(f"Total (both ±z): {total_area_cm2:.2f} cm²")

    return total_area_cm2


def calculate_muonendcap():
    """
    MuonEndcap: 11 layers, each with 2 sensitive Polystyrene scintillators
    12-fold symmetry polyhedra, reflected in +z and -z
    """
    rmin = 366.0  # mm
    rmax = 6054.0  # mm
    nsides = 12
    nlayers = 11
    nsensitive_per_layer = 2  # Both polystyrene layers are sensitive in endcap

    # Calculate endcap area (annular polygon)
    area_per_layer = calculate_polygon_endcap_area(rmin, rmax, nsides)

    # Total area for one endcap (accounting for 2 sensitive layers per layer)
    total_area_one_side = area_per_layer * nlayers * nsensitive_per_layer

    # Multiply by 2 for both endcaps
    total_area_mm2 = total_area_one_side * 2
    total_area_cm2 = total_area_mm2 * MM_TO_CM**2

    print(f"\n=== MuonEndcap ===")
    print(f"12-fold polygon annulus: rmin={rmin} mm, rmax={rmax} mm")
    print(f"Area per sensitive layer: {area_per_layer:.1f} mm²")
    print(f"Number of layers: {nlayers} × {nsensitive_per_layer} sensitive = {nlayers * nsensitive_per_layer}")
    print(f"Total (one side): {total_area_one_side:.1f} mm²")
    print(f"Total (both ±z): {total_area_cm2:.2f} cm²")

    return total_area_cm2


# ============================================================================
# MAIN
# ============================================================================

def main():
    print("="*80)
    print("SiD_o2_v04 Sensitive Detector Surface Area Calculations")
    print("="*80)

    # Barrel detectors
    print("\n" + "="*80)
    print("BARREL DETECTORS")
    print("="*80)

    sivertexbarrel_area = calculate_sivertexbarrel()
    sitrackerbarrel_area = calculate_sitrackerbarrel()
    ecalbarrel_area = calculate_ecalbarrel()
    hcalbarrel_area = calculate_hcalbarrel()
    muonbarrel_area = calculate_muonbarrel()

    # Endcap detectors
    print("\n" + "="*80)
    print("ENDCAP/FORWARD DETECTORS")
    print("="*80)

    sivertexendcap_area = calculate_sivertexendcap()
    sitrackerforward_area = calculate_sitrackerforward()
    sitrackerendcap_area = calculate_sitrackerendcap()
    ecalendcap_area = calculate_ecalendcap()
    hcalendcap_area = calculate_hcalendcap()
    lumical_area = calculate_lumical()
    beamcal_area = calculate_beamcal()
    muonendcap_area = calculate_muonendcap()

    # Summary table
    print("\n" + "="*80)
    print("SUMMARY TABLE")
    print("="*80)
    print("\nBARREL DETECTORS:")
    print(f"{'Detector':<25} {'Surface Area (cm²)':>25}")
    print("-" * 52)
    print(f"{'SiVertexBarrel':<25} {sivertexbarrel_area:>25,.2f}")
    print(f"{'SiTrackerBarrel':<25} {sitrackerbarrel_area:>25,.2f}")
    print(f"{'ECALBarrel':<25} {ecalbarrel_area:>25,.2f}")
    print(f"{'HCALBarrel':<25} {hcalbarrel_area:>25,.2f}")
    print(f"{'MuonBarrel':<25} {muonbarrel_area:>25,.2f}")

    print("\nENDCAP/FORWARD DETECTORS:")
    print(f"{'Detector':<25} {'Surface Area (cm²)':>25}")
    print("-" * 52)
    print(f"{'SiVertexEndcap':<25} {sivertexendcap_area:>25,.2f}")
    print(f"{'SiTrackerForward':<25} {sitrackerforward_area:>25,.2f}")
    print(f"{'SiTrackerEndcap':<25} {sitrackerendcap_area:>25,.2f}")
    print(f"{'ECALEndcap':<25} {ecalendcap_area:>25,.2f}")
    print(f"{'HCALEndcap':<25} {hcalendcap_area:>25,.2f}")
    print(f"{'LumiCal':<25} {lumical_area:>25,.2f}")
    print(f"{'BeamCal':<25} {beamcal_area:>25,.2f}")
    print(f"{'MuonEndcap':<25} {muonendcap_area:>25,.2f}")

    print("\n" + "="*80)
    print(f"Total Barrel Area:        {sivertexbarrel_area + sitrackerbarrel_area + ecalbarrel_area + hcalbarrel_area + muonbarrel_area:>25,.2f} cm²")
    print(f"Total Endcap/Forward Area: {sivertexendcap_area + sitrackerforward_area + sitrackerendcap_area + ecalendcap_area + hcalendcap_area + lumical_area + beamcal_area + muonendcap_area:>25,.2f} cm²")
    print(f"Grand Total:              {sivertexbarrel_area + sitrackerbarrel_area + ecalbarrel_area + hcalbarrel_area + muonbarrel_area + sivertexendcap_area + sitrackerforward_area + sitrackerendcap_area + ecalendcap_area + hcalendcap_area + lumical_area + beamcal_area + muonendcap_area:>25,.2f} cm²")
    print("="*80)


if __name__ == "__main__":
    main()
