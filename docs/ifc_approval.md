# IFC File Validation Workflow

This document outlines how Industry Foundation Classes (IFC) files should be validated as part of the OpenPermit submission process. The goal is to ensure that building models conform to open standards and local code requirements before they are used in permitting workflows.

## 1. Schema Validation

1. **Validate against the official IFC schema**
   - Use tools such as [IfcOpenShell](https://ifcopenshell.org/) or `ifc-validator` to check compliance with the appropriate IFC release (e.g., IFC4 or IFC4x3).
   - Ensure that geometry and property sets are defined according to the EXPRESS schema.

2. **Check JSON representations**
   - When IFC models are provided in JSON form (e.g., IFC.JSON), validate them using buildingSMART's IFC specifications at [technical.buildingsmart.org](https://technical.buildingsmart.org/) or similar libraries.

## 2. Code and Rule Compliance

1. **Local code requirements**
   - Run rule-based checks to verify that the model meets municipal code constraints (e.g., maximum building height, required safety clearances).
   - Libraries like [BIMTester](https://github.com/opensourcebim/BIMTester) or the [IfcOpenShell Python API](https://ifcopenshell.org/python.html) can automate these rule checks.

2. **Geometry and spatial validation**
   - Validate spatial relationships (e.g., clashes, accessibility) using open-source tools such as [IfcOpenShell's `ifc-clash`](https://ifcopenshell.org) or [BCF](https://github.com/BuildingSMART/BCF-API) workflows.

## 3. Integration with OpenPermit

1. **Submission pipeline**
   - When an applicant uploads an IFC file, trigger automated validation steps before the file is accepted into the permit review queue.
   - Validation scripts can be run in a continuous integration (CI) environment or as server-side hooks.
   - The helper script [`scripts/ifc_validate.py`](../scripts/ifc_validate.py) wraps common IfcOpenShell checks and can be executed manually:

     ```bash
     $ python scripts/ifc_validate.py example.ifc
     IFC validation passed
     ```

2. **Feedback and reporting**
   - Collect validation results (errors, warnings, and rule violations) and store them alongside the permit record.
   - Provide applicants with a report highlighting issues that need to be resolved.

3. **Manual review**
   - After automated checks pass, reviewers can inspect the model using tools like [BlenderBIM](https://blenderbim.org/) or other IFC viewers to confirm compliance.

## 4. Recommended Tools

- **IfcOpenShell** – open-source library for parsing, validating, and manipulating IFC files.
- **BIMTester** – behavior-driven testing framework for IFC models.
- **BlenderBIM** – IFC authoring and review toolkit built on Blender.
- **ifc-validator** – lightweight command-line validator for IFC schema compliance.

## Summary

By integrating schema validation and rule-based checks into the submission workflow, OpenPermit ensures that IFC files are consistent with open standards and local regulations. Automated validation provides immediate feedback to applicants, while manual review tools help authorities confirm compliance before issuing permits.

