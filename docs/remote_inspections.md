# Remote Inspection API

The `remote_inspection` package provides a stub interface for collecting photos from the field. Each image is uploaded with latitude and longitude coordinates and undergoes a simple validation step.

## Capabilities

- **Upload geo‑tagged photos** – `PhotoInspectionAPI.upload_photo()` accepts a file path and GPS coordinates.
- **Basic image validation** – files are checked with Python's `imghdr` module to ensure they are recognized images.
- **AI hooks** – the `_run_ai_analysis()` method is a placeholder where computer‑vision models can be integrated to detect issues automatically.

Uploaded photos are stored in memory as `PhotoRecord` objects containing the location and validation metadata. This stub does not persist data or handle authentication but demonstrates how remote inspections could be integrated into OpenPermit.
