"""
IRC 2021 R602.3 - Stud Spacing Validation Rule

Deterministic validation for load-bearing wall stud spacing per IRC 2021.

Code Reference: IRC R602.3 - Design and Construction
"Studs shall be spaced at not more than 16 inches (406 mm) on center for
load-bearing walls supporting one floor, roof and ceiling."

This is a DETERMINISTIC rule - same input always produces same output.
No AI interpretation, no probabilistic reasoning.
"""

from typing import Dict, Any, Literal
from dataclasses import dataclass
from datetime import datetime


@dataclass
class ValidationResult:
    """Result of a validation check"""
    rule_id: str
    code_reference: str
    result: Literal["pass", "fail", "not_applicable"]
    message: str
    measured_value: Any = None
    required_value: Any = None
    ifc_global_id: str = None
    timestamp: str = None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.utcnow().isoformat() + "Z"


def check_stud_spacing(ifc_wall: Dict[str, Any]) -> ValidationResult:
    """
    IRC R602.3 - Validate stud spacing for load-bearing walls

    Args:
        ifc_wall: Dictionary representing an IfcWall element with properties:
            - ifcGlobalId: str
            - isLoadBearing: bool
            - studSpacing: float (in inches)
            - floorsSupported: int

    Returns:
        ValidationResult with pass/fail/not_applicable

    Examples:
        >>> wall = {"ifcGlobalId": "2O2Fr$t4X7Zf8NOew3FNr2",
        ...         "isLoadBearing": True,
        ...         "studSpacing": 16.0,
        ...         "floorsSupported": 1}
        >>> result = check_stud_spacing(wall)
        >>> result.result
        'pass'

        >>> wall = {"ifcGlobalId": "2O2Fr$t4X7Zf8NOew3FNr2",
        ...         "isLoadBearing": True,
        ...         "studSpacing": 20.0,
        ...         "floorsSupported": 1}
        >>> result = check_stud_spacing(wall)
        >>> result.result
        'fail'
    """

    rule_id = "IRC-R602.3-stud-spacing"
    code_ref = "IRC R602.3"
    ifc_id = ifc_wall.get("ifcGlobalId")

    # Check applicability: Rule only applies to load-bearing walls
    if not ifc_wall.get("isLoadBearing", False):
        return ValidationResult(
            rule_id=rule_id,
            code_reference=code_ref,
            result="not_applicable",
            message="Non-load-bearing wall - stud spacing rule does not apply",
            ifc_global_id=ifc_id
        )

    # Get measured values
    stud_spacing = ifc_wall.get("studSpacing")  # inches
    floors_supported = ifc_wall.get("floorsSupported", 0)

    # Validate data exists
    if stud_spacing is None:
        return ValidationResult(
            rule_id=rule_id,
            code_reference=code_ref,
            result="fail",
            message="Missing stud spacing data - cannot validate",
            ifc_global_id=ifc_id
        )

    # Apply deterministic rule for single-floor support
    if floors_supported == 1:
        max_spacing = 16.0  # inches

        if stud_spacing <= max_spacing:
            return ValidationResult(
                rule_id=rule_id,
                code_reference=code_ref,
                result="pass",
                message=f"Stud spacing {stud_spacing}\" complies with IRC R602.3 maximum {max_spacing}\" for single-floor load-bearing wall",
                measured_value=stud_spacing,
                required_value=f"<= {max_spacing}",
                ifc_global_id=ifc_id
            )
        else:
            return ValidationResult(
                rule_id=rule_id,
                code_reference=code_ref,
                result="fail",
                message=f"Stud spacing {stud_spacing}\" exceeds IRC R602.3 maximum {max_spacing}\" for single-floor load-bearing wall",
                measured_value=stud_spacing,
                required_value=f"<= {max_spacing}",
                ifc_global_id=ifc_id
            )

    # For walls supporting more than one floor, refer to engineered design
    else:
        return ValidationResult(
            rule_id=rule_id,
            code_reference=code_ref,
            result="not_applicable",
            message=f"Wall supports {floors_supported} floors - requires engineered design per IRC R301.1.3",
            ifc_global_id=ifc_id
        )


def check_ceiling_height(ifc_space: Dict[str, Any]) -> ValidationResult:
    """
    IRC R305.1 - Validate minimum ceiling height

    Code Reference: IRC R305.1 - Minimum Room Heights
    "Habitable rooms shall have a ceiling height of not less than 7 feet (2134 mm)."

    Args:
        ifc_space: Dictionary representing an IfcSpace element with properties:
            - ifcGlobalId: str
            - spaceType: str (e.g., "bedroom", "living room", "bathroom")
            - ceilingHeight: float (in feet)

    Returns:
        ValidationResult with pass/fail/not_applicable
    """

    rule_id = "IRC-R305.1-ceiling-height"
    code_ref = "IRC R305.1"
    ifc_id = ifc_space.get("ifcGlobalId")

    space_type = ifc_space.get("spaceType", "").lower()
    ceiling_height = ifc_space.get("ceilingHeight")  # feet

    # Define habitable rooms per IRC
    habitable_rooms = ["bedroom", "living room", "dining room", "family room", "den"]

    # Check applicability
    if space_type not in habitable_rooms:
        return ValidationResult(
            rule_id=rule_id,
            code_reference=code_ref,
            result="not_applicable",
            message=f"Space type '{space_type}' is not a habitable room - minimum height rule does not apply",
            ifc_global_id=ifc_id
        )

    if ceiling_height is None:
        return ValidationResult(
            rule_id=rule_id,
            code_reference=code_ref,
            result="fail",
            message="Missing ceiling height data - cannot validate",
            ifc_global_id=ifc_id
        )

    # Apply deterministic rule
    min_height = 7.0  # feet

    if ceiling_height >= min_height:
        return ValidationResult(
            rule_id=rule_id,
            code_reference=code_ref,
            result="pass",
            message=f"Ceiling height {ceiling_height}' meets IRC R305.1 minimum {min_height}' for habitable room ({space_type})",
            measured_value=ceiling_height,
            required_value=f">= {min_height}",
            ifc_global_id=ifc_id
        )
    else:
        return ValidationResult(
            rule_id=rule_id,
            code_reference=code_ref,
            result="fail",
            message=f"Ceiling height {ceiling_height}' below IRC R305.1 minimum {min_height}' for habitable room ({space_type})",
            measured_value=ceiling_height,
            required_value=f">= {min_height}",
            ifc_global_id=ifc_id
        )


def check_egress_window_area(ifc_window: Dict[str, Any]) -> ValidationResult:
    """
    IRC R310.2.1 - Validate emergency egress window area

    Code Reference: IRC R310.2.1 - Minimum Opening Area
    "Emergency egress and rescue openings shall have a minimum net clear opening
    of 5.7 square feet (0.530 m²)."

    Args:
        ifc_window: Dictionary representing an IfcWindow element with properties:
            - ifcGlobalId: str
            - isEgressWindow: bool
            - clearOpeningArea: float (in square feet)
            - locatedInBasement: bool

    Returns:
        ValidationResult with pass/fail/not_applicable
    """

    rule_id = "IRC-R310.2.1-egress-area"
    code_ref = "IRC R310.2.1"
    ifc_id = ifc_window.get("ifcGlobalId")

    # Check applicability: Rule only applies to egress windows
    if not ifc_window.get("isEgressWindow", False):
        return ValidationResult(
            rule_id=rule_id,
            code_reference=code_ref,
            result="not_applicable",
            message="Not designated as egress window - area requirement does not apply",
            ifc_global_id=ifc_id
        )

    clear_area = ifc_window.get("clearOpeningArea")  # sq ft
    in_basement = ifc_window.get("locatedInBasement", False)

    if clear_area is None:
        return ValidationResult(
            rule_id=rule_id,
            code_reference=code_ref,
            result="fail",
            message="Missing clear opening area data - cannot validate",
            ifc_global_id=ifc_id
        )

    # Determine minimum area (basements have different requirement)
    if in_basement:
        min_area = 5.7  # sq ft (IRC R310.2.1)
    else:
        min_area = 5.7  # sq ft (same for above-grade)

    # Apply deterministic rule
    if clear_area >= min_area:
        return ValidationResult(
            rule_id=rule_id,
            code_reference=code_ref,
            result="pass",
            message=f"Egress window clear opening area {clear_area} sq ft meets IRC R310.2.1 minimum {min_area} sq ft",
            measured_value=clear_area,
            required_value=f">= {min_area}",
            ifc_global_id=ifc_id
        )
    else:
        return ValidationResult(
            rule_id=rule_id,
            code_reference=code_ref,
            result="fail",
            message=f"Egress window clear opening area {clear_area} sq ft below IRC R310.2.1 minimum {min_area} sq ft",
            measured_value=clear_area,
            required_value=f">= {min_area}",
            ifc_global_id=ifc_id
        )


# Export all validation functions
VALIDATION_RULES = {
    "IRC-R602.3-stud-spacing": check_stud_spacing,
    "IRC-R305.1-ceiling-height": check_ceiling_height,
    "IRC-R310.2.1-egress-area": check_egress_window_area,
}


def validate_element(rule_id: str, ifc_element: Dict[str, Any]) -> ValidationResult:
    """
    Validate an IFC element against a specific IRC rule

    Args:
        rule_id: IRC rule identifier (e.g., "IRC-R602.3-stud-spacing")
        ifc_element: IFC element data as dictionary

    Returns:
        ValidationResult

    Raises:
        ValueError: If rule_id not found
    """

    if rule_id not in VALIDATION_RULES:
        raise ValueError(f"Unknown rule ID: {rule_id}. Available rules: {list(VALIDATION_RULES.keys())}")

    validation_func = VALIDATION_RULES[rule_id]
    return validation_func(ifc_element)


if __name__ == "__main__":
    # Example usage and testing
    import json

    # Test case 1: Compliant stud spacing
    wall_pass = {
        "ifcGlobalId": "2O2Fr$t4X7Zf8NOew3FNr2",
        "isLoadBearing": True,
        "studSpacing": 16.0,
        "floorsSupported": 1
    }

    result = check_stud_spacing(wall_pass)
    print(f"Test 1 (Compliant stud spacing): {result.result}")
    print(f"  Message: {result.message}\n")

    # Test case 2: Non-compliant stud spacing
    wall_fail = {
        "ifcGlobalId": "3P3Gs$u5Y8Ag9OPfx4GOt3",
        "isLoadBearing": True,
        "studSpacing": 20.0,
        "floorsSupported": 1
    }

    result = check_stud_spacing(wall_fail)
    print(f"Test 2 (Non-compliant stud spacing): {result.result}")
    print(f"  Message: {result.message}\n")

    # Test case 3: Compliant ceiling height
    bedroom = {
        "ifcGlobalId": "1A1Bt$c3W6Ye7MPdw2ENq1",
        "spaceType": "bedroom",
        "ceilingHeight": 8.0
    }

    result = check_ceiling_height(bedroom)
    print(f"Test 3 (Compliant ceiling height): {result.result}")
    print(f"  Message: {result.message}\n")

    # Output as JSON for API response
    print("Example API response:")
    print(json.dumps(result.__dict__, indent=2))
